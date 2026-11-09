from lib import *
import math
F={}
def fig(name,alt,w,h):
    def d(fn): F[name]=svg(w,h,fn(),alt); return fn
    return d
@fig('p-projectile','Projectile path with horizontal and vertical velocity components',340,220)
def _():
    a=Ax(30,30,290,150,0,10,0,5.2); g=lambda x:0.8*x*(10-x)/5*1.25
    o=[a.axes('x','y'),a.curve(lambda x:x*(10-x)*0.2,0,10,BL)]
    for x in (0,2.5,5,7.5):
        y=x*(10-x)*0.2; X,Y=a.X(x),a.Y(y); vy=(10-2*x)*0.2*14
        o+= [A(X,Y,X+40,Y,OR,2,8)]
        if abs(vy)>2: o+=[A(X,Y,X,Y-vy,GR,2,8)]
    o+=[T(a.X(0)+44,a.Y(0)-10,'vₓ constant',OR,12,'start'),T(a.X(5),a.Y(5)-14,'top: v_y = 0',GR,12),T(a.X(1.6),a.Y(3.6),'v_y',GR,12,'end'),
        T(a.X(9.9),a.Y(3.6),'a = g',INK,12,'end'),A(a.X(9.4),a.Y(3.2),a.X(9.4),a.Y(2.0),INK,1.6,7),
        T(170,205,'Horizontal: s = vₓt   ·   Vertical: suvat with a = −g',INK,12)]
    return o
@fig('p-vt-graph','Velocity–time graph: gradient is acceleration, area is displacement',340,210)
def _():
    a=Ax(40,25,270,140,0,10,0,12)
    o=[a.area(lambda t:min(10,2.5*t) if t<8 else 10-5*(t-8),0,10,BL,0.18),a.axes('t / s','v / m s⁻¹'),
       PL([(a.X(0),a.Y(0)),(a.X(4),a.Y(10)),(a.X(8),a.Y(10)),(a.X(10),a.Y(0))],BL,2.6),
       T(a.X(0.2),a.Y(11.4),'gradient = acceleration',OR,12,'start'),
       T(a.X(6),a.Y(5),'area under line',BL,12,b=True),T(a.X(6),a.Y(3.6),'= displacement',BL,12,b=True),
       a.xt(4,'4'),a.xt(8,'8'),a.yt(10,'10'),T(170,198,'Negative gradient = deceleration',INK,12)]
    return o
@fig('p-slope-fbd','Free-body diagram for a block on a rough slope',340,220)
def _():
    th=math.radians(30); x0,y0=30,190; L1=280
    top=(x0+L1*math.cos(th),y0-L1*math.sin(th))
    o=[PL([(x0,y0),(top[0],y0),top],INK,2,fill=LT,close=True)]
    cx,cy=x0+150*math.cos(th),y0-150*math.sin(th)
    ux,uy=math.cos(th),-math.sin(th); nx,ny=-math.sin(th),-math.cos(th)
    bx,by=cx+nx*18,cy+ny*18
    pts=[(cx-ux*24,cy-uy*24),(cx+ux*24,cy+uy*24),(cx+ux*24+nx*36,cy+uy*24+ny*36),(cx-ux*24+nx*36,cy-uy*24+ny*36)]
    o+=[PL(pts,INK,2,fill='#c9ecfd',close=True)]
    o+=[A(bx,by,bx,by+70,RD,2.4),T(bx+8,by+76,'W = mg',RD,13,'start',b=True),
        A(bx,by,bx+nx*70,by+ny*70,BL,2.4),T(bx+nx*74-4,by+ny*74-6,'R (normal)',BL,13,'end',b=True),
        A(bx,by,bx+ux*72,by+uy*72,GR,2.4),T(bx+ux*76+4,by+uy*76,'friction F',GR,13,'start',b=True),
        P(f'M{x0+46},{y0} A46,46 0 0 0 {f(x0+46*math.cos(th))},{f(y0-46*math.sin(th))}',INK,1.5),T(x0+58,y0-12,'θ',INK,13,i=True),
        T(170,16,'Along slope: mg sin θ   ·   Perpendicular: R = mg cos θ',INK,12)]
    return o
