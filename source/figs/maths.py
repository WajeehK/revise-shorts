from lib import *
import math
F={}
def fig(name,alt,w,h):
    def d(fn): F[name]=svg(w,h,fn(),alt); return fn
    return d
base=lambda x:(x-1)*(x+1)*(x-2)*0.5+1  # sample curve
@fig('m-transl','Translations of y = f(x): f(x) + a and f(x + a)',340,220)
def _():
    o=[]
    for k,(name,fn,lab) in enumerate([('y = f(x) + 2',lambda x:base(x)+2,'up 2: (x, y) → (x, y + 2)'),('y = f(x + 2)',lambda x:base(x+2),'left 2: (x, y) → (x − 2, y)')]):
        a=Ax(15+k*165,20,145,140,-4,4,-3,6)
        o+=[a.axes('x','y',0,0),a.curve(base,-4,4,GY,2,dash='5 4'),a.curve(fn,-4,4,[BL,OR][k],2.6),T(a.x+72,172,name,[BL,OR][k],13,b=True),T(a.x+72,188,lab,INK,10.5)]
    o+=[T(170,210,'Grey dashed curve: y = f(x)',GY,11)]
    return o
@fig('m-stretch','Stretches of y = f(x): a f(x) and f(ax)',340,220)
def _():
    g=lambda x:math.sin(x*math.pi/2)*1.5
    o=[]
    for k,(name,fn,lab) in enumerate([('y = 2f(x)',lambda x:2*g(x),'vertical ×2'),('y = f(2x)',lambda x:g(2*x),'horizontal ×½')]):
        a=Ax(15+k*165,20,145,140,-4,4,-3.6,3.6)
        o+=[a.axes('x','y',0,0),a.curve(g,-4,4,GY,2,dash='5 4'),a.curve(fn,-4,4,[BL,OR][k],2.6),T(a.x+72,172,name,[BL,OR][k],13,b=True),T(a.x+72,188,lab,INK,10.5)]
    o+=[T(170,210,'a f(x): y-values × a   ·   f(ax): x-values ÷ a',INK,11)]
    return o
@fig('m-reflect-mod','Reflections and the modulus function',340,220)
def _():
    o=[]
    for k,(name,fn,lab) in enumerate([('y = −f(x)',lambda x:-base(x),'reflect in x-axis'),('y = |f(x)|',lambda x:abs(base(x)-1.5),'negative parts flip up')]):
        a=Ax(15+k*165,20,145,140,-3,3,-4,4)
        b0=(lambda x:base(x)) if k==0 else (lambda x:base(x)-1.5)
        o+=[a.axes('x','y',0,0),a.curve(b0,-3,3,GY,2,dash='5 4'),a.curve(fn,-3,3,[BL,OR][k],2.6),T(a.x+72,172,name,[BL,OR][k],13,b=True),T(a.x+72,188,lab,INK,10.5)]
    o+=[T(170,210,'Also y = f(−x): reflect in the y-axis',INK,11)]
    return o
@fig('m-unit-circle','Unit circle: cos θ and sin θ as coordinates',340,230)
def _():
    cx,cy,r=100,115,78; t=math.radians(40); px,py=cx+r*math.cos(t),cy-r*math.sin(t)
    o=[A(cx-r-15,cy,cx+r+18,cy,INK,1.5,7),A(cx,cy+r+12,cx,cy-r-16,INK,1.5,7),C(cx,cy,r,GY,1.6),L(cx,cy,px,py,BL,2.4),L(px,py,px,cy,RD,2,'5 3'),L(cx,cy+0.5,px,cy+0.5,GR,3),
       C(px,py,4,BL,1,fill=BL),P(f'M{cx+26},{cy} A26,26 0 0 0 {f(cx+26*math.cos(t))},{f(cy-26*math.sin(t))}',INK,1.5),T(cx+34,cy-10,'θ',INK,13,i=True),
       T(px+6,py-10,'(cos θ, sin θ)',BL,12,'start',b=True),T((cx+px)/2,cy+14,'cos θ',GR,12),T(px+6,(py+cy)/2,'sin θ',RD,12,'start'),T(cx-8,cy-r-6,'1',INK,11,'end'),T(cx+r+4,cy+12,'1',INK,11),
       T(cx+(px-cx)/2-14,(cy+py)/2-8,'1',BL,12),
       T(268,84,'sin²θ + cos²θ = 1',INK,11.5,b=True),T(268,104,'tan θ = sin θ / cos θ',INK,12),T(268,128,'radians:',INK,12),T(268,144,'π rad = 180°',INK,12),T(268,166,'arc s = rθ',INK,12),T(268,182,'area = ½r²θ',INK,12)]
    return o
