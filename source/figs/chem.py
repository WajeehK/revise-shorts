from lib import *
import math
F={}
def fig(name,alt,w,h):
    def d(fn): F[name]=svg(w,h,fn(),alt); return fn
    return d
@fig('c-orbitals','Shapes of s and p orbitals',340,150)
def _():
    o=[C(45,70,26,BL,2,fill=BL+'33'),T(45,70,'•',INK,10),T(45,122,'s (sphere)',INK,12)]
    def lobe(cx,cy,ang,c):
        a=math.radians(ang); out=''
        for sg in (1,-1):
            x,y=cx+sg*20*math.cos(a),cy-sg*20*math.sin(a)
            out+=f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="20" ry="11" transform="rotate({-ang} {f(x)} {f(y)})" stroke="{c}" stroke-width="2" fill="{c}" fill-opacity=".2"/>'
        return out
    for k,(lab,ang) in enumerate([('p_x',0),('p_y',90),('p_z',35)]):
        cx=135+k*85; o+=[L(cx-38,70,cx+38,70,GY,1,'3 3'),L(cx,32,cx,108,GY,1,'3 3'),lobe(cx,70,ang,[OR,GR,PU][k]),T(cx,122,lab,INK,13)]
    o+=[T(170,143,'p orbitals: dumbbells along x, y, z. Each orbital holds 2 e⁻',INK,11.5)]
    return o
@fig('c-ie-period3','First ionisation energies across Period 3',340,220)
def _():
    el=['Na','Mg','Al','Si','P','S','Cl','Ar']; v=[496,738,578,787,1012,1000,1251,1521]
    a=Ax(50,25,270,145,0,7.4,300,1600); pts=[(a.X(i),a.Y(x)) for i,x in enumerate(v)]
    o=[a.axes('','1st IE / kJ mol⁻¹'),PL(pts,BL,2.2)]
    for i,x in enumerate(v): o+=[C(*pts[i],4,BL,1,fill=BL),T(a.X(i),184,el[i],INK,12)]
    o+=[T(a.X(2)-6,a.Y(578)+18,'Al: 3p e⁻ higher in energy',RD,11,'start'),T(a.X(5)-4,a.Y(1000)+18,'S: paired 3p e⁻ repel',RD,11,'start'),
        a.yt(500,'500'),a.yt(1000,'1000'),a.yt(1500,'1500'),T(185,206,'General rise: more protons, same shielding',INK,12)]
    return o
