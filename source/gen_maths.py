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
    a('m-alg',1,N(f'Find the remainder when f(x) = x³{sgn(p)}x²{sgn(q)}x{sgn(r)} is divided by (x{sgn(-k)}).',k**3+p*k*k+q*k+r,0,'',f'Remainder theorem: the remainder is f({fm(k)}) = ({fm(k)})³ + {p}({fm(k)})² + ({q})({fm(k)}) + ({r}) = {fm(k**3+p*k*k+q*k+r)}.'))
for _ in range(2):
    m,c,n=ri(2,5),ri(-5,5),ri(1,4)
    a('m-alg',1,N(f'f(x) = {m}x{sgn(c)} and g(x) = x² + {n}. Find fg(2).',m*(4+n)+c,0,'',f'fg(2) means apply g first: g(2) = 4 + {n} = {4+n}. Then f({4+n}) = {m} × {4+n}{sgn(c)} = {m*(4+n)+c}.'))
for _ in range(3):
    r1,b,c=ri(1,4),ri(-5,5),ri(-8,8)
    c-=(r1**3+b*r1+c)%(r1*r1); k=-(r1**3+b*r1+c)/(r1*r1)
    a('m-alg',2,N(f'(x − {r1}) is a factor of x³ + kx²{sgn(b)}x{sgn(c)}. Find k.',k,0,'',f'Factor theorem: f({r1}) = 0, so {r1**3} + {r1*r1}k{sgn(b*r1)}{sgn(c)} = 0, giving {r1*r1}k = {fm(-(r1**3+b*r1+c))} and k = {fm(k)}.'))
for _ in range(3):
    m,c=ri(2,6),ri(1,9); x=ri(2,8)
    a('m-alg',2,N(f'f(x) = (x + {c})/{m}, x ∈ ℝ. Find f⁻¹({x}).',m*x-c,0,'',f'Let y = (x + {c})/{m}, so x = {m}y − {c}. Hence f⁻¹(x) = {m}x − {c} and f⁻¹({x}) = {m*x} − {c} = {m*x-c}.'))
for _ in range(2):
    k=ri(2,5);b=ri(1,6)
    a('m-alg',2,N(f'Solve |{k}x − {b}| = {b+k*2} for the positive solution x.',(b+b+k*2)/k,0.5,'',f'Take the positive case: {k}x − {b} = {b+2*k}, so {k}x = {2*b+2*k} and x = {fm((2*b+2*k)/k,3)}. (The negative case gives a negative x.)'))
for _ in range(3):
    p,q=ri(1,4),ri(1,5); A0,B0=ri(1,5),ri(-4,5)
    while B0==0:B0=ri(-4,5)
    # (A(x+q)+B(x-p))/((x-p)(x+q))
    num1=A0+B0; num0=A0*q-B0*p
    a('m-alg',3,N(f'Express ({fm(num1)}x{sgn(num0)})/((x − {p})(x + {q})) as A/(x − {p}) + B/(x + {q}). Find A.',A0,0,'',f'Multiply through: {fm(num1)}x{sgn(num0)} ≡ A(x + {q}) + B(x − {p}). Substitute x = {p} so the B term vanishes: {fm(num1*p+num0)} = {p+q}A, so A = {A0}.'))
for _ in range(2):
    c=ri(1,9);k=ri(2,4)
    a('m-alg',3,N(f'f(x) = {k}(x − 1)² + {c} for x ≥ 1. Find f⁻¹({k*9+c}).',4,0,'',f'Minimum {c} at x = 1. Solve {k}(x − 1)² + {c} = {k*9+c}: x − 1 = 3, x = 4.'))
for _ in range(2):
    p=ri(2,5);q=ri(1,6)
    a('m-alg',3,N(f'f(x) = e^x + {q}, g(x) = {p}x. Solve fg(x) = {q+math.e**p:.4f} (3 s.f.).',1,0.5,'',f'fg(x) = f({p}x) = e^({p}x) + {q}. Setting this equal to {q} + e^{p} gives e^({p}x) = e^{p}, so {p}x = {p} and x = 1.'))
# ---- coordinate geometry
for _ in range(3):
    x1,y1,x2,y2=ri(-5,5),ri(-5,5),ri(-5,8),ri(-5,8)
    while x2==x1:x2=ri(-5,8)
    a('m-coord',1,N(f'Find the gradient of the line through ({x1}, {y1}) and ({x2}, {y2}).',(y2-y1)/(x2-x1),0.5,'',f'Gradient = Δy ÷ Δx = ({y2} − ({y1})) ÷ ({x2} − ({x1})) = {y2-y1} ÷ {x2-x1} = {fm((y2-y1)/(x2-x1),3)}.'))
for _ in range(2):
    x1,y1,x2,y2=ri(-6,6),ri(-6,6),ri(-6,6),ri(-6,6)
    a('m-coord',1,N(f'Find the length of the line from ({x1}, {y1}) to ({x2}, {y2}) (3 s.f.).',math.hypot(x2-x1,y2-y1),0.5,'',f'Length = √((Δx)² + (Δy)²) = √(({x2-x1})² + ({y2-y1})²) = √{(x2-x1)**2+(y2-y1)**2} = {fm(math.hypot(x2-x1,y2-y1),3)}.'))
for _ in range(3):
    h,k,r=ri(-5,5),ri(-5,5),ri(2,7)
    D,E,Fc=-2*h,-2*k,h*h+k*k-r*r
    a('m-coord',2,N(f'Circle x² + y²{sgn(D)}x{sgn(E)}y{sgn(Fc)} = 0. Find its radius.',r,0,'',f'Complete the square: (x{sgn(-h)})² + (y{sgn(-k)})² = {h*h} + {k*k}{sgn(-Fc)} = {r*r}, so the radius is √{r*r} = {r}.'))
for _ in range(3):
    m=pick(2,3,-2,4,0.5);c=ri(-5,5);px=ri(-3,3)
    pg={2:'−½',3:'−⅓',-2:'½',4:'−¼',0.5:'−2'}[m]
    a('m-coord',2,N(f'Line L passes through ({px}, {fm(m*px+c)}) and is perpendicular to y = {pg}x + 1. Find the y-intercept of L.',c,0.5,'',f'Perpendicular gradients multiply to −1, so L has gradient {fm(m)}. y = {fm(m)}x + c through ({px}, {fm(m*px+c)}): c = {fm(m*px+c)} − ({fm(m)}) × ({px}) = {fm(c)}.'))
for _ in range(2):
    t=ri(1,4)
    a('m-coord',2,N(f'A curve has x = t² + 1, y = 2t³. Find dy/dx when t = {t}.',3*t,0,'',f'dy/dt = 6t² and dx/dt = 2t, so dy/dx = 6t² ÷ 2t = 3t. At t = {t}, dy/dx = {3*t}.'))