@fig('p-moments','Principle of moments on a balanced beam',340,190)
def _():
    o=[R(30,80,280,12,INK,2,fill='#ffe2cc',rx=3),PL([(170,92),(155,122),(185,122)],INK,2,fill=LT,close=True),
       A(70,92,70,150,RD,2.4),T(70,160,'F₁',RD,13,b=True),A(270,92,270,140,RD,2.4),T(270,150,'F₂',RD,13,b=True),
       A(170,50,170,78,BL,2.2),T(170,40,'reaction at pivot',BL,12),
       A(74,66,166,66,INK,1.4,7,both=True),T(120,58,'d₁',INK,13,i=True),A(174,66,266,66,INK,1.4,7,both=True),T(220,58,'d₂',INK,13,i=True),
       T(170,178,'Balanced: F₁d₁ = F₂d₂ (anticlockwise = clockwise)',INK,12)]
    return o
@fig('p-terminal','Terminal velocity: velocity–time graph for a falling object with drag',340,200)
def _():
    a=Ax(40,25,270,130,0,10,0,10)
    o=[a.axes('t','v'),a.curve(lambda t:9*(1-math.exp(-t/2)),0,10,BL),L(a.X(0),a.Y(9),a.X(10),a.Y(9),GY,1.4,'5 4'),
       T(a.X(10),a.Y(9)-10,'terminal velocity',GY,12,'end'),T(a.X(0.6),a.Y(4.5),'gradient = g',OR,12,'start'),T(a.X(0.6),a.Y(3.3),'at start',OR,12,'start'),
       T(170,175,'Drag rises with speed until drag = weight,',INK,12),T(170,190,'so the resultant force and acceleration are zero',INK,12)]
    return o
@fig('p-work-angle','Work done by a force at an angle to the displacement',340,170)
def _():
    o=[L(20,130,320,130,INK,2),R(60,95,60,35,INK,2,fill='#c9ecfd',rx=3),A(120,112,210,60,RD,2.6),T(214,52,'F',RD,14,'start',b=True,i=True),
       L(120,112,215,112,GY,1.4,'5 4'),P('M150,112 A30,30 0 0 0 146,97',INK,1.5),T(160,102,'θ',INK,13,i=True),
       A(60,148,240,148,BL,2,8),T(150,160,'displacement x',BL,12),T(225,100,'F cos θ',GY,12,'start'),
       T(170,18,'W = Fx cos θ   (only the component along x does work)',INK,12)]
    return o
@fig('p-force-ext','Force–extension graph: Hooke’s law region and elastic potential energy',340,210)
def _():
    a=Ax(40,25,270,140,0,10,0,10)
    fn=lambda x: x if x<=6 else 6+2.2*(1-math.exp(-(x-6)/1.5))
    o=[a.area(lambda x:x,0,6,OR,0.22),a.axes('extension x','force F'),a.curve(fn,0,10,BL),a.dot(6,6,RD),
       T(a.X(6)-6,a.Y(6)-12,'limit of proportionality',RD,12,'end'),T(a.X(3.6),a.Y(1.4),'area = ½Fx = energy stored',OR,12),
       T(a.X(1.9),a.Y(4.7),'gradient = k',INK,12,'end'),T(170,195,'F = kx (straight line through origin)',INK,12)]
    return o
@fig('p-stress-strain','Stress–strain curves for brittle, ductile and polymeric materials',340,220)
def _():
    a=Ax(40,25,270,150,0,10,0,10)
    o=[a.axes('strain','stress'),PL([(a.X(0),a.Y(0)),(a.X(1.6),a.Y(9))],RD,2.4),a.dot(1.6,9,RD),T(a.X(1.6)+6,a.Y(9),'brittle (glass)',RD,12,'start'),
       a.curve(lambda x:4.5*x if x<1.2 else 5.4+1.6*(1-math.exp(-(x-1.2)/2)),0,8,BL),a.dot(8,5.4+1.6*(1-math.exp(-6.8/2)),BL),
       T(a.X(8),a.Y(7.6),'ductile (copper)',BL,12,'end'),T(a.X(1.4),a.Y(4.6),'yield point',BL,11,'start'),
       a.curve(lambda x:0.25*x+0.06*x**2 if x<9.5 else None,0,9.5,GR),T(a.X(9.6),a.Y(3.6),'polymer',GR,12,'end'),
       T(170,205,'Young modulus = gradient of the linear part',INK,12)]
    return o
