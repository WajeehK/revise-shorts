#!/usr/bin/env python3
"""Spec coverage audit. Checks every extracted spec point (src/coverage/points_*.txt) against the
revision notes and questions of the topic it maps to, using keyword evidence, and writes source/COVERAGE.md.
Manual keyword sets for a point can be given in src/coverage/kw.txt as  ref|notes kws (all, ';'-separated)|question kws (any group; '&' = all in one question)."""
import json,re,os,sys,math,collections
R=os.path.dirname(os.path.abspath(__file__))
D=json.load(open(os.path.join(R,'../app/data/questions.json'),encoding='utf8'))
NOTES={f[:-3]:open(os.path.join(R,'notes',f),encoding='utf8').read() for f in os.listdir(os.path.join(R,'notes')) if f.endswith('.md')}
Q=collections.defaultdict(list);TITLE={};SEC={}
for s in D['subjects']:
    for sec in s['sections']:
        for t in sec['topics']:
            TITLE[t['id']]=t['title'];SEC[t['id']]=sec['name']
            for z in t['quizzes']:
                for q in z: Q[t['id']].append(' '.join(str(x) for x in [q.get('q',''),q.get('a',''),' '.join(q.get('w',[]) or []),q.get('e',''),' '.join(q.get('k',[]) and [' '.join(g) for g in q['k']] or []),' '.join(q.get('items',[]) or []),' '.join(a+' '+b for a,b in (q.get('pairs') or []))]))
def norm(s):
    s=s.lower().replace('–','-').replace('’',"'")
    s=re.sub(r'[₀-₉]',lambda m:'0123456789'['₀₁₂₃₄₅₆₇₈₉'.index(m.group())],s)
    s=re.sub(r'\\[a-z]+',' ',s)
    return s
STOP=set('''understand use using used know knowing knowledge including include includes ability able apply application applications demonstrate
students student should will expected learners recall describe description explain explanation deduce determine calculate calculations
calculation simple terms term work working with from that this these those their there which where when what into onto than then also such
both each other between within without about given give make made making show only must have been being more most less least very some
many much well same different number numbers value values example examples context contexts problem problems solve solving case cases
type types range form forms method methods idea ideas concept concepts principle principles effect effects including relevant appropriate
suitable carry carried out appreciate interpret interpreting investigate investigation evaluate evaluation identify identification
techniques technique procedures procedure determine determining their them they into over under limited extend extended relation
relationship relationships equation equations following involving involve involves level levels process processes
perform construct constructing whilst sufficient related convert vice versa familiar unfamiliar existence based typical sketch select predict
qualitative quantitative accounts account illustrated deficiency important importance asked according themselves arrange specified represent
represented associated further study consider considers mathematical enable enables occurring occur attainment derived derive varies vary place
having full studied above below whose would could being necessary detail details various certain particular general generally specific
specification section sections provides provide understanding fabric aims module topic topics introduce conventions
obtain obtaining record recording affect affects affecting approach approaches together therefore wide
measure measured measures measurement significance significant changes change changing large small'''.split())
def stem(w):
    w=w.lower().strip("'")
    for _ in range(2):
        for suf in ['isations','isation','ations','ation','ising','izing','ities','ments','ment','ness','ings','ing','ies','ied','ive','ed','es','s','al','ly','ic','e','y']:
            if len(w)>len(suf)+3 and w.endswith(suf): w=w[:-len(suf)];break
    return w[:6]
def terms(st):
    ws=re.findall(r"[a-zA-Z][a-zA-Z']{3,}",norm(st))
    out=[]
    for w in ws:
        lw=w.lower().strip("'")
        if lw in STOP or len(lw)<4: continue
        s_=stem(lw)
        if s_ not in out: out.append(s_)
    return out
def stems_of(text):
    return set(stem(w) for w in re.findall(r"[a-zA-Z][a-zA-Z']{2,}",norm(text)))
NS={k:stems_of(v) for k,v in NOTES.items()}
QS={k:[stems_of(x) for x in v] for k,v in Q.items()}
QN={k:[norm(x) for x in v] for k,v in Q.items()}
MAN={}
p=os.path.join(R,'coverage','kw.txt')
if os.path.exists(p):
    for l in open(p,encoding='utf8'):
        l=l.rstrip('\n')
        if not l or l.startswith('#'): continue
        r,nk,qk=(l.split('|')+['',''])[:3];MAN[r]=(nk,qk)
def topic(subj,ref):
    if subj=='physics':
        a,b,_=ref.split('(')[0].split('.')
        return 'p-1' if a=='1' else f'p-{a}-{b}'
    if subj=='chemistry':
        if ref.startswith('RP'):
            return {'RP1':'c-1-2','RP2':'c-1-4','RP3':'c-1-5','RP4':'c-2-3','RP5':'c-3-5','RP6':'c-3-6','RP7':'c-1-9','RP8':'c-1-11','RP9':'c-1-12','RP10':'c-3-9','RP11':'c-2-6','RP12':'c-3-16'}[ref]
        p_=ref.split('.');return f'c-{p_[1]}-{p_[2]}'
    m=re.match(r'([PSM])(\d+)\.',ref);t=int(m.group(2))
    return {'P':['m-proof','m-alg','m-coord','m-seq','m-trig','m-exp','m-diff','m-int','m-num','m-vec'],'S':['s-samp','s-data','s-prob','s-dist','s-hyp'],'M':[None,None,None,None,None,'k-units','k-kin','k-force','k-mom']}[m.group(1)][t-1]