for _ in range(3):
    h,k,r=ri(1,5),ri(1,5),5; px,py=h+3,k+4
    a('m-coord',3,N(f'A circle has centre ({h}, {k}) and passes through ({px}, {py}). The tangent at ({px}, {py}) meets the x-axis at A. Find the x-coordinate of A.',px+py*4/3,0.5,'',f'Radius gradient = 4/3, so the tangent gradient is −3/4. Tangent: y − {py} = −¾(x − {px}). At y = 0: x = {px} + 4 × {py}/3 = {fm(px+py*4/3,3)}.'))
for _ in range(2):
    m=ri(2,3);c=ri(-3,-1)
    # intersection of y = mx + c with x²+y²=25 -> count via discriminant
    A=1+m*m;Bq=2*m*c;C=c*c-25;disc=Bq*Bq-4*A*C
    a('m-coord',3,N(f'Find the discriminant of the quadratic in x formed by substituting y = {m}x{sgn(c)} into x² + y² = 25.',disc,0,'',f'x² + ({m}x{sgn(c)})² = 25 gives {A}x²{sgn(Bq)}x{sgn(C)} = 0. Discriminant = b² − 4ac = ({Bq})² − 4 × {A} × ({C}) = {disc}. Positive, so the line crosses the circle twice.'))
# ---- sequences
for _ in range(3):
    A0,d,n=ri(2,9),ri(2,7),ri(10,30)
    a('m-seq',1,N(f'Arithmetic sequence: a = {A0}, d = {d}. Find the {n}th term.',A0+(n-1)*d,0,'',f'uₙ = a + (n − 1)d = {A0} + {n-1} × {d} = {A0+(n-1)*d}.'))
for _ in range(2):
    A0,r=ri(2,6),pick(2,3)
    a('m-seq',1,N(f'Geometric sequence: first term {A0}, ratio {r}. Find the 6th term.',A0*r**5,0,'',f'uₙ = arⁿ⁻¹, so u₆ = {A0} × {r}⁵ = {A0} × {r**5} = {A0*r**5}.'))
for _ in range(3):
    n=ri(4,8);k=ri(2,3);p=ri(2,3)
    a('m-seq',2,N(f'Find the coefficient of x^{p} in ({1} + {k}x)^{n}.',math.comb(n,p)*k**p,0,'',f'The x^{p} term is {n}C{p} × 1^{n-p} × ({k}x)^{p}, so the coefficient is {math.comb(n,p)} × {k**p} = {math.comb(n,p)*k**p}.'))
for _ in range(2):
    A0,r=ri(10,90),pick(0.5,0.25,0.2,0.8)
    a('m-seq',2,N(f'Find the sum to infinity of a geometric series with first term {A0} and ratio {r}.',A0/(1-r),0.5,'',f'The ratio has modulus less than 1, so S∞ = a ÷ (1 − r) = {A0} ÷ {fm(1-r)} = {fm(A0/(1-r),4)}.'))
for _ in range(3):
    A0,d=ri(3,9),ri(2,5);S=ri(200,600)
    n=math.ceil(next(n for n in range(1,400) if n/2*(2*A0+(n-1)*d)>S))
    a('m-seq',3,N(f'An arithmetic series has a = {A0}, d = {d}. Find the least n for which Sₙ > {S}.',n,0,'',f'Sₙ = n/2 × (2 × {A0} + (n − 1) × {d}). S{n-1} = {fm((n-1)/2*(2*A0+(n-2)*d))} (not enough) and S{n} = {fm(n/2*(2*A0+(n-1)*d))}, which exceeds {S}. So n = {n}.'))
for _ in range(2):
    P0,r=ri(1000,5000),pick(1.03,1.04,1.05)
    a('m-seq',3,N(f'£{P0} is invested at {round((r-1)*100)}% compound interest per year. Find the least number of whole years for it to exceed £{2*P0}.',math.ceil(math.log(2)/math.log(r)),0,'years',f'{P0} × {r}ⁿ > {2*P0} gives {r}ⁿ > 2, so n > ln 2 ÷ ln {r} = {math.log(2)/math.log(r):.3g}. The least whole number is {math.ceil(math.log(2)/math.log(r))}.'))
for _ in range(2):
    x=pick(0.1,0.05,0.02)
    a('m-seq',3,N(f'Use the first three terms of the expansion of √(1 + 4x) to estimate √(1 + 4×{x}) (4 d.p.).',1+2*x-2*x*x,0.05,'',f'(1 + 4x)^½ ≈ 1 + ½(4x) + (½)(−½)/2 × (4x)² = 1 + 2x − 2x². With x = {x}: 1 + {2*x:g} − {2*x*x:g} = {1+2*x-2*x*x:.4f}.'))
# ---- trig
for _ in range(3):
    r,th=ri(3,12),pick(0.8,1.2,1.5,2.1)
    a('m-trig',1,N(f'Sector radius {r} cm, angle {th} rad. Find its area.',0.5*r*r*th,0.5,'cm²',f'Area of a sector = ½r²θ (θ in radians) = ½ × {r}² × {th} = {fm(0.5*r*r*th,4)} cm².'))
for _ in range(2):
    d=pick(45,120,135,210,300)
    a('m-trig',1,N(f'Convert {d}° to radians (3 s.f.).',math.radians(d),0.5,'rad',f'Multiply by π/180: {d} × π/180 = {math.radians(d):.3g} rad.'))
for _ in range(3):
    v=pick(0.3,0.4,0.6,0.7)
    a('m-trig',2,N(f'Solve sin x = {v} for 90° < x < 180° (1 d.p.).',180-math.degrees(math.asin(v)),0.2,'°',f'sin⁻¹({v}) = {math.degrees(math.asin(v)):.1f}°, which is outside the range. Sine is positive in the second quadrant, so x = 180° − {math.degrees(math.asin(v)):.1f}° = {180-math.degrees(math.asin(v)):.1f}°.'))
for _ in range(2):
    R0=pick((3,4),(5,12),(8,15))
    a('m-trig',2,N(f'Write {R0[0]} sin x + {R0[1]} cos x as R sin(x + α). Find R.',math.hypot(*R0),0,'',f'R sin(x + α) = R sin x cos α + R cos x sin α, so R cos α = {R0[0]} and R sin α = {R0[1]}. Square and add: R = √({R0[0]}² + {R0[1]}²) = {fm(math.hypot(*R0),4)}.'))