@fig('p-collision','Momentum conservation in a collision: before and after',340,190)
def _():
    o=[T(80,18,'Before',INK,13,b=True),T(250,18,'After (stick together)',INK,13,b=True),L(170,10,170,108,GY,1,'4 4'),
       R(20,50,44,32,INK,2,fill='#c9ecfd',rx=4),T(42,67,'2 kg',size=12),A(66,66,104,66,RD,2.2,8),T(85,56,'3 m/s',RD,12),
       R(110,50,34,32,INK,2,fill='#ffe2cc',rx=4),T(127,67,'1 kg',size=12),T(127,96,'at rest',GY,12),
       R(196,50,44,32,INK,2,fill='#c9ecfd',rx=4),R(240,50,34,32,INK,2,fill='#ffe2cc',rx=4),A(278,66,318,66,RD,2.2,8),T(298,56,'v',RD,13,i=True),
       T(170,128,'Total momentum before = total momentum after',INK,12),T(170,148,'2 × 3 + 1 × 0 = 3v  →  v = 2 m/s',BL,13,b=True),
       T(170,172,'KE is lost, so this collision is inelastic',INK,12)]
    return o
@fig('p-iv','I–V characteristics of a resistor, filament lamp and diode',340,190)
def _():
    o=[];labs=['ohmic resistor','filament lamp','diode']
    fns=[lambda v:v,lambda v:1.8*math.tanh(0.8*v),lambda v:(math.exp((v-0.3)*5)-1)*0.1 if v>0 else 0]
    for k in range(3):
        a=Ax(14+k*110,30,92,110,-2,2,-2,2); o+=[a.axes('V','I',0,0),a.curve(fns[k],-2,2,[BL,OR,GR][k]),T(60+k*110,165,labs[k],INK,12)]
    o+=[T(170,184,'Lamp: R rises as it heats.  Diode: conducts above ≈0.6 V forward.',INK,11)]
    return o
@fig('p-series-parallel','Series and parallel circuits with ammeters',340,200)
def _():
    o=[T(85,14,'Series: same I',INK,13,b=True),T(255,14,'Parallel: same V',INK,13,b=True)]
    o+=[wire([(20,48),(150,48),(150,150),(20,150),(20,48)]),cell(85,150,lab=None),resistor(55,48,lab='R₁'),resistor(115,48,lab='R₂'),meter(150,99,'A'),
        T(85,180,'R = R₁ + R₂',BL,13,b=True)]
    o+=[wire([(190,48),(320,48),(320,150),(190,150),(190,48)]),wire([(220,48),(220,99),(290,99),(290,48)]),cell(255,150),resistor(255,48,lab='R₁'),resistor(255,99,lab=None),
        T(255,117,'R₂',size=12),junc(220,48),junc(290,48),meter(190,99,'A'),T(255,180,'1/R = 1/R₁ + 1/R₂',BL,13,b=True)]
    return o
@fig('p-potdiv','Potential divider with a light-dependent resistor',340,226)
def _():
    o=[wire([(60,30),(200,30),(200,190),(60,190),(60,30)]),cell(60,110,'v',lab=None),T(30,110,'V_in',INK,12,'middle'),
       resistor(200,70,'v'),T(222,70,'R₁',size=12,a='start'),ldr(200,150,'v'),T(232,155,'LDR',size=12,a='start'),
       junc(200,110),wire([(200,110),(280,110)]),wire([(200,190),(280,190)]),junc(200,190),C(280,110,3,INK,1.5,fill='#fff'),C(280,190,3,INK,1.5,fill='#fff'),
       A(292,114,292,186,BL,1.6,7),T(300,150,'V_out',BL,12,'start'),
       T(170,200,'V_out = V_in × R_LDR / (R₁ + R_LDR)',INK,12),T(170,214,'More light → R_LDR falls → V_out falls',INK,12)]
    return o