def has(text_norm,kw):
    kw=kw.strip().lower()
    return kw in text_norm
res=[];
for subj,board in [('chemistry','AQA 7405'),('physics','OCR A H556'),('maths','Edexcel 9MA0')]:
    for l in open(os.path.join(R,'coverage',f'points_{subj}.txt'),encoding='utf8'):
        l=l.rstrip('\n')
        if not l: continue
        ref,st=l.split('|',1);tid=topic(subj,ref)
        if ref in MAN and MAN[ref][0]=='SKIP':
            res.append((subj,ref,st,tid,None,None,'skip:'+MAN[ref][1],[],0));continue
        if ref in MAN:
            nk,qk=MAN[ref];nt=norm(NOTES[tid])
            nks=[k for k in nk.split(';') if k.strip()]
            nok=all(has(nt,k) for k in nks);nmiss=[k for k in nks if not has(nt,k)]
            qok=False;qhit=0
            for i,qt in enumerate(QN[tid]):
                for g in qk.split(';'):
                    g=[x for x in g.split('&') if x.strip()]
                    if g and all(has(qt,x) for x in g): qok=True;qhit+=1;break
            res.append((subj,ref,st,tid,nok,qok,'manual',nmiss,qhit));continue
        T=terms(st)
        if not T: res.append((subj,ref,st,tid,True,True,'auto',[],0));continue
        hit=[t for t in T if t in NS[tid]];frac=len(hit)/len(T)
        nok=frac>=0.6 or len(T)-len(hit)<=1 and len(T)>=2
        need=1 if len(T)<=2 else 2
        qhit=sum(1 for s_ in QS[tid] if len([t for t in T if t in s_])>=need)
        res.append((subj,ref,st,tid,nok,qhit>0,'auto',[t for t in T if t not in NS[tid]],qhit))
if '--fails' in sys.argv:
    for r in res:
        if r[4] is None: continue
        if not (r[4] and r[5]): print(f"{r[1]}|{r[3]}|N{'+' if r[4] else '-'}Q{'+' if r[5] else '-'}|{r[2][:150]}|miss:{','.join(r[7][:8])}")
    sys.exit()
# write markdown
out=['# Specification coverage matrix (v11)','',f'Generated by `source/coverage.py` from the official specifications (AQA 7405, OCR A H556, Edexcel 9MA0).',
'Every spec point extracted from the specification text is mapped to a topic, then checked for evidence in that topic\'s revision notes and in at least one of its questions. Points that the automatic keyword check could not confirm were reviewed by hand; for those, the keywords used as evidence are listed in `source/coverage/kw.txt`.','']
tot=collections.Counter();ok=collections.Counter()
SK=[r for r in res if r[4] is None];res=[r for r in res if r[4] is not None]
for r in res:
    tot[r[0]]+=1; ok[r[0]]+=(r[4] and r[5])
out.append('| Subject | Spec points | Notes ✓ | Question ✓ | Fully covered |');out.append('|---|---|---|---|---|')
for s in ['chemistry','physics','maths']:
    n=sum(1 for r in res if r[0]==s and r[4]);q=sum(1 for r in res if r[0]==s and r[5])
    out.append(f'| {s.title()} | {tot[s]} | {n} | {q} | {ok[s]} ({100*ok[s]/tot[s]:.1f}%) |')
T_=sum(tot.values());O_=sum(ok.values())
out.append(f'| **All** | **{T_}** | | | **{O_} ({100*O_/T_:.1f}%)** |');out.append('')
for s in ['chemistry','physics','maths']:
    out.append(f'## {s.title()}');out.append('')
    cur=None
    for r in res:
        if r[0]!=s: continue
        if r[3]!=cur:
            cur=r[3];out.append('');out.append(f'### {TITLE.get(cur,cur)} — `{cur}` ({SEC.get(cur,"")})');out.append('');out.append('| Ref | Spec point | Notes | Qs |');out.append('|---|---|---|---|')
        st=r[2].replace('|','/')
        if len(st)>140: st=st[:137]+'…'
        out.append(f"| {r[1]} | {st} | {'✓' if r[4] else '✗'} | {('✓ '+str(r[8])) if r[5] else '✗'} |")
    out.append('')
out.append('## Excluded extractor lines');out.append('');out.append('Lines the extractor picked up that are not assessable spec statements (section headings, list lead-ins, section introduction paragraphs). Each was checked by hand.');out.append('');out.append('| Ref | Text | Reason |');out.append('|---|---|---|')
for r in SK: out.append(f"| {r[1]} | {r[2][:90].replace('|','/')} | {r[6][5:]} |")
open(os.path.join(R,'COVERAGE.md'),'w',encoding='utf8').write('\n'.join(out)+'\n')
print('coverage',{s:f'{ok[s]}/{tot[s]}' for s in tot},'total',f'{O_}/{T_}')
fails=[r for r in res if not (r[4] and r[5])]
print('fails',len(fails),'notes-fail',sum(1 for r in fails if not r[4]),'q-fail',sum(1 for r in fails if not r[5]))
sys.exit(0 if not fails else 1)