for _ in range(3):
    A0,Bc=pick((3,4),(5,12),(1,1),(2,3))
    al=math.degrees(math.atan2(Bc,A0)); Rr=math.hypot(A0,Bc)
    a('m-trig',3,N(f'{A0} sin x + {Bc} cos x = R sin(x + α). Find the maximum value of 1/(20 − ({A0} sin x + {Bc} cos x)) (3 s.f.).',1/(20-Rr),0.5,'',f'R = √({A0}² + {Bc}²) = {fm(Rr,4)}. The fraction is greatest when the denominator is least, i.e. when sin(x + α) = 1: 1/(20 − {fm(Rr,4)}) = {1/(20-Rr):.3g}.'))
for _ in range(2):
    a('m-trig',3,N('Solve 2cos²x + 3sin x = 3 for 0 < x < 90° (in degrees).',30,0,'°','2(1 − sin²x) + 3sin x − 3 = 0 → (2 sin x − 1)(sin x − 1) = 0; sin x = ½.'))
    break
a('m-trig',3,N('Solve tan²x − 3 = 0 for 0 < x < 90° (degrees).',60,0,'°','tan²x = 3, so tan x = ±√3. In 0 < x < 90° tan is positive, so tan x = √3 and x = 60°.'))
a('m-trig',3,N('Using small-angle approximations, find the limit of (1 − cos 2θ)/θ² as θ → 0.',2,0,'','For small θ, cos 2θ ≈ 1 − (2θ)²/2 = 1 − 2θ². So 1 − cos 2θ ≈ 2θ², and dividing by θ² gives 2.'))
# ---- exp & logs
for _ in range(3):
    b,c=pick(2,3,5,7),ri(10,90)
    a('m-exp',1,N(f'Solve {b}^x = {c} (3 s.f.).',math.log(c)/math.log(b),0.5,'',f'Take logs: x ln {b} = ln {c}, so x = ln {c} ÷ ln {b} = {math.log(c)/math.log(b):.3g}.'))
for _ in range(2):
    k=pick(2,3,4,5)
    a('m-exp',1,N(f'Solve ln x = {k} (3 s.f.).',math.e**k,0.5,'',f'ln and e are inverses, so x = e^{k} = {math.e**k:.3g}.'))
for _ in range(3):
    A0,k,t=ri(50,500),pick(0.02,0.05,0.1,0.15),ri(5,20)
    a('m-exp',2,N(f'N = {A0}e^({k}t). Find t when N = {2*A0} (3 s.f.).',math.log(2)/k,0.5,'',f'{2*A0} = {A0}e^({k}t), so e^({k}t) = 2 and {k}t = ln 2. t = ln 2 ÷ {k} = {math.log(2)/k:.3g}.'))
for _ in range(2):
    n=pick(8,27,32,81)
    b={8:2,27:3,32:2,81:3}[n]
    a('m-exp',2,N(f'Solve 2 log_{b} x = log_{b} {n*n}.',n,0,'',f'2 log x = log x² (power law), so x² = {n*n} and x = {n} (x must be positive for the log to exist).'))
for _ in range(3):
    A0,k=ri(100,900),pick(0.1,0.2,0.3)
    a('m-exp',3,N(f'A model gives log₁₀P = {fm(math.log10(A0),4)} + {k}t. Find P when t = 5 (3 s.f.).',10**(math.log10(round(A0*10**4)/10**4) if False else math.log10(A0)+5*k) if False else 10**(float(fm(math.log10(A0),4))+5*k),0.5,'',f'At t = 5, log₁₀P = {fm(math.log10(A0),4)} + {k} × 5 = {float(fm(math.log10(A0),4))+5*k:.4f}, so P = 10^{float(fm(math.log10(A0),4))+5*k:.4f} = {10**(float(fm(math.log10(A0),4))+5*k):.3g}.'))
for _ in range(2):
    k=pick(0.2,0.3,0.5);T0=ri(60,90)
    a('m-exp',3,N(f'Coffee cools as T = 20 + {T0-20}e^(−{k}t). Find the time when T = 40 (3 s.f.).',math.log((T0-20)/20)/k,0.5,'min',f'40 = 20 + {T0-20}e^(−{k}t), so e^(−{k}t) = 20/{T0-20}. Take ln: t = ln({T0-20}/20) ÷ {k} = {math.log((T0-20)/20)/k:.3g} min.'))
for _ in range(2):
    A0=ri(2,6);n=ri(2,4)
    a('m-exp',3,N(f'y = ax^n. A graph of log y against log x is a straight line through (0, {fm(math.log10(A0),4)}) with gradient {n}. Find y when x = 2 (3 s.f.).',A0*2**n,0.5,'',f'log y = log a + n log x, so log a = {fm(math.log10(A0),4)} gives a = {A0}, and n = {n}. y = {A0} × 2^{n} = {A0*2**n}.'))
# ---- differentiation
for _ in range(3):
    p,q,x=ri(1,5),pick(-6,-5,-4,-3,-2,-1,1,2,3,4,5,6),ri(-3,3)
    a('m-diff',1,N(f'y = {p}x³{sgn(q)}x². Find dy/dx at x = {x}.',3*p*x*x+2*q*x,0,'',f'dy/dx = {3*p}x²{sgn(2*q)}x. At x = {fm(x)}: {3*p} × {x*x}{sgn(2*q*x)} = {fm(3*p*x*x+2*q*x)}.'))
for _ in range(2):
    k=ri(2,5)
    a('m-diff',1,N(f'y = {k}√x. Find dy/dx at x = 4.',k/(2*2),0.5,'',f'y = {k}x^½, so dy/dx = {k} × ½x^(−½) = {fm(k/2)}/√x. At x = 4: {fm(k/2)} ÷ 2 = {fm(k/4)}.'))
for _ in range(3):
    k,x=ri(2,4),pick(0,1,2)
    a('m-diff',2,N(f'y = x e^({k}x). Find dy/dx at x = {x} (3 s.f.).',math.e**(k*x)*(1+k*x),0.5,'',f'Product rule: dy/dx = e^({k}x) + {k}x e^({k}x) = e^({k}x)(1 + {k}x). At x = {x}: e^{k*x} × {1+k*x} = {math.e**(k*x)*(1+k*x):.3g}.'))
for _ in range(2):
    k=ri(2,5)
    a('m-diff',2,N(f'y = ln({k}x² + 1). Find dy/dx at x = 1 (3 s.f.).',2*k/(k+1),0.5,'',f'Chain rule: dy/dx = {2*k}x ÷ ({k}x² + 1). At x = 1: {2*k} ÷ {k+1} = {2*k/(k+1):.3g}.'))
for _ in range(2):
    k=ri(2,4)
    a('m-diff',2,N(f'y = sin({k}x)/x. Find dy/dx at x = π (3 s.f.).',(k*math.pi*math.cos(k*math.pi)-math.sin(k*math.pi))/math.pi**2,0.5,'',f'Quotient rule: dy/dx = ({k}x cos {k}x − sin {k}x) ÷ x². At x = π, sin {k}π = 0 and cos {k}π = {round(math.cos(k*math.pi))}, so dy/dx = {round(math.cos(k*math.pi))*k}π ÷ π² = {(k*math.pi*math.cos(k*math.pi)-math.sin(k*math.pi))/math.pi**2:.3g}.'))
