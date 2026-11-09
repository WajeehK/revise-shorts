from lib import *
import math
B=Bank(1); R=B.R; a=B.add
def ri(x,y): return R.randint(x,y)
def pick(*xs): return R.choice(xs)
def sgn(c,first=False):
    s=fm(abs(c)); return (('−' if c<0 else '')+s) if first else ((' − ' if c<0 else ' + ')+s)
# ---- algebra
for _ in range(3):
    p,q,r,k=ri(1,4),ri(-6,6),ri(-9,9),ri(-3,3)
    while k==0:k=ri(-3,3)
    a('m-alg',1,N(f'Find the remainder when f(x) = x³{sgn(p)}x²{sgn(q)}x{sgn(r)} is divided by (x{sgn(-k)}).',k**3+p*k*k+q*k+r,0,'',f'Remainder theorem: f({fm(k)}).'))
for _ in range(2):
    m,c,n=ri(2,5),ri(-5,5),ri(1,4)
    a('m-alg',1,N(f'f(x) = {m}x{sgn(c)} and g(x) = x² + {n}. Find fg(2).',m*(4+n)+c,0,'','g(2) first, then apply f.'))
for _ in range(3):
    r1,b,c=ri(1,4),ri(-5,5),ri(-8,8)
    c-=(r1**3+b*r1+c)%(r1*r1); k=-(r1**3+b*r1+c)/(r1*r1)
    a('m-alg',2,N(f'(x − {r1}) is a factor of x³ + kx²{sgn(b)}x{sgn(c)}. Find k.',k,0,'',f'Factor theorem: f({r1}) = 0.'))
for _ in range(3):
    m,c=ri(2,6),ri(1,9); x=ri(2,8)
    a('m-alg',2,N(f'f(x) = (x + {c})/{m}, x ∈ ℝ. Find f⁻¹({x}).',m*x-c,0,'','f⁻¹(x) = '+f'{m}x − {c}.'))
for _ in range(2):
    k=ri(2,5);b=ri(1,6)
    a('m-alg',2,N(f'Solve |{k}x − {b}| = {b+k*2} for the positive solution x.',(b+b+k*2)/k,0.5,'',f'{k}x − {b} = {b+2*k}.'))
for _ in range(3):
    p,q=ri(1,4),ri(1,5); A0,B0=ri(1,5),ri(-4,5)
    while B0==0:B0=ri(-4,5)
    # (A(x+q)+B(x-p))/((x-p)(x+q))
    num1=A0+B0; num0=A0*q-B0*p
    a('m-alg',3,N(f'Express ({fm(num1)}x{sgn(num0)})/((x − {p})(x + {q})) as A/(x − {p}) + B/(x + {q}). Find A.',A0,0,'',f'Substitute x = {p}: A = ({fm(num1*p+num0)})/({p+q}).'))
for _ in range(2):
    c=ri(1,9);k=ri(2,4)
    a('m-alg',3,N(f'f(x) = {k}(x − 1)² + {c} for x ≥ 1. Find f⁻¹({k*9+c}).',4,0,'',f'Minimum {c} at x = 1. Solve {k}(x − 1)² + {c} = {k*9+c}: x − 1 = 3, x = 4.'))
for _ in range(2):
    p=ri(2,5);q=ri(1,6)
    a('m-alg',3,N(f'f(x) = e^x + {q}, g(x) = {p}x. Solve fg(x) = {q+math.e**p:.4f} (3 s.f.).',1,0.5,'',f'e^({p}x) = e^{p}, so x = 1.'))
# ---- coordinate geometry
for _ in range(3):
    x1,y1,x2,y2=ri(-5,5),ri(-5,5),ri(-5,8),ri(-5,8)
    while x2==x1:x2=ri(-5,8)
    a('m-coord',1,N(f'Find the gradient of the line through ({x1}, {y1}) and ({x2}, {y2}).',(y2-y1)/(x2-x1),0.5,'','Δy/Δx.'))
for _ in range(2):
    x1,y1,x2,y2=ri(-6,6),ri(-6,6),ri(-6,6),ri(-6,6)
    a('m-coord',1,N(f'Find the length of the line from ({x1}, {y1}) to ({x2}, {y2}) (3 s.f.).',math.hypot(x2-x1,y2-y1),0.5,'','Pythagoras.'))
for _ in range(3):
    h,k,r=ri(-5,5),ri(-5,5),ri(2,7)
    D,E,Fc=-2*h,-2*k,h*h+k*k-r*r
    a('m-coord',2,N(f'Circle x² + y²{sgn(D)}x{sgn(E)}y{sgn(Fc)} = 0. Find its radius.',r,0,'','Complete the square.'))
