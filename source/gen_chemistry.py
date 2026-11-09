from lib import *
import math
B=B_=Bank(3); R=B.R; a=B.add
Rg=8.31;NA=6.022e23
def ri(x,y): return R.randint(x,y)
def pk(*x): return R.choice(x)
def rep(n,f):
    for _ in range(n): f()
T=lambda tid,lv,q,ans,u,ex,tol=0.5: a(tid,lv,N(q,ans,tol,u,ex))
def table_mc(tid,lv,rows,qfmt,ki,vi,expl='',n=None,others=None):
    """rows: list of tuples; question asks for column vi given column ki."""
    vals=list(dict.fromkeys(r[vi] for r in rows))
    rs=rows[:] ; R.shuffle(rs)
    for r in rs[:n or len(rs)]:
        w=[v for v in vals if v!=r[vi]]; R.shuffle(w)
        if len(w)<3: continue
        a(tid,lv,M(qfmt.format(*r),r[vi],w[:3],expl.format(*r) if expl else ''))
AR={'H':1.0,'C':12.0,'N':14.0,'O':16.0,'Na':23.0,'Mg':24.3,'Al':27.0,'S':32.1,'Cl':35.5,'K':39.1,'Ca':40.1,'Fe':55.8,'Cu':63.5,'Zn':65.4,'Br':79.9,'Ag':107.9,'Ba':137.3,'Mn':54.9,'Cr':52.0,'I':126.9}
CMP={'H₂O':{'H':2,'O':1},'CO₂':{'C':1,'O':2},'NaCl':{'Na':1,'Cl':1},'CaCO₃':{'Ca':1,'C':1,'O':3},'H₂SO₄':{'H':2,'S':1,'O':4},'NaOH':{'Na':1,'O':1,'H':1},'MgO':{'Mg':1,'O':1},'C₂H₅OH':{'C':2,'H':6,'O':1},'CH₄':{'C':1,'H':4},'NH₃':{'N':1,'H':3},'C₆H₁₂O₆':{'C':6,'H':12,'O':6},'Na₂CO₃':{'Na':2,'C':1,'O':3},'KMnO₄':{'K':1,'Mn':1,'O':4},'CuSO₄':{'Cu':1,'S':1,'O':4},'Fe₂O₃':{'Fe':2,'O':3},'HCl':{'H':1,'Cl':1},'C₃H₈':{'C':3,'H':8},'CH₃COOH':{'C':2,'H':4,'O':2}}
def Mr(f): return sum(AR[e]*n for e,n in CMP[f].items())
# ---------- 3.1.1 atomic structure
EL=[('Na',11,23),('Mg',12,24),('Al',13,27),('S',16,32),('Cl',17,35),('K',19,39),('Ca',20,40),('Fe',26,56),('Cu',29,64),('Br',35,80),('O',8,16),('F',9,19)]
ION={'Na':1,'Mg':2,'Al':3,'S':-2,'Cl':-1,'K':1,'Ca':2,'Fe':3,'Cu':2,'Br':-1,'O':-2,'F':-1}
def f():
    s,Z,A=pk(*EL); ch=ION[s]
    T('c-1-1',1,f'How many neutrons in ^{A}{s}?',A-Z,'','A − Z.',0)
rep(3,f)
def f():
    s,Z,A=pk(*EL); ch=ION[s]
    lab=f"{s}{'' if abs(ch)==1 else abs(ch)}{'+' if ch>0 else '−'}"
    T('c-1-1',1,f'How many electrons in a {lab} ion?',Z-ch,'','Z − charge.',0)
rep(3,f)
def f():
    m1,m2=pk((35,37),(79,81),(10,11),(24,25),(6,7));p=round(R.uniform(20,80),1)
    T('c-1-1',2,f'An element has isotopes of mass {m1} ({p}%) and {m2} ({round(100-p,1)}%). Find Ar (3 s.f.).',(m1*p+m2*(100-p))/100,'','Weighted mean.')
rep(3,f)
CONF=[('Ca','1s² 2s² 2p⁶ 3s² 3p⁶ 4s²'),('Cr','[Ar] 3d⁵ 4s¹'),('Cu','[Ar] 3d¹⁰ 4s¹'),('Fe³⁺','[Ar] 3d⁵'),('Cu²⁺','[Ar] 3d⁹'),('Zn²⁺','[Ar] 3d¹⁰'),('S²⁻','1s² 2s² 2p⁶ 3s² 3p⁶'),('Ti','[Ar] 3d² 4s²'),('Mn²⁺','[Ar] 3d⁵'),('Al³⁺','1s² 2s² 2p⁶'),('Ni','[Ar] 3d⁸ 4s²'),('Co²⁺','[Ar] 3d⁷')]
table_mc('c-1-1',2,CONF,'Electron configuration of {0}?',0,1,'Fill 4s before 3d; remove 4s first for ions. Cr and Cu are exceptions.',7)
def f():
    m=pk(35,37,79,81,24);KE=round(R.uniform(1,5),1)*1e-16;d=pk(1.0,1.5,2.0)
    mk=m/1000/NA;t=d/math.sqrt(2*KE/mk)
    T('c-1-1',3,f'TOF mass spec: ions of m/z {m} (charge +1) have KE {KE/1e-16:g} × 10⁻¹⁶ J and drift {d} m. Time of flight (µs, 3 s.f.)?',t*1e6,'µs','m = (Mr/1000)/Nₐ; v = √(2KE/m); t = d/v.')
rep(4,f)
def f():
    m1,m2=pk((63,65),(69,71),(107,109));Ar=round(R.uniform(m1+0.3,m2-0.3),2)
    T('c-1-1',3,f'An element has two isotopes, {m1} and {m2}, and Ar = {Ar}. Find the % abundance of the {m1} isotope (3 s.f.).',(m2-Ar)/(m2-m1)*100,'%','Let x% be mass 63: x·m₁ + (100 − x)·m₂ = 100·Ar.')
rep(3,f)
# ---------- 3.1.2 amount
def f():
    c=pk(*CMP);m=round(R.uniform(1,50),1)
    T('c-1-2',1,f'Moles in {m} g of {c} (3 s.f.)? (Ar values: {", ".join(f"{e} = {AR[e]:g}" for e in CMP[c])})',m/Mr(c),'mol','n = m/Mr.')
rep(4,f)
def f():
    c=pk(*CMP)
    T('c-1-2',1,f'Relative formula mass of {c} (3 s.f.)? (Ar: {", ".join(f"{e} = {AR[e]:g}" for e in CMP[c])})',Mr(c),'','Sum of Ar.')
rep(3,f)
def f():
    v1,c1=round(R.uniform(15,30),2),pk(0.100,0.0500,0.200);vt=round(R.uniform(20,28),2);ratio=pk(1,2)
    acid='HCl' if ratio==1 else 'H₂SO₄'
    T('c-1-2',2,f'{vt} cm³ of {acid} neutralises {v1} cm³ of {c1} mol dm⁻³ NaOH. Find [{acid}] (3 s.f.).',c1*v1/ratio/vt,'mol dm⁻³',f'Ratio acid : NaOH = 1 : {ratio}.')