@fig('m-trig-graphs','Graphs of y = sin x and y = cos x for 0° ≤ x ≤ 360°',340,200)
def _():
    a=Ax(35,25,280,130,0,360,-1.25,1.25)
    o=[a.axes('','y',0,0),a.curve(lambda x:math.sin(math.radians(x)),0,360,BL),a.curve(lambda x:math.cos(math.radians(x)),0,360,OR)]
    for v in (90,180,270,360): o+=[L(a.X(v),a.Y(0)-3,a.X(v),a.Y(0)+3,INK,1.4),L(a.X(v),a.Y(0),a.X(v),a.Y(-1.25),GY,0.8,'2 3'),T(a.X(v),a.Y(-1.25)+10,f'{v}°',INK,11)]
    o+=[a.yt(1,'1'),a.yt(-1,'−1'),T(a.X(60),a.Y(1.1),'sin x',BL,12,b=True),T(a.X(330),a.Y(1.1),'cos x',OR,12,b=True),
        T(170,190,'Period 360° (2π). Use symmetry to find every solution in range',INK,11)]
    return o
@fig('m-cast','CAST diagram: which trig ratios are positive in each quadrant',340,200)
def _():
    cx,cy=110,100
    o=[A(cx-85,cy,cx+88,cy,INK,1.5,7),A(cx,cy+85,cx,cy-88,INK,1.5,7),T(cx+42,cy-40,'A',GR,22,b=True),T(cx-42,cy-40,'S',BL,22,b=True),T(cx-42,cy+42,'T',OR,22,b=True),T(cx+42,cy+42,'C',PU,22,b=True),
       T(cx+92,cy+12,'0°',INK,11),T(cx+8,cy-82,'90°',INK,11,'start'),T(cx-92,cy+12,'180°',INK,11),T(cx+8,cy+82,'270°',INK,11,'start'),
       T(262,40,'A: all positive',GR,12),T(262,62,'S: sin positive',BL,12),T(262,84,'T: tan positive',OR,12),T(262,106,'C: cos positive',PU,12),
       T(262,140,'sin(180° − θ) = sin θ',INK,11),T(262,158,'cos(360° − θ) = cos θ',INK,11),T(262,176,'tan(180° + θ) = tan θ',INK,11)]
    return o
@fig('m-circle','Circle with centre (a, b), radius r and a tangent',340,220)
def _():
    cx,cy,r=95,105,62; t=math.radians(35); px,py=cx+r*math.cos(t),cy-r*math.sin(t)
    dx,dy=-math.sin(t),-math.cos(t)
    o=[C(cx,cy,r,BL,2.4),C(cx,cy,3.5,INK,1,fill=INK),T(cx-6,cy+14,'(a, b)',INK,12,'end'),L(cx,cy,px,py,INK,1.8),T((cx+px)/2-6,(cy+py)/2-8,'r',INK,13,i=True),
       L(px-45*dx,py-45*dy,px+55*dx,py+55*dy,RD,2.2),C(px,py,3.5,RD,1,fill=RD),
       PL([(px+(-math.cos(t))*10,py+math.sin(t)*10),(px+(-math.cos(t))*10+dx*10,py+math.sin(t)*10+dy*10),(px+dx*10,py+dy*10)],INK,1.4),T(px+30,py+46,'tangent',RD,12,'start'),
       T(262,140,'(x − a)² + (y − b)² = r²',INK,12,b=True),T(262,162,'tangent ⟂ radius:',INK,11.5),T(262,178,'m_tangent = −1 / m_radius',INK,11.5),T(262,200,'angle in a semicircle = 90°',INK,11)]
    return o