for _ in range(3):
    p=ri(2,6)
    a('m-diff',3,N(f'y = x³ − {3*p*p}x. Find the y-coordinate of the local minimum.',p**3-3*p*p*p,0,'',f'dy/dx = 3x² − {3*p*p} = 0 → x = ±{p}. d²y/dx² = 6x > 0 at x = {p}, so it is the minimum: y = {p**3} − {3*p*p*p} = {p**3-3*p*p*p}.'))
for _ in range(2):
    V=pick(500,1000,2000)
    r=(V/(2*math.pi))**(1/3)
    a('m-diff',3,N(f'A closed cylinder has volume {V} cm³. Find the radius that minimises its surface area (3 s.f.).',r,0.5,'cm',f'h = V/(πr²), so A = 2πr² + 2V/r. dA/dr = 4πr − 2V/r² = 0 gives r³ = V/(2π) = {V/(2*math.pi):.4g}, so r = {r:.3g} cm (d²A/dr² > 0, a minimum).'))
for _ in range(2):
    k=ri(2,5)
    a('m-diff',3,N(f'x² + y² + {k}xy = 7 + {k*2}... Find dy/dx at (1, 2) for x² + y² + {k}xy = {5+2*k} (3 s.f.).'.split('... ')[1],-(2+2*k)/(4+k),0.5,'',f'Differentiate implicitly: 2x + 2y dy/dx + {k}(y + x dy/dx) = 0. At (1, 2): 2 + 4 dy/dx + {2*k} + {k} dy/dx = 0, so dy/dx = −{2+2*k}/{4+k} = {-(2+2*k)/(4+k):.3g}.'))
# ---- integration
for _ in range(3):
    p,q,b=ri(1,6),ri(1,6),ri(1,4)
    a('m-int',1,N(f'Evaluate ∫₀^{b} ({p}x² + {q}) dx.',p*b**3/3+q*b,0.5,'',f'[{fm(p/3,4)}x³ + {q}x] from 0 to {b} = {fm(p/3,4)} × {b**3} + {q*b} = {fm(p*b**3/3+q*b,4)}.'))
for _ in range(2):
    k=ri(2,6)
    a('m-int',1,N(f'Evaluate ∫₁^{k} (1/x) dx (3 s.f.).',math.log(k),0.5,'',f'∫(1/x) dx = ln x, so the answer is ln {k} − ln 1 = ln {k}.'))
for _ in range(3):
    k=ri(2,4)
    a('m-int',2,N(f'Evaluate ∫₀^(π/2) sin({k}x) dx (3 s.f.).',(1-math.cos(k*math.pi/2))/k,0.5,'',f'∫ sin({k}x) dx = −cos({k}x)/{k}. From 0 to π/2: (−cos({k}π/2) + cos 0)/{k} = (1 − {fm(round(math.cos(k*math.pi/2)))})/{k} = {fm((1-math.cos(k*math.pi/2))/k,3)}.'))
for _ in range(2):
    k=ri(1,3)
    a('m-int',2,N(f'Evaluate ∫₀¹ x e^({k}x) dx (3 s.f.).',(math.e**k*(k-1)+1)/k**2,0.5,'',f'By parts with u = x, dv/dx = e^({k}x): ∫ = [x e^({k}x)/{k}] − ∫ e^({k}x)/{k} dx = [x e^({k}x)/{k} − e^({k}x)/{k*k}] from 0 to 1 = {(math.e**k*(k-1)+1)/k**2:.3g}.'))
for _ in range(2):
    p=ri(2,5)
    a('m-int',2,N(f'Find the area enclosed between y = x({p} − x) and the x-axis (3 s.f.).',p**3/6,0.5,'',f'The curve meets the x-axis at 0 and {p}. Area = ∫₀^{p} ({p}x − x²) dx = [{fm(p/2)}x² − x³/3] = {fm(p**3/2)} − {fm(p**3/3,4)} = {fm(p**3/6,3)}.'))
for _ in range(3):
    m=ri(1,3)
    # area between y=x^2 and y=mx+... use y = x^2 and y = kx
    k=ri(2,5)
    a('m-int',3,N(f'Find the area enclosed by y = x² and y = {k}x (3 s.f.).',k**3/6,0.5,'',f'x² = {k}x at x = 0 and x = {k}. The line is above the curve between them: area = ∫₀^{k} ({k}x − x²) dx = {k}³/2 − {k}³/3 = {k**3}/6 = {fm(k**3/6,3)}.'))
for _ in range(2):
    k=ri(1,3)
    a('m-int',3,N(f'Use the substitution u = 1 + x² to evaluate ∫₀^{k} 2x/(1 + x²) dx (3 s.f.).',math.log(1+k*k),0.5,'',f'u = 1 + x² gives du = 2x dx, and the limits become 1 and {1+k*k}. ∫ du/u = [ln u] from 1 to {1+k*k} = ln {1+k*k} = {math.log(1+k*k):.3g}.'))
for _ in range(2):
    k=pick(0.5,1,2)
    a('m-int',3,N(f'dy/dx = {k}y, y = 3 when x = 0. Find y when x = 1 (3 s.f.).',3*math.e**k,0.5,'',f'Separate: ∫ dy/y = ∫ {k} dx, so ln y = {k}x + c and y = Ae^({k}x). y = 3 at x = 0 gives A = 3. At x = 1: y = 3e^{k} = {3*math.e**k:.3g}.'))
a('m-int',3,N('Evaluate ∫₁^e ln x dx.',1,0,'','By parts: [x ln x − x]₁^e = 0 − (−1) = 1.'))
# ---- numerical methods
for _ in range(3):
    c=ri(3,15)
    f=lambda x:x**3-c; x0=round(c**(1/3))+0.5
    x1=x0-f(x0)/(3*x0*x0)
    a('m-num',1,N(f'Newton–Raphson for f(x) = x³ − {c} with x₀ = {x0}. Find x₁ (4 s.f.).',x1,0.05,'',f'f′(x) = 3x². x₁ = {x0} − ({x0}³ − {c}) ÷ (3 × {x0}²) = {x0} − ({fm(f(x0),4)}) ÷ {fm(3*x0*x0,4)} = {x1:.4g}.'))
for _ in range(2):
    c=ri(2,6)
    a('m-num',1,N(f'Evaluate f(1.5) for f(x) = x² − {c} to decide the sign (give the value).',2.25-c,0,'',f'f(1.5) = 1.5² − {c} = 2.25 − {c} = {fm(2.25-c)}, so f(1.5) is negative.'))