@fig('p-wave','Transverse wave showing wavelength and amplitude',340,180)
def _():
    a=Ax(20,30,300,110,0,2.2,-1.3,1.3)
    o=[L(20,a.Y(0),320,a.Y(0),GY,1.2,'4 4'),a.curve(lambda x:math.sin(2*math.pi*x),0,2.2,BL),
       A(a.X(0.25),a.Y(1)-12,a.X(1.25),a.Y(1)-12,OR,1.6,7,both=True),T(a.X(0.75),a.Y(1)-22,'wavelength λ',OR,12),
       A(a.X(1.75),a.Y(0),a.X(1.75),a.Y(-1)+2,GR,1.6,7,both=True),T(a.X(1.75)+6,a.Y(-0.5),'amplitude A',GR,12,'start'),
       T(170,170,'v = fλ   ·   f = 1/T',INK,13,b=True)]
    return o
@fig('p-interference','Double-slit interference: path difference and fringes',340,230)
def _():
    o=[L(60,20,60,95,INK,3),L(60,105,60,125,INK,3),L(60,135,60,210,INK,3),T(52,90,'S₁',size=11,a='end'),T(52,141,'S₂',size=11,a='end'),
       L(300,20,300,210,INK,2.5)]
    for k in range(-3,4):
        y=115+k*26; col=BL if k%2==0 else LT
        o.append(R(302,y-6,14,12,'none',0,fill=BL if k%2==0 else '#dfe4ea',rx=2))
    o+=[L(60,100,300,167,OR,1.6),L(60,130,300,167,OR,1.6),A(36,100,36,130,INK,1.2,6,both=True),T(30,115,'a',INK,12,'end',i=True),A(70,115,290,115,GY,1,7,dash='4 4'),
        T(180,98,'paths meet at a bright fringe',OR,11),T(180,214,'a = slit separation · x = fringe spacing',INK,11),
        A(322,115,322,167,INK,1.2,6,both=True),T(326,141,'x',INK,12,'start',i=True),T(180,40,'λ = ax / D',BL,15,b=True),
        T(180,60,'bright: path difference = nλ',INK,11),T(180,74,'dark: (n + ½)λ',INK,11),A(70,186,290,186,INK,1.2,7,both=True),T(180,178,'D',INK,12,i=True)]
    return o
@fig('p-stationary','Stationary wave on a string with nodes and antinodes',340,170)
def _():
    a=Ax(30,30,280,100,0,3,-1.2,1.2)
    o=[a.curve(lambda x:math.sin(math.pi*x),0,3,BL),a.curve(lambda x:-math.sin(math.pi*x),0,3,BL,dash='5 4')]
    for k in range(4): o+=[a.dot(k,0,RD,4)]
    o+=[T(a.X(1),a.Y(0)+16,'N',RD,12,b=True),T(a.X(1.5),a.Y(1)-10,'A',GR,12,b=True),T(a.X(0.5),a.Y(1)-10,'A',GR,12,b=True),
        A(a.X(1),a.Y(-1.15)-4,a.X(2),a.Y(-1.15)-4,OR,1.4,7,both=True),T(a.X(1.5),a.Y(-1.15)+8,'node to node = λ/2',OR,12),
        T(170,160,'N = node (no motion) · A = antinode (max amplitude)',INK,11.5)]
    return o
@fig('p-photoelectric','Photoelectric effect: maximum kinetic energy against frequency',340,210)
def _():
    a=Ax(40,25,270,140,0,10,-4,6)
    o=[a.axes('f','KEmax',0,0),a.curve(lambda x:x-3.5,3.5,10,BL),a.curve(lambda x:x-3.5,0,3.5,BL,dash='5 4'),a.dot(3.5,0,RD),
       T(a.X(3.5),a.Y(0)+14,'f₀ threshold',RD,12),T(a.X(0)+8,a.Y(-3.5),'−φ (work function)',PU,12,'start'),a.dot(0,-3.5,PU),
       T(a.X(7.2),a.Y(3.6)-14,'gradient = h',BL,13,'end',b=True),T(170,195,'hf = φ + KEmax  ·  below f₀ no electrons, however intense',INK,11)]
    return o
