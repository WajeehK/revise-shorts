import json,re,sys,math,importlib
sys.path.insert(0,'src')
PL={'physics':'PLGvD8d3gDHUWcVw3HaPiIRH5VLn_isI8g','chemistry':'PLGvD8d3gDHUV5K3QoUwcxP37te57MzMRo'}
def parse_line(p,k):
    if k=='M': assert len(p)==7; return dict(t='mc',q=p[1],a=p[2],w=p[3:6],e=p[6])
    if k=='N':
        assert len(p) in (6,7); q=dict(t='num',q=p[1],a=float(p[2]),tol=float(p[3]),u=p[4],e=p[5])
        if len(p)==7:
            v=eval(p[6],{**math.__dict__})
            tol=max(q['tol'],0.1)/100*abs(q['a'])+1e-9
            assert abs(v-q['a'])<=tol, f'CHECK FAIL computed {v} vs {q["a"]}'
            q['_chk']=1
            m=re.search(r'(\d) s\.f\.',q['q']); md=re.search(r'(\d) d\.p\.',q['q'])
            want=float(f'{v*(1+1e-11):.{int(m.group(1))}g}') if m and v else (round(v*(1+1e-11),int(md.group(1))) if md else None)
            if want is not None and abs(want-q['a'])>1e-9*max(1,abs(want)): SFW.append(f"SF {q['q'][:60]} stored {q['a']} vs correctly rounded {want}")
        return q
    if k=='W': assert len(p)==4; return dict(t='text',q=p[1],k=[[a.strip().lower() for a in g.split(';') if a.strip()] for g in p[2].split(' & ')],e=p[3])
    if k=='S': assert len(p)==4; return dict(t='order',q=p[1],items=p[2].split(';'),e=p[3])
    if k=='P':
        assert len(p)==4; q=dict(t='match',q=p[1],pairs=[x.split('=',1) for x in p[2].split(';')],e=p[3]); assert all(len(x)==2 for x in q['pairs']); return q
    raise Exception('type '+k)
out=[];errs=0;report=[];SFW=[]
# v10: synonym classes for written-answer keyword marking (any member of a class counts for the others)
SYN=[['same','identical','equal','the same'],['equal','same','identical','equals','balance'],
 ['constant','unchanged','does not change','doesn\'t change','stays the same','remains the same','uniform','fixed','steady'],
 ['zero','0','nil','none'],
 ['increase','increases','rises','goes up','larger','bigger','greater','higher'],['larger','bigger','greater','increase','higher'],['greater','larger','bigger','higher','more than'],['bigger','larger','greater'],
 ['decrease','decreases','falls','goes down','smaller','lower','reduces','reduce','drops'],['smaller','lower','decrease','reduced','fewer'],
 ['faster','quicker','more quickly','increases the rate','higher rate'],['stronger','greater force','more strongly','stronger forces'],
 ['attract','attraction','pull','pulled'],['attraction','attract','pull'],['repel','repulsion','push apart','repulsive'],['opposite','reverse','opposes','other direction','reversed'],
 ['absorb','absorption','absorbed','take in','takes in'],['delocalised','delocalized','spread over','shared over','delocalisation','delocalization'],['delocalis','delocaliz','spread over'],
 ['split','break','breaks','broken','splits','divides'],['vary','varies','change','changes','different'],['varies','vary','changes','different'],
 ['every','all','each'],['proportional','∝','directly proportional','in proportion'],['electrons','e-','e⁻','electron'],['proton','h+','h⁺','hydrogen ion'],['h+','h⁺','proton','hydrogen ion'],
 ['shielding','screening','shielded','inner electrons','inner shells'],['shield','screen','inner electrons','inner shells'],['perpendicular','right angle','right angles','90°','90 degrees','normal to'],
 ['reversible','⇌','both directions','go both ways','backwards and forwards'],['toxic','poisonous','harmful'],['stable','stability','lower in energy','more stable'],['planar','flat'],
 ['polar','dipole','δ+','delta'],['infinity','infinitely far','∞','infinite distance'],['lost','loses','removed','given off','released'],['hot','heat','heated','warm','high temperature'],
 ['distance','length','how far'],['straight line','linear','straight'],['average','mean'],['incomplete','not enough oxygen','limited oxygen','insufficient oxygen','lack of oxygen'],
 ['van der waals','vdw','london','induced dipole','dispersion','temporary dipole'],['hydrogen bond','hydrogen bonding','h-bond','h bond','hydrogen bonds'],['stationary','at rest','not moving'],
 ['further','more','again','multiple','repeated'],['temperature','temp'],['charge','charged'],['random','by chance','randomly'],['consistent','repeatable','reliable','agree','close together'],
 ['close','near','similar','agree'],['spread','range','scatter'],['component','resolve','resolved','part of the force'],['weight','mg','gravity'],['speed','velocity'],['displacement','distance in a direction'],
 ['activation energy','minimum energy','eₐ'],['ea','activation energy','minimum energy'],['surface area','area','surface'],['negative','minus'],['kinetic','kinetic energy','movement energy'],
 ['ion','ions','ionic'],['covalent','shared pair','sharing electrons','shared electrons'],['lattice','giant','lattice structure'],['secondary','2°'],['carbocation','carbonium','c+','c⁺','positive carbon'],
 ['nuclear charge','more protons','proton number','atomic number','charge on the nucleus','protons'],['reflect','reflected','reflection','reflects','bounce'],
 ['denature','denatured','denatures','loses its shape','changes shape','active site changes'],['shape','structure','active site','3d'],
 ['shell','shells','further from the nucleus','further away','energy level','larger radius','farther'],['decay','decreases','falls','declines','decrease'],
 ['point','particle','negligible size','no size','dimensions are ignored','ignore its size'],['stratified','simple random','random sample','random sampling','systematic sampling'],
 ['not representative','unrepresentative','does not represent',"doesn't represent",'differs from the population','systematically different','skewed'],
 ['addition','adds','add across','added','adding'],['c=c','double bond','alkene','unsaturated','pi bond','π bond'],['gas','escapes','given off','fumes'],
 ['mobile','moving phase','solvent','eluent'],['components','component','parts','horizontal and vertical','two perpendicular'],['eliminate','remove','substitute','get rid of'],
 ['rate','rates','speed','how fast'],['neutron','neutrons'],['reaction','react','reacting','reactions'],
 ['inductive','electron releasing','electron-releasing','pushes electrons','donates electrons','positive inductive'],['alkyl','methyl','ethyl','r group','carbon chain'],['opposite','reverse','opposes']]