@fig('m-tangent-normal','Tangent and normal to a curve at a point',340,220)
def _():
    a=Ax(35,20,270,160,-1,4,-1,7); fn=lambda x:0.5*x*x+0.5; x0=1.6; y0=fn(x0); m=x0
    o=[a.axes('x','y',0,0),a.curve(fn,-1,3.6,BL),a.curve(lambda x:y0+m*(x-x0),-0.2,3.6,RD,2.2),a.curve(lambda x:y0-(x-x0)/m,-1,4,GR,2.2),a.dot(x0,y0),
       T(a.X(3.7),a.Y(6.2),'tangent: gradient = f′(x₁)',RD,11.5,'end'),T(a.X(-0.9),a.Y(4.4),'normal: −1 / f′(x₁)',GR,11.5,'start'),T(a.X(x0)-8,a.Y(y0)-8,'(x₁, y₁)',INK,12,'end'),T(a.X(-0.9),a.Y(1.6),'y = f(x)',BL,12,'start'),
       T(170,205,'y − y₁ = m(x − x₁)',INK,12,b=True)]
    return o
@fig('m-stationary','Stationary points: maximum, minimum and point of inflection',340,210)
def _():
    a=Ax(20,20,300,150,-2.2,2.6,-3,4); fn=lambda x:x**3-3*x+0.5
    o=[a.axes('x','y',0,0),a.curve(fn,-2.2,2.3,BL),a.dot(-1,fn(-1),RD),a.dot(1,fn(1),GR),
       T(a.X(-2.1),a.Y(fn(-1))-14,'max: dy/dx = 0, d²y/dx² < 0',RD,11,'start'),T(a.X(2.55),a.Y(fn(1))+16,'min: dy/dx = 0, d²y/dx² > 0',GR,11,'end'),
       T(170,196,'Increasing where f′(x) > 0 · decreasing where f′(x) < 0',INK,11)]
    return o
@fig('m-area','Area under a curve and between a curve and a line',340,220)
def _():
    o=[]
    a=Ax(15,20,145,140,0,4,-0.5,5); fn=lambda x:-0.6*(x-2)**2+4.2
    o+=[a.area(fn,0.6,3.4,BL,0.3),a.axes('x','y',0,0),a.curve(fn,0,4,BL),a.xt(0.6,'a'),a.xt(3.4,'b'),T(a.x+72,a.Y(1.5),'∫ₐᵇ y dx',INK,12,b=True),T(87,180,'area under curve',INK,11)]
    b=Ax(180,20,145,140,0,4,-0.5,5); g=lambda x:1+0.5*x
    pts=[]
    o+=[b.axes('x','y',0,0)]
    xs=[0.5+i*0.05 for i in range(0,63)]
    o+=['<polygon points="'+' '.join(f'{f(b.X(x))},{f(b.Y(fn(x)))}' for x in xs if fn(x)>=g(x))+' '+' '.join(f'{f(b.X(x))},{f(b.Y(g(x)))}' for x in reversed(xs) if fn(x)>=g(x))+f'" fill="{OR}" fill-opacity=".3" stroke="none"/>',
        b.curve(fn,0,4,BL),b.curve(g,0,4,RD,2.2),T(b.x+72,180,'∫ (top − bottom) dx',INK,11)]
    o+=[T(170,205,'Area below the x-axis gives a negative integral: split at roots',INK,11)]
    return o