rep(4,f)
def f():
    n,T_,p=round(R.uniform(0.05,2),2),ri(273,400),pk(100,101,200)
    T('c-1-2',2,f'Volume of {n} mol of gas at {T_} K and {p} kPa (dm³, 3 s.f.)?',n*Rg*T_/(p*1000)*1000,'dm³','V = nRT/p, convert m³ to dm³.')
rep(3,f)
def f():
    m=round(R.uniform(2,10),2);act=round(m*R.uniform(0.5,0.9),2)
    mCaO=m*56.1/100.1
    T('c-1-2',2,f'{m} g CaCO₃ decomposes: CaCO₃ → CaO + CO₂. {act*56.1/100.1:.2f} g CaO is obtained. Percentage yield (3 s.f.)? (Mr CaCO₃ 100.1, CaO 56.1)',act/m*100,'%','Actual ÷ theoretical × 100.')
rep(3,f)
def f():
    x=pk(5,6,7,10,2);mh=round(R.uniform(2,5),2)
    MrA=pk((159.6,'CuSO₄'),(142.1,'Na₂SO₄'),(120.4,'MgSO₄'))
    ma=mh*MrA[0]/(MrA[0]+18*x)
    T('c-1-2',3,f'{mh} g of hydrated {MrA[1]}·xH₂O is heated to constant mass, leaving {ma:.3f} g anhydrous salt (Mr {MrA[0]}). Find x.',x,'','Moles of water ÷ moles of salt.',2)
rep(4,f)
def f():
    v=round(R.uniform(20,25),2);c=0.0200
    mFe=pk(1.2,1.5,2.0)
    nMn=c*v/1000;nFe=5*nMn
    T('c-1-2',3,f'{v} cm³ of 0.0200 mol dm⁻³ KMnO₄ reacts with Fe²⁺ from {mFe} g of iron tablets (MnO₄⁻ : Fe²⁺ = 1 : 5). Percentage of iron by mass (3 s.f., Ar Fe = 55.8)?',nFe*55.8/mFe*100,'%','n(Fe) = 5 × n(MnO₄⁻).')
rep(3,f)
# ---------- 3.1.3 bonding (shape table)
SH=[('CH₄','tetrahedral','109.5°'),('NH₃','trigonal pyramidal','107°'),('H₂O','bent','104.5°'),('BF₃','trigonal planar','120°'),('CO₂','linear','180°'),('SF₆','octahedral','90°'),('PCl₅','trigonal bipyramidal','90° and 120°'),('NH₄⁺','tetrahedral','109.5°'),('XeF₄','square planar','90°'),('ClF₃','T-shaped','≈ 87.5°'),('BeCl₂','linear','180°'),('SiCl₄','tetrahedral','109.5°'),('PH₃','trigonal pyramidal','≈ 93.5°'),('H₂S','bent','≈ 92°'),('AlCl₄⁻','tetrahedral','109.5°'),('SF₄','see-saw','≈ 102° and 173°')]
table_mc('c-1-3',1,[r for r in SH if r[1] in('tetrahedral','linear','bent','trigonal planar','trigonal pyramidal','octahedral')],'Shape of {0}?',0,1,'Count bonding and lone pairs.',4)
table_mc('c-1-3',2,SH,'Shape of {0}?',0,1,'Electron pair repulsion: lone pairs repel more.',6)
table_mc('c-1-3',3,[r for r in SH if '≈' not in r[2]],'Bond angle in {0}?',0,2,'Each lone pair reduces the angle by about 2.5°.',6)
FORCE=[('HF','hydrogen bonding'),('CH₄','van der Waals only'),('HCl','permanent dipole–dipole'),('NH₃','hydrogen bonding'),('Ne','van der Waals only'),('CH₃OH','hydrogen bonding'),('CO₂','van der Waals only'),('CHCl₃','permanent dipole–dipole'),('I₂','van der Waals only'),('H₂O','hydrogen bonding')]
table_mc('c-1-3',2,FORCE,'Strongest intermolecular force between {0} molecules?',0,1,'H bonded to N, O or F → hydrogen bonding.',5)
# ---------- 3.1.4 energetics
def f():
    m,dT,n=ri(25,100),round(R.uniform(2,15),1),round(R.uniform(0.01,0.1),3)
    q=m*4.18*dT
    T('c-1-4',1,f'{m} g of water rises by {dT} K (c = 4.18 J g⁻¹ K⁻¹). Find q in J (3 s.f.).',q,'J','q = mcΔT.')
rep(3,f)
def f():
    m,dT,n=ri(25,100),round(R.uniform(2,15),1),round(R.uniform(0.01,0.1),3)
    q=m*4.18*dT
    T('c-1-4',2,f'Burning {n} mol of fuel heats {m} g of water by {dT} K (c = 4.18). Find ΔcH (kJ mol⁻¹, 3 s.f.).',-q/n/1000,'kJ mol⁻¹','ΔH = −q/n (exothermic).')
rep(4,f)
def f():
    c1,v=pk(1.0,2.0,0.5),pk(25,50);dT=round(R.uniform(3,13),1)
    n=c1*v/1000;q=2*v*4.18*dT
    T('c-1-4',2,f'{v} cm³ of {c1} mol dm⁻³ HCl + {v} cm³ of {c1} mol dm⁻³ NaOH; ΔT = {dT} K. Find ΔneutH (kJ mol⁻¹, 3 s.f.). Assume total mass {2*v} g, c = 4.18.',-q/n/1000,'kJ mol⁻¹','q from total volume; n = c × V of acid.')
rep(3,f)
BE={'C–H':413,'C–C':347,'O=O':498,'C=O':805,'O–H':464,'H–H':436,'Cl–Cl':243,'H–Cl':432,'C=C':612,'C–Cl':346,'N≡N':945,'N–H':391}
RX=[('CH₄ + 2O₂ → CO₂ + 2H₂O',{'C–H':4,'O=O':2},{'C=O':2,'O–H':4}),('H₂ + Cl₂ → 2HCl',{'H–H':1,'Cl–Cl':1},{'H–Cl':2}),('C₂H₄ + H₂ → C₂H₆',{'C=C':1,'H–H':1,'C–H':4},{'C–C':1,'C–H':6}),('N₂ + 3H₂ → 2NH₃',{'N≡N':1,'H–H':3},{'N–H':6}),('CH₄ + Cl₂ → CH₃Cl + HCl',{'C–H':4,'Cl–Cl':1},{'C–H':3,'C–Cl':1,'H–Cl':1}),('2H₂ + O₂ → 2H₂O',{'H–H':2,'O=O':1},{'O–H':4})]
for r in RX:
    dh=sum(BE[k]*v for k,v in r[1].items())-sum(BE[k]*v for k,v in r[2].items())
    data=', '.join(f'{k} {BE[k]}' for k in dict.fromkeys(list(r[1])+list(r[2])))
    a('c-1-4',3,N(f'Use mean bond enthalpies ({data} kJ mol⁻¹) to find ΔH for {r[0]}.',dh,0.5,'kJ mol⁻¹','Bonds broken − bonds made.'))