nsyn=0;nsynq=0
def syn(q):
    global nsyn,nsynq
    if q.get('t')!='text': return q
    added=0
    for g in q['k']:
        for k in list(g):
            for cl in SYN:
                if cl[0]==k:
                    for x in cl[1:]:
                        if x not in g: g.append(x); added+=1
    if added: nsyn+=added; nsynq+=1
    return q
UFIX={'m/s':'m s⁻¹','km/s':'km s⁻¹','rad/s':'rad s⁻¹','mm/s':'mm s⁻¹','N/kg':'N kg⁻¹','MJ/kg':'MJ kg⁻¹','N/m':'N m⁻¹','V/m':'V m⁻¹','m/s²':'m s⁻²','y':'years','y⁻¹':'year⁻¹','kg/m³':'kg m⁻³'}
nufix=0
def fixu(q):
    global nufix
    if q.get('t')=='num' and q.get('u') in UFIX: q['u']=UFIX[q['u']]; nufix+=1
    return q
FIGS=json.load(open('app/data/figs.json',encoding='utf8')); nfigq=0
def figq(q):
    global errs,nfigq
    m=re.match(r'\[fig:([\w-]+)\]\s*',q['q'])
    if m:
        if m.group(1) not in FIGS: print('ERR unknown fig',m.group(1)); errs+=1
        q['fig']=m.group(1); q['q']=q['q'][m.end():]; nfigq+=1
    return q
for f in ['maths','physics','chemistry']:
    subj=None;tops={}
    files=[f'src/{f}.txt']+[x for x in [f'src/{f}_more.txt',f'src/{f}_figs.txt',f'src/{f}_cov.txt'] if __import__('os').path.exists(x)]
    for fn in files:
      for ln,line in enumerate(open(fn,encoding='utf8'),1):
        line=line.rstrip('\n')
        if not line.strip() or line.startswith('//'): continue
        if line.startswith('@ '):
            if subj: continue
            i,n,b,c=line[2:].split('|');subj=dict(id=i,name=n,board=b,color=c,playlist=PL.get(i),sections=[]);out.append(subj);continue
        if line.startswith('# '):
            i,t,s=line[2:].split('|')
            if i in tops: top=tops[i]; continue
            sec=next((x for x in subj['sections'] if x['name']==s),None)
            if not sec: sec=dict(name=s,topics=[]);subj['sections'].append(sec)
            top=dict(id=i,title=t,qs=[]);sec['topics'].append(top);tops[i]=top;continue
        lv=1
        if line[0] in '123': lv=int(line[0]);line=line[1:]
        p=line.split('|')
        try: q=syn(fixu(figq(parse_line(p,p[0]))))
        except Exception as ex: print('ERR',fn,ln,ex,line[:70]);errs+=1;continue
        top['qs'].append((lv,q))
    try:
        g=importlib.import_module('gen_'+f)
        for tid,lst in g.B.T.items():
            if tid not in tops: print('ERR gen unknown topic',tid);errs+=1;continue
            tops[tid]['qs']+=[(lv,syn(fixu(figq(q)))) for lv,q in lst]
    except ModuleNotFoundError: pass
    # bucket into quizzes
    for t in tops.values():
        b={1:[],2:[],3:[]};seen=set()
        for lv,q in t['qs']:
            if q['q'] in seen: continue
            seen.add(q['q']);b[lv].append(q)
        # rebalance toward 10 each: move surplus to the nearest short bucket
        for _ in range(60):
            over=[k for k in (1,2,3) if len(b[k])>10]; under=[k for k in (1,2,3) if len(b[k])<10]
            if not over or not under: break
            o=over[0]; u=min(under,key=lambda k:abs(k-o))
            b[u].append(b[o].pop(-1 if u>o else 0))
        t['quizzes']=[b[1],b[2],b[3]]
        n=sum(map(len,t['quizzes']))
        t['n']=n
        if n<30 or any(len(x)<10 for x in t['quizzes']): report.append(f"  SHORT {t['id']} {[len(x) for x in t['quizzes']]}")
        del t['qs']