@fig('m-trapezium','Trapezium rule estimate of an integral',340,210)
def _():
    a=Ax(30,24,280,136,0,4.6,0,6.6); fn=lambda x:0.25*x*x+1; xs=[0.4,1.4,2.4,3.4,4.4][:4]+[4.4]
    xs=[0.4+i*1.0 for i in range(5)]
    o=[]
    for i in range(4):
        x1,x2=xs[i],xs[i+1]
        o.append(PL([(a.X(x1),a.Y(0)),(a.X(x1),a.Y(fn(x1))),(a.X(x2),a.Y(fn(x2))),(a.X(x2),a.Y(0))],OR,1.6,fill=OR+'33',close=True))
    for i,x in enumerate(xs): o.append(T(a.X(x)-(8 if i==4 else 0),a.Y(fn(x))-14,f'y{"₀₁₂₃₄"[i]}',OR,11))
    o+=[a.axes('x','y'),a.curve(fn,0,4.4,BL),A(a.X(xs[1]),a.Y(0)+12,a.X(xs[2]),a.Y(0)+12,INK,1.2,6,both=True),T(a.X(1.9),a.Y(0)+24,'h',INK,12,i=True),
        T(170,192,'∫ y dx ≈ ½h[y₀ + 2(y₁ + y₂ + y₃) + y₄]',INK,12,b=True),T(170,207,'Curve convex (bends up) → trapezia overestimate',GY,10.5)]
    return o
@fig('m-newton','Newton–Raphson: following tangents to a root',340,210)
def _():
    a=Ax(30,20,280,150,0,4,-1.5,8); fn=lambda x:x*x-2; d=lambda x:2*x
    o=[a.axes('x','y',0,0),a.curve(fn,0.8,3.3,BL)]
    x=3.0
    for k in range(2):
        y=fn(x); x2=x-y/d(x)
        o+=[L(a.X(x),a.Y(0),a.X(x),a.Y(y),GY,1.2,'4 3'),a.curve(lambda t,x=x,y=y:y+d(x)*(t-x),x2-0.15,x+0.1,RD,1.8),a.dot(x,y,INK,3),T(a.X(x),a.Y(0)+14,f'x{"₀₁₂"[k]}',INK,12)]
        x=x2
    o+=[a.dot(math.sqrt(2),0,GR,4),T(a.X(1.414)-6,a.Y(0)-12,'root',GR,11,'end'),T(170,195,'xₙ₊₁ = xₙ − f(xₙ) / f′(xₙ)   (fails if f′(xₙ) ≈ 0)',INK,12,b=True)]
    return o
@fig('m-vectors','Vector addition and position vectors',340,200)
def _():
    O=(40,160); A_=(150,70); B_=(290,120)
    o=[A(*O,*A_,BL,2.4),A(*A_,*B_,OR,2.4),A(*O,*B_,PU,2.6),C(*O,3.5,INK,1,fill=INK),T(O[0]-6,O[1]+12,'O',INK,12),T(A_[0],A_[1]-12,'A',INK,12,b=True),T(B_[0]+8,B_[1],'B',INK,12,'start',b=True),
       T(84,104,'a',BL,14,b=True),T(228,84,'b − a',OR,13,b=True),T(170,160,'b',PU,14,b=True),
       T(170,186,'OB = OA + AB,  so  AB = b − a',INK,12,b=True)]
    return o
@fig('m-exp-ln','Graphs of y = eˣ and y = ln x: reflections in y = x',340,220)
def _():
    a=Ax(30,15,215,180,-3,4.5,-3,4.5)
    o=[a.axes('x','y',0,0),a.curve(lambda x:x,-3,4.5,GY,1.4,dash='5 4'),a.curve(math.exp,-3,1.5,BL),a.curve(lambda x:math.log(x) if x>0 else None,0.04,4.5,OR),a.dot(0,1,BL),a.dot(1,0,OR),
       T(a.X(1.2),a.Y(3.9),'y = eˣ',BL,12,'end',b=True),T(a.X(4.4),a.Y(1.9),'y = ln x',OR,12,'end',b=True),T(a.X(4.2),a.Y(3.7),'y = x',GY,11,'end'),T(a.X(0)-6,a.Y(1),'(0, 1)',BL,11,'end'),T(a.X(1)+4,a.Y(0)+12,'(1, 0)',OR,11,'start'),
       T(296,130,'eˣ > 0',INK,11),T(296,146,'ln x: x > 0',INK,11),T(296,168,'y = 0 and x = 0',INK,10),T(296,182,'are asymptotes',INK,10)]
    return o