FH={'CO₂(g)':-394,'H₂O(l)':-286,'CH₄(g)':-75,'C₂H₆(g)':-85,'C₂H₅OH(l)':-277,'C₃H₈(g)':-104,'NH₃(g)':-46,'NO(g)':90,'CaCO₃(s)':-1207,'CaO(s)':-635}
RX2=[('C₂H₆ + 3½O₂ → 2CO₂ + 3H₂O',{'C₂H₆(g)':1},{'CO₂(g)':2,'H₂O(l)':3}),('C₂H₅OH + 3O₂ → 2CO₂ + 3H₂O',{'C₂H₅OH(l)':1},{'CO₂(g)':2,'H₂O(l)':3}),('C₃H₈ + 5O₂ → 3CO₂ + 4H₂O',{'C₃H₈(g)':1},{'CO₂(g)':3,'H₂O(l)':4}),('CaCO₃ → CaO + CO₂',{'CaCO₃(s)':1},{'CaO(s)':1,'CO₂(g)':1})]
for r in RX2:
    dh=sum(FH[k]*v for k,v in r[2].items())-sum(FH[k]*v for k,v in r[1].items())
    data=', '.join(f'{k} {FH[k]}' for k in dict.fromkeys(list(r[1])+list(r[2])))
    a('c-1-4',3,N(f'ΔfH values ({data} kJ mol⁻¹; elements = 0). Find ΔH for {r[0]}.',dh,0.5,'kJ mol⁻¹','ΣΔfH(products) − ΣΔfH(reactants).'))
# ---------- 3.1.5 kinetics
def f():
    c0,c1,t=round(R.uniform(0.5,2),2),0,ri(20,200)
    c1=round(c0*R.uniform(0.3,0.8),2)
    T('c-1-5',2,f'[A] falls from {c0} to {c1} mol dm⁻³ in {t} s. Mean rate (× 10⁻³ mol dm⁻³ s⁻¹, 3 s.f.)?',(c0-c1)/t*1000,'× 10⁻³','Δ[A]/Δt.')
rep(4,f)
def f():
    v,t=ri(20,90),ri(10,120)
    T('c-1-5',1,f'{v} cm³ of gas is collected in {t} s. Mean rate (cm³ s⁻¹, 3 s.f.)?',v/t,'cm³ s⁻¹','Volume ÷ time.')
rep(3,f)
# ---------- 3.1.6 Kc
def f():
    a0,b0,x=round(R.uniform(0.5,2),1),round(R.uniform(0.5,2),1),None
    x=round(min(a0,b0)*R.uniform(0.3,0.8),2)
    V=pk(1,2)
    # H2 + I2 <=> 2HI, start a0 H2, b0 I2
    Kc=(2*x/V)**2/(((a0-x)/V)*((b0-x)/V))
    T('c-1-6',3,f'{a0} mol H₂ and {b0} mol I₂ in {V} dm³ reach equilibrium with {x} mol of H₂ reacted (H₂ + I₂ ⇌ 2HI). Find Kc (3 s.f.).',Kc,'','Equilibrium moles: H₂ = a − x, I₂ = b − x, HI = 2x (V cancels).')
rep(4,f)
def f():
    A,B,C=round(R.uniform(0.1,1),2),round(R.uniform(0.1,1),2),round(R.uniform(0.1,2),2)
    T('c-1-6',2,f'A + B ⇌ C. At equilibrium [A] = {A}, [B] = {B}, [C] = {C} mol dm⁻³. Kc (3 s.f.)?',C/(A*B),'mol⁻¹ dm³','Kc = [C]/[A][B].')
rep(4,f)
def f():
    n0=round(R.uniform(1,3),1);x=round(n0*R.uniform(0.2,0.6),2);V=pk(1,2,5)
    Kc=(2*x/V)**2/((n0-x)/V)
    T('c-1-6',3,f'{n0} mol N₂O₄ in {V} dm³: N₂O₄ ⇌ 2NO₂. At equilibrium {x} mol N₂O₄ has dissociated. Kc (mol dm⁻³, 3 s.f.)?',Kc,'mol dm⁻³','[NO₂] = 2x/V, [N₂O₄] = (n₀ − x)/V.')
rep(3,f)
# ---------- 3.1.7 oxidation states
OX=[('Cr in Cr₂O₇²⁻',6),('Mn in MnO₄²⁻',6),('N in NO₃⁻',5),('N in NH₄⁺',-3),('S in SO₃²⁻',4),('S in S₂O₃²⁻',2),('Cl in ClO₃⁻',5),('Cl in ClO⁻',1),('Fe in Fe₃O₄ (average)',8/3),('V in VO₂⁺',5),('V in VO²⁺',4),('C in CO₃²⁻',4),('O in H₂O₂',-1),('H in NaH',-1),('P in PO₄³⁻',5),('I in IO₃⁻',5)]
for s,v in OX:
    a('c-1-7',1 if R.random()<0.5 else 2,N(f'Oxidation state of {s}?',v,0.5,'','Sum of oxidation states = overall charge.'))
def f():
    v=round(R.uniform(10,30),2);c=pk(0.0200,0.0100)
    T('c-1-7',3,f'{v} cm³ of {c} mol dm⁻³ K₂Cr₂O₇ oxidises Fe²⁺ (Cr₂O₇²⁻ + 14H⁺ + 6Fe²⁺ → 2Cr³⁺ + 7H₂O + 6Fe³⁺). Moles of Fe²⁺ (× 10⁻³, 3 s.f.)?',6*c*v,'× 10⁻³ mol','n(Fe²⁺) = 6 × n(Cr₂O₇²⁻).')
rep(4,f)
# ---------- 3.1.8 thermodynamics
def f():
    H,S=ri(-200,200),ri(-300,300)
    while H*S<=0 or abs(H)<10: H,S=ri(-200,200),ri(-300,300)
    T('c-1-8',2,f'ΔH = {H} kJ mol⁻¹, ΔS = {S} J K⁻¹ mol⁻¹. Temperature at which ΔG = 0 (3 s.f.)?',H*1000/S,'K','T = ΔH/ΔS (units!).')
rep(4,f)
def f():
    H,S,T_=ri(-200,200),ri(-300,300),ri(250,1200)
    T('c-1-8',2,f'ΔH = {H} kJ mol⁻¹, ΔS = {S} J K⁻¹ mol⁻¹, T = {T_} K. Find ΔG (kJ mol⁻¹, 3 s.f.).',H-T_*S/1000,'kJ mol⁻¹','ΔG = ΔH − TΔS.',1)
