# Extracts a spec-point checklist from the official spec PDFs' text (pdftotext -layout) into points_<subj>.txt: ref|statement
import re,sys
SP='/workspace/specs/'
def left(line,maxind=40):
    line=line.replace('\t','    ').rstrip()
    ind=len(line)-len(line.lstrip())
    if ind>maxind or not line.strip(): return None,ind
    t=line.strip(); t=re.split(r'\s{4,}',t)[0]
    return t,ind
def clean(s):
    s=re.sub(r'\s+',' ',s)
    s=re.split(r' (Cambridge OCR Level 3|Version \d\.\d)',s)[0].strip(' ;.')
    return s
def ocr():
    L=open(SP+'ocr_raw.txt',encoding='utf8').read().split('\n')
    starts=[i for i,l in enumerate(L) if l.startswith('1.1.1 Planning')]
    start=starts[-1]
    end=next(i for i,l in enumerate(L) if i>start+3000 and re.match(r'\s*3[a-z]?\.?\s*Assessment of|^3 Assessment|Assessment Overview',l))
    out=[];sec=None;item=None;sub=None;mode=0;buf=[]
    def flush():
        if sec and item and buf:
            st=clean(' '.join(buf))
            if len(st)>3: out.append((f"{sec}({item})"+(f"({sub})" if sub else ''),st))
        buf.clear()
    for l in L[start:end]:
        t=l.replace('\t',' ').strip()
        m=re.match(r'(\d\.\d\.\d)\s+([A-Z].*)',t)
        if m and len(t)<80:
            flush();sec=m.group(1);item=None;sub=None;mode=0;continue
        m=re.match(r'\(([a-z])\)\s*(.*)$',t)
        if m and m.group(1) in 'iv' and item and not (m.group(1)=='i' and item=='h') and not (m.group(1)=='v' and item=='u'): m=None
        if m and sec:
            flush();item=m.group(1);sub=None;mode=1;t=m.group(2)
        m=re.match(r'\((i{1,3}|iv|vi{0,3}|v)\)\s*(.*)$',t)
        if m and item:
            flush();sub=m.group(1);mode=1;t=m.group(2)
        if mode==1:
            if not t:
                if buf: mode=2
                continue
            if re.match(r'(HSW|PAG|M\d|Version|© |Cambridge OCR|Learners |Including)',t): mode=2 if buf else 1;continue
            buf.append(t)
    flush();return out
def ocr_layout():
    L=open(SP+'ocrH556.txt',encoding='utf8').read().split('\n')
    out=[];st={'sec':None,'item':None,'sub':None};buf=[]
    def flush():
        if st['sec'] and st['item'] and buf:
            t=clean(' '.join(buf))
            if len(t)>3: out.append((f"{st['sec']}({st['item']})"+(f"({st['sub']})" if st['sub'] else ''),t))
        buf.clear()
    start=next(i for i,l in enumerate(L) if re.match(r'\s*1\.1\.1 Planning',l) and i>200)
    for l in L[start:]:
        if re.search(r'Assessment Overview|^\s*3\s+Assessment of',l): break
        l=l.replace('\t','    ')
        m=re.match(r'\s*(\d\.\d\.\d)\s+([A-Z][^ ].*)',l)
        if m and not re.search(r'\s{4,}',l.strip()) and len(l.strip())<70:
            flush();st.update(sec=m.group(1),item=None,sub=None);continue
        if re.search(r'Version \d|OCR 20|Learning outcomes|Learners should be able|apply their knowledge',l): continue
        ind=len(l)-len(l.lstrip())
        if ind>14 and not re.match(r'\s*\((i{1,3}|iv|v|vi{0,3})\)',l): 
            t=l.strip()
            if ind<=20 and st['item']: buf.append(re.split(r'\s{4,}',t)[0])
            continue
        t=l.strip()
        m=re.match(r'\(([a-z])\)\s*(.*)',t)
        if m and not (m.group(1) in 'iv' and st['item'] and not (m.group(1)=='i' and st['item']=='h')):
            flush();st.update(item=m.group(1),sub=None);t=m.group(2).strip()
        m=re.match(r'\((i{1,3}|iv|v|vi{0,3})\)\s*(.*)',t)
        if m and st['item']:
            flush();st['sub']=m.group(1);t=m.group(2).strip()
        t=re.split(r'\s{4,}',t)[0]
        if st['item'] and t and not re.fullmatch(r'[\dA-Z]{1,3}|HSW.*|PAG.*|M\d.*',t): buf.append(t)
    flush();return out