@fig('p-energy-levels','Energy levels in hydrogen with photon emission (not to scale)',340,215)
def _():
    lv=[(190,'n = 1','−13.6 eV'),(112,'n = 2','−3.40 eV'),(80,'n = 3','−1.51 eV'),(60,'n = 4','−0.85 eV'),(40,'∞','0 eV')]
    o=[]
    for y,n,lab in lv: o+=[L(80,y,250,y,INK if y>40 else GY,2,None if y>40 else '5 4'),T(72,y,n,size=12,a='end'),T(258,y,lab,size=12,a='start')]
    o+=[A(125,80,125,112,OR,2,8),T(121,96,'1.89 eV (red)',OR,11,'end'),A(190,112,190,190,PU,2,8),T(196,151,'10.2 eV (UV)',PU,11,'start'),
        T(170,16,'hf = E_upper − E_lower',INK,13,b=True),T(165,207,'not to scale',GY,10)]
    return o
@fig('p-shm','SHM: displacement, velocity and acceleration against time',340,240)
def _():
    o=[]
    for k,(lab,fn,c) in enumerate([('x',math.cos,BL),('v',lambda t:-math.sin(t),OR),('a',lambda t:-math.cos(t),GR)]):
        a=Ax(40,14+k*72,280,52,0,4*math.pi,-1.2,1.2)
        o+=[L(40,a.Y(0),324,a.Y(0),GY,1),A(40,a.y+a.h,40,a.y-4,INK,1.4,6),T(28,a.Y(0),lab,c,14,b=True,i=True),a.curve(fn,0,4*math.pi,c)]
    o+=[L(40,14,40,228,GY,1,'3 3'),T(180,232,'v leads x by T/4  ·  a = −ω²x (always opposite to x)',INK,11)]
    return o
@fig('p-circular','Uniform circular motion: velocity is tangential, acceleration towards the centre',340,210)
def _():
    cx,cy,r=130,105,72
    o=[C(cx,cy,r,GY,1.6,dash='5 4'),C(cx,cy,3,INK,1,fill=INK),T(cx,cy+14,'centre',GY,11)]
    for ang in (-30,90,210):
        t=math.radians(ang); x,y=cx+r*math.cos(t),cy-r*math.sin(t)
        o+=[C(x,y,7,INK,1.6,fill='#c9ecfd'),A(x,y,x-52*math.sin(t),y-52*math.cos(t),OR,2.2,8),A(x,y,x+(cx-x)*0.55,y+(cy-y)*0.55,RD,2.2,8)]
    o+=[T(250,60,'v (tangent)',OR,12,'start'),T(250,80,'F, a (to centre)',RD,12,'start'),T(250,120,'a = v²/r = ω²r',INK,12,'start'),
        T(250,140,'F = mv²/r',INK,12,'start'),T(250,160,'v = ωr',INK,12,'start'),T(170,198,'Speed is constant but velocity changes direction',INK,12)]
    return o
@fig('p-gfield','Radial gravitational field lines and g against r',340,200)
def _():
    cx,cy=85,95; o=[]
    for k in range(12):
        t=k*math.pi/6; o.append(A(cx+75*math.cos(t),cy+75*math.sin(t),cx+34*math.cos(t),cy+34*math.sin(t),BL,1.6,7))
    o+=[C(cx,cy,26,INK,2,fill='#d4f8b0'),T(cx,cy,'M',INK,14,b=True)]
    a=Ax(190,30,130,120,0,5,0,1.1); o+=[a.axes('r','g'),a.curve(lambda r:1/r**2 if r>=1 else r,0,5,RD),L(a.X(1),a.Y(1),a.X(1),a.Y(0),GY,1,'3 3'),a.xt(1,'R'),
        T(255,95,'g = GM/r²',RD,12,'start'),T(170,188,'Lines point inwards: gravity always attracts',INK,12)]
    return o
@fig('p-cap-circuit','Capacitor charging and discharging circuit with a two-way switch',340,220)
def _():
    o=[wire([(40,40),(150,40)]),wire([(190,40),(300,40),(300,170),(40,170),(40,40)]),wire([(155,74),(155,170)]),
       cell(40,105,'v'),T(18,105,'V₀',size=12),resistor(300,80,'v'),T(318,80,'R',size=13,a='start',b=True),capacitor(300,135,'v'),T(318,135,'C',size=13,a='start',b=True),
       meter(245,40,'A'),C(150,40,3,INK,1.5,fill='#fff'),C(190,40,3,INK,1.5,fill='#fff'),C(155,74,3,INK,1.5,fill='#fff'),L(188,38,154,34,INK,2.2),
       T(150,24,'1',GY,11),T(140,78,'2',GY,11),junc(155,170),
       T(170,192,'Switch at 1: C charges from the cell through R.',INK,11.5),T(170,208,'Switch at 2: C discharges through R.',INK,11.5)]
    return o