for _ in range(3):
    c=ri(2,9);x=1.0
    for i in range(3): x=(x+c)**(1/3)
    a('m-num',2,N(f'xₙ₊₁ = ∛(xₙ + {c}), x₀ = 1. Find x₃ (4 d.p.).',x,0.02,'',f'x₁ = ∛(1 + {c}) = {(1+c)**(1/3):.4f}, then x₂ = ∛(x₁ + {c}) = {((1+c)**(1/3)+c)**(1/3):.4f}, then x₃ = {x:.4f}.'))
for _ in range(3):
    h=0.5
    k=ri(1,3)
    ys=[math.sqrt(1+k*(h*i)**2) for i in range(5)]
    T=h/2*(ys[0]+ys[-1]+2*sum(ys[1:-1]))
    a('m-num',2,N(f'Use the trapezium rule with 4 strips to estimate ∫₀² √(1 + {k}x²) dx (3 s.f.).',T,0.5,'',f'h = 0.5; y-values at x = 0, 0.5, 1, 1.5, 2 are {", ".join(f"{v:.4f}" for v in ys)}. Area ≈ ½h(y₀ + y₄ + 2(y₁ + y₂ + y₃)) = {T:.3g}.'))
for _ in range(3):
    c=ri(2,8)
    x=1.5
    for i in range(2): x=x-(x**3+x-c)/(3*x*x+1)
    a('m-num',3,N(f'f(x) = x³ + x − {c}. Starting at x₀ = 1.5, apply Newton–Raphson twice. Find x₂ (4 d.p.).',x,0.02,'',f'f′(x) = 3x² + 1. x₁ = 1.5 − f(1.5)/f′(1.5) = {1.5-(1.5**3+1.5-c)/(3*1.5**2+1):.4f}; repeating once more gives x₂ = {x:.4f}.'))
for _ in range(2):
    k=ri(2,4)
    ys=[math.e**(-(0.25*i)**2*k) for i in range(5)]
    T=0.25/2*(ys[0]+ys[-1]+2*sum(ys[1:-1]))
    a('m-num',3,N(f'Trapezium rule, 4 strips, for ∫₀¹ e^(−{k}x²) dx (4 s.f.).',T,0.2,'',f'h = 0.25; y-values at x = 0, 0.25, 0.5, 0.75, 1 are {", ".join(f"{v:.4f}" for v in ys)}. Area ≈ ½ × 0.25 × (y₀ + y₄ + 2(y₁ + y₂ + y₃)) = {T:.4g}.'))
# ---- vectors
for _ in range(3):
    x,y,z=ri(-6,6),ri(-6,6),ri(-6,6)
    a('m-vec',1,N(f'Find |{x}i{sgn(y)}j{sgn(z)}k| (3 s.f.).',math.sqrt(x*x+y*y+z*z),0.5,'',f'Magnitude = √({fm(x)}² + ({fm(y)})² + ({fm(z)})²) = √{x*x+y*y+z*z} = {math.sqrt(x*x+y*y+z*z):.3g}.'))
for _ in range(2):
    x,y=ri(1,6),ri(1,6)
    a('m-vec',1,N(f'Find the angle between {x}i + {y}j and the positive x-axis (3 s.f.).',math.degrees(math.atan2(y,x)),0.5,'°',f'tan θ = {y}/{x}, so θ = tan⁻¹({fm(y/x,4)}) = {math.degrees(math.atan2(y,x)):.3g}°.'))
for _ in range(3):
    A0=[ri(-4,4) for _ in range(3)];Bv=[ri(-4,6) for _ in range(3)]
    a('m-vec',2,N(f'A = ({A0[0]}, {A0[1]}, {A0[2]}), B = ({Bv[0]}, {Bv[1]}, {Bv[2]}). Find |AB| (3 s.f.).',math.dist(A0,Bv),0.5,'',f'AB = b − a = ({Bv[0]-A0[0]}, {Bv[1]-A0[1]}, {Bv[2]-A0[2]}). Its length is √({(Bv[0]-A0[0])**2} + {(Bv[1]-A0[1])**2} + {(Bv[2]-A0[2])**2}) = {math.dist(A0,Bv):.3g}.'))
for _ in range(2):
    k=ri(2,5)
    a('m-vec',2,N(f'a = 2i + {k}j and b = 6i + pj are parallel. Find p.',3*k,0,'',f'Parallel vectors are multiples: the i-components give b = 3a, so p = 3 × {k} = {3*k}.'))
for _ in range(3):
    A0=[ri(-3,3) for _ in range(3)];Bv=[ri(-3,6) for _ in range(3)]
    M_=[(x+y)/2 for x,y in zip(A0,Bv)]
    a('m-vec',3,N(f'A = ({A0[0]}, {A0[1]}, {A0[2]}), B = ({Bv[0]}, {Bv[1]}, {Bv[2]}). M is the midpoint of AB. Find |OM| (3 s.f.).',math.sqrt(sum(m*m for m in M_)),0.5,'',f'OM = ½(a + b) = ({fm(M_[0])}, {fm(M_[1])}, {fm(M_[2])}). Its magnitude is √({fm(M_[0]**2)} + {fm(M_[1]**2)} + {fm(M_[2]**2)}) = {math.sqrt(sum(m*m for m in M_)):.3g}.'))
for _ in range(2):
    p,q=ri(2,6),ri(2,6)
    a('m-vec',3,N(f'Triangle with vertices O, A({p}, 0, 0) and B(0, {q}, 0). Find the area of triangle OAB.',p*q/2,0,'',f'OA lies along the x-axis and OB along the y-axis, so the angle at O is 90°. Area = ½ × {p} × {q} = {fm(p*q/2)}.'))
a('m-vec',3,N('OABC is a parallelogram with a = 3i + j, c = i + 4j. Find |OB| (3 s.f.).',math.hypot(4,5),0.5,'','OB = OA + AB = a + c = 4i + 5j, so its length is √(4² + 5²) = √41 = 6.40.'))
a('m-vec',3,N('A particle moves with velocity (3i − 4j) m/s from position 2i + j. Find its distance from the origin after 2 s (3 s.f.).',math.hypot(8,-7),0.5,'m','r = r₀ + vt = (2i + j) + 2(3i − 4j) = 8i − 7j. Distance = √(8² + 7²) = √113 = 10.6 m.'))
# ---- statistics
for _ in range(3):
    xs=[ri(1,20) for _ in range(6)]
    a('s-data',1,N(f'Find the mean of {", ".join(map(str,xs))} (3 s.f.).',sum(xs)/6,0.5,'',f'Mean = Σx ÷ n = {sum(xs)} ÷ 6 = {sum(xs)/6:.3g}.'))