for _ in range(3):
    m=pick(2,3,-2,4,0.5);c=ri(-5,5);px=ri(-3,3)
    a('m-coord',2,N(f'Line L passes through ({px}, {fm(m*px+c)}) and is perpendicular to y = {fm(-1/m)}x + 1. Find the y-intercept of L.',c,0.5,'',f'Gradient of L = {fm(m)}.'))
for _ in range(2):
    t=ri(1,4)
    a('m-coord',2,N(f'A curve has x = t² + 1, y = 2t³. Find dy/dx when t = {t}.',3*t,0,'','dy/dx = 6t²/2t = 3t.'))
for _ in range(3):
    h,k,r=ri(1,5),ri(1,5),5; px,py=h+3,k+4
    a('m-coord',3,N(f'A circle has centre ({h}, {k}) and passes through ({px}, {py}). The tangent at ({px}, {py}) meets the x-axis at A. Find the x-coordinate of A.',px+py*4/3,0.5,'','Radius gradient 4/3, tangent gradient −3/4.'))
for _ in range(2):
    m=ri(1,3);c=ri(-3,0)
    # intersection of y = mx + c with x²+y²=25 -> count via discriminant
    A=1+m*m;Bq=2*m*c;C=c*c-25;disc=Bq*Bq-4*A*C
    a('m-coord',3,N(f'Find the discriminant of the quadratic in x formed by substituting y = {m}x{sgn(c)} into x² + y² = 25.',disc,0,'','Positive ⇒ two intersections.'))
# ---- sequences
for _ in range(3):
    A0,d,n=ri(2,9),ri(2,7),ri(10,30)
    a('m-seq',1,N(f'Arithmetic sequence: a = {A0}, d = {d}. Find the {n}th term.',A0+(n-1)*d,0,'','a + (n − 1)d.'))
for _ in range(2):
    A0,r=ri(2,6),pick(2,3)
    a('m-seq',1,N(f'Geometric sequence: first term {A0}, ratio {r}. Find the 6th term.',A0*r**5,0,'',f'uₙ = arⁿ⁻¹, so u₆ = {A0} × {r}⁵.'))
for _ in range(3):
    n=ri(4,8);k=ri(2,3);p=ri(2,3)
    a('m-seq',2,N(f'Find the coefficient of x^{p} in ({1} + {k}x)^{n}.',math.comb(n,p)*k**p,0,'',f'ⁿC_{p} × {k}^{p}.'))
for _ in range(2):
    A0,r=ri(10,90),pick(0.5,0.25,0.2,0.8)
    a('m-seq',2,N(f'Find the sum to infinity of a geometric series with first term {A0} and ratio {r}.',A0/(1-r),0.5,'','a/(1 − r).'))
for _ in range(3):
    A0,d=ri(3,9),ri(2,5);S=ri(200,600)
    n=math.ceil(next(n for n in range(1,400) if n/2*(2*A0+(n-1)*d)>S))
    a('m-seq',3,N(f'An arithmetic series has a = {A0}, d = {d}. Find the least n for which Sₙ > {S}.',n,0,'','Solve n/2(2a + (n − 1)d) > S, then round up.'))
for _ in range(2):
    P0,r=ri(1000,5000),pick(1.03,1.04,1.05)
    a('m-seq',3,N(f'£{P0} is invested at {round((r-1)*100)}% compound interest per year. Find the least number of whole years for it to exceed £{2*P0}.',math.ceil(math.log(2)/math.log(r)),0,'years','Solve r^n > 2 with logs.'))
for _ in range(2):
    x=pick(0.1,0.05,0.02)
    a('m-seq',3,N(f'Use the first three terms of the expansion of √(1 + 4x) to estimate √(1 + 4×{x}) (4 d.p.).',1+2*x-2*x*x,0.05,'','(1 + 4x)^½ ≈ 1 + 2x − 2x².'))
# ---- trig
for _ in range(3):
    r,th=ri(3,12),pick(0.8,1.2,1.5,2.1)
    a('m-trig',1,N(f'Sector radius {r} cm, angle {th} rad. Find its area.',0.5*r*r*th,0.5,'cm²','½r²θ.'))
for _ in range(2):
    d=pick(45,120,135,210,300)
    a('m-trig',1,N(f'Convert {d}° to radians (3 s.f.).',math.radians(d),0.5,'rad','× π/180.'))
for _ in range(3):
    v=pick(0.3,0.4,0.6,0.7)
    a('m-trig',2,N(f'Solve sin x = {v} for 90° < x < 180° (1 d.p.).',180-math.degrees(math.asin(v)),0.2,'°','x = 180° − sin⁻¹.'))