@fig('c-shapes','Shapes of molecules from electron-pair repulsion',340,250)
def _():
    o=[]
    def cell(k,name,ang,body):
        x=45+(k%4)*83; y=58+(k//4)*118
        o.append(G(body,x,y)); o.append(T(x,y+42,name,INK,11,b=True)); o.append(T(x,y+55,ang,GY,11))
    cell(0,'linear','180°  CO₂',[bond(-30,0,-9,0),bond(9,0,30,0),atom(0,0,'C',size=13),atom(-36,0,'O',size=12),atom(36,0,'O',size=12)])
    cell(1,'trig. planar','120°  BF₃',[bond(0,0,0,-26),bond(0,0,-23,13),bond(0,0,23,13),atom(0,0,'B',size=13),atom(0,-32,'F',size=12),atom(-28,16,'F',size=12),atom(28,16,'F',size=12)])
    cell(2,'tetrahedral','109.5°  CH₄',[bond(0,0,0,-28),bond(0,0,-24,10),wedge(0,0,22,16),hashb(0,0,22,-2) if False else hashb(2,2,26,0),atom(0,0,'C',size=13),atom(0,-32,'H',size=12),atom(-29,12,'H',size=12),atom(26,20,'H',size=12),atom(31,-2,'H',size=12)])
    cell(3,'pyramidal','107°  NH₃',[bond(0,0,-24,14),wedge(0,0,22,18),hashb(2,2,27,2),atom(0,0,'N',size=13),lp(0,-14,90),atom(-29,16,'H',size=12),atom(26,22,'H',size=12),atom(32,2,'H',size=12)])
    cell(4,'bent','104.5°  H₂O',[bond(0,0,-22,16),bond(0,0,22,16),atom(0,0,'O',size=13),lp(-8,-12,60),lp(8,-12,120),atom(-27,20,'H',size=12),atom(27,20,'H',size=12)])
    cell(5,'trig. bipyramidal','120° & 90°  PCl₅',[bond(0,0,0,-28),bond(0,0,0,28),bond(0,0,-26,4),wedge(0,0,18,12),hashb(2,1,18,-10),atom(0,0,'P',size=13),atom(0,-32,'Cl',size=10),atom(0,32,'Cl',size=10),atom(-33,4,'Cl',size=10),atom(26,15,'Cl',size=10),atom(26,-13,'Cl',size=10)])
    cell(6,'octahedral','90°  SF₆',[bond(0,0,0,-28),bond(0,0,0,28),bond(0,0,-28,0),bond(0,0,28,0),wedge(0,0,-16,14),hashb(1,-1,17,-14),atom(0,0,'S',size=13),atom(0,-32,'F',size=11),atom(0,32,'F',size=11),atom(-32,0,'F',size=11),atom(32,0,'F',size=11),atom(-20,18,'F',size=11),atom(21,-18,'F',size=11)])
    o+=[T(294,166,'Lone pairs',INK,10.5),T(294,180,'repel more',INK,10.5),T(294,194,'than bonding',INK,10.5),T(294,208,'pairs: ≈2.5°',INK,10.5),T(294,222,'less per pair',INK,10.5)]
    return o
@fig('c-profiles','Energy profiles for exothermic and endothermic reactions',340,200)
def _():
    o=[]
    for k,(name,r,p,c) in enumerate([('Exothermic (ΔH < 0)',3,1,RD),('Endothermic (ΔH > 0)',1,3,BL)]):
        a=Ax(25+k*165,30,135,120,0,10,0,6)
        hump=lambda x,r=r,p=p: r+(p-r)*(1/(1+math.exp(-(x-5)*1.4)))+2.4*math.exp(-((x-5)/1.6)**2)
        o+=[a.axes('progress','energy'),a.curve(hump,0.5,9.5,INK),A(a.X(8.6),a.Y(r),a.X(8.6),a.Y(p),c,1.8,7),T(a.X(8.9),a.Y((r+p)/2),'ΔH',c,12,'start'),
            L(a.X(0.5),a.Y(r),a.X(8.8),a.Y(r),GY,1,'3 3'),A(a.X(3.1),a.Y(r),a.X(3.1),a.Y(hump(5))+2,OR,1.6,7),T(a.X(2.9),a.Y((r+hump(5))/2+0.3),'Eₐ',OR,12,'end'),
            T(a.X(1.2),a.Y(r)+11,'reactants',GY,10,'start'),T(a.X(9.5),a.Y(p)+11 if p<r else a.Y(p)-10,'products',GY,10,'end'),T(a.x+68,178,name,c,12,b=True)]
    return o
@fig('c-maxwell','Maxwell–Boltzmann distribution at two temperatures with activation energy',340,232)
def _():
    a=Ax(40,25,270,140,0,10,0,1.0)
    mb=lambda e,T: (e**0.5)*math.exp(-e/T)/(T**1.5)*2.05
    o=[a.area(lambda e:mb(e,1.6),6.5,10,BL,0.25),a.area(lambda e:mb(e,1.0),6.5,10,RD,0.35),a.axes('energy','number of molecules'),
       a.curve(lambda e:mb(e,1.0),0,10,RD),a.curve(lambda e:mb(e,1.6),0,10,BL),L(a.X(6.5),a.Y(0),a.X(6.5),a.Y(0.8),INK,1.6,'5 4'),T(a.X(6.5),a.Y(0.86),'Eₐ',INK,13,b=True),
       T(a.X(1.6),a.Y(0.92),'T₁',RD,12,b=True),T(a.X(3.6),a.Y(0.55),'T₂ > T₁',BL,12,'start',b=True),
       T(170,192,'Higher T: peak lower and further right; area unchanged.',INK,11.5),T(170,207,'Many more molecules have E ≥ Eₐ (shaded).',INK,11.5),T(170,222,'Curve starts at the origin and never touches the energy axis',GY,10)]
    return o
@fig('c-catalyst','Energy profile with and without a catalyst',340,206)
def _():
    a=Ax(40,25,270,130,0,10,0,7)
    base=lambda x:3+(1-3)*(1/(1+math.exp(-(x-5)*1.4)))
    o=[a.axes('progress of reaction','energy'),a.curve(lambda x:base(x)+3*math.exp(-((x-5)/1.6)**2),0.5,9.5,INK),a.curve(lambda x:base(x)+1.4*math.exp(-((x-5)/1.6)**2),0.5,9.5,GR,2.4,dash='6 4'),
       A(a.X(5),a.Y(3),a.X(5),a.Y(5)+2,INK,1.4,6),A(a.X(4.6),a.Y(3),a.X(4.6),a.Y(3.59)+2,GR,1.6,6),L(a.X(0.6),a.Y(6.4),a.X(1.6),a.Y(6.4),INK,2.2),T(a.X(1.8),a.Y(6.4),'uncatalysed (higher Eₐ)',INK,11,'start'),
       L(a.X(0.6),a.Y(5.6),a.X(1.6),a.Y(5.6),GR,2.2,'6 4'),T(a.X(1.8),a.Y(5.6),'catalysed (lower Eₐ)',GR,11,'start'),
       L(a.X(0.5),a.Y(3),a.X(4.5),a.Y(3),GY,1,'3 3'),T(170,184,'A catalyst gives an alternative route with lower Eₐ;',INK,11.5),T(170,199,'ΔH is unchanged',INK,11.5)]
    return o
def _bh(q=False):
    S=0.19; base=262; Y=lambda e: base-(e+411)*S   # energy (kJ/mol relative to elements=0) → y
    lv={'el':0,'naG':107,'cl':229,'ion':725,'ea':376,'nacl':-411}
    o=[]
    def lev(e,x1,x2,lab,a='start',dx=4):
        return L(x1,Y(e),x2,Y(e),INK,2)+T(x2+dx if a=='start' else x1-dx,Y(e),lab,INK,10.5,a)
    o+=[lev(0,40,190,'Na(s) + ½Cl₂(g)'),lev(107,40,190,'Na(g) + ½Cl₂(g)'),lev(229,40,190,'Na(g) + Cl(g)'),lev(725,40,190,'Na⁺(g) + e⁻ + Cl(g)'),
        L(140,Y(376),312,Y(376),INK,2),T(312,Y(376)-10,'Na⁺(g) + Cl⁻(g)',INK,10.5,'end'),L(40,Y(-411),312,Y(-411),INK,2),T(70,Y(-411)-8,'NaCl(s)',INK,10.5,'start')]
    o+=[A(60,Y(0),60,Y(107),BL,1.8,7),T(64,(Y(0)+Y(107))/2,'+107 atomisation Na',BL,10,'start'),
        A(60,Y(107),60,Y(229),BL,1.8,7),T(64,(Y(107)+Y(229))/2,'+122 atomisation Cl',BL,10,'start'),
        A(60,Y(229),60,Y(725),BL,1.8,7),T(64,(Y(229)+Y(725))/2,'+496 1st IE Na',BL,10,'start'),
        A(150,Y(725),150,Y(376),RD,1.8,7),T(154,(Y(725)+Y(376))/2+18,'−349 EA Cl',RD,10,'start'),
        A(300,Y(376),300,Y(-411),RD,2.2,8),T(294,Y(-250),'lattice formation',RD,10,'end'),T(294,Y(-250)+13,'enthalpy = ?' if q else 'enthalpy = −787',RD,10.5,'end',b=True),
        A(48,Y(0),48,Y(-411),PU,1.8,7),T(52,Y(-200),'−411 ΔfH',PU,10,'start')]
    o+=[T(170,282,'Values in kJ mol⁻¹',INK,11)] if q else [T(170,282,'ΔfH = sum of all the other steps, so',INK,11),T(170,296,'LE = −411 − (107 + 122 + 496 − 349) = −787 kJ mol⁻¹',INK,11,b=True)]
    return o
fig('c-born-haber','Born–Haber cycle for sodium chloride',340,306)(lambda:_bh())
fig('c-born-haber-q','Born–Haber cycle for sodium chloride (lattice enthalpy unknown)',340,292)(lambda:_bh(True))
@fig('c-cell','Zinc–copper electrochemical cell with a salt bridge',340,230)
def _():
    o=[R(30,95,110,95,INK,2,fill='#d8ecff',rx=6),R(200,95,110,95,INK,2,fill='#cfe6ff',rx=6),R(30,120,110,70,'none',0,fill=BL,op=0.18),R(200,120,110,70,'none',0,fill=BL,op=0.35),
       R(70,60,16,110,INK,2,fill='#b8bec7'),R(254,60,16,110,INK,2,fill='#d9894a'),
       P('M110,128 L110,70 Q170,40 230,70 L230,128',INK,10,'none'),P('M110,128 L110,70 Q170,40 230,70 L230,128','#fff6d6',7,'none'),
       wire([(78,60),(78,28),(155,28)]),wire([(185,28),(262,28),(262,60)]),meter(170,28,'V'),
       T(78,180,'Zn',INK,12,b=True),T(262,180,'Cu',INK,12,b=True),T(85,205,'Zn²⁺(aq) 1.00 mol dm⁻³',INK,10.5),T(255,205,'Cu²⁺(aq) 1.00 mol dm⁻³',INK,10.5),
       T(170,90,'salt bridge',GY,10.5),T(170,103,'(KNO₃ aq)',GY,10.5),T(36,42,'− electrode',BL,10.5,'start'),T(304,42,'+ electrode',RD,10.5,'end'),A(110,18,140,18,OR,1.4,6),T(100,12,'e⁻',OR,11),
       T(170,222,'Zn(s) | Zn²⁺(aq) || Cu²⁺(aq) | Cu(s)   E°cell = +1.10 V',INK,11,b=True)]
    return o
@fig('c-she','Standard hydrogen electrode',340,230)
def _():
    o=[R(60,100,120,90,INK,2,fill='#fff',rx=6),R(60,125,120,65,'none',0,fill=BL,op=0.25),
       P('M100,40 L100,150 Q120,165 140,150 L140,40',INK,2,'none'),R(112,135,16,16,INK,1.5,fill='#cfcfd6'),wire([(120,135),(120,20),(230,20)]),
       A(30,60,96,60,GY,1.6,7),T(30,50,'H₂(g) 100 kPa',INK,10.5,'start'),T(120,168,'',INK),
       T(190,145,'platinum electrode',INK,11,'start'),A(188,145,130,143,GY,1.2,6),T(190,175,'1.00 mol dm⁻³ H⁺(aq)',INK,11,'start'),T(190,190,'298 K',INK,11,'start'),
       T(235,20,'to the other half-cell',GY,10.5,'start'),T(170,214,'2H⁺(aq) + 2e⁻ ⇌ H₂(g)   E° = 0.00 V',INK,12,b=True)]
    return o
@fig('c-titration','pH curves: strong acid–strong base and weak acid–strong base',340,230)
def _():
    o=[]
    def sa(v):  # 25 cm3 0.1 HCl + 0.1 NaOH
        na,nb=2.5e-3,v*1e-4; V=(25+v)/1000
        if abs(na-nb)<1e-9: return 7
        return -math.log10((na-nb)/V) if na>nb else 14+math.log10((nb-na)/V)
    def wa(v):
        na,nb=2.5e-3,v*1e-4; V=(25+v)/1000; Ka=1.74e-5
        if v<0.05: c=0.1; return -math.log10(math.sqrt(Ka*c))
        if nb<na-1e-9: return -math.log10(Ka)+math.log10(nb/(na-nb))
        if abs(nb-na)<1e-9: c=na/V; return 14+math.log10(math.sqrt(1e-14/Ka*c))
        return 14+math.log10((nb-na)/V)
    for k,(name,fn) in enumerate([('strong acid + strong base',sa),('weak acid + strong base',wa)]):
        a=Ax(30+k*165,25,135,135,0,50,0,14)
        o+=[a.axes('V / cm³','pH'),a.curve(fn,0,50,[RD,BL][k],2.4,300),L(a.X(25),a.Y(0),a.X(25),a.Y(13),GY,1,'3 3'),a.xt(25,'25'),a.yt(7,'7'),T(a.x+68,186,name,INK,11,b=True)]
        if k==1: o+=[a.dot(12.5,4.76,OR),T(a.X(12.5),a.Y(4.76)-12,'pH = pKₐ',OR,10.5),T(a.X(12.5),a.Y(4.76)+14,'(half-neutralised)',OR,9.5)]
    o+=[T(170,207,'25.0 cm³ of 0.100 mol dm⁻³ acid, 0.100 mol dm⁻³ NaOH added.',INK,10.5),T(170,222,'Choose an indicator that changes in the vertical section',INK,10.5)]
    return o
@fig('c-rate-orders','Rate against concentration for zero, first and second order',340,180)
def _():
    o=[]
    for k,(name,fn) in enumerate([('zero order',lambda x:0.6),('first order',lambda x:x/10),('second order',lambda x:(x/10)**2)]):
        a=Ax(18+k*110,25,90,100,0,10,0,1.05); o+=[a.axes('[A]','rate'),a.curve(fn,0,10,[GR,BL,PU][k]),T(a.x+45,150,name,INK,12,b=True),T(a.x+45,166,['rate = k','rate = k[A]','rate = k[A]²'][k],GY,11)]
    return o
@fig('c-sn2','Nucleophilic substitution: hydroxide ion with bromoethane',340,170)
def _():
    o=[atom(42,80,'HO',size=15),T(30,62,'−',INK,14),lp(42,66,0),
       bond(160,80,203,80),atom(160,80,'C',size=15),atom(222,80,'Br',size=15),bond(160,80,160,48),atom(160,40,'H',size=13),bond(160,80,160,112),atom(160,120,'CH₃',size=13),
       bond(160,80,135,95),atom(125,103,'H',size=13),T(176,98,'δ+',RD,11,'start'),T(228,62,'δ−',BL,11),
       curly(46,64,95,30,150,70),curly(185,76,200,46,218,66),
       T(268,80,'→',INK,20),T(170,148,'CH₃CH₂Br + OH⁻ → CH₃CH₂OH + Br⁻',INK,12,b=True),T(170,164,'OH⁻ lone pair attacks δ+ C; C–Br bond breaks heterolytically',INK,10.5),
       T(300,72,'CH₃CH₂OH',INK,11),T(300,90,'+ Br⁻',INK,11)]
    return o
@fig('c-elec-add','Electrophilic addition of hydrogen bromide to ethene',340,200)
def _():
    o=[atom(40,70,'H₂C',size=14),bond(56,70,92,70,2),atom(110,70,'CH₂',size=14),
       atom(85,128,'H',size=14),bond(85,138,85,160),atom(85,172,'Br',size=14),T(97,124,'δ+',RD,10,'start'),T(102,176,'δ−',BL,10,'start'),
       curly(74,64,40,100,80,118),curly(90,148,110,152,92,164),
       T(150,100,'→',INK,20),
       atom(190,70,'H₂C',size=14),T(220,58,'+',INK,14),bond(206,70,232,70),atom(250,70,'CH₂',size=14),bond(250,80,250,104),atom(250,114,'H',size=13),
       atom(200,140,'Br',size=14),T(210,128,'−',INK,13),lp(200,126,0),curly(204,128,195,100,190,82),
       T(255,150,'carbocation',GY,10.5),T(285,72,'→',INK,16),T(312,64,'CH₂Br',INK,11),T(312,80,'|',INK,11),T(312,94,'CH₃',INK,11),
       T(170,190,'C=C (high electron density) attacks Hδ+, then Br⁻ attacks C⁺',INK,10.5)]
    return o
@fig('c-nuc-add','Nucleophilic addition of cyanide to ethanal',340,200)
def _():
    o=[atom(40,80,'⁻:CN',size=14),atom(140,80,'C',size=15),bond(140,80,140,48,2),atom(140,40,'O',size=15),bond(140,80,170,98),atom(184,105,'H',size=13),bond(140,80,110,98),atom(100,108,'CH₃',size=13),
       T(152,78,'δ+',RD,10,'start'),T(154,36,'δ−',BL,10,'start'),curly(32,70,70,40,132,74),curly(146,62,165,52,148,44),
       T(212,80,'→',INK,20),
       atom(270,80,'C',size=15),bond(270,80,270,50),atom(270,42,'O⁻',size=14),bond(270,80,240,96),atom(226,104,'CH₃',size=12),bond(270,80,300,96),atom(312,104,'H',size=12),bond(270,80,270,110),atom(270,120,'CN',size=12),
       atom(302,22,'H⁺',size=13),curly(262,34,268,14,292,20),
       T(170,160,'CN⁻ attacks δ+ C from either face of the planar C=O,',INK,10.5),T(170,175,'then O⁻ takes H⁺ → 2-hydroxypropanenitrile',INK,10.5),T(170,190,'(racemic mixture)',GY,10.5)]
    return o
@fig('c-nitration','Electrophilic substitution: nitration of benzene',340,190)
def _():
    def ring(cx,cy,r=26,circ=True,part=False):
        pts=[(cx+r*math.cos(math.radians(90+60*k)),cy-r*math.sin(math.radians(90+60*k))) for k in range(6)]
        out=PL(pts,INK,2,close=True)
        if circ: out+=C(cx,cy,r*0.58,INK,1.6)
        if part: out+=P(f'M{f(cx-14)},{f(cy-12)} A17,17 0 1 0 {f(cx-14)},{f(cy+12)}',INK,1.6)+T(cx-6,cy,'+',INK,13)
        return out
    o=[ring(55,85),atom(125,50,'⁺NO₂',size=13),curly(62,72,82,30,110,46),T(150,85,'→',INK,20),
       ring(210,85,26,False),P('M197,77 A15,15 0 1 0 223,77',INK,1.6),T(210,88,'+',INK,13),bond(210,59,196,42),atom(190,36,'H',size=12),bond(210,59,226,42),atom(240,34,'NO₂',size=12),
       curly(203,50,184,70,203,80),
       T(272,85,'→',INK,16),ring(312,92,20),bond(312,72,312,52),atom(312,42,'NO₂',size=12),
       T(170,140,'NO₂⁺ forms from conc. HNO₃ + conc. H₂SO₄ (50 °C)',INK,10.5),T(170,157,'The C–H bond breaks to restore the stable delocalised ring',INK,10.5),
       T(170,178,'C₆H₆ + NO₂⁺ → C₆H₅NO₂ + H⁺',INK,12,b=True)]
    return o
@fig('c-enantiomers','Enantiomers of butan-2-ol as mirror images',340,200)
def _():
    def mol(cx,sg):
        return [bond(cx,95,cx,58),atom(cx,50,'OH',size=13),bond(cx,95,cx-sg*34,112),atom(cx-sg*52,118,'CH₃' if sg>0 else 'CH₃',size=12),
                wedge(cx,95,cx+sg*26,124),atom(cx+sg*38,134,'C₂H₅',size=12),hashb(cx,95,cx+sg*30,98),atom(cx+sg*40,98,'H',size=12),atom(cx,95,'C',size=15),T(cx+sg*0+10,82,'*',RD,14)]
    o=mol(85,1)+mol(255,-1)+[L(170,25,170,165,GY,1.6,'6 5'),T(170,18,'mirror',GY,11),
       T(170,178,'Chiral C* has 4 different groups. The two forms are',INK,11),T(170,193,'non-superimposable mirror images (optical isomers)',INK,11)]
    return o
@fig('c-polymers','Repeat units of a polyester and a polyamide',340,210)
def _():
    o=[T(170,16,'Polyester (diol + dicarboxylic acid, − H₂O)',BL,12,b=True),
       T(170,46,'[ –O–CH₂–CH₂–O–C(=O)–C₆H₄–C(=O)– ]ₙ',INK,13),
       T(170,70,'ester link –COO– (PET / Terylene)',RD,11),
       T(170,106,'Polyamide (diamine + dicarboxylic acid, − H₂O)',OR,12,b=True),
       T(170,136,'[ –NH–(CH₂)₆–NH–C(=O)–(CH₂)₄–C(=O)– ]ₙ',INK,12.5),
       T(170,160,'amide link –CONH– (nylon-6,6)',RD,11),
       T(170,188,'Polar links can be hydrolysed by acid or alkali,',INK,11),T(170,202,'so these polymers are biodegradable; poly(alkenes) are not',INK,11)]
    return o
@fig('c-nmr','Schematic ¹H NMR spectrum of ethanol',340,210)
def _():
    a=Ax(30,30,280,120,0,5,0,1.1)
    X=lambda d:a.X(5-d)
    o=[A(30,a.Y(0),318,a.Y(0),INK,1.6,7),T(310,a.Y(0)+28,'δ / ppm',INK,12,'end')]
    for d in (0,1,2,3,4,5): o+=[L(X(d),a.Y(0),X(d),a.Y(0)+4,INK,1.4),T(X(d),a.Y(0)+15,str(d),INK,11)]
    def peaks(c,n,hgt,col):
        out='';from math import comb
        cs=[comb(n-1,k) for k in range(n)]; m=max(cs)
        for k,v in enumerate(cs): x=X(c+(k-(n-1)/2)*0.07); out+=L(x,a.Y(0),x,a.Y(hgt*v/m),col,2.4)
        return out
    o+=[peaks(1.2,3,0.95,BL),peaks(3.7,4,0.65,OR),peaks(2.6,1,0.32,GR),L(X(0),a.Y(0),X(0),a.Y(0.5),GY,2.4),
        T(X(1.2),a.Y(1.0)-8,'CH₃ triplet (3H)',BL,10.5),T(X(3.7),a.Y(0.7)-8,'CH₂ quartet (2H)',OR,10.5),T(X(2.6),a.Y(0.4)-10,'OH singlet (1H)',GR,10.5),T(X(0),a.Y(0.55)-8,'TMS',GY,10.5),
        T(170,188,'n + 1 rule: a peak is split by n H on adjacent carbons',INK,11),T(170,203,'Integration ratio 3 : 2 : 1   (shifts approximate)',INK,11)]
    return o
@fig('c-tlc','Thin-layer chromatography plate and Rf value',340,230)
def _():
    o=[R(40,20,90,190,INK,2,fill='#f7f7f2',rx=4),L(40,180,130,180,GY,1.4,'4 3'),T(136,196,'baseline (pencil)',GY,10.5,'start'),L(40,40,130,40,BL,1.4,'4 3'),T(136,40,'solvent front',BL,10.5,'start'),
       C(65,180,4,INK,1.2,fill=INK),C(105,180,4,INK,1.2,fill=INK),f'<ellipse cx="65" cy="80" rx="8" ry="6" fill="{PU}" fill-opacity=".7"/>',f'<ellipse cx="105" cy="130" rx="8" ry="6" fill="{OR}" fill-opacity=".8"/>',
       f'<ellipse cx="105" cy="80" rx="8" ry="6" fill="{PU}" fill-opacity=".7"/>',A(28,180,28,82,PU,1.4,6,both=True),T(22,131,'x',PU,12,'end',i=True),A(16,180,16,42,BL,1.4,6,both=True),T(10,110,'y',BL,12,'end',i=True),
       T(240,90,'Rf = x / y',INK,15,'middle',b=True),T(240,112,'distance moved by spot',INK,10.5),T(240,126,'÷ distance moved by solvent',INK,10.5),
       T(240,146,'Same Rf as a known',INK,10.5),T(240,160,'(same conditions)',INK,10.5),T(240,174,'→ same compound',INK,10.5),T(65,222,'A',INK,11,b=True),T(105,222,'B',INK,11,b=True)]
    return o
@fig('c-complexes','Shapes of transition metal complex ions',340,190)
def _():
    o=[]
    def cell(k,name,sub,body):
        x=45+k*83; o.append(G(body,x,78)); o.append(T(x,138,name,INK,11,b=True)); o.append(T(x,153,sub,GY,10))
    cell(0,'octahedral','[Cu(H₂O)₆]²⁺ 90°',[bond(0,0,0,-30),bond(0,0,0,30),bond(0,0,-30,0),bond(0,0,30,0),wedge(0,0,-17,15),hashb(1,-1,18,-15),atom(0,0,'Cu',size=11),*[T(x,y,'L',BL,10) for x,y in ((0,-36),(0,36),(-36,0),(36,0),(-22,20),(23,-20))]])
    cell(1,'tetrahedral','[CuCl₄]²⁻ 109.5°',[bond(0,0,0,-30),bond(0,0,-26,12),wedge(0,0,22,18),hashb(2,2,28,0),atom(0,0,'Cu',size=11),*[T(x,y,'Cl',BL,10) for x,y in ((0,-37),(-33,15),(28,24),(35,0))]])
    cell(2,'square planar','cisplatin 90°',[bond(0,0,-24,-18),bond(0,0,24,-18),bond(0,0,-24,18),bond(0,0,24,18),atom(0,0,'Pt',size=11),T(-34,-24,'Cl',BL,10),T(34,-24,'Cl',BL,10),T(-36,24,'H₃N',BL,9.5),T(36,24,'NH₃',BL,9.5)])
    cell(3,'linear','[Ag(NH₃)₂]⁺ 180°',[bond(-26,0,-9,0),bond(9,0,26,0),atom(0,0,'Ag',size=11),T(-36,0,'H₃N',BL,9.5),T(36,0,'NH₃',BL,9.5)])
    o.append(T(170,180,'L = ligand: forms a co-ordinate bond to the metal ion',INK,11))
    return o
@fig('c-hess','Hess’s law cycle using enthalpies of combustion',340,200)
def _():
    o=[T(60,40,'3C(s) + 4H₂(g)',INK,12,b=True),T(280,40,'C₃H₈(g)',INK,12,b=True),T(170,160,'3CO₂(g) + 4H₂O(l)',INK,12,b=True),
       A(108,40,240,40,PU,2,8),T(174,28,'ΔfH = ?',PU,12),A(70,52,140,145,BL,2,8),T(80,110,'Σ ΔcH reactants',BL,11,'end'),A(270,52,205,145,RD,2,8),T(262,110,'ΔcH C₃H₈',RD,11,'start'),
       T(170,186,'ΔfH = Σ ΔcH(reactants) − Σ ΔcH(products)',INK,12,b=True)]
    return o
@fig('c-mass-spec','Mass spectrum of chlorine molecules',340,200)
def _():
    a=Ax(40,25,270,130,66,76,0,10)
    o=[a.axes('m/z','abundance')]
    for mz,h,lab in ((70,9,'³⁵Cl–³⁵Cl'),(72,6,'³⁵Cl–³⁷Cl'),(74,1,'³⁷Cl–³⁷Cl')):
        o+=[L(a.X(mz),a.Y(0),a.X(mz),a.Y(h),BL,6),a.xt(mz,str(mz)),T(a.X(mz),a.Y(h)-10,f'{h}',BL,12,b=True),T(a.X(mz)+(0 if mz!=74 else 0),a.Y(h)-24,lab,INK,10)]
    o+=[T(170,186,'³⁵Cl : ³⁷Cl = 3 : 1, so Cl₂⁺ peaks are 9 : 6 : 1',INK,12)]
    return o
@fig('c-hbond','Hydrogen bonding between water molecules',340,160)
def _():
    def w(x,y,rot):
        return G([bond(0,0,-20,14),bond(0,0,20,14),atom(0,0,'O',size=14),atom(-25,18,'H',size=12),atom(25,18,'H',size=12),T(0,-16,'δ−',BL,10),T(-32,30,'δ+',RD,10),T(32,30,'δ+',RD,10),lp(-7,-9,60),lp(7,-9,120)],x,y)
    o=[w(80,50,0),w(195,100,0),L(105,68,188,92,OR,2,'2 4'),T(150,70,'H-bond',OR,11),
       T(170,145,'Lone pair on O attracted to δ+ H on a neighbouring molecule',INK,11)]
    return o
@fig('c-gibbs','ΔG against temperature: a reaction becomes feasible when ΔG ≤ 0',340,200)
def _():
    a=Ax(40,25,270,130,0,10,-4,6)
    o=[a.axes('T / K','ΔG',0,0),a.curve(lambda t:5-1*t,0,9.8,BL),a.dot(5,0,RD),T(a.X(5)+6,a.Y(0)-12,'feasible above this T',RD,11,'start'),
       T(a.X(0)+8,a.Y(5),'intercept = ΔH',INK,11,'start'),T(a.X(6.2),a.Y(-2.8),'gradient = −ΔS',INK,11,'start'),
       T(170,180,'ΔG = ΔH − TΔS ;  at ΔG = 0, T = ΔH / ΔS',INK,12,b=True),T(170,195,'(ΔS in kJ K⁻¹ mol⁻¹ to match ΔH in kJ mol⁻¹)',GY,10.5)]
    return o
@fig('c-equilibrium','Concentrations reaching dynamic equilibrium',340,198)
def _():
    a=Ax(40,25,270,120,0,10,0,1.05)
    o=[a.axes('time','concentration'),a.curve(lambda t:0.35+0.6*math.exp(-t/1.4),0,10,BL),a.curve(lambda t:0.6*(1-math.exp(-t/1.4)),0,10,OR),
       L(a.X(5),a.Y(0),a.X(5),a.Y(1),GY,1,'4 4'),T(a.X(5)+6,a.Y(0.95),'equilibrium reached',GY,11,'start'),T(a.X(9.8),a.Y(0.35)-10,'reactants',BL,11,'end'),T(a.X(9.8),a.Y(0.6)-10,'products',OR,11,'end'),
       T(170,176,'Concentrations constant: forward rate = reverse rate',INK,11.5),T(170,191,'(closed system)',GY,10.5)]
    return o
@fig('c-half-life','First-order reaction: constant half-life on a concentration–time graph',340,200)
def _():
    a=Ax(45,25,265,130,0,6,0,1.05); k=math.log(2)
    o=[a.axes('time','[A]'),a.curve(lambda t:math.exp(-k*t),0,6,PU)]
    for n,(t,c) in enumerate([(1,0.5),(2,0.25),(3,0.125)]):
        o+=[L(a.X(0),a.Y(c),a.X(t),a.Y(c),GY,1,'3 3'),L(a.X(t),a.Y(0),a.X(t),a.Y(c),GY,1,'3 3'),a.xt(t,f'{t}t½')]
    o+=[a.yt(1,'[A]₀'),a.yt(0.5,'½'),a.yt(0.25,'¼'),T(170,183,'Each half-life is the same length: t½ = ln 2 / k',INK,12)]
    return o