for _ in range(3):
    n=ri(10,20);sx=ri(50,200);m=sx/n;sxx=round(n*(m*m+ri(4,25)))
    a('s-data',2,N(f'n = {n}, Σx = {sx}, Σx² = {sxx}. Find the standard deviation (3 s.f.).',math.sqrt(sxx/n-m*m),0.5,'',f'x̄ = {sx}/{n} = {m:.4g}. σ = √(Σx²/n − x̄²) = √({sxx}/{n} − {m:.4g}²) = √{sxx/n-m*m:.4g} = {math.sqrt(sxx/n-m*m):.3g}.'))
for _ in range(2):
    q1,q3=ri(10,30),ri(35,60)
    a('s-data',2,N(f'Q₁ = {q1}, Q₃ = {q3}. Find the lower outlier boundary (Q₁ − 1.5 × IQR).',q1-1.5*(q3-q1),0,'',f'IQR = {q3} − {q1} = {q3-q1}; boundary = {q1} − 1.5 × {q3-q1} = {fm(q1-1.5*(q3-q1))}.'))
for _ in range(2):
    w,f=pick(5,10,20),ri(12,60)
    a('s-data',2,N(f'A class of width {w} has frequency {f}. Find its frequency density.',f/w,0.5,'',f'Frequency density = frequency ÷ class width = {f} ÷ {w} = {fm(f/w,3)}.'))
for _ in range(3):
    a_,b_=ri(2,9),pick(0.5,1.2,2.5)
    xv=ri(10,30)
    a('s-data',3,N(f'Coded data y = (x − {a_*10})/{b_*2 if False else 5} has mean 2.4 and standard deviation 1.2. Find the standard deviation of x.',6,0,'',f'x = 5y + {a_*10}. Adding a constant does not change the spread and multiplying by 5 multiplies it by 5, so σx = 5 × 1.2 = 6.'))
    break
a('s-data',3,N('Coded y = (x − 100)/5 has ȳ = 2.4. Find x̄.',112,0,'','Rearrange the coding: x = 5y + 100, so x̄ = 5ȳ + 100 = 5 × 2.4 + 100 = 112.'))
a('s-data',3,N('Grouped data: 10–20 (f = 4), 20–30 (f = 6), 30–50 (f = 10). Estimate the mean using midpoints.',(15*4+25*6+40*10)/20,0.5,'','Midpoints 15, 25 and 40. Σfx = 15 × 4 + 25 × 6 + 40 × 10 = 610 and Σf = 20, so the estimated mean = 610 ÷ 20 = 30.5.'))
a('s-data',3,N('Same data: estimate the median by interpolation (classes 10–20 f 4, 20–30 f 6, 30–50 f 10).',30,0.5,'','n = 20, so the median is the 10th value (n/2). Cumulative frequencies are 4, 10, 20, so the 10th value is at the end of the 20–30 class: median ≈ 30.'))
a('s-data',3,N('Regression line y = 2.3 + 0.8x for x in [10, 40]. Predict y at x = 25.',22.3,0,'','y = 2.3 + 0.8 × 25 = 2.3 + 20 = 22.3. x = 25 is within the data range, so this is interpolation and reasonably reliable.'))
for _ in range(3):
    pa,pb=pick(0.2,0.3,0.4,0.5),pick(0.1,0.2,0.3,0.6)
    a('s-prob',1,N(f'A and B are independent with P(A) = {pa}, P(B) = {pb}. Find P(A ∪ B).',pa+pb-pa*pb,0.5,'',f'Independent, so P(A ∩ B) = {pa} × {pb} = {fm(pa*pb)}. P(A ∪ B) = {pa} + {pb} − {fm(pa*pb)} = {fm(pa+pb-pa*pb)}.'))
for _ in range(2):
    r,b=ri(3,8),ri(2,7)
    a('s-prob',1,N(f'A bag has {r} red and {b} blue balls. Two are taken without replacement. Find P(both red) (3 s.f.).',r*(r-1)/((r+b)*(r+b-1)),0.5,'',f'({r}/{r+b}) × ({r-1}/{r+b-1}): one fewer red and one fewer ball for the second pick.'))
for _ in range(3):
    pa,pab=pick(0.4,0.5,0.6),pick(0.1,0.15,0.2)
    a('s-prob',2,N(f'P(A) = {pa}, P(A ∩ B) = {pab}. Find P(B given A) (3 s.f.).',pab/pa,0.5,'',f'P(B given A) = P(A ∩ B) ÷ P(A) = {pab} ÷ {pa} = {pab/pa:.3g}.'))
for _ in range(2):
    p=pick(0.01,0.02,0.05);s=pick(0.95,0.9,0.98);fp=pick(0.05,0.1)
    a('s-prob',3,N(f'A disease affects {p*100:g}% of people. A test detects it {s*100:g}% of the time and gives a false positive {fp*100:g}% of the time. Find P(disease given positive) (3 s.f.).',p*s/(p*s+(1-p)*fp),0.5,'',f'P(positive) = {p} × {s} + {fm(1-p)} × {fp} = {p*s+(1-p)*fp:.4g}. P(disease given positive) = {fm(p*s,4)} ÷ {p*s+(1-p)*fp:.4g} = {p*s/(p*s+(1-p)*fp):.3g}. Most positives are false because the disease is rare.'))
for _ in range(3):
    pa,pb,pab=0.5,pick(0.3,0.4),pick(0.1,0.2)
    a('s-prob',3,N(f'P(A) = {pa}, P(B) = {pb}, P(A ∩ B) = {pab}. Find P(A′ ∩ B′).',1-(pa+pb-pab),0.5,'',f'P(A ∪ B) = {pa} + {pb} − {pab} = {fm(pa+pb-pab)}. P(A′ ∩ B′) = 1 − P(A ∪ B) = {fm(1-(pa+pb-pab))}.'))
a('s-prob',2,N('P(A) = 0.3, P(B) = 0.5, A and B mutually exclusive. Find P(A ∪ B).',0.8,0,'','Mutually exclusive, so P(A ∩ B) = 0 and P(A ∪ B) = 0.3 + 0.5.'))
a('s-prob',2,N('Two fair dice are rolled. Find P(sum = 7).',1/6,0.5,'','There are 36 equally likely outcomes, and 6 give a sum of 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1). P = 6/36 = 1/6.'))
for _ in range(3):
    n,p,k=ri(8,15),pick(0.2,0.3,0.4),ri(1,4)
    a('s-dist',1,N(f'X ~ B({n}, {p}). Find P(X = {k}) (3 s.f.).',math.comb(n,k)*p**k*(1-p)**(n-k),0.5,'',f'P(X = {k}) = {n}C{k} × {p}^{k} × {fm(1-p)}^{n-k} = {math.comb(n,k)} × {p**k:.4g} × {(1-p)**(n-k):.4g} = {math.comb(n,k)*p**k*(1-p)**(n-k):.3g}.'))