@fig('s-normal','Normal distribution with the 68–95–99.7 rule',340,210)
def _():
    a=Ax(20,20,300,130,-3.6,3.6,0,0.45); pdf=lambda z:math.exp(-z*z/2)/math.sqrt(2*math.pi)
    o=[a.area(pdf,-2,2,BL,0.15),a.area(pdf,-1,1,BL,0.25),A(20,a.Y(0),326,a.Y(0),INK,1.5,7),a.curve(pdf,-3.6,3.6,BL)]
    for z,l in ((-2,'μ − 2σ'),(-1,'μ − σ'),(0,'μ'),(1,'μ + σ'),(2,'μ + 2σ')): o+=[L(a.X(z),a.Y(0),a.X(z),a.Y(pdf(z)),GY,1,'3 3'),T(a.X(z),a.Y(0)+14,l,INK,11)]
    o+=[T(a.X(0),a.Y(0.2),'≈ 68%',INK,12,b=True),T(a.X(0),a.Y(0.07),'≈ 95% within ±2σ',INK,10.5),
        T(170,186,'X ~ N(μ, σ²): symmetric about μ; points of inflection at μ ± σ',INK,11),T(170,201,'≈ 99.7% within μ ± 3σ.  Z = (X − μ)/σ',INK,11)]
    return o
@fig('s-crit','Two-tailed hypothesis test: critical regions in the tails',340,200)
def _():
    a=Ax(20,20,300,120,-3.6,3.6,0,0.45); pdf=lambda z:math.exp(-z*z/2)/math.sqrt(2*math.pi)
    o=[a.area(pdf,-3.6,-1.96,RD,0.45),a.area(pdf,1.96,3.6,RD,0.45),A(20,a.Y(0),326,a.Y(0),INK,1.5,7),a.curve(pdf,-3.6,3.6,BL),
       T(a.X(-2.6),a.Y(0.12),'2.5%',RD,11,b=True),T(a.X(2.6),a.Y(0.12),'2.5%',RD,11,b=True),T(a.X(0),a.Y(0.15),'accept H₀',GY,12),
       a.xt(-1.96,'−1.96',14),a.xt(1.96,'1.96',14),T(170,172,'5% two-tailed: reject H₀ if the test statistic lies in a tail',INK,11),T(170,188,'(half the significance level in each tail)',GY,10.5)]
    return o
@fig('s-boxplot','Box plot with quartiles and an outlier',340,170)
def _():
    X=lambda v:30+v*2.8
    o=[L(X(0),120,X(100),120,INK,1.5)]
    for v in range(0,101,20): o+=[L(X(v),117,X(v),123,INK,1.4),T(X(v),134,str(v),INK,11)]
    o+=[L(X(12),70,X(28),70,INK,2),L(X(12),60,X(12),80,INK,2),R(X(28),52,X(55)-X(28),36,BL,2.2,fill=BL+'22'),L(X(41),52,X(41),88,BL,2.6),R(X(41),52,X(55)-X(41),36,BL,2.2),
        L(X(55),70,X(70),70,INK,2),L(X(70),60,X(70),80,INK,2),T(X(92),70,'×',RD,16,b=True),
        T(X(12),44,'min',INK,10),T(X(28),40,'Q₁',INK,11),T(X(41),40,'Q₂',INK,11),T(X(55),40,'Q₃',INK,11),T(X(70),44,'max*',INK,10),T(X(92),52,'outlier',RD,10.5),
        T(170,152,'IQR = Q₃ − Q₁. Outlier: e.g. > Q₃ + 1.5 × IQR',INK,11.5),T(170,166,'*whisker ends at the largest value that is not an outlier',GY,9.5)]
    return o
@fig('s-venn','Venn diagram for two events',340,190)
def _():
    o=[R(20,20,210,140,INK,1.6,rx=6),C(95,90,52,BL,2.2,fill=BL+'22'),C(155,90,52,OR,2.2,fill=OR+'22'),T(70,90,'0.3',INK,13),T(125,90,'0.2',INK,13,b=True),T(182,90,'0.1',INK,13),T(205,145,'0.4',INK,13),
       T(60,38,'A',BL,14,b=True),T(190,38,'B',OR,14,b=True),T(212,30,'ξ',INK,13),
       T(285,50,'P(A ∩ B) = 0.2',INK,11.5),T(285,70,'P(A ∪ B) = 0.6',INK,11.5),T(285,90,'P(A) = 0.5',INK,11.5),T(285,110,'P(B | A) = 0.2/0.5',INK,11.5),T(285,126,'= 0.4',INK,11.5),
       T(170,180,'Independent if P(A ∩ B) = P(A) × P(B): here 0.2 ≠ 0.5 × 0.3',INK,10.5)]
    return o