# v11: spec-section layout (AQA 7405 splits AS content from A-level-only content)
LAYOUT={'chemistry':[('Physical Chemistry','AS · 3.1.1–3.1.7',[f'c-1-{i}' for i in range(1,8)]),('Inorganic Chemistry','AS · 3.2.1–3.2.3',[f'c-2-{i}' for i in range(1,4)]),
  ('Organic Chemistry','AS · 3.3.1–3.3.6',[f'c-3-{i}' for i in range(1,7)]),('Advanced Physical Chemistry','A-level only · 3.1.8–3.1.12',[f'c-1-{i}' for i in range(8,13)]),
  ('Advanced Inorganic Chemistry','A-level only · 3.2.4–3.2.6',[f'c-2-{i}' for i in range(4,7)]),('Advanced Organic Chemistry','A-level only · 3.3.7–3.3.16',[f'c-3-{i}' for i in range(7,17)])],
 'physics':[('Module 1: Development of practical skills in physics','AS and A level',['p-1']),('Module 2: Foundations of physics','AS and A level',['p-2-1','p-2-2','p-2-3']),
  ('Module 3: Forces and motion','AS and A level',['p-3-1','p-3-2','p-3-3','p-3-4','p-3-5']),('Module 4: Electrons, waves and photons','AS and A level',['p-4-1','p-4-2','p-4-3','p-4-4','p-4-5']),
  ('Module 5: Newtonian world and astrophysics','A level only',['p-5-1','p-5-2','p-5-3','p-5-4','p-5-5']),('Module 6: Particles and medical physics','A level only',['p-6-1','p-6-2','p-6-3','p-6-4','p-6-5'])],
 'maths':[('Pure Mathematics','Papers 1 and 2 · Topics 1–10',['m-proof','m-alg','m-coord','m-seq','m-trig','m-exp','m-diff','m-int','m-num','m-vec']),
  ('Statistics','Paper 3 Section A · Topics 1–5',['s-samp','s-data','s-prob','s-dist','s-hyp']),('Mechanics','Paper 3 Section B · Topics 6–9',['k-units','k-kin','k-force','k-mom'])]}
for s in out:
    allt={t['id']:t for sec in s['sections'] for t in sec['topics']}
    lay=LAYOUT[s['id']]; placed=[i for _,_,l in lay for i in l]
    assert sorted(placed)==sorted(allt), ('layout mismatch',s['id'],set(placed)^set(allt))
    s['sections']=[dict(name=n,note=d,topics=[allt[i] for i in l]) for n,d,l in lay]
total=0
for s in out:
    ts=[t for sec in s['sections'] for t in sec['topics']]
    total+=sum(t['n'] for t in ts)
    print(s['name'],'topics',len(ts),'questions',sum(t['n'] for t in ts),'min',min(t['n'] for t in ts))
    for t in ts: del t['n']
print('\n'.join(report) or 'all topics 30+ with 10/10/10')
chk=sum(1 for s in out for sec in s['sections'] for t in sec['topics'] for qz in t['quizzes'] for q in qz if q.get('t')=='num')
print('\n'.join(SFW) or 'sf check: all stated-precision answers match');print('unit notation normalised',nufix);print('keyword synonyms added',nsyn,'to',nsynq,'written questions');print('numeric questions',chk,'questions with diagrams',nfigq)
for s in out:
    for sec in s['sections']:
        for t in sec['topics']:
            for qz in t['quizzes']:
                for q in qz: q.pop('_chk',None)
print('TOTAL questions',total)
import datetime
json.dump(dict(version=3,count=total,built=datetime.date.today().strftime('%d %b %Y'),subjects=out),open('app/data/questions.json','w',encoding='utf8'),ensure_ascii=False,separators=(',',':'))
sys.exit(1 if errs else 0)