for _ in range(2):
    R0=pick((3,4),(5,12),(8,15))
    a('m-trig',2,N(f'Write {R0[0]} sin x + {R0[1]} cos x as R sin(x + α). Find R.',math.hypot(*R0),0,'','R = √(a² + b²).'))
for _ in range(3):
    A0,Bc=pick((3,4),(5,12),(1,1),(2,3))
    al=math.degrees(math.atan2(Bc,A0)); Rr=math.hypot(A0,Bc)
    a('m-trig',3,N(f'{A0} sin x + {Bc} cos x = R sin(x + α). Find the maximum value of 1/(10 − ({A0} sin x + {Bc} cos x)) (3 s.f.).',1/(10-Rr),0.5,'',f'Greatest when sin(x + α) = 1, so the bracket equals R = {fm(Rr,4)}.'))
for _ in range(2):
    a('m-trig',3,N('Solve 2cos²x + 3sin x = 3 for 0 < x < 90° (in degrees).',30,0,'°','2(1 − sin²x) + 3sin x − 3 = 0 → (2 sin x − 1)(sin x − 1) = 0; sin x = ½.'))
    break
a('m-trig',3,N('Solve tan²x − 3 = 0 for 0 < x < 90° (degrees).',60,0,'°','tan x = √3.'))
a('m-trig',3,N('Using small-angle approximations, find the limit of (1 − cos 2θ)/θ² as θ → 0.',2,0,'','1 − (1 − 2θ²) = 2θ².'))
# ---- exp & logs
for _ in range(3):
    b,c=pick(2,3,5,7),ri(10,90)
    a('m-exp',1,N(f'Solve {b}^x = {c} (3 s.f.).',math.log(c)/math.log(b),0.5,'','x = ln c / ln b.'))
for _ in range(2):
    k=pick(2,3,4,5)
    a('m-exp',1,N(f'Solve ln x = {k} (3 s.f.).',math.e**k,0.5,'','x = e^k.'))
for _ in range(3):
    A0,k,t=ri(50,500),pick(0.02,0.05,0.1,0.15),ri(5,20)
    a('m-exp',2,N(f'N = {A0}e^({k}t). Find t when N = {2*A0} (3 s.f.).',math.log(2)/k,0.5,'','ln 2 / k.'))
for _ in range(2):
    n=pick(8,27,32,81)
    b={8:2,27:3,32:2,81:3}[n]
    a('m-exp',2,N(f'Solve 2 log_{b} x = log_{b} {n*n}.',n,0,'','log x² = log n² so x = n.'))
for _ in range(3):
    A0,k=ri(100,900),pick(0.1,0.2,0.3)
    a('m-exp',3,N(f'A model gives log₁₀P = {fm(math.log10(A0),4)} + {k}t. Find P when t = 5 (3 s.f.).',10**(math.log10(round(A0*10**4)/10**4) if False else math.log10(A0)+5*k) if False else 10**(float(fm(math.log10(A0),4))+5*k),0.5,'','P = 10^(c + kt).'))
for _ in range(2):
    k=pick(0.2,0.3,0.5);T0=ri(60,90)
    a('m-exp',3,N(f'Coffee cools as T = 20 + {T0-20}e^(−{k}t). Find the time when T = 40 (3 s.f.).',math.log((T0-20)/20)/k,0.5,'min','Rearrange and take ln.'))
for _ in range(2):
    A0=ri(2,6);n=ri(2,4)
    a('m-exp',3,N(f'y = ax^n. A graph of log y against log x is a straight line through (0, {fm(math.log10(A0),4)}) with gradient {n}. Find y when x = 2 (3 s.f.).',A0*2**n,0.5,'','a = 10^intercept, n = gradient.'))
# ---- differentiation
for _ in range(3):
    p,q,x=ri(1,5),ri(-6,6),ri(-3,3)
    a('m-diff',1,N(f'y = {p}x³{sgn(q)}x². Find dy/dx at x = {x}.',3*p*x*x+2*q*x,0,'','Power rule.'))
for _ in range(2):
    k=ri(2,5)
    a('m-diff',1,N(f'y = {k}√x. Find dy/dx at x = 4.',k/(2*2),0.5,'','d/dx(x^½) = ½x^−½.'))
for _ in range(3):
    k,x=ri(2,4),pick(0,1,2)
    a('m-diff',2,N(f'y = x e^({k}x). Find dy/dx at x = {x} (3 s.f.).',math.e**(k*x)*(1+k*x),0.5,'','Product rule.'))
for _ in range(2):
    k=ri(2,5)
    a('m-diff',2,N(f'y = ln({k}x² + 1). Find dy/dx at x = 1 (3 s.f.).',2*k/(k+1),0.5,'','Chain rule: 2kx/(kx² + 1).'))