for _ in range(3):
    n,p=ri(10,30),pick(0.2,0.25,0.4)
    a('s-dist',2,N(f'X ~ B({n}, {p}). Find P(X ≤ 1) (3 s.f.).',(1-p)**n+n*p*(1-p)**(n-1),0.5,'',f'P(X ≤ 1) = P(X = 0) + P(X = 1) = {fm(1-p)}^{n} + {n} × {p} × {fm(1-p)}^{n-1} = {(1-p)**n:.4g} + {n*p*(1-p)**(n-1):.4g} = {(1-p)**n+n*p*(1-p)**(n-1):.3g}.'))
for _ in range(3):
    mu,sd,x=ri(40,80),ri(3,10),None
    z=pick(1,1.5,2);x=mu+z*sd
    Phi=0.5*(1+math.erf(z/math.sqrt(2)))
    a('s-dist',2,N(f'X ~ N({mu}, {sd}²). Find P(X > {fm(x)}) (3 s.f.).',1-Phi,0.5,'',f'Standardise: z = ({fm(x)} − {mu}) ÷ {sd} = {z}. P(X > {fm(x)}) = P(Z > {z}) = 1 − {Phi:.4f} = {1-Phi:.3g}.'))
for _ in range(3):
    mu,sd=ri(100,200),ri(5,20);x1,x2=mu-sd,mu+2*sd
    Phi=lambda z:0.5*(1+math.erf(z/math.sqrt(2)))
    a('s-dist',3,N(f'X ~ N({mu}, {sd}²). Find P({x1} < X < {x2}) (3 s.f.).',Phi(2)-Phi(-1),0.5,'',f'z-values: ({x1} − {mu})/{sd} = −1 and ({x2} − {mu})/{sd} = 2. P(−1 < Z < 2) = 0.9772 − 0.1587 = 0.819.'))
for _ in range(2):
    mu=ri(50,80)
    a('s-dist',3,N(f'X ~ N({mu}, σ²) and P(X > {mu+10}) = 0.1587. Find σ.',10,0.5,'',f'P(Z > 1) = 0.1587, so {mu+10} is 1 standard deviation above the mean: ({mu+10} − {mu})/σ = 1, so σ = 10.'))
a('s-dist',3,N('X ~ B(100, 0.4). Using a normal approximation, find the variance of the approximating normal.',24,0,'','The approximating normal has σ² = np(1 − p) = 100 × 0.4 × 0.6 = 24.'))
a('s-dist',3,N('X ~ B(50, 0.5). Find the mean of the normal approximation.',25,0,'','μ = np = 50 × 0.5 = 25.'))
# hypothesis tests (binomial)
def bcdf(n,p,k): return sum(math.comb(n,i)*p**i*(1-p)**(n-i) for i in range(k+1))
for _ in range(3):
    n=ri(10,20);p=pick(0.2,0.3);x=ri(0,1)
    a('s-hyp',2,N(f'H₀: p = {p}, H₁: p < {p}, n = {n}. Observed X = {x}. Find the p-value P(X ≤ {x}) (3 s.f.).',bcdf(n,p,x),0.5,'',f'Under H₀, X ~ B({n}, {p}). p-value = P(X ≤ {x}) = {bcdf(n,p,x):.3g}. Compare it with the significance level: reject H₀ if it is smaller.'))
for _ in range(3):
    n=ri(15,25);p=pick(0.3,0.4,0.5)
    c=next(k for k in range(n+1) if 1-bcdf(n,p,k-1)<=0.05)
    a('s-hyp',3,N(f'X ~ B({n}, {p}) under H₀. H₁: p > {p} at 5%. Find the smallest c with P(X ≥ c) ≤ 0.05 (critical value).',c,0,'',f'P(X ≥ {c}) = 1 − P(X ≤ {c-1}) = {1-bcdf(n,p,c-1):.4f}, which is at most 0.05, but P(X ≥ {c-1}) = {1-bcdf(n,p,c-2):.4f} is greater than 0.05. So c = {c}.'))
for _ in range(2):
    n=ri(15,25);p=0.4
    c=next(k for k in range(n+1) if 1-bcdf(n,p,k-1)<=0.05)
    a('s-hyp',3,N(f'For X ~ B({n}, 0.4), the critical region is X ≥ {c}. Find the actual significance level (4 d.p.).',1-bcdf(n,p,c-1),1,'',f'Actual significance level = P(X ≥ {c}) = 1 − P(X ≤ {c-1}).'))
for _ in range(2):
    mu,sd,n=ri(50,100),ri(5,15),pick(16,25,36)
    a('s-hyp',3,N(f'Sample mean of {n} values from N(μ, {sd}²) is x̄. Find the standard error of x̄ (3 s.f.).',sd/math.sqrt(n),0.5,'',f'Standard error = σ/√n = {sd} ÷ √{n} = {sd} ÷ {int(math.sqrt(n))} = {sd/math.sqrt(n):.3g}.'))
# mechanics
for _ in range(3):
    u,a_,t=ri(0,10),ri(1,5),ri(2,8)
    a('k-kin',1,N(f'u = {u} m/s, a = {a_} m s⁻², t = {t} s. Find the displacement.',u*t+0.5*a_*t*t,0,'m',f's = ut + ½at² = {u} × {t} + ½ × {a_} × {t}² = {fm(u*t+0.5*a_*t*t)} m.'))
for _ in range(3):
    u,h=ri(5,20),ri(5,40)
    v=math.sqrt(u*u+2*9.8*h)
    a('k-kin',2,N(f'A stone is thrown down at {u} m/s from a height of {h} m. Find its speed on hitting the ground (g = 9.8, 3 s.f.).',v,0.5,'m/s',f'Taking down as positive: v² = u² + 2as = {u}² + 2 × 9.8 × {h} = {u*u+2*9.8*h:.4g}, so v = {v:.3g} m/s.'))
for _ in range(2):
    k=ri(1,4)
    a('k-kin',2,N(f'v = {k}t² + 2t m/s. Find the displacement from t = 0 to t = 3.',k*9+9,0.5,'m',f's = ∫₀³ ({k}t² + 2t) dt = [{fm(k/3,4)}t³ + t²]₀³ = {9*k} + 9 = {9*k+9} m.'))
for _ in range(3):
    U,ang=ri(15,30),pick(30,40,45,60)
    th=math.radians(ang);T=2*U*math.sin(th)/9.8
    a('k-kin',3,N(f'A projectile is launched at {U} m/s at {ang}° above horizontal level ground. Find its range (g = 9.8, 3 s.f.).',U*math.cos(th)*T,0.5,'m',f'Vertical: 0 = ({U} sin {ang}°)t − 4.9t², so t = {T:.3g} s. Horizontal: range = {U} cos {ang}° × {T:.3g} = {U*math.cos(th)*T:.3g} m.'))