@fig('p-discharge','Capacitor discharge: exponential decay with time constant RC',340,210)
def _():
    a=Ax(40,25,270,140,0,5,0,1.05)
    o=[a.axes('t','Q, V or I'),a.curve(lambda t:math.exp(-t),0,5,BL),L(a.X(1),a.Y(0),a.X(1),a.Y(math.exp(-1)),GY,1.2,'4 4'),L(a.X(0),a.Y(math.exp(-1)),a.X(1),a.Y(math.exp(-1)),GY,1.2,'4 4'),
       a.xt(1,'RC'),a.xt(2,'2RC'),a.yt(1,'x₀'),a.yt(math.exp(-1),'0.37x₀'),T(a.X(2.6),a.Y(0.55),'x = x₀ e^(−t/RC)',BL,13,'start',b=True),
       T(170,198,'After each RC the value falls to 37% of what it was',INK,12)]
    return o
@fig('p-charging','Capacitor charging: p.d. rises while current falls',340,200)
def _():
    o=[]
    for k,(lab,fn,c) in enumerate([('V across C',lambda t:1-math.exp(-t),BL),('current I',lambda t:math.exp(-t),OR)]):
        a=Ax(30+k*160,30,125,110,0,4,0,1.1); o+=[a.axes('t',lab),a.curve(fn,0,4,c),L(a.X(0),a.Y(1),a.X(4),a.Y(1),GY,1,'4 4') if k==0 else '',
             T(a.x+62,165,['V = V₀(1 − e^(−t/RC))','I = I₀ e^(−t/RC)'][k],c,11)]
    o+=[T(170,190,'Area under the I–t graph = charge stored Q',INK,12)]
    return o
@fig('p-efield-plates','Uniform electric field between parallel plates with equipotentials',340,210)
def _():
    o=[R(40,30,260,10,INK,1.5,fill='#ffd0d0'),R(40,160,260,10,INK,1.5,fill='#cfe6ff')]
    for k in range(8): x=60+k*32; o.append(A(x,44,x,154,BL,1.6,7))
    for k,yy in enumerate((72,100,128)): o+=[L(40,yy,300,yy,GR,1.4,'6 5')]
    o+=[T(30,35,'+',RD,18,b=True),T(30,165,'−',BL,20,b=True),T(310,100,'equipotentials',GR,11,'end'),
        T(170,22,'+V',INK,12),T(170,186,'0 V',INK,12),T(170,203,'E = V/d (uniform field); lines ⟂ equipotentials',INK,12)]
    return o
@fig('p-efield-radial','Electric field lines around a positive and a negative point charge',340,190)
def _():
    o=[]
    for cx,sg,col in ((85,1,RD),(255,-1,BL)):
        for k in range(8):
            t=k*math.pi/4; a,b=(cx+20*math.cos(t),90+20*math.sin(t)),(cx+68*math.cos(t),90+68*math.sin(t))
            o.append(A(*a,*b,col,1.6,7) if sg>0 else A(*b,*a,col,1.6,7))
        o+=[C(cx,90,15,INK,2,fill='#ffd0d0' if sg>0 else '#cfe6ff'),T(cx,91,'+' if sg>0 else '−',INK,18,b=True)]
    o+=[T(170,178,'Field lines show the force on a positive test charge',INK,12)]
    return o
@fig('p-electron-deflect','Electron deflected in a parabola between charged plates',340,190)
def _():
    o=[R(110,30,170,9,INK,1.5,fill='#ffd0d0'),R(110,140,170,9,INK,1.5,fill='#cfe6ff'),T(100,35,'+',RD,16,b=True,a='end'),T(100,145,'−',BL,18,b=True,a='end'),
       A(20,110,108,110,OR,2,8),T(50,98,'e⁻',OR,13)]
    pts=[(110+t,110-0.0022*t*t) for t in range(0,171,5)]
    o+=[PL(pts,OR,2.4),A(280,46.4,320,16.5,OR,2,8),T(195,170,'constant horizontal velocity; constant force towards +',INK,11),
        T(195,184,'→ parabolic path, like a projectile',INK,11)]
    return o