rep(4,f)
BH=[('NaCl',{'Na at':107,'Cl at':122,'IE1 Na':496,'EA Cl':-349,'ΔfH NaCl':-411}),('KCl',{'K at':89,'Cl at':122,'IE1 K':419,'EA Cl':-349,'ΔfH KCl':-437}),('NaBr',{'Na at':107,'Br at':112,'IE1 Na':496,'EA Br':-325,'ΔfH NaBr':-361})]
for s,d in BH:
    vals=list(d.values());le=vals[4]-sum(vals[:4])
    a('c-1-8',3,N(f'Born–Haber for {s}: '+', '.join(f'{k} {v:+d}' for k,v in d.items())+' kJ mol⁻¹. Find the lattice enthalpy of formation.',le,0.5,'kJ mol⁻¹','ΔLH = ΔfH − (atomisations + IE + EA).'))
SS={'N₂':192,'H₂':131,'NH₃':193,'O₂':205,'H₂O(l)':70,'CO₂':214,'CH₄':186,'C(s)':5.7}
for eq,rs,ps in [('N₂ + 3H₂ → 2NH₃',{'N₂':1,'H₂':3},{'NH₃':2}),('CH₄ + 2O₂ → CO₂ + 2H₂O(l)',{'CH₄':1,'O₂':2},{'CO₂':1,'H₂O(l)':2}),('C(s) + O₂ → CO₂',{'C(s)':1,'O₂':1},{'CO₂':1})]:
    ds=sum(SS[k]*v for k,v in ps.items())-sum(SS[k]*v for k,v in rs.items())
    a('c-1-8',3,N(f'S° values ('+', '.join(f'{k} {SS[k]}' for k in dict.fromkeys(list(rs)+list(ps)))+f' J K⁻¹ mol⁻¹). Find ΔS for {eq}.',ds,0.5,'J K⁻¹ mol⁻¹','ΣS(products) − ΣS(reactants).'))
# ---------- 3.1.9 rate equations
def f():
    m,n,k=pk(0,1,2),pk(0,1,2),round(R.uniform(0.01,5),2)
    A,Bc=round(R.uniform(0.1,1),2),round(R.uniform(0.1,1),2)
    T('c-1-9',1,f'rate = k[A]^{m}[B]^{n}, k = {k}, [A] = {A}, [B] = {Bc} (consistent units). Rate (3 s.f.)?',k*A**m*Bc**n,'mol dm⁻³ s⁻¹','Substitute.')
rep(3,f)
def f():
    o=pk(0,1,2);fa=pk(2,3)
    T('c-1-9',2,f'When [A] is multiplied by {fa} (all else constant), the rate is multiplied by {fa**o}. What is the order with respect to A?',o,'','rate factor = (conc factor)^order.',0)
rep(4,f)
def f():
    m,n=pk(1,2),pk(0,1,2);k=round(R.uniform(0.1,9),2);A,Bc=0.10,0.20
    rate=k*A**m*Bc**n
    KU={0:'mol dm⁻³ s⁻¹',1:'s⁻¹',2:'mol⁻¹ dm³ s⁻¹',3:'mol⁻² dm⁶ s⁻¹'}
    T('c-1-9',3,f'rate = k[A]^{m}[B]^{n}. When [A] = 0.10 and [B] = 0.20 mol dm⁻³, rate = {rate:.3g} mol dm⁻³ s⁻¹. Find k (3 s.f.).',float(f'{rate:.3g}')/(A**m*Bc**n),KU[m+n],f'k = rate/([A]^{m}[B]^{n}); overall order {m+n}, so the units are {KU[m+n]}.')
rep(4,f)
def f():
    T1,T2=pk(298,300,310),pk(320,330,340);Ea=ri(40,90)
    k2k1=math.exp(-Ea*1000/Rg*(1/T2-1/T1))
    T('c-1-9',3,f'k increases by a factor of {k2k1:.3g} from {T1} K to {T2} K. Find Ea (kJ mol⁻¹, 3 s.f.).',math.log(float(f'{k2k1:.3g}'))*Rg/(1/T1-1/T2)/1000,'kJ mol⁻¹','ln(k₂/k₁) = (Ea/R)(1/T₁ − 1/T₂).')
rep(3,f)
UN=[('zero','mol dm⁻³ s⁻¹'),('first','s⁻¹'),('second','mol⁻¹ dm³ s⁻¹'),('third','mol⁻² dm⁶ s⁻¹')]
table_mc('c-1-9',2,UN,'Units of k for an overall {0}-order reaction?',0,1,'rate/[conc]^order.')
# ---------- 3.1.10 Kp
def f():
    x,P=round(R.uniform(0.1,0.7),2),ri(100,1000)
    T('c-1-10',1,f'Mole fraction {x}, total pressure {P} kPa. Partial pressure (3 s.f.)?',x*P,'kPa','p = xP.')
rep(3,f)
def f():
    na,nb,nc=round(R.uniform(0.2,2),1),round(R.uniform(0.2,2),1),round(R.uniform(0.2,2),1)
    T('c-1-10',2,f'A mixture has {na} mol N₂, {nb} mol H₂ and {nc} mol NH₃. Mole fraction of NH₃ (3 s.f.)?',nc/(na+nb+nc),'','n/n_total.')
rep(4,f)
def f():
    pa,pb=ri(20,200),ri(20,200)
    T('c-1-10',2,f'N₂O₄ ⇌ 2NO₂. p(N₂O₄) = {pa} kPa, p(NO₂) = {pb} kPa. Kp (kPa, 3 s.f.)?',pb**2/pa,'kPa','Kp = p(NO₂)²/p(N₂O₄).')
rep(3,f)
def f():
    n0=1.0;x=round(R.uniform(0.2,0.7),2);P=ri(100,500)
    nt=n0+x;pN=(n0-x)/nt*P;pO=2*x/nt*P
    T('c-1-10',3,f'1.0 mol N₂O₄ ⇌ 2NO₂; at equilibrium {x} mol N₂O₄ has dissociated and total pressure is {P} kPa. Find Kp (kPa, 3 s.f.).',pO**2/pN,'kPa','Moles: N₂O₄ 1 − x, NO₂ 2x; total 1 + x; partial pressures then Kp.')
rep(4,f)
def f():
    P=ri(100,500);xa,xb=round(R.uniform(0.2,0.4),2),round(R.uniform(0.2,0.4),2);xc=round(1-xa-xb,2)
    T('c-1-10',3,f'H₂ + I₂ ⇌ 2HI at {P} kPa: mole fractions H₂ {xa}, I₂ {xb}, HI {xc}. Kp (3 s.f.)?',xc**2/(xa*xb),'','Kp has no units here; P cancels.')