def aqa():
    L=open(SP+'aqa7405.txt',encoding='utf8').read().split('\n')
    out=[];sec=None;buf=[];k=0
    start=next(i for i,l in enumerate(L) if l.startswith('3.1.1.1 ') and i>300)
    end=next(i for i,l in enumerate(L) if i>start and re.match(r'(4|8) (Scheme of assessment|Practical assessment)',l.strip()))
    def flush():
        nonlocal k
        if sec and buf:
            st=clean(' '.join(buf))
            if len(st)>8 and not re.match(r'(Students should be able to|Students will not be expected|Content$)',st):
                k+=1;out.append((f'{sec}.{k}',st))
        buf.clear()
    for l in L[start:end]:
        m=re.match(r'(3\.\d+\.\d+(\.\d+)?)\s+([A-Z].*)',l.strip())
        if m and not re.search(r'\s{4,}',l.strip()):
            flush();sec=m.group(1);k=0;continue
        if re.search(r'Visit for the most|AQA AS and A-level|^Content\s|Opportunities for skills|^\s*development\s*$',l): continue
        t,ind=left(l,30)
        if t is None or ind>30:
            continue
        if re.match(r'(MS|AT|PS) ?\d',t): continue
        if t.startswith('•'):
            flush();buf.append(t[1:].strip());continue
        if re.match(r'Students (should|will)',t) or (buf and buf[-1].endswith('.')):
            flush()
        buf.append(t)
    flush()
    secs4={r.rsplit('.',1)[0] for r,_ in out if r.count('.')==4}
    out=[(r,t) for r,t in out if not (r.count('.')==3 and r.rsplit('.',1)[0] in {x.rsplit('.',1)[0] for x in secs4})]
    RP=['Make up a volumetric solution and carry out a simple acid–base titration','Measurement of an enthalpy change','Investigation of how the rate of a reaction changes with temperature','Carry out simple test-tube reactions to identify cations and anions in aqueous solution','Distillation of a product from a reaction','Tests for alcohol, aldehyde, alkene and carboxylic acid','Measuring the rate of reaction by an initial rate method and by a continuous monitoring method','Measuring the EMF of an electrochemical cell','Investigate how pH changes when a weak acid reacts with a strong base and when a strong acid reacts with a weak base','Preparation of a pure organic solid and test of its purity; preparation of a pure organic liquid','Carry out simple test-tube reactions to identify transition metal ions in aqueous solution','Separation of species by thin-layer chromatography']
    out+= [(f'RP{i+1}',t) for i,t in enumerate(RP)]
    return out
def ed():
    L=open(SP+'ed9ma0.txt',encoding='utf8').read().split('\n')
    p1=next(i for i,l in enumerate(L) if re.search(r'^\s*1\s+1\.1\s+Understand and use the',l))
    p3=next(i for i,l in enumerate(L) if i>p1+200 and re.search(r'^\s*1\s+1\.1\s+Understand and use the',l))
    end=next(i for i,l in enumerate(L) if i>p3 and re.search(r'^\s*Assessment information',l))
    out=[];ref=None;buf=[];k=[0];cc,gc=21,66;part='P'
    def flush():
        if ref and buf:
            st=clean(' '.join(buf))
            if len(st)>6:
                k[0]+=1;out.append((ref+('' if k[0]==1 else chr(96+k[0])),st))
        buf.clear()
    for n in range(p1-6,end):
        l=L[n].replace('\t','    ')
        if n>=p3: part='S'
        m=re.search(r'Content\s+Guidance',l)
        if m: cc=l.index('Content');gc=l.index('Guidance');continue
        if re.search(r'Pearson Edexcel|Specification – Issue|What students need to learn|^\s*Topics\s*$',l): continue
        seg=l[cc:gc] if len(l)>cc else ''
        m=re.match(r'\s*(\d{1,2}\.\d{1,2})\s+(\S.*)',seg)
        if m:
            flush();t=int(m.group(1).split('.')[0])
            pp='M' if part=='S' and t>=6 else part
            ref=pp+m.group(1);k[0]=0;buf.append(m.group(2).strip());continue
        if not seg.strip(): continue
        if re.match(r'\s*\d{1,2}\s*$',l[:cc]) and False: pass
        buf.append(seg.strip())
    flush();return out
if __name__=='__main__':
    def ocr_merged():
        b=ocr();a=ocr_layout();have={r for r,_ in a}
        import re as _r
        good=lambda r:_r.match(r'\d\.\d\.\d\([a-z]\)',r)
        a=[x for x in a if good(x[0])]
        have={r for r,_ in a}
        extra=[x for x in b if x[0] not in have and good(x[0])]
        key=lambda r:[int(p) if p.isdigit() else p for p in _r.split(r'[.()]',r) if p]
        allp=sorted(a+extra,key=lambda x:key(x[0]))
        res=[];prev={}
        for r,t in allp:
            m=_r.match(r'(\d\.\d\.\d)\(([a-z])\)',r);sec,let=m.group(1),m.group(2)
            p=prev.get(sec,'`')
            if ord(let)-ord(p)>3: continue
            prev[sec]=max(p,let);res.append((r,t))
        res.append(('6.2.4(a)','electric potential at a point as the work done in bringing unit positive charge from infinity to the point; electric potential is zero at infinity'))
        res=sorted(res,key=lambda x:key(x[0]))
        # two-column pages leak the next section's points under the previous ref: keep only the LAST copy of identical text
        nt=lambda t:_r.sub(r'\W+','',t.lower())[:60]
        last={nt(t):i for i,(r,t) in enumerate(res)}
        res=[(r,t) for i,(r,t) in enumerate(res) if last[nt(t)]==i and t.strip().lower()!='learning outcomes']
        cut=lambda t:_r.split(r'\.\s+(?:Module \d+:|\d\.\d\s+[A-Z]|2d\. Prior)',t)[0].strip()
        return [(r,cut(t)) for r,t in res]
    for name,f in [('physics',ocr_merged),('chemistry',aqa),('maths',ed)]:
        pts=f();open(f'/workspace/scienceshorts-clone/src/coverage/points_{name}.txt','w',encoding='utf8').write('\n'.join(f'{r}|{s}' for r,s in pts)+'\n')
        print(name,len(pts))