for _ in range(2):
    k=ri(2,4)
    a('m-diff',2,N(f'y = sin({k}x)/x. Find dy/dx at x = π (3 s.f.).',(k*math.pi*math.cos(k*math.pi)-math.sin(k*math.pi))/math.pi**2,0.5,'','Quotient rule.'))
for _ in range(3):
    p=ri(2,6)
    a('m-diff',3,N(f'y = x³ − {3*p*p}x. Find the y-coordinate of the local minimum.',p**3-3*p*p*p,0,'',f'dy/dx = 3x² − {3*p*p} = 0 → x = ±{p}; d²y/dx² > 0 at x = {p}.'))
for _ in range(2):
    V=pick(500,1000,2000)
    r=(V/(2*math.pi))**(1/3)
    a('m-diff',3,N(f'A closed cylinder has volume {V} cm³. Find the radius that minimises its surface area (3 s.f.).',r,0.5,'cm','A = 2πr² + 2V/r; dA/dr = 0 → r³ = V/2π.'))
for _ in range(2):
    k=ri(2,5)
    a('m-diff',3,N(f'x² + y² + {k}xy = 7 + {k*2}... Find dy/dx at (1, 2) for x² + y² + {k}xy = {5+2*k} (3 s.f.).'.split('... ')[1],-(2+2*k)/(4+k),0.5,'','Implicit: 2x + 2y dy/dx + k(y + x dy/dx) = 0.'))
# ---- integration
for _ in range(3):
    p,q,b=ri(1,6),ri(1,6),ri(1,4)
    a('m-int',1,N(f'Evaluate ∫₀^{b} ({p}x² + {q}) dx.',p*b**3/3+q*b,0.5,'','Integrate then substitute.'))
for _ in range(2):
    k=ri(2,6)
    a('m-int',1,N(f'Evaluate ∫₁^{k} (1/x) dx (3 s.f.).',math.log(k),0.5,'',f'∫(1/x) dx = ln x, so the answer is ln {k} − ln 1 = ln {k}.'))
for _ in range(3):
    k=ri(2,4)
    a('m-int',2,N(f'Evaluate ∫₀^(π/2) sin({k}x) dx (3 s.f.).',(1-math.cos(k*math.pi/2))/k,0.5,'','[−cos(kx)/k].'))
for _ in range(2):
    k=ri(1,3)
    a('m-int',2,N(f'Evaluate ∫₀¹ x e^({k}x) dx (3 s.f.).',(math.e**k*(k-1)+1)/k**2,0.5,'','By parts.'))
for _ in range(2):
    p=ri(2,5)
    a('m-int',2,N(f'Find the area enclosed between y = x({p} − x) and the x-axis (3 s.f.).',p**3/6,0.5,'','∫₀^p (px − x²) dx = p³/6.'))
for _ in range(3):
    m=ri(1,3)
    # area between y=x^2 and y=mx+... use y = x^2 and y = kx
    k=ri(2,5)
    a('m-int',3,N(f'Find the area enclosed by y = x² and y = {k}x (3 s.f.).',k**3/6,0.5,'','Intersect at 0 and k; ∫(kx − x²) dx.'))
for _ in range(2):
    k=ri(1,3)
    a('m-int',3,N(f'Use the substitution u = 1 + x² to evaluate ∫₀^{k} 2x/(1 + x²) dx (3 s.f.).',math.log(1+k*k),0.5,'','= ln(1 + k²).'))
for _ in range(2):
    k=pick(0.5,1,2)
    a('m-int',3,N(f'dy/dx = {k}y, y = 3 when x = 0. Find y when x = 1 (3 s.f.).',3*math.e**k,0.5,'','Separate variables: y = 3e^(kx).'))
a('m-int',3,N('Evaluate ∫₁^e ln x dx.',1,0,'','By parts: [x ln x − x]₁^e = 0 − (−1) = 1.'))
# ---- numerical methods
for _ in range(3):
    c=ri(3,15)
    f=lambda x:x**3-c; x0=round(c**(1/3))+0.5
    x1=x0-f(x0)/(3*x0*x0)
    a('m-num',1,N(f'Newton–Raphson for f(x) = x³ − {c} with x₀ = {x0}. Find x₁ (4 s.f.).',x1,0.05,'','x₁ = x₀ − f(x₀)/f′(x₀).'))
for _ in range(2):
    c=ri(2,6)
    a('m-num',1,N(f'Evaluate f(1.5) for f(x) = x² − {c} to decide the sign (give the value).',2.25-c,0,'','Substitute.'))