rep(3,f)
# ---------- 3.1.11 electrochemistry
EP=[('Zn²⁺/Zn',-0.76),('Fe²⁺/Fe',-0.44),('Cu²⁺/Cu',0.34),('Ag⁺/Ag',0.80),('Mg²⁺/Mg',-2.37),('Pb²⁺/Pb',-0.13),('Cl₂/Cl⁻',1.36),('Fe³⁺/Fe²⁺',0.77),('MnO₄⁻/Mn²⁺',1.51),('Br₂/Br⁻',1.09),('I₂/I⁻',0.54),('Ni²⁺/Ni',-0.25)]
def f():
    x,y=R.sample(EP,2)
    T('c-1-11',1 if R.random()<0.4 else 2,f'E° {x[0]} = {x[1]:+.2f} V and {y[0]} = {y[1]:+.2f} V. Find E°cell (3 s.f.).',abs(x[1]-y[1]),'V','E(positive) − E(negative).',0.5)
rep(8,f)
def f():
    x,y=R.sample(EP,2)
    lo=x if x[1]<y[1] else y
    a('c-1-11',2,M(f'Cell from {x[0]} ({x[1]:+.2f} V) and {y[0]} ({y[1]:+.2f} V): which half-cell is the negative electrode?',lo[0],[x[0] if lo==y else y[0],'neither – they are equal','depends on concentration only'],'The more negative E° is oxidised (negative electrode).'))
rep(4,f)
def f():
    x,y=R.sample(EP,2)
    oxid=x if x[1]>y[1] else y
    sp=oxid[0].split('/')[0]
    a('c-1-11',3,M(f'Which is the strongest oxidising agent: {x[0].split("/")[0]} (E° {x[1]:+.2f} V) or {y[0].split("/")[0]} (E° {y[1]:+.2f} V)?',sp,[ (y if oxid==x else x)[0].split('/')[0],'both equally','neither'],'More positive E° = stronger oxidising agent.'))
rep(4,f)
# ---------- 3.1.12 acids & bases
def f():
    c=pk(0.1,0.05,0.02,0.01,0.25,0.005)
    T('c-1-12',1,f'pH of {c} mol dm⁻³ HCl (3 s.f.)?',-math.log10(c),'','pH = −log[H⁺].')
rep(3,f)
def f():
    pH=round(R.uniform(1,13),2)
    T('c-1-12',1,f'[H⁺] for pH {pH} (× 10⁻ⁿ notation: give the number, e.g. 3.2e-5)?',10**-pH,'mol dm⁻³','[H⁺] = 10^(−pH).',1)
rep(2,f)
def f():
    c=pk(0.1,0.05,0.02,0.5)
    T('c-1-12',2,f'pH of {c} mol dm⁻³ NaOH at 298 K (Kw = 1.00 × 10⁻¹⁴, 3 s.f.)?',14+math.log10(c),'','[H⁺] = Kw/[OH⁻].')
rep(3,f)
def f():
    Ka,c=pk(1.74e-5,1.35e-5,6.3e-5,1.8e-4),pk(0.1,0.05,0.2,0.5)
    T('c-1-12',2,f'Weak acid, Ka = {sci(Ka,3)} mol dm⁻³, c = {c} mol dm⁻³. pH (3 s.f.)?',-math.log10(math.sqrt(Ka*c)),'','[H⁺] = √(Ka c).')
rep(4,f)
def f():
    Ka=pk(1.74e-5,1.35e-5,6.3e-5);ca,cs=round(R.uniform(0.05,0.5),2),round(R.uniform(0.05,0.5),2)
    T('c-1-12',3,f'Buffer: weak acid {ca} mol dm⁻³ and its salt {cs} mol dm⁻³, Ka = {sci(Ka,3)}. pH (3 s.f.)?',-math.log10(Ka*ca/cs),'','[H⁺] = Ka[HA]/[A⁻].')
rep(4,f)
def f():
    va,ca,vb,cb=25.0,pk(0.1,0.2),round(R.uniform(5,20),1),pk(0.1,0.2)
    ex=ca*va-cb*vb
    if ex<=0: vb=5.0;ex=ca*va-cb*vb
    T('c-1-12',3,f'{vb} cm³ of {cb} mol dm⁻³ NaOH is added to 25.0 cm³ of {ca} mol dm⁻³ HCl. pH of the mixture (3 s.f.)?',-math.log10(ex/(va+vb)),'','Excess H⁺ moles ÷ total volume.')
