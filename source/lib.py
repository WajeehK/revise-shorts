import random, math
def fm(x,sf=None):
    if sf: x=float(f'{x:.{sf}g}')
    if abs(x-round(x))<1e-9: return str(int(round(x))).replace('-','−')
    return (f'{x:.6g}').replace('-','−')
class Bank:
    def __init__(s,seed): s.R=random.Random(seed); s.T={}
    def add(s,tid,lv,q):
        if q.get('e'): q['e']=tidy(q['e'])
        s.T.setdefault(tid,[]).append((lv,q))
def N(q,a,tol=0.5,u='',e=''): return dict(t='num',q=q,a=round(float(a),8),tol=tol,u=u,e=e)
def M(q,a,w,e=''):
    w=[x for x in dict.fromkeys(w) if x!=a][:3]
    assert len(w)==3,(q,a,w); return dict(t='mc',q=q,a=a,w=w,e=e)
def W(q,k,e): return dict(t='text',q=q,k=[[a.strip().lower() for a in g.split(';') if a.strip()] for g in k.split(' & ')],e=e)
SUP=str.maketrans('-0123456789','⁻⁰¹²³⁴⁵⁶⁷⁸⁹')
def sci(x,sf=2):
    m,ex=f'{x:.{sf-1}e}'.split('e'); return f'{m} × 10{str(int(ex)).translate(SUP)}'

import re as _re
def _sci(m):
    v=float(m.group(0));ex=int(m.group(2)+m.group(3))
    if -4<=ex<=5: return f'{v:.6g}' if 'e' not in f'{v:.6g}' else f'{v:f}'.rstrip('0').rstrip('.')
    return sci(v,len(m.group(1).replace('.',''))).replace('-','−')
def tidy(e):
    """v11: turn Python e-notation (3.75e+03) in worked explanations into normal or × 10ⁿ form; use proper minus signs before numbers."""
    e=_re.sub(r'(\d(?:\.\d+)?)e([+-])(\d+)',_sci,e)
    return e
