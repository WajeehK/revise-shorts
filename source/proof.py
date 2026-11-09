# Scripted proofreading for Revise Shorts. Usage: tools/venv/bin/python src/proof.py [--words]
import json,re,sys,collections,math
import os; Q=json.load(open(os.environ.get('QJSON','app/data/questions.json'),encoding='utf8'))
ALL=[]
for s in Q['subjects']:
    for sec in s['sections']:
        for t in sec['topics']:
            for qi,qz in enumerate(t['quizzes']):
                for q in qz: ALL.append((s['id'],t['id'],qi+1,q))
iss=collections.defaultdict(list)
def add(k,where,msg): iss[k].append(f'{where}: {msg}')
nz=lambda x:re.sub(r'[^a-z0-9⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉+−-]','',str(x).lower())
seen={}
UNITS=set(open('src/units_allow.txt',encoding='utf8').read().split('\n'))
for subj,tid,qn,q in ALL:
    w=f'{tid}/Q{qn}'; qt=q['q']
    if '$' in qt or '\\' in qt: add('katex-in-question',w,qt[:60])
    k=(nz(qt),q['t'],nz(q.get('a','')))
    if k in seen and seen[k]!=w: add('duplicate',w,f'same as {seen[k]}: {qt[:60]}')
    seen.setdefault(k,w)
    e=q.get('e','').strip()
    if not e: add('empty-explanation',w,qt[:60])
    elif len(e)<8 and q['t']!='text': add('short-explanation',w,f'{qt[:50]} → "{e}"')
    if q['t']=='mc':
        opts=[q['a']]+q['w']
        if len({re.sub(r'\s+','',o.lower()) for o in opts})<len(opts): add('mc-duplicate-option',w,f'{qt[:50]} {opts}')
        if any(not o.strip() for o in opts): add('mc-empty-option',w,qt[:50])
        if len(opts)!=4: add('mc-option-count',w,qt[:50])
    if q['t']=='match':
        L=[p[0] for p in q['pairs']]; R=[p[1] for p in q['pairs']]
        if len(set(map(nz,L)))<len(L) or len(set(map(nz,R)))<len(R): add('match-not-unique',w,f'{qt[:50]} {q["pairs"]}')
        if len(L)<3: add('match-too-few',w,qt[:50])
    if q['t']=='order':
        if len(set(map(nz,q['items'])))<len(q['items']): add('order-not-unique',w,qt[:50])
        if len(q['items'])<3: add('order-too-few',w,qt[:50])
    if q['t']=='text':
        if not q['k'] or any(not g for g in q['k']): add('text-no-keywords',w,qt[:50])
    if q['t']=='num':
        u=q.get('u','').strip()
        if u and u not in UNITS and not re.match(r'^× 10[⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+( \S.*)?$',u): add('unit-unrecognised',w,f'"{u}" in {qt[:50]}')
        if re.search(r'\b(m/s|kg/m|J/kg|N/m)\b',qt+' '+u) and subj!='maths' and False: pass
        a=q['a']; tol=max(q['tol'],0.1)/100*abs(a)+1e-9
        m=re.search(r'\((\d) s\.f\.|(\d) s\.f\.|(\d) significant',qt); md=re.search(r'(\d) d\.p\.',qt)
        cand=None
        if m and a!=0:
            sf=int(next(g for g in m.groups() if g)); cand=float(f'{a:.{sf}g}')
        elif md: cand=round(a,int(md.group(1)))
        if cand is not None and abs(cand-a)>tol: add('sf-rounded-answer-rejected',w,f'{qt[:60]} a={a} rounded={cand} tol={q["tol"]}%')
        if cand is None and a!=0:
            digs=len(re.sub(r'[^0-9]','',f'{abs(a):.10g}').strip('0'))
            if digs>=5 and q['tol']<0.5: add('sf-precision-without-instruction',w,f'{qt[:60]} a={a} tol={q["tol"]}%')
OFF={'maths':r'\b(momentum|impulse|kinetic energy|potential energy|work done|power of|poisson|chi-squared|spearman|maclaurin|matri(x|ces)|complex number|hyperbolic|polar coordinates|simpson)\b',
     'physics':r'\b(bernoulli|reynolds|lorentz|special relativity|time dilation|schr[oö]dinger|hall probe|transistor|op-amp|operational amplifier)\b',
     'chemistry':r'\b(sn1|sn2|e1|e2 mechanism|grignard|diazonium|azo dye|nernst|crystal field|ligand field|ozonolysis|markownikoff\'s anti|lindlar|ka2)\b'}
for subj,tid,qn,q in ALL:
    txt=' '.join([q['q'],q.get('e',''),str(q.get('a','')),' '.join(q.get('w',[]))]).lower()
    m=re.search(OFF[subj],txt)
    if m: add('off-spec-term',f'{tid}/Q{qn}',f'"{m.group(0)}" in {q["q"][:60]}')
# notes
import glob as _g
NOTEFILES=sorted(_g.glob('src/notes/*.md'))
SUBJ=lambda f:{'c':'chemistry','p':'physics'}.get(__import__('os').path.basename(f)[0],'maths')
for fp in NOTEFILES:
    f=__import__('os').path.basename(fp)
    for i,l in enumerate(open(fp,encoding='utf8'),1):
        if l.count('$')%2: add('notes-unbalanced-$',f'{f}:{i}',l[:60])
        if not l.startswith('!fig') and re.search(OFF[SUBJ(fp)],l.lower()): add('off-spec-term',f'{f}:{i}',re.search(OFF[SUBJ(fp)],l.lower()).group(0))
# spelling
if '--words' in sys.argv or True:
    try:
        from spellchecker import SpellChecker
        sp=SpellChecker(language='en'); allow=set(open('src/words_allow.txt',encoding='utf8').read().split()) if __import__('os').path.exists('src/words_allow.txt') else set()
        cnt=collections.Counter(); where={}
        texts=[(f'{tid}/Q{qn}',' '.join([q['q'],q.get('e',''),str(q.get('a','')),' '.join(q.get('w',[])),' '.join(q.get('items',[])),' '.join(a+' '+b for a,b in q.get('pairs',[]))])) for subj,tid,qn,q in ALL]
        for fp in NOTEFILES:
            for i,l in enumerate(open(fp,encoding='utf8'),1): texts.append((__import__('os').path.basename(fp)+f':{i}',re.sub(r'\$[^$]*\$','',l)))
        for w,t in texts:
            for word in re.findall(r"[A-Za-z][a-z]{3,}",t):
                lw=word.lower()
                if lw in allow: continue
                if word[0].isupper() and word[1:].islower() and lw not in sp: pass
                if lw not in sp: cnt[lw]+=1; where.setdefault(lw,w)
        unk=sorted(cnt.items(),key=lambda x:-x[1])
        for wd,c in unk: add('spelling-unknown',where[wd],f'{wd} ×{c}')
    except ImportError: print('(no spellchecker)')
tot=0
for k,v in sorted(iss.items()):
    print(f'== {k}: {len(v)}'); tot+=len(v)
    for x in v[:int(sys.argv[sys.argv.index('-n')+1]) if '-n' in sys.argv else 15]: print('  ',x)
print('TOTAL',tot)
json.dump({k:len(v) for k,v in iss.items()},open('/tmp/proof_counts.json','w'))