rep(3,f)
# ================= INORGANIC
P3=[('Na','metallic','Na₂O','ionic','giant ionic','about 14','basic'),('Mg','metallic','MgO','ionic','giant ionic','about 9','basic'),('Al','metallic','Al₂O₃','ionic (some covalent character)','giant ionic','7 (insoluble)','amphoteric'),('Si','giant covalent','SiO₂','covalent','giant covalent (macromolecular)','7 (insoluble)','acidic'),('P','simple molecular (P₄)','P₄O₁₀','covalent','simple molecular','about 0–1','acidic'),('S','simple molecular (S₈)','SO₂','covalent','simple molecular','about 2–3','acidic')]
table_mc('c-2-4',1,P3,'Formula of the oxide formed when {0} burns in excess oxygen (most common Period 3 oxide)?',0,2,'{0} forms {2}. Period 3: Na₂O, MgO, Al₂O₃, SiO₂, P₄O₁₀, SO₂.')
table_mc('c-2-4',1,P3,'Structure of the oxide {2}?',2,4,'Ionic oxides are giant; non-metal oxides are covalent.')
table_mc('c-2-4',2,P3,'pH of the solution when {2} is added to water?',2,5,'Ionic oxides give alkaline solutions; non-metal oxides give acidic solutions.')
table_mc('c-2-4',2,P3,'Acid–base character of {2}?',2,6,'{2} is {6}: metal oxides are basic, Al₂O₃ is amphoteric, non-metal oxides are acidic.')
table_mc('c-2-1',1,P3,'Structure of the element {0} at room temperature?',0,1,'{0}: {1}. Na–Al metallic; Si giant covalent; P₄, S₈ and Cl₂ simple molecular; Ar monatomic.')
P3MP=[('Na','metallic bonding, 1 delocalised electron per atom'),('Mg','metallic bonding, 2 delocalised electrons per atom, smaller ion'),('Al','metallic bonding, 3 delocalised electrons per atom'),('Si','strong covalent bonds in a giant lattice'),('P','weak van der Waals between P₄ molecules'),('S','van der Waals between larger S₈ molecules'),('Cl','weak van der Waals between Cl₂ molecules'),('Ar','very weak van der Waals between single atoms')]
table_mc('c-2-1',2,P3MP,'Which best explains the melting point of {0}?',0,1,'{0}: {1}. The stronger the bonding that must be overcome, the higher the melting point.',8)
G2=[('Mg','very slow with cold water; burns in steam to MgO + H₂','Mg(OH)₂ – least soluble hydroxide','MgSO₄ – most soluble sulfate'),('Ca','reacts steadily with cold water forming Ca(OH)₂ + H₂','Ca(OH)₂ – slightly soluble','CaSO₄ – sparingly soluble'),('Sr','reacts quickly with cold water','Sr(OH)₂ – fairly soluble','SrSO₄ – very sparingly soluble'),('Ba','reacts vigorously with cold water','Ba(OH)₂ – most soluble hydroxide','BaSO₄ – insoluble')]
table_mc('c-2-2',1,G2,'Reaction of {0} with water?',0,1,'Reactivity increases down the group.')
table_mc('c-2-2',2,G2,'Which statement about the hydroxide of {0} is correct?',0,2,'Hydroxide solubility increases down the group.')
table_mc('c-2-2',2,G2,'Which statement about the sulfate of {0} is correct?',0,3,'Sulfate solubility decreases down the group.')
USE=[('Mg(OH)₂','antacid for indigestion'),('Ca(OH)₂','neutralising acidic soil'),('BaSO₄','barium meal for X-rays'),('CaO / CaCO₃','removing SO₂ from flue gases'),('Mg','extracting titanium from TiCl₄'),('BaCl₂ (acidified)','testing for sulfate ions')]
table_mc('c-2-2',1,USE,'A use of {0}?',0,1,'{0} is used for {1}.')
table_mc('c-2-2',3,[(b,a_) for a_,b in USE],'Which Group 2 compound or element is used for {0}?',0,1,'{1} is used for {0}.')
HAL=[('Cl⁻','white precipitate','dissolves in dilute NH₃','HCl only (steamy fumes)'),('Br⁻','cream precipitate','dissolves in concentrated NH₃ only','HBr, Br₂ (orange-brown) and SO₂'),('I⁻','yellow precipitate','insoluble even in concentrated NH₃','HI, I₂ (purple/black), S and H₂S (bad eggs)'),('F⁻','no precipitate (AgF soluble)','–','HF only (steamy fumes)')]
table_mc('c-2-3',1,[h for h in HAL],'Result of adding acidified AgNO₃(aq) to a solution of {0}?',0,1,'Silver halide precipitates.')
table_mc('c-2-3',2,HAL[:3],'Solubility of the silver halide precipitate from {0} in ammonia?',0,2,'AgCl dissolves in dilute NH₃, AgBr only in concentrated NH₃, and AgI in neither.')
table_mc('c-2-3',3,HAL,'Products when solid sodium halide containing {0} reacts with concentrated H₂SO₄?',0,3,'Reducing power increases down the group.')
DISP=[('Cl₂(aq) + KBr(aq)','orange solution – Br₂ displaced'),('Cl₂(aq) + KI(aq)','brown solution – I₂ displaced'),('Br₂(aq) + KI(aq)','brown solution – I₂ displaced'),('Br₂(aq) + KCl(aq)','no reaction'),('I₂(aq) + KBr(aq)','no reaction')]
for r in DISP:
    a('c-2-3',2,M(f'Observation for {r[0]}?',r[1],[x for x in ['orange solution – Br₂ displaced','brown solution – I₂ displaced','no reaction','white precipitate'] if x!=r[1]][:3],'A more reactive halogen displaces a less reactive halide.'))
CX=[('[Cu(H₂O)₆]²⁺','octahedral','6','+2','blue'),('[CuCl₄]²⁻','tetrahedral','4','+2','yellow'),('[Co(NH₃)₆]²⁺','octahedral','6','+2','pale brown (straw)'),('[CoCl₄]²⁻','tetrahedral','4','+2','blue'),('[Ag(NH₃)₂]⁺','linear','2','+1','colourless'),('[Pt(NH₃)₂Cl₂]','square planar','4','+2','pale yellow'),('[Fe(H₂O)₆]³⁺','octahedral','6','+3','pale violet (yellow in solution)'),('[Cr(H₂O)₆]³⁺','octahedral','6','+3','violet (green in solution)'),('[Cu(NH₃)₄(H₂O)₂]²⁺','octahedral','6','+2','deep blue'),('[Co(H₂O)₆]²⁺','octahedral','6','+2','pink')]
table_mc('c-2-5',1,CX,'Shape of {0}?',0,1,'Small ligands → 6; large Cl⁻ → 4 (tetrahedral).',6)
table_mc('c-2-5',2,CX,'Oxidation state of the metal in {0}?',0,3,'Charge of complex − total ligand charge.',6)
table_mc('c-2-5',2,CX,'Colour of {0}?',0,4,'{0} is {4}. Colour depends on the metal, its oxidation state, the ligands and the co-ordination number.',6)
def f():
    lam=ri(400,700)
    T('c-2-5',3,f'A complex absorbs light of wavelength {lam} nm. Find ΔE (× 10⁻¹⁹ J, 3 s.f.; h = 6.63 × 10⁻³⁴, c = 3.00 × 10⁸).',6.63e-34*3e8/(lam*1e-9)/1e-19,'× 10⁻¹⁹ J','ΔE = hc/λ.')
rep(3,f)
def f():
    A_,eps,l=round(R.uniform(0.2,1.2),2),pk(10,20,50),1.0
    T('c-2-5',3,f'Colorimetry: absorbance {A_}, calibration gives A = {eps}c (c in mol dm⁻³). Find c (3 s.f.).',A_/eps,'mol dm⁻³','A ∝ c.')