for _ in range(3):
    c=ri(2,9);x=1.0
    for i in range(3): x=(x+c)**(1/3)
    a('m-num',2,N(f'xₙ₊₁ = ∛(xₙ + {c}), x₀ = 1. Find x₃ (4 d.p.).',x,0.02,'','Iterate three times.'))
for _ in range(3):
    h=0.5
    k=ri(1,3)
    ys=[math.sqrt(1+k*(h*i)**2) for i in range(5)]
    T=h/2*(ys[0]+ys[-1]+2*sum(ys[1:-1]))
    a('m-num',2,N(f'Use the trapezium rule with 4 strips to estimate ∫₀² √(1 + {k}x²) dx (3 s.f.).',T,0.5,'','h = 0.5.'))
for _ in range(3):
    c=ri(2,8)
    x=1.5
    for i in range(2): x=x-(x**3+x-c)/(3*x*x+1)
    a('m-num',3,N(f'f(x) = x³ + x − {c}. Starting at x₀ = 1.5, apply Newton–Raphson twice. Find x₂ (4 d.p.).',x,0.02,'','Two iterations.'))
for _ in range(2):
    k=ri(2,4)
    ys=[math.e**(-(0.25*i)**2*k) for i in range(5)]
    T=0.25/2*(ys[0]+ys[-1]+2*sum(ys[1:-1]))
    a('m-num',3,N(f'Trapezium rule, 4 strips, for ∫₀¹ e^(−{k}x²) dx (4 s.f.).',T,0.2,'','h = 0.25.'))
# ---- vectors
for _ in range(3):
    x,y,z=ri(-6,6),ri(-6,6),ri(-6,6)
    a('m-vec',1,N(f'Find |{x}i{sgn(y)}j{sgn(z)}k| (3 s.f.).',math.sqrt(x*x+y*y+z*z),0.5,'','√(x² + y² + z²).'))
for _ in range(2):
    x,y=ri(1,6),ri(1,6)
    a('m-vec',1,N(f'Find the angle between {x}i + {y}j and the positive x-axis (3 s.f.).',math.degrees(math.atan2(y,x)),0.5,'°','tan⁻¹(y/x).'))
for _ in range(3):
    A0=[ri(-4,4) for _ in range(3)];Bv=[ri(-4,6) for _ in range(3)]
    a('m-vec',2,N(f'A = ({A0[0]}, {A0[1]}, {A0[2]}), B = ({Bv[0]}, {Bv[1]}, {Bv[2]}). Find |AB| (3 s.f.).',math.dist(A0,Bv),0.5,'',' |b − a|.'))
for _ in range(2):
    k=ri(2,5)
    a('m-vec',2,N(f'a = 2i + {k}j and b = 6i + pj are parallel. Find p.',3*k,0,'','b = 3a.'))
for _ in range(3):
    A0=[ri(-3,3) for _ in range(3)];Bv=[ri(-3,6) for _ in range(3)]
    M_=[(x+y)/2 for x,y in zip(A0,Bv)]
    a('m-vec',3,N(f'A = ({A0[0]}, {A0[1]}, {A0[2]}), B = ({Bv[0]}, {Bv[1]}, {Bv[2]}). M is the midpoint of AB. Find |OM| (3 s.f.).',math.sqrt(sum(m*m for m in M_)),0.5,'','OM = ½(a + b).'))
for _ in range(2):
    p,q=ri(2,6),ri(2,6)
    a('m-vec',3,N(f'Triangle with vertices O, A({p}, 0, 0) and B(0, {q}, 0). Find the area of triangle OAB.',p*q/2,0,'','Right angle at O.'))
a('m-vec',3,N('OABC is a parallelogram with a = 3i + j, c = i + 4j. Find |OB| (3 s.f.).',math.hypot(4,5),0.5,'','OB = a + c = 4i + 5j.'))
a('m-vec',3,N('A particle moves with velocity (3i − 4j) m/s from position 2i + j. Find its distance from the origin after 2 s (3 s.f.).',math.hypot(8,-7),0.5,'m','r = (2 + 6)i + (1 − 8)j.'))
# ---- statistics
for _ in range(3):
    xs=[ri(1,20) for _ in range(6)]
    a('s-data',1,N(f'Find the mean of {", ".join(map(str,xs))} (3 s.f.).',sum(xs)/6,0.5,'','Σx/n.'))
for _ in range(3):
    n=ri(10,20);sx=ri(50,200);m=sx/n;sxx=round(n*(m*m+ri(4,25)))
    a('s-data',2,N(f'n = {n}, Σx = {sx}, Σx² = {sxx}. Find the standard deviation (3 s.f.).',math.sqrt(sxx/n-m*m),0.5,'','σ = √(Σx²/n − x̄²).'))