@fig('s-tree','Tree diagram for two events',340,200)
def _():
    o=[];r=(30,100)
    first=[('R',0.6,55),('B',0.4,145)]
    for lab,p,y in first:
        o+=[L(*r,120,y,INK,1.8),T(128,y,lab,BL,13,b=True),T(75,(100+y)/2-(8 if y<100 else -8),str(p),INK,11)]
        for lab2,q,dy in (('R',0.5 if lab=='R' else 0.6,-22),('B',0.5 if lab=='R' else 0.4,22)):
            o+=[L(138,y,220,y+dy,INK,1.8),T(228,y+dy,lab2,OR,13,b=True),T(178,y+dy/2-(8 if dy<0 else -8),str(q),INK,11),T(250,y+dy,f'{lab}{lab2}: {p*q:.2f}'.replace('0.','0.'),INK,11,'start')]
    o+=[T(170,190,'Multiply along branches; add the end results you need',INK,11)]
    return o
@fig('k-suvat-vt','Kinematics: velocity–time graph for constant acceleration',340,200)
def _():
    a=Ax(40,25,270,130,0,10,0,10)
    o=[a.area(lambda t:2+0.7*t,0,10,BL,0.15),a.axes('','v'),a.curve(lambda t:2+0.7*t,0,10,BL),L(a.X(0),a.Y(2),a.X(10),a.Y(2),GY,1,'4 4'),L(a.X(10),a.Y(0),a.X(10),a.Y(9),GY,1,'4 4'),
       a.yt(2,'u'),a.yt(9,'v'),a.xt(10,'t'),T(a.X(5),a.Y(1),'ut',INK,12),T(a.X(6.6),a.Y(3.9),'½(v − u)t',INK,12),A(a.X(10)+12,a.Y(2),a.X(10)+12,a.Y(9),OR,1.4,6,both=True),T(a.X(10)+16,a.Y(5.5),'at',OR,12,'start'),
       T(170,185,'Area = s = ½(u + v)t   ·   gradient = a = (v − u)/t',INK,11.5)]
    return o
@fig('k-pulley','Connected particles over a smooth pulley on a rough table',340,210)
def _():
    o=[R(20,90,220,10,INK,1.8,fill=LT),L(240,90,240,200,INK,1.8),C(250,90,10,INK,2,fill='#fff'),C(250,90,2,INK,1,fill=INK),
       R(90,60,50,30,INK,2,fill='#c9ecfd',rx=3),T(115,75,'A (m₁)',INK,11),L(140,80,250,80,INK,1.6),L(260,90,260,140,INK,1.6),R(245,140,30,30,INK,2,fill='#ffe2cc',rx=3),T(260,155,'B',INK,11),
       A(140,72,200,72,BL,2,7),T(170,64,'T',BL,13,i=True),A(260,140,260,110,BL,2,7),T(268,116,'T',BL,13,'start',i=True),A(90,82,50,82,GR,2,7),T(55,70,'F = μR',GR,12),
       A(115,90,115,125,RD,2,7),T(115,135,'m₁g',RD,11),A(115,60,115,30,PU,2,7),T(122,36,'R',PU,12,'start'),A(260,170,260,200,RD,2,7),T(270,196,'m₂g',RD,11,'start'),
       T(120,160,'Same tension and same |a| for both',INK,11),T(120,176,'(light inextensible string)',INK,11),T(120,198,'B: m₂g − T = m₂a   A: T − F = m₁a',INK,11,b=True)]
    return o