rep(2,f)
AQ=[('Cu²⁺','blue precipitate','blue precipitate (no change)','blue precipitate','deep blue solution','blue-green precipitate (CuCO₃)'),('Fe²⁺','green precipitate','green precipitate (no change)','green precipitate','green precipitate (no change)','green precipitate (FeCO₃)'),('Fe³⁺','orange-brown precipitate','orange-brown precipitate (no change)','orange-brown precipitate','orange-brown precipitate (no change)','brown precipitate + CO₂ bubbles'),('Al³⁺','white precipitate','colourless solution','white precipitate','white precipitate (no change)','white precipitate + CO₂ bubbles')]
table_mc('c-2-6',1,AQ,'Observation when a few drops of NaOH(aq) are added to {0}(aq)?',0,1,'Metal hydroxide precipitates.')
table_mc('c-2-6',2,AQ,'Observation with excess NaOH(aq) for {0}(aq)?',0,2,'Only amphoteric Al(OH)₃ dissolves.')
table_mc('c-2-6',2,AQ,'Observation with excess NH₃(aq) for {0}(aq)?',0,4,'Cu²⁺ undergoes ligand substitution with NH₃.')
table_mc('c-2-6',3,AQ,'Observation with Na₂CO₃(aq) for {0}(aq)?',0,5,'3+ ions are acidic enough to release CO₂.')
# ================= ORGANIC
RXN=[('c-3-2','methane → chloromethane','Cl₂, UV light','free-radical substitution'),
('c-3-3','bromoethane → ethanol','NaOH(aq), warm','nucleophilic substitution'),
('c-3-3','bromoethane → ethene','KOH in ethanol, hot','elimination'),
('c-3-3','bromoethane → propanenitrile','KCN in aqueous ethanol, reflux','nucleophilic substitution'),
('c-3-3','bromoethane → ethylamine','excess NH₃ in ethanol, heat under pressure','nucleophilic substitution'),
('c-3-4','ethene → bromoethane','HBr, room temperature','electrophilic addition'),
('c-3-4','ethene → 1,2-dibromoethane','Br₂, room temperature','electrophilic addition'),
('c-3-4','ethene → ethyl hydrogensulfate','cold concentrated H₂SO₄','electrophilic addition'),
('c-3-5','ethene → ethanol','steam, H₃PO₄ catalyst, 300 °C, 6–7 MPa','hydration (electrophilic addition)'),
('c-3-5','glucose → ethanol','yeast, 35 °C, anaerobic','fermentation'),
('c-3-5','ethanol → ethanal','acidified K₂Cr₂O₇, distil as formed','oxidation'),
('c-3-5','ethanol → ethanoic acid','excess acidified K₂Cr₂O₇, reflux','oxidation'),
('c-3-5','propan-2-ol → propanone','acidified K₂Cr₂O₇, heat','oxidation'),
('c-3-5','ethanol → ethene','concentrated H₃PO₄, heat','elimination (dehydration)'),
('c-3-8','propanal → propan-1-ol','NaBH₄ in aqueous solution','nucleophilic addition'),
('c-3-8','propanone → 2-hydroxy-2-methylpropanenitrile','KCN then dilute acid','nucleophilic addition'),
('c-3-9','ethanoic acid → ethyl ethanoate','ethanol, concentrated H₂SO₄ catalyst, heat','esterification'),
('c-3-9','ethyl ethanoate → ethanoic acid + ethanol','dilute acid, reflux','hydrolysis'),
('c-3-9','ethanoyl chloride → ethanamide','concentrated NH₃','nucleophilic addition–elimination'),
('c-3-9','ethanoyl chloride → N-methylethanamide','methylamine','nucleophilic addition–elimination'),
('c-3-9','ethanoic anhydride → aspirin','with 2-hydroxybenzoic acid','nucleophilic addition–elimination'),
('c-3-10','benzene → nitrobenzene','concentrated HNO₃ + concentrated H₂SO₄, 50 °C','electrophilic substitution'),
('c-3-10','benzene → phenylethanone','CH₃COCl, AlCl₃ catalyst','electrophilic substitution (Friedel–Crafts acylation)'),
('c-3-11','nitrobenzene → phenylamine','Sn + concentrated HCl, then NaOH','reduction'),
('c-3-11','propanenitrile → propylamine','LiAlH₄ or H₂/Ni','reduction'),
('c-3-11','ethylamine → N-ethylethanamide','ethanoyl chloride','nucleophilic addition–elimination')]
for tid,ch,reag,mech in RXN:
    others=[r[2] for r in RXN if r[2]!=reag];R.shuffle(others)
    a(tid,1,M(f'Reagents/conditions for {ch}?',reag,others[:3],f'Mechanism: {mech}.'))
    om=list(dict.fromkeys(r[3] for r in RXN if r[3]!=mech));R.shuffle(om)
    a(tid,2,M(f'Mechanism/type of reaction for {ch} ({reag})?',mech,om[:3],f'{ch} with {reag} is {mech}.'))
    a('c-3-14',3 if R.random()<0.6 else 2,M(f'Synthesis step: which reagents convert {ch.replace(" → "," into ")}?',reag,others[3:6],f'{mech}.'))
NAME=[('CH₃CH₂CH₂OH','propan-1-ol'),('CH₃CH(OH)CH₃','propan-2-ol'),('CH₃CH₂CHO','propanal'),('CH₃COCH₃','propanone'),('CH₃CH₂COOH','propanoic acid'),('CH₃COOCH₂CH₃','ethyl ethanoate'),('CH₃CH₂CH₂Br','1-bromopropane'),('CH₃CHBrCH₃','2-bromopropane'),('CH₂=CHCH₃','propene'),('CH₃CH₂NH₂','ethylamine'),('CH₃CONH₂','ethanamide'),('CH₃COCl','ethanoyl chloride'),('CH₃CH₂CN','propanenitrile'),('(CH₃)₃COH','2-methylpropan-2-ol'),('CH₃CH=CHCH₃','but-2-ene'),('C₆H₅NH₂','phenylamine'),('HCOOCH₃','methyl methanoate'),('CH₃CH(CH₃)CH₂CH₃','2-methylbutane')]
table_mc('c-3-1',1,NAME,'IUPAC name of {0}?',0,1,'{0} is {1}: the longest carbon chain gives the stem, the functional group gives the suffix or prefix, with the lowest locant.',8)
table_mc('c-3-1',2,NAME,'IUPAC name of {0}?',0,1,'{0} is {1}: the longest carbon chain gives the stem, the functional group gives the suffix or prefix, with the lowest locant.',8)
CLS=[('propan-1-ol','primary alcohol'),('propan-2-ol','secondary alcohol'),('2-methylpropan-2-ol','tertiary alcohol'),('butan-2-ol','secondary alcohol'),('ethanol','primary alcohol'),('2-methylbutan-2-ol','tertiary alcohol')]
table_mc('c-3-5',1,CLS,'{0} is a',0,1,'Count carbons attached to the C–OH carbon.')
TESTS=[('alkene','bromine water: orange → colourless'),('aldehyde','Tollens\u2019 reagent: silver mirror'),('carboxylic acid','Na₂CO₃: effervescence (CO₂)'),('primary/secondary alcohol','acidified K₂Cr₂O₇: orange → green'),('halogenoalkane','warm with NaOH(aq), acidify, AgNO₃: precipitate'),('aldehyde or ketone','2,4-DNPH: orange precipitate')]
table_mc('c-3-6',1,TESTS,'A positive test for a {0}?',0,1,'{0}: {1}.')
table_mc('c-3-6',2,[(b,a_) for a_,b in TESTS],'{0} indicates a',0,1,'{0} is the positive test for a {1}.')
IR=[('O–H (alcohols)','3230–3550 cm⁻¹ (broad)'),('O–H (acids)','2500–3000 cm⁻¹ (very broad)'),('C=O','1680–1750 cm⁻¹'),('N–H','3300–3500 cm⁻¹'),('C–H','2850–3300 cm⁻¹'),('C=C','1620–1680 cm⁻¹'),('C≡N','2220–2260 cm⁻¹')]
table_mc('c-3-6',2,IR,'IR absorption range for {0}?',0,1,'Data sheet.')
def f():
    m,mr=pk((44.0,'C₃H₈ or CO₂'),(28.0,'C₂H₄ or CO')),None
    a('c-3-6',3,M('High-resolution MS gives M⁺ = 44.0262. Which formula fits? (C 12.0000, H 1.0078, O 15.9949)','C₂H₄O',['C₃H₈','CO₂','CH₄N₂'],'C₂H₄O = 44.0262; C₃H₈ = 44.0624; CO₂ = 43.9898.'))