for _ in range(2):
    q1,q3=ri(10,30),ri(35,60)
    a('s-data',2,N(f'Q₁ = {q1}, Q₃ = {q3}. Find the lower outlier boundary (Q₁ − 1.5 × IQR).',q1-1.5*(q3-q1),0,'',f'IQR = {q3} − {q1} = {q3-q1}; boundary = {q1} − 1.5 × {q3-q1} = {fm(q1-1.5*(q3-q1))}.'))
for _ in range(2):
    w,f=pick(5,10,20),ri(12,60)
    a('s-data',2,N(f'A class of width {w} has frequency {f}. Find its frequency density.',f/w,0.5,'','f ÷ width.'))
for _ in range(3):
    a_,b_=ri(2,9),pick(0.5,1.2,2.5)
    xv=ri(10,30)
    a('s-data',3,N(f'Coded data y = (x − {a_*10})/{b_*2 if False else 5} has mean 2.4 and standard deviation 1.2. Find the standard deviation of x.',6,0,'','σx = 5σy.'))
    break
a('s-data',3,N('Coded y = (x − 100)/5 has ȳ = 2.4. Find x̄.',112,0,'','x̄ = 5ȳ + 100.'))
a('s-data',3,N('Grouped data: 10–20 (f = 4), 20–30 (f = 6), 30–50 (f = 10). Estimate the mean using midpoints.',(15*4+25*6+40*10)/20,0.5,'','Σfx/Σf.'))
a('s-data',3,N('Same data: estimate the median by interpolation (classes 10–20 f 4, 20–30 f 6, 30–50 f 10).',30,0.5,'','10th value: end of 20–30 class.'))
a('s-data',3,N('Regression line y = 2.3 + 0.8x for x in [10, 40]. Predict y at x = 25.',22.3,0,'','Interpolation – reliable.'))
for _ in range(3):
    pa,pb=pick(0.2,0.3,0.4,0.5),pick(0.1,0.2,0.3,0.6)
    a('s-prob',1,N(f'A and B are independent with P(A) = {pa}, P(B) = {pb}. Find P(A ∪ B).',pa+pb-pa*pb,0.5,'','P(A) + P(B) − P(A)P(B).'))
for _ in range(2):
    r,b=ri(3,8),ri(2,7)
    a('s-prob',1,N(f'A bag has {r} red and {b} blue balls. Two are taken without replacement. Find P(both red) (3 s.f.).',r*(r-1)/((r+b)*(r+b-1)),0.5,'',f'({r}/{r+b}) × ({r-1}/{r+b-1}): one fewer red and one fewer ball for the second pick.'))
for _ in range(3):
    pa,pab=pick(0.4,0.5,0.6),pick(0.1,0.15,0.2)
    a('s-prob',2,N(f'P(A) = {pa}, P(A ∩ B) = {pab}. Find P(B given A) (3 s.f.).',pab/pa,0.5,'',f'P(B | A) = P(A ∩ B)/P(A) = {pab}/{pa}.'))
for _ in range(2):
    p=pick(0.01,0.02,0.05);s=pick(0.95,0.9,0.98);fp=pick(0.05,0.1)
    a('s-prob',3,N(f'A disease affects {p*100:g}% of people. A test detects it {s*100:g}% of the time and gives a false positive {fp*100:g}% of the time. Find P(disease given positive) (3 s.f.).',p*s/(p*s+(1-p)*fp),0.5,'','Bayes via a tree diagram.'))
for _ in range(3):
    pa,pb,pab=0.5,pick(0.3,0.4),pick(0.1,0.2)
    a('s-prob',3,N(f'P(A) = {pa}, P(B) = {pb}, P(A ∩ B) = {pab}. Find P(A′ ∩ B′).',1-(pa+pb-pab),0.5,'','1 − P(A ∪ B).'))
a('s-prob',2,N('P(A) = 0.3, P(B) = 0.5, A and B mutually exclusive. Find P(A ∪ B).',0.8,0,'','Mutually exclusive, so P(A ∩ B) = 0 and P(A ∪ B) = 0.3 + 0.5.'))
a('s-prob',2,N('Two fair dice are rolled. Find P(sum = 7).',1/6,0.5,'','6/36.'))
for _ in range(3):
    n,p,k=ri(8,15),pick(0.2,0.3,0.4),ri(1,4)
    a('s-dist',1,N(f'X ~ B({n}, {p}). Find P(X = {k}) (3 s.f.).',math.comb(n,k)*p**k*(1-p)**(n-k),0.5,'',f'P(X = {k}) = ({n}C{k}) × {p}^{k} × {fm(1-p)}^{n-k}.'))