@fig('k-ladder','Ladder against a smooth wall on rough ground',340,230)
def _():
    o=[L(40,200,300,200,INK,2.4),L(270,20,270,200,INK,2.4),L(120,200,270,40,OR,6),
       A(120,200,120,150,PU,2,7),T(126,152,'R',PU,13,'start'),A(120,200,170,200,GR,2,7),T(150,214,'F (friction)',GR,11),
       A(270,40,225,40,BL,2,7),T(222,30,'S',BL,13,'end'),A(195,120,195,165,RD,2,7),T(201,166,'W',RD,13,'start'),C(195,120,3,INK,1,fill=INK),
       P('M150,200 A30,30 0 0 0 140,178',INK,1.4),T(152,186,'θ',INK,13,i=True),
       T(100,40,'Resolve: F = S, R = W',INK,11.5),T(100,58,'Moments about the foot:',INK,11.5),T(100,74,'W × ½l cos θ = S × l sin θ',INK,11.5),T(100,96,'Limiting friction: F = μR',INK,11.5)]
    return o
@fig('k-incline','Particle on a rough inclined plane: resolving forces',340,220)
def _():
    th=math.radians(25); x0,y0=25,195; L1=290; top=(x0+L1*math.cos(th),y0-L1*math.sin(th))
    ux,uy=math.cos(th),-math.sin(th); nx,ny=-math.sin(th),-math.cos(th); cx,cy=x0+170*math.cos(th),y0-170*math.sin(th); bx,by=cx+nx*15,cy+ny*15
    pts=[(cx-ux*20,cy-uy*20),(cx+ux*20,cy+uy*20),(cx+ux*20+nx*30,cy+uy*20+ny*30),(cx-ux*20+nx*30,cy-uy*20+ny*30)]
    o=[PL([(x0,y0),(top[0],y0),top],INK,2,fill=LT,close=True),PL(pts,INK,2,fill='#ffe2cc',close=True),
       A(bx,by,bx+ux*70,by+uy*70,BL,2.2),T(bx+ux*74,by+uy*74-8,'P (pull)',BL,12,'start'),A(bx,by,bx-ux*60,by-uy*60,GR,2.2),T(bx-ux*64-2,by-uy*64+12,'F ≤ μR',GR,12,'end'),
       A(bx,by,bx+nx*60,by+ny*60,PU,2.2),T(bx+nx*64,by+ny*64-6,'R',PU,13),A(bx,by,bx,by+64,RD,2.2),T(bx+6,by+70,'mg',RD,13,'start'),
       P(f'M{x0+40},{y0} A40,40 0 0 0 {f(x0+40*math.cos(th))},{f(y0-40*math.sin(th))}',INK,1.4),T(x0+50,y0-8,'α',INK,13,i=True),
       T(170,16,'⟂ plane: R = mg cos α   ·   along: P − F − mg sin α = ma',INK,11)]
    return o
@fig('k-moments-beam','Uniform beam resting on two supports',340,180)
def _():
    X=lambda m:30+m*45
    o=[R(X(0),70,X(6)-X(0),12,INK,2,fill='#ffe2cc',rx=2),PL([(X(1),82),(X(1)-12,104),(X(1)+12,104)],INK,2,fill=LT,close=True),PL([(X(5),82),(X(5)-12,104),(X(5)+12,104)],INK,2,fill=LT,close=True),
       A(X(1),70,X(1),30,PU,2,7),T(X(1)+6,32,'R_C',PU,12,'start'),A(X(5),70,X(5),30,PU,2,7),T(X(5)+6,32,'R_D',PU,12,'start'),A(X(3),82,X(3),130,RD,2,7),T(X(3)-6,126,'W (at centre)',RD,12,'end'),
       A(X(4.4),82,X(4.4),118,OR,2,7),T(X(4.4),128,'man',OR,11),
       T(X(0),60,'A',INK,12),T(X(6),60,'B',INK,12),T(X(1),114,'C',INK,11),T(X(5),114,'D',INK,11),
       T(170,152,'Equilibrium: ↑ forces = ↓ forces and moments about any point balance',INK,10.5),T(170,168,'On the point of tilting about D: R_C = 0',INK,10.5)]
    return o