f()
CHI=[('butan-2-ol','yes'),('2-bromobutane','yes'),('propan-2-ol','no'),('2-hydroxypropanoic acid (lactic acid)','yes'),('alanine (2-aminopropanoic acid)','yes'),('glycine (aminoethanoic acid)','no'),('1-chloropropane','no'),('2-chlorobutane','yes'),('3-methylhexane','yes'),('pentan-3-ol','no')]
table_mc('c-3-7',1,[(a_,'Yes – it has a chiral carbon' if b=='yes' else 'No – no carbon has four different groups') for a_,b in CHI],'Does {0} show optical isomerism?',0,1,'Look for a carbon with four different groups.') if False else None
for nm,y in CHI:
    a('c-3-7',2 if R.random()<0.5 else 1,M(f'Does {nm} show optical isomerism?','Yes – it has a chiral carbon' if y=='yes' else 'No – no carbon has four different groups',['No – no carbon has four different groups' if y=='yes' else 'Yes – it has a chiral carbon','Only E/Z isomerism','Only when heated'],'Look for a carbon with four different groups.'))
NMR=[('propanone',1,2),('ethanol',3,2),('propan-1-ol',4,3),('propan-2-ol',3,2),('ethyl ethanoate',3,4),('methylpropane',2,2),('benzene',1,1),('butanone',4,4),('ethanoic acid',2,2),('1-chloropropane',3,3),('2-chloropropane',2,2),('methyl propanoate',3,4)]
for nm,h1,c13 in NMR:
    a('c-3-15',R.choice([1,2,2,3]),N(f'Number of peaks in the ¹H NMR spectrum of {nm}?',h1,0,'','Count H environments.'))
    a('c-3-15',R.choice([1,2,3]),N(f'Number of peaks in the ¹³C NMR spectrum of {nm}?',c13,0,'','Count C environments.'))
SPLIT=[('CH₃ next to CH₂','triplet'),('CH₂ next to CH₃','quartet'),('CH next to two CH₃ groups','septet (heptet)'),('CH₃ next to CH','doublet'),('CH₃ next to C=O (no adjacent H)','singlet'),('CH₂ between CH₃ and C=O','quartet')]
table_mc('c-3-15',2,SPLIT,'¹H NMR splitting for a {0}?',0,1,'n + 1 rule.')
def f():
    d,s=round(R.uniform(1,6),1),round(R.uniform(6.5,9),1)
    T('c-3-16',1,f'Spot {d} cm, solvent front {s} cm. Rf (3 s.f.)?',d/s,'','Rf = spot ÷ front.')
rep(4,f)
def f():
    rf,s=round(R.uniform(0.2,0.8),2),round(R.uniform(6,10),1)
    T('c-3-16',2,f'Rf = {rf}, solvent front {s} cm. Distance moved by the spot (cm, 3 s.f.)?',rf*s,'cm','d = Rf × front.')
rep(3,f)
POLY=[('ethene','addition','poly(ethene)'),('propene','addition','poly(propene)'),('chloroethene','addition','PVC'),('ethane-1,2-diol + benzene-1,4-dicarboxylic acid','condensation','Terylene (PET, a polyester)'),('hexane-1,6-diamine + hexanedioic acid','condensation','nylon-6,6 (a polyamide)'),('benzene-1,4-diamine + benzene-1,4-dicarbonyl chloride','condensation','Kevlar (a polyamide)'),('2-hydroxypropanoic acid','condensation','poly(lactic acid) (a polyester)')]
table_mc('c-3-12',1,POLY,'Polymer made from {0}?',0,2,'{0} gives {2} by {1} polymerisation.')
for r in POLY:
    a('c-3-12',2,M(f'Type of polymerisation for {r[0]} → {r[2]}?',r[1]+' polymerisation',['addition polymerisation' if r[1]=='condensation' else 'condensation polymerisation','free-radical substitution','hydrolysis'],'Condensation eliminates a small molecule.'))
AA=[('glycine','H'),('alanine','CH₃'),('serine','CH₂OH'),('cysteine','CH₂SH'),('lysine','(CH₂)₄NH₂'),('aspartic acid','CH₂COOH')]
table_mc('c-3-13',1,AA,'R group of {0}?',0,1,'General formula H₂NCH(R)COOH.')
PH=[('in strong acid (low pH)','H₃N⁺CH(R)COOH (cation)'),('at the isoelectric point','H₃N⁺CH(R)COO⁻ (zwitterion)'),('in strong alkali (high pH)','H₂NCH(R)COO⁻ (anion)')]
for p_,s in PH:
    a('c-3-13',2,M(f'Form of an amino acid {p_}?',s,[x for _,x in PH if x!=s]+['H₂NCH(R)COOH (neutral molecule)'],'Low pH protonates NH₂ to NH₃⁺; high pH deprotonates COOH to COO⁻; at the isoelectric point both are ionised (zwitterion).'))
for n_ in (2,3,4):
    a('c-3-13',3,N(f'How many water molecules are released when {n_+1} amino acids join into one chain?',n_,0,'','One per peptide bond.'))
def f():
    m1,m2=round(R.uniform(2,10),2),None
    y=round(R.uniform(40,95),0)
    mr1,mr2=pk((46.0,88.0,'ethanol','ethyl ethanoate'),(60.0,102.0,'propan-1-ol','propyl ethanoate'))[0:2],None
    T('c-3-14',3,f'{m1} g ethanol (Mr 46.0) gives ethyl ethanoate (Mr 88.0) in {int(y)}% yield. Mass of ester (g, 3 s.f.)?',m1/46*88*y/100,'g','Moles × Mr × yield.')
rep(3,f)
def f():
    y1,y2,y3=ri(50,95),ri(50,95),ri(50,95)
    T('c-3-14',3,f'A 3-step synthesis has yields {y1}%, {y2}% and {y3}%. Overall yield (%, 3 s.f.)?',y1*y2*y3/1e4,'%','Multiply the fractions.')
rep(3,f)
ALK=[('C₈H₁₈','2CO₂? no'),]
def f():
    n=ri(5,12)
    T('c-3-2',1,f'Molecular formula of the alkane with {n} carbons: how many H atoms?',2*n+2,'','CₙH₂ₙ₊₂.',0)
rep(3,f)
def f():
    n=ri(3,10)
    T('c-3-2',2,f'Moles of O₂ needed to burn 1 mol of an alkane with {n} carbons completely.',(3*n+1)/2,'mol','CₙH₂ₙ₊₂ + (3n + 1)/2 O₂.')
rep(3,f)
def f():
    n=ri(4,8)
    T('c-3-4',1,f'How many H atoms in an alkene with {n} carbons and one C=C?',2*n,'','CₙH₂ₙ.',0)
rep(2,f)
def f():
    m=round(R.uniform(1,10),2)
    T('c-3-5',2,f'Mass of ethanol from {m} g glucose by fermentation (Mr 180.0 → 2 × 46.0), 3 s.f.?',m/180*2*46,'g','1 glucose → 2 ethanol.')
rep(2,f)