@fig('p-bfield-circle','Charged particle moving in a circle in a magnetic field',340,200)
def _():
    o=[]
    for i in range(6):
        for j in range(4): o.append(T(40+i*52,22+j*44,'×',GY,14))
    cx,cy,r=170,95,62
    o+=[C(cx,cy,r,OR,2.2),C(cx+r,cy,7,INK,1.5,fill='#ffd0d0'),T(cx+r,cy+1,'+',INK,11,b=True),A(cx+r,cy,cx+r,cy-46,BL,2.2,8),T(cx+r+8,cy-40,'v',BL,13,'start',i=True),
       A(cx+r,cy,cx+r-44,cy,RD,2.2,8),T(cx+r-46,cy-10,'F',RD,13,i=True),T(170,178,'B into page (×). F = BQv ⟂ v, so r = mv/(BQ)',INK,12),T(30,190,'',INK)]
    return o
@fig('p-binding','Binding energy per nucleon against nucleon number',340,210)
def _():
    a=Ax(40,25,270,140,0,240,0,9.5)
    def be(A_):
        if A_<4: return 1.1*A_
        return 8.8-1.2*math.exp(-(A_-4)/9)-0.012*max(0,A_-56)*0.78- (0.4 if A_<12 else 0)
    o=[a.axes('nucleon number A','BE per nucleon / MeV'),a.curve(lambda x:8.8-6.5*math.exp(-(x)/14)-0.0076*max(0,x-56),2,238,BL),a.dot(56,8.8-6.5*math.exp(-4)-0,RD),
       T(a.X(56)+8,a.Y(8.7)+14,'Fe-56: most stable',RD,12,'start'),A(a.X(30),a.Y(5.4),a.X(48),a.Y(7.6),GR,1.6,7),T(a.X(20),a.Y(4.6),'fusion',GR,12),
       A(a.X(215),a.Y(6.6),a.X(150),a.Y(7.6),OR,1.6,7),T(a.X(215),a.Y(5.9),'fission',OR,12),a.xt(56,'56')]
    return o
@fig('p-heating','Heating curve: temperature against time for a substance',340,212)
def _():
    a=Ax(40,25,270,130,0,10,0,10)
    o=[a.axes('time','temperature'),PL([(a.X(0),a.Y(1)),(a.X(1.5),a.Y(3)),(a.X(3.5),a.Y(3)),(a.X(5.5),a.Y(7)),(a.X(9),a.Y(7)),(a.X(10),a.Y(9))],BL,2.6),
       T(a.X(2.5),a.Y(3)-12,'melting',OR,12),T(a.X(7.2),a.Y(7)-12,'boiling',OR,12),T(a.X(4.6),a.Y(4.2),'liquid',GY,11,'start'),T(a.X(0.6),a.Y(1.4),'solid',GY,11,'start'),
       T(170,186,'Flat parts: energy breaks bonds (latent heat),',INK,12),T(170,201,'internal energy rises but temperature does not',INK,12)]
    return o
@fig('p-errorbars','Error bars with best-fit and worst-fit lines',340,210)
def _():
    a=Ax(40,25,270,140,0,6,0,12); pts=[(1,2.1),(2,4.2),(3,5.7),(4,8.3),(5,9.9)]
    o=[a.axes('x','y')]
    for x,y in pts: o+=[L(a.X(x),a.Y(y-0.7),a.X(x),a.Y(y+0.7),INK,1.4),L(a.X(x)-4,a.Y(y-0.7),a.X(x)+4,a.Y(y-0.7),INK,1.4),L(a.X(x)-4,a.Y(y+0.7),a.X(x)+4,a.Y(y+0.7),INK,1.4),a.dot(x,y)]
    o+=[a.curve(lambda x:2*x,0,5.8,BL),a.curve(lambda x:1.2+1.6*x,0,6,OR,2,dash='6 4'),T(a.X(4.6),a.Y(11.6),'best fit',BL,12,'end'),T(a.X(5.9),a.Y(8.6),'worst fit',OR,12,'end'),
       T(170,195,'% uncertainty in gradient = |best − worst| / best × 100',INK,11.5)]
    return o