for _ in range(3):
    n,p=ri(10,30),pick(0.2,0.25,0.4)
    a('s-dist',2,N(f'X ~ B({n}, {p}). Find P(X ≤ 1) (3 s.f.).',(1-p)**n+n*p*(1-p)**(n-1),0.5,'',f'P(X = 0) + P(X = 1) = {fm(1-p)}^{n} + {n} × {p} × {fm(1-p)}^{n-1}.'))
for _ in range(3):
    mu,sd,x=ri(40,80),ri(3,10),None
    z=pick(1,1.5,2);x=mu+z*sd
    Phi=0.5*(1+math.erf(z/math.sqrt(2)))
    a('s-dist',2,N(f'X ~ N({mu}, {sd}²). Find P(X > {fm(x)}) (3 s.f.).',1-Phi,0.5,'',f'z = {z}.'))
for _ in range(3):
    mu,sd=ri(100,200),ri(5,20);x1,x2=mu-sd,mu+2*sd
    Phi=lambda z:0.5*(1+math.erf(z/math.sqrt(2)))
    a('s-dist',3,N(f'X ~ N({mu}, {sd}²). Find P({x1} < X < {x2}) (3 s.f.).',Phi(2)-Phi(-1),0.5,'','Standardise both limits.'))
for _ in range(2):
    mu=ri(50,80)
    a('s-dist',3,N(f'X ~ N({mu}, σ²) and P(X > {mu+10}) = 0.1587. Find σ.',10,0.5,'','P(Z > 1) = 0.1587, so 10/σ = 1.'))
a('s-dist',3,N('X ~ B(100, 0.4). Using a normal approximation, find the variance of the approximating normal.',24,0,'','np(1 − p).'))
a('s-dist',3,N('X ~ B(50, 0.5). Find the mean of the normal approximation.',25,0,'','μ = np = 50 × 0.5 = 25.'))
# hypothesis tests (binomial)
def bcdf(n,p,k): return sum(math.comb(n,i)*p**i*(1-p)**(n-i) for i in range(k+1))
for _ in range(3):
    n=ri(10,20);p=pick(0.2,0.3);x=ri(0,1)
    a('s-hyp',2,N(f'H₀: p = {p}, H₁: p < {p}, n = {n}. Observed X = {x}. Find the p-value P(X ≤ {x}) (3 s.f.).',bcdf(n,p,x),0.5,'','Compare with the significance level.'))
for _ in range(3):
    n=ri(15,25);p=pick(0.3,0.4,0.5)
    c=next(k for k in range(n+1) if 1-bcdf(n,p,k-1)<=0.05)
    a('s-hyp',3,N(f'X ~ B({n}, {p}) under H₀. H₁: p > {p} at 5%. Find the smallest c with P(X ≥ c) ≤ 0.05 (critical value).',c,0,'','Use cumulative binomial probabilities.'))
for _ in range(2):
    n=ri(15,25);p=0.4
    c=next(k for k in range(n+1) if 1-bcdf(n,p,k-1)<=0.05)
    a('s-hyp',3,N(f'For X ~ B({n}, 0.4), the critical region is X ≥ {c}. Find the actual significance level (4 d.p.).',1-bcdf(n,p,c-1),1,'',f'Actual significance level = P(X ≥ {c}) = 1 − P(X ≤ {c-1}).'))
for _ in range(2):
    mu,sd,n=ri(50,100),ri(5,15),pick(16,25,36)
    a('s-hyp',3,N(f'Sample mean of {n} values from N(μ, {sd}²) is x̄. Find the standard error of x̄ (3 s.f.).',sd/math.sqrt(n),0.5,'','σ/√n.'))
# mechanics
for _ in range(3):
    u,a_,t=ri(0,10),ri(1,5),ri(2,8)
    a('k-kin',1,N(f'u = {u} m/s, a = {a_} m s⁻², t = {t} s. Find the displacement.',u*t+0.5*a_*t*t,0,'m','s = ut + ½at².'))
for _ in range(3):
    u,h=ri(5,20),ri(5,40)
    v=math.sqrt(u*u+2*9.8*h)
    a('k-kin',2,N(f'A stone is thrown down at {u} m/s from a height of {h} m. Find its speed on hitting the ground (g = 9.8, 3 s.f.).',v,0.5,'m/s','v² = u² + 2as.'))
for _ in range(2):
    k=ri(1,4)
    a('k-kin',2,N(f'v = {k}t² + 2t m/s. Find the displacement from t = 0 to t = 3.',k*9+9,0.5,'m','Integrate v.'))