for _ in range(2):
    U,ang=ri(15,30),pick(30,45,60)
    th=math.radians(ang)
    a('k-kin',3,N(f'Launched at {U} m/s at {ang}°. Find its maximum height (g = 9.8, 3 s.f.).',(U*math.sin(th))**2/(2*9.8),0.5,'m',f'At the top the vertical velocity is 0: 0 = ({U} sin {ang}°)² − 2 × 9.8 × h, so h = {(U*math.sin(th))**2:.4g} ÷ 19.6 = {(U*math.sin(th))**2/(2*9.8):.3g} m.'))
for _ in range(3):
    m,F,mu=ri(2,10),ri(20,60),pick(0.1,0.2,0.3)
    acc=(F-mu*m*9.8)/m
    if acc<=0: F+=40;acc=(F-mu*m*9.8)/m
    a('k-force',2,N(f'A {m} kg box is pulled horizontally by {F} N on a rough floor, μ = {mu}. Find its acceleration (g = 9.8, 3 s.f.).',acc,0.5,'m s⁻²',f'R = mg = {m*9.8:.4g} N, so friction = {mu} × {m*9.8:.4g} = {mu*m*9.8:.4g} N. F − friction = ma: a = ({F} − {mu*m*9.8:.4g}) ÷ {m} = {acc:.3g} m s⁻².'))
for _ in range(2):
    m,ang=ri(2,8),pick(20,30,40)
    a('k-force',1,N(f'A {m} kg block on a smooth slope at {ang}°. Find its acceleration (g = 9.8, 3 s.f.).',9.8*math.sin(math.radians(ang)),0.5,'m s⁻²',f'The only force along the smooth slope is mg sin θ, so a = g sin θ = 9.8 × sin {ang}° = {9.8*math.sin(math.radians(ang)):.3g} m s⁻² (the mass cancels).'))
for _ in range(3):
    m1,m2=ri(2,6),ri(1,5);mu=pick(0.2,0.3)
    acc=(m2*9.8-mu*m1*9.8)/(m1+m2)
    if acc<=0: m2+=4;acc=(m2*9.8-mu*m1*9.8)/(m1+m2)
    a('k-force',3,N(f'A {m1} kg block on a rough table (μ = {mu}) is joined by a light string over a smooth pulley to a hanging {m2} kg mass. Find the acceleration (g = 9.8, 3 s.f.).',acc,0.5,'m s⁻²',f'Hanging mass: {m2}g − T = {m2}a. Block: T − {mu} × {m1}g = {m1}a. Add: {m2*9.8:.4g} − {mu*m1*9.8:.4g} = {m1+m2}a, so a = {acc:.3g} m s⁻².'))
for _ in range(2):
    m,ang,mu=ri(2,8),pick(25,30,35),pick(0.2,0.3)
    th=math.radians(ang)
    a('k-force',3,N(f'A {m} kg block slides down a rough {ang}° slope, μ = {mu}. Find its acceleration (g = 9.8, 3 s.f.).',9.8*(math.sin(th)-mu*math.cos(th)),0.5,'m s⁻²',f'R = mg cos θ, so friction = μmg cos θ. mg sin θ − μmg cos θ = ma, so a = 9.8(sin {ang}° − {mu} cos {ang}°) = {9.8*(math.sin(th)-mu*math.cos(th)):.3g} m s⁻².'))
for _ in range(3):
    L,W_=ri(4,8),ri(50,200);x=ri(1,L-1);Wc=ri(20,100)
    Rb=(W_*L/2+Wc*x)/L
    a('k-mom',2,N(f'A uniform {L} m beam of weight {W_} N rests on supports at each end. A {Wc} N load is {x} m from the left end. Find the reaction at the right support (3 s.f.).',Rb,0.5,'N',f'Moments about the left end: R × {L} = {W_} × {fm(L/2)} + {Wc} × {x} = {fm(W_*L/2+Wc*x)}, so R = {Rb:.3g} N.'))
for _ in range(3):
    L,W_=ri(4,8),ri(80,200);
    a('k-mom',3,N(f'A uniform {L} m ladder of weight {W_} N rests against a smooth wall at 60° to rough ground and is about to slip. Find the friction at the ground (3 s.f.).',W_*(L/2)*math.cos(math.radians(60))/(L*math.sin(math.radians(60))),0.5,'N','Moments about the base: F = S, S × L sin 60° = W × (L/2) cos 60°.'))
for _ in range(2):
    L,W_=ri(3,6),ri(40,120);x=ri(1,L-1)
    a('k-mom',3,N(f'A uniform {L} m rod of weight {W_} N is held horizontal by a vertical string at one end and a pivot at the other. Find the tension (3 s.f.).',W_/2,0.5,'N',f'Moments about the pivot: T × {L} = {W_} × {fm(L/2)} (weight at the midpoint), so T = {W_} ÷ 2 = {fm(W_/2)} N.'))
for _ in range(2):
    m=ri(2,9)
    a('k-units',1,N(f'Convert {m*18} km/h to m/s.',m*5,0,'m/s',f'{m*18} km/h = {m*18000} m ÷ 3600 s = {m*5} m/s (divide by 3.6).'))
for _ in range(2):
    m=ri(2,9)
    a('k-units',2,N(f'Find the weight of {m*100} g on the Moon (g = 1.6).',m*0.16,0.5,'N',f'{m*100} g = {m/10:g} kg. W = mg = {m/10:g} × 1.6 = {fm(m*0.16)} N.'))
a('k-units',2,N('Convert a density of 2.7 g/cm³ to kg/m³.',2700,0,'kg m⁻³','1 g/cm³ = 0.001 kg ÷ 10⁻⁶ m³ = 1000 kg/m³, so 2.7 g/cm³ = 2700 kg/m³.'))
a('k-units',2,N('Convert 500 cm² to m².',0.05,0,'m²','1 m² = 100 cm × 100 cm = 10 000 cm², so 500 cm² = 500 ÷ 10 000 = 0.05 m².'))
a('k-units',3,N('A 1500 kg car accelerates from 0 to 27 m/s in 9 s. Find the resultant force.',4500,0,'N','a = (27 − 0) ÷ 9 = 3 m s⁻². F = ma = 1500 × 3 = 4500 N.'))
a('k-units',3,N('A force of 6 kN acts on 1.2 tonnes. Find the acceleration.',5,0,'m s⁻²','6 kN = 6000 N and 1.2 tonnes = 1200 kg. a = F ÷ m = 6000 ÷ 1200 = 5 m s⁻².'))