for _ in range(3):
    U,ang=ri(15,30),pick(30,40,45,60)
    th=math.radians(ang);T=2*U*math.sin(th)/9.8
    a('k-kin',3,N(f'A projectile is launched at {U} m/s at {ang}° above horizontal level ground. Find its range (g = 9.8, 3 s.f.).',U*math.cos(th)*T,0.5,'m','Time of flight then horizontal distance.'))
for _ in range(2):
    U,ang=ri(15,30),pick(30,45,60)
    th=math.radians(ang)
    a('k-kin',3,N(f'Launched at {U} m/s at {ang}°. Find its maximum height (g = 9.8, 3 s.f.).',(U*math.sin(th))**2/(2*9.8),0.5,'m','v_y = 0 at the top.'))
for _ in range(3):
    m,F,mu=ri(2,10),ri(20,60),pick(0.1,0.2,0.3)
    acc=(F-mu*m*9.8)/m
    if acc<=0: F+=40;acc=(F-mu*m*9.8)/m
    a('k-force',2,N(f'A {m} kg box is pulled horizontally by {F} N on a rough floor, μ = {mu}. Find its acceleration (g = 9.8, 3 s.f.).',acc,0.5,'m s⁻²','F − μmg = ma.'))
for _ in range(2):
    m,ang=ri(2,8),pick(20,30,40)
    a('k-force',1,N(f'A {m} kg block on a smooth slope at {ang}°. Find its acceleration (g = 9.8, 3 s.f.).',9.8*math.sin(math.radians(ang)),0.5,'m s⁻²','g sin θ.'))
for _ in range(3):
    m1,m2=ri(2,6),ri(1,5);mu=pick(0.2,0.3)
    acc=(m2*9.8-mu*m1*9.8)/(m1+m2)
    if acc<=0: m2+=4;acc=(m2*9.8-mu*m1*9.8)/(m1+m2)
    a('k-force',3,N(f'A {m1} kg block on a rough table (μ = {mu}) is joined by a light string over a smooth pulley to a hanging {m2} kg mass. Find the acceleration (g = 9.8, 3 s.f.).',acc,0.5,'m s⁻²','Equations for each particle, then add.'))
for _ in range(2):
    m,ang,mu=ri(2,8),pick(25,30,35),pick(0.2,0.3)
    th=math.radians(ang)
    a('k-force',3,N(f'A {m} kg block slides down a rough {ang}° slope, μ = {mu}. Find its acceleration (g = 9.8, 3 s.f.).',9.8*(math.sin(th)-mu*math.cos(th)),0.5,'m s⁻²','mg sin θ − μmg cos θ = ma.'))
for _ in range(3):
    L,W_=ri(4,8),ri(50,200);x=ri(1,L-1);Wc=ri(20,100)
    Rb=(W_*L/2+Wc*x)/L
    a('k-mom',2,N(f'A uniform {L} m beam of weight {W_} N rests on supports at each end. A {Wc} N load is {x} m from the left end. Find the reaction at the right support (3 s.f.).',Rb,0.5,'N','Moments about the left end.'))
for _ in range(3):
    L,W_=ri(4,8),ri(80,200);
    a('k-mom',3,N(f'A uniform {L} m ladder of weight {W_} N rests against a smooth wall at 60° to rough ground and is about to slip. Find the friction at the ground (3 s.f.).',W_*(L/2)*math.cos(math.radians(60))/(L*math.sin(math.radians(60))),0.5,'N','Moments about the base: F = S, S × L sin 60° = W × (L/2) cos 60°.'))
for _ in range(2):
    L,W_=ri(3,6),ri(40,120);x=ri(1,L-1)
    a('k-mom',3,N(f'A uniform {L} m rod of weight {W_} N is held horizontal by a vertical string at one end and a pivot at the other. Find the tension (3 s.f.).',W_/2,0.5,'N','Moments about the pivot.'))
for _ in range(2):
    m=ri(2,9)
    a('k-units',1,N(f'Convert {m*18} km/h to m/s.',m*5,0,'m/s','÷ 3.6.'))
for _ in range(2):
    m=ri(2,9)
    a('k-units',2,N(f'Find the weight of {m*100} g on the Moon (g = 1.6).',m*0.16,0.5,'N','Convert grams to kg first.'))
a('k-units',2,N('Convert a density of 2.7 g/cm³ to kg/m³.',2700,0,'kg m⁻³','×1000.'))
a('k-units',2,N('Convert 500 cm² to m².',0.05,0,'m²','÷ 10⁴.'))
a('k-units',3,N('A 1500 kg car accelerates from 0 to 27 m/s in 9 s. Find the resultant force.',4500,0,'N','a = 3 m s⁻².'))
a('k-units',3,N('A force of 6 kN acts on 1.2 tonnes. Find the acceleration.',5,0,'m s⁻²','Convert to N and kg.'))
