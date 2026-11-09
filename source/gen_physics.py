from lib import *
import math
B=Bank(2); R=B.R; a=B.add
g=9.81;e=1.60e-19;h=6.63e-34;c=3.00e8;me=9.11e-31;G=6.67e-11;kB=1.38e-23;NA=6.02e23;Rg=8.31;e0=8.85e-12
def ri(x,y): return R.randint(x,y)
def pk(*x): return R.choice(x)
def rep(n,f):
    for _ in range(n): f()
T=lambda tid,lv,q,ans,u,ex,tol=0.5: a(tid,lv,N(q,ans,tol,u,ex))
# p-1 practical: uncertainty / gradient calcs
def f():
    r=[round(R.uniform(2.0,2.6),2) for _ in range(4)]
    T('p-1',1,f'Repeat readings: {", ".join(map(str,r))} s. Find the mean (3 s.f.).',sum(r)/4,'s','Add and divide by 4.')
rep(3,f)
def f():
    r=[round(R.uniform(2.0,2.6),2) for _ in range(4)]
    T('p-1',2,f'Readings {", ".join(map(str,r))} s. Find the absolute uncertainty as half the range.',(max(r)-min(r))/2,'s','½(max − min).',1)
rep(3,f)
def f():
    x1,y1,x2,y2=ri(1,3),ri(2,9),ri(6,10),ri(12,40)
    T('p-1',1,f'A best-fit line passes through ({x1}, {y1}) and ({x2}, {y2}). Find its gradient (3 s.f.).',(y2-y1)/(x2-x1),'','Δy/Δx using points far apart.')
rep(3,f)
def f():
    gb,gw=round(R.uniform(2,5),2),0
    gw=round(gb*R.uniform(1.04,1.12),2)
    T('p-1',3,f'Best-fit gradient {gb}, worst-fit gradient {gw}. Find the percentage uncertainty in the gradient (3 s.f.).',abs(gw-gb)/gb*100,'%','(worst − best)/best × 100.')
rep(3,f)
def f():
    L,dL,t,dt=round(R.uniform(0.5,1.2),2),0.005,round(R.uniform(1.4,2.2),2),0.05
    T('p-1',3,f'g = 4π²L/T². L = {L} ± {dL} m, T = {t} ± {dt} s. Find the percentage uncertainty in g (3 s.f.).',(dL/L+2*dt/t)*100,'%','%L + 2 × %T.')
rep(3,f)
def f():
    d=round(R.uniform(0.2,0.6),2)
    T('p-1',2,f'A micrometer reads {d} mm ± 0.01 mm. Find the percentage uncertainty in the cross-sectional area (3 s.f.).',2*0.01/d*100,'%','A ∝ d², so double the percentage.')
rep(3,f)
# p-2-1 units / prefixes / estimation
def f():
    v=ri(2,9);p=pk(('m',1e-3,'milli'),('µ',1e-6,'micro'),('n',1e-9,'nano'),('k',1e3,'kilo'),('M',1e6,'mega'))
    T('p-2-1',1,f'Write {v} {p[0]}A in amps (give the number in standard form; enter e.g. 3e-6).',v*p[1],'A',f'{p[2]} = {p[1]:g}.')
rep(4,f)
def f():
    P,t=ri(2,9)*100,ri(2,8)
    T('p-2-1',2,f'A {P} W heater runs for {t} hours. Find the energy in MJ (3 s.f.).',P*t*3600/1e6,'MJ','E = Pt, t in seconds.')
rep(3,f)
def f():
    m,v=ri(50,90),ri(3,8)
    T('p-2-1',1,f'Estimate: KE of a {m} kg runner at {v} m/s.',0.5*m*v*v,'J','½mv².')
rep(3,f)
def f():
    r=pk(2,3,4,5)
    T('p-2-1',3,f'Density of a sphere: mass {r*10} g, radius {r} cm. Find the density in kg m⁻³ (3 s.f.).',(r*10e-3)/(4/3*math.pi*(r/100)**3),'kg m⁻³','Convert to kg and m³ first.')
rep(4,f)
def f():
    x=pk(2,3,4)
    T('p-2-1',3,f'Drag F = kv². F = {x*10} N at {x} m/s. Find k and give its value (3 s.f.) — units kg m⁻¹.',x*10/x**2,'kg m⁻¹','k = F/v²; N m⁻² s² = kg m⁻¹.')
rep(3,f)
# p-2-2 uncertainties
def f():
    v,dv=ri(20,90),ri(1,3)
    T('p-2-2',1,f'{v} ± {dv} cm. Percentage uncertainty (3 s.f.)?',dv/v*100,'%','Δx/x × 100.')
rep(4,f)
def f():
    a1,a2=ri(1,5),ri(1,5)
    T('p-2-2',2,f'Length {a1}% uncertain, width {a2}% uncertain. Percentage uncertainty in area?',a1+a2,'%','Add percentages.')
rep(3,f)
def f():
    V,dV,I,dI=round(R.uniform(3,12),1),0.1,round(R.uniform(0.2,1.5),2),0.02
    T('p-2-2',2,f'V = {V} ± {dV} V, I = {I} ± {dI} A. Find the percentage uncertainty in R = V/I (3 s.f.).',(dV/V+dI/I)*100,'%','Add percentage uncertainties.')
rep(4,f)
def f():
    d,dd=round(R.uniform(0.3,0.9),2),0.01
    L=round(R.uniform(1.0,2.0),2)
    T('p-2-2',3,f'ρ = RA/L with A = πd²/4. d = {d} ± {dd} mm, L = {L} ± 0.01 m, R known to 2%. Percentage uncertainty in ρ (3 s.f.)?',(2+2*dd/d*100+0.01/L*100),'%','2% + 2(%d) + %L.')
rep(4,f)
def f():
    x,dx=round(R.uniform(2,6),1),0.1
    T('p-2-2',3,f'y = x³ with x = {x} ± {dx}. Find the absolute uncertainty in y (3 s.f.).',x**3*3*dx/x,'','Δy = y × 3(Δx/x).')
rep(3,f)
# p-2-3 vectors
def f():
    F,ang=ri(10,80),pk(20,30,35,40,50,60)
    T('p-2-3',1,f'A {F} N force acts at {ang}° above horizontal. Find the vertical component (3 s.f.).',F*math.sin(math.radians(ang)),'N','F sin θ.')
rep(4,f)
def f():
    a1,b1=ri(3,20),ri(3,20)
    T('p-2-3',2,f'Perpendicular forces {a1} N and {b1} N. Find the angle of the resultant to the {a1} N force (3 s.f.).',math.degrees(math.atan2(b1,a1)),'°','tan⁻¹(opp/adj).')
rep(4,f)
def f():
    v,w=ri(2,6),ri(1,4)
    T('p-2-3',2,f'A boat heads across a river at {v} m/s; the current is {w} m/s. Find the resultant speed (3 s.f.).',math.hypot(v,w),'m/s','Pythagoras.')
rep(3,f)
def f():
    F1,F2,th=ri(10,40),ri(10,40),pk(60,90,120)
    T('p-2-3',3,f'Two forces {F1} N and {F2} N act at {th}° to each other. Find the resultant magnitude (3 s.f.).',math.sqrt(F1*F1+F2*F2+2*F1*F2*math.cos(math.radians(th))),'N','Resolve or cosine rule.')
rep(4,f)
def f():
    m,ang=ri(2,10),pk(20,30,40)
    T('p-2-3',3,f'A {m} kg mass rests on a slope at {ang}°. Find the friction needed to stop it sliding (3 s.f., g = 9.81).',m*g*math.sin(math.radians(ang)),'N','Equals mg sin θ.')
rep(3,f)
# p-3-1 motion
def f():
    u,acc,t=ri(0,10),ri(1,6),ri(2,8)
    T('p-3-1',1,f'u = {u} m/s, a = {acc} m s⁻², t = {t} s. Find v.',u+acc*t,'m/s','v = u + at.',0)
rep(4,f)
def f():
    v,tr,dec=ri(15,30),round(R.uniform(0.5,1.0),1),ri(4,8)
    T('p-3-1',2,f'A car at {v} m/s: reaction time {tr} s, deceleration {dec} m s⁻². Find the stopping distance (3 s.f.).',v*tr+v*v/(2*dec),'m','Thinking + braking distance.')
rep(4,f)
def f():
    hh=ri(5,40)
    T('p-3-1',2,f'An object is dropped from {hh} m. Find the time to fall (3 s.f., g = 9.81).',math.sqrt(2*hh/g),'s','s = ½gt².')
rep(3,f)
def f():
    U,ang=ri(10,30),pk(30,40,50,60)
    th=math.radians(ang)
    T('p-3-1',3,f'A ball is kicked at {U} m/s at {ang}° on level ground. Find its range (3 s.f., g = 9.81).',U*U*math.sin(2*th)/g,'m','Time of flight × horizontal velocity.')
rep(4,f)
def f():
    U,hh=ri(5,15),ri(10,40)
    t=(U+math.sqrt(U*U+2*g*hh))/g
    T('p-3-1',3,f'A stone is thrown vertically up at {U} m/s from a {hh} m cliff top. Find the time to hit the ground below (3 s.f.).',t,'s','s = ut + ½at² with s = −h.')
rep(3,f)
# p-3-2 forces in action
def f():
    m=ri(2,20);F=ri(10,100)
    T('p-3-2',1,f'Resultant force {F} N on {m} kg. Acceleration (3 s.f.)?',F/m,'m s⁻²','a = F/m.')
rep(3,f)
def f():
    hh,rho=ri(2,30),pk(1000,1030,800)
    T('p-3-2',1,f'Find the pressure at {hh} m depth in a fluid of density {rho} kg m⁻³ (3 s.f., kPa).',hh*rho*g/1000,'kPa','p = hρg.')
rep(3,f)
def f():
    V,rho=round(R.uniform(0.5,3),2)/1000,pk(1000,1030)
    T('p-3-2',2,f'Find the upthrust on a fully submerged object of volume {V*1000:g} × 10⁻³ m³ in fluid of density {rho} kg m⁻³ (3 s.f.).',V*rho*g,'N','Weight of fluid displaced.')
rep(4,f)
def f():
    F,d,ang=ri(10,50),round(R.uniform(0.2,0.8),2),pk(30,45,60)
    T('p-3-2',2,f'A {F} N force acts at {ang}° to a spanner of length {d} m. Find the moment about the nut (3 s.f.).',F*d*math.sin(math.radians(ang)),'N m','F × perpendicular distance.')
rep(3,f)
def f():
    F,d=ri(5,30),round(R.uniform(0.1,0.5),2)
    T('p-3-2',3,f'A couple of two {F} N forces {d} m apart. Find the torque.',F*d,'N m','One force × separation.')
rep(3,f)
def f():
    m,W2,x=ri(1,5),ri(10,40),pk(0.05,0.10,0.15,0.20,0.25,0.30)
    L=1.0
    T('p-3-2',3,f'A uniform 1.0 m ruler of weight {m} N is pivoted at 0.40 m. What weight at the 0.{int(x*100):02d} m mark balances it? (3 s.f.)',m*0.10/(0.40-x),'N','Moments about the pivot.')
rep(4,f)
# p-3-3 work energy power
def f():
    m,v=ri(1,10),ri(2,15)
    T('p-3-3',1,f'KE of {m} kg at {v} m/s?',0.5*m*v*v,'J','½mv².',0)
rep(3,f)
def f():
    m,hh=ri(1,10),ri(2,20)
    T('p-3-3',1,f'GPE gained by {m} kg raised {hh} m (3 s.f., g = 9.81)?',m*g*hh,'J',f'ΔEp = mgΔh = {m} × 9.81 × {hh}.')
rep(3,f)
def f():
    P,v=ri(10,60)*1000,ri(15,40)
    T('p-3-3',2,f'A car’s engine delivers {P/1000:g} kW at a steady {v} m/s. Find the driving force (3 s.f.).',P/v,'N','P = Fv.')
rep(4,f)
def f():
    m,hh,t,eff=ri(50,300),ri(5,20),ri(10,40),pk(0.6,0.7,0.8)
    T('p-3-3',3,f'A motor of efficiency {int(eff*100)}% lifts {m} kg through {hh} m in {t} s. Find its input power (3 s.f.).',m*g*hh/t/eff,'W','Useful power ÷ efficiency.')
rep(4,f)
def f():
    m,hh,v=ri(40,80),ri(5,20),ri(3,8)
    vmax=math.sqrt(2*g*hh)
    if v>=vmax: v=int(vmax)-1
    T('p-3-3',3,f'A {m} kg skier descends {hh} m from rest and reaches {v} m/s. Find the energy dissipated (3 s.f.).',m*g*hh-0.5*m*v*v,'J','GPE lost − KE gained.')
rep(3,f)
# p-3-4 materials
def f():
    F,k=ri(2,20),ri(50,400)
    T('p-3-4',1,f'A spring (k = {k} N/m) has a {F} N load. Extension (cm, 3 s.f.)?',F/k*100,'cm','x = F/k.')
rep(3,f)
def f():
    F,d=ri(20,200),pk(0.3,0.5,0.8,1.0)
    A=math.pi*(d/1000)**2/4
    T('p-3-4',2,f'A wire of diameter {d} mm carries {F} N. Find the stress (3 s.f., give × 10⁸ Pa).',F/A/1e8,'× 10⁸ Pa','A = πd²/4.')
rep(4,f)
def f():
    L,x=round(R.uniform(1,3),2),round(R.uniform(0.5,3),1)
    T('p-3-4',1,f'A {L} m wire extends by {x} mm. Find the strain (3 s.f., × 10⁻³).',x/1000/L*1000,'× 10⁻³','ε = x/L.')
rep(3,f)
def f():
    F,d,L,x=ri(50,200),pk(0.5,0.8,1.0),round(R.uniform(1.5,3),1),round(R.uniform(0.8,3),1)
    A=math.pi*(d/1000)**2/4
    T('p-3-4',3,f'A wire: length {L} m, diameter {d} mm, load {F} N, extension {x} mm. Find the Young modulus (3 s.f., × 10¹¹ Pa).',(F/A)/(x/1000/L)/1e11,'× 10¹¹ Pa','E = stress/strain.')
rep(4,f)
def f():
    k1,k2=ri(20,80),ri(20,80)
    T('p-3-4',2,f'Springs of {k1} N/m and {k2} N/m in parallel. Combined k?',k1+k2,'N/m','Parallel springs add.',0)
rep(2,f)
def f():
    k1,k2=ri(20,80),ri(20,80)
    T('p-3-4',3,f'Springs of {k1} N/m and {k2} N/m in series carry 6.0 N. Find the total elastic energy stored (3 s.f.).',0.5*36*(1/k1+1/k2),'J','E = F²/2k_total, 1/k = 1/k₁ + 1/k₂.')
rep(3,f)
# p-3-5 momentum
def f():
    m1,u1,m2=ri(1,6),ri(2,8),ri(1,6)
    T('p-3-5',1,f'A {m1} kg trolley at {u1} m/s sticks to a stationary {m2} kg trolley. Common velocity (3 s.f.)?',m1*u1/(m1+m2),'m/s','Conservation of momentum.')
rep(3,f)
def f():
    m,u,v,t=round(R.uniform(0.05,0.5),2),ri(5,20),ri(5,20),round(R.uniform(0.01,0.1),2)
    T('p-3-5',2,f'A {m} kg ball hits a wall at {u} m/s and rebounds at {v} m/s, contact {t} s. Find the average force (3 s.f.).',m*(u+v)/t,'N','Δp = m(u + v).')
rep(4,f)
def f():
    M,m,v=ri(2,8),round(R.uniform(0.01,0.05),3),ri(200,500)
    T('p-3-5',2,f'A {M} kg gun fires a {m} kg bullet at {v} m/s. Recoil speed (3 s.f.)?',m*v/M,'m/s','Total momentum stays zero.')
rep(3,f)
def f():
    m1,u1,m2,u2=ri(2,6),ri(3,8),ri(1,5),-ri(1,4)
    v=(m1*u1+m2*u2)/(m1+m2)
    ke=0.5*m1*u1**2+0.5*m2*u2**2-0.5*(m1+m2)*v*v
    T('p-3-5',3,f'{m1} kg at {u1} m/s collides head-on with {m2} kg moving at {abs(u2)} m/s the other way; they stick. Find the KE lost (3 s.f.).',ke,'J','Find v, then compare KE before and after.')
rep(4,f)
def f():
    rho,A,v=1000,round(R.uniform(0.001,0.01),3),ri(5,20)
    T('p-3-5',3,f'Water (ρ = 1000 kg m⁻³) leaves a hose of area {A} m² at {v} m/s and stops on a wall. Find the force (3 s.f.).',rho*A*v*v,'N','F = (dm/dt)v = ρAv².')
rep(3,f)
# p-4-1
def f():
    I,t=round(R.uniform(0.1,5),1),ri(10,600)
    T('p-4-1',1,f'{I} A for {t} s. Charge (3 s.f.)?',I*t,'C','Q = It.')
rep(4,f)
def f():
    I=round(R.uniform(0.5,5),1)
    T('p-4-1',2,f'How many electrons pass a point per second for {I} A? (give × 10¹⁸, 3 s.f.)',I/e/1e18,'× 10¹⁸','N = I/e.')
rep(4,f)
def f():
    n,d,I=pk(8.5e28,6.0e28),pk(0.5,1.0,1.5),round(R.uniform(0.5,3),1)
    A=math.pi*(d/1000)**2/4
    T('p-4-1',3,f'Wire diameter {d} mm, n = {sci(n)} m⁻³, I = {I} A. Mean drift velocity (mm/s, 3 s.f.)?',I/(n*A*e)*1000,'mm/s','v = I/(nAe).')
rep(4,f)
def f():
    q,t=ri(10,200),ri(2,60)
    T('p-4-1',2,f'{q} C passes in {t} s. Current (3 s.f.)?',q/t,'A','I = Q/t.')
rep(3,f)
def f():
    I1,I2=round(R.uniform(0.2,2),1),round(R.uniform(0.2,2),1)
    T('p-4-1',3,f'At a junction {I1} A and {I2} A flow in; one wire carries 0.3 A out. Find the current in the other outgoing wire.',I1+I2-0.3,'A','Kirchhoff’s first law.')
rep(3,f)
# p-4-2
def f():
    V,R_=ri(2,24),ri(2,100)
    T('p-4-2',1,f'Power dissipated in {R_} Ω with {V} V across it (3 s.f.)?',V*V/R_,'W','P = V²/R.')
rep(4,f)
def f():
    rho,L,d=pk(1.7e-8,4.9e-7,1.1e-6),round(R.uniform(0.5,3),1),pk(0.2,0.3,0.5)
    A=math.pi*(d/1000)**2/4
    T('p-4-2',2,f'Wire: ρ = {sci(rho)} Ω m, L = {L} m, diameter {d} mm. Resistance (3 s.f.)?',rho*L/A,'Ω','R = ρL/A.')
rep(4,f)
def f():
    P,t,cost=pk(2000,3000,1500,800),ri(1,4),ri(20,35)
    T('p-4-2',2,f'A {P} W appliance runs {t} h. At {cost}p per kWh, find the cost (p).',P/1000*t*cost,'p','kWh × price.')
rep(3,f)
def f():
    V,P=pk(230,12),pk(60,100,40)
    R_=V*V/P
    T('p-4-2',3,f'A {V} V, {P} W lamp is run at {V//2 if V==230 else 6} V (assume constant R). Find its power (3 s.f.).',(V/2)**2/R_ if V==230 else 36/R_,'W','R = V²/P at rated values, then P = V²/R.')
rep(4,f)
def f():
    R0=ri(2,20);
    T('p-4-2',3,f'A wire of resistance {R0} Ω is stretched to twice its length (same volume). New resistance?',4*R0,'Ω','L doubles, A halves → R × 4.',0)
rep(2,f)
# p-4-3 circuits
def f():
    r1,r2,r3=ri(2,20),ri(2,20),ri(2,20)
    T('p-4-3',1,f'{r1} Ω, {r2} Ω and {r3} Ω in series. Total?',r1+r2+r3,'Ω',f'In series R = R₁ + R₂ + R₃ = {r1} + {r2} + {r3}.',0)
rep(3,f)
def f():
    r1,r2=ri(2,30),ri(2,30)
    T('p-4-3',2,f'{r1} Ω in parallel with {r2} Ω. Total (3 s.f.)?',1/(1/r1+1/r2),'Ω','1/R = 1/R₁ + 1/R₂.')
rep(4,f)
def f():
    E,r,R_=pk(1.5,6,9,12),round(R.uniform(0.2,2),1),ri(2,20)
    T('p-4-3',2,f'EMF {E} V, internal resistance {r} Ω, load {R_} Ω. Current (3 s.f.)?',E/(R_+r),'A','I = E/(R + r).')
rep(3,f)
def f():
    E,r1,r2,r3=pk(6,9,12),ri(2,10),ri(2,10),ri(2,10)
    Rp=1/(1/r2+1/r3);I=E/(r1+Rp)
    T('p-4-3',3,f'{r1} Ω in series with ({r2} Ω ∥ {r3} Ω), across {E} V (no internal resistance). Current through the {r2} Ω resistor (3 s.f.)?',I*Rp/r2,'A','Find total current, pd across the parallel pair, then I = V/R.')
rep(4,f)
def f():
    Vin,R1,R2=pk(5,9,12),ri(1,10),ri(1,10)
    T('p-4-3',3,f'Potential divider: {Vin} V across {R1} kΩ (top) and an LDR (bottom). The LDR falls to {R2} kΩ. Find V across the LDR (3 s.f.).',Vin*R2/(R1+R2),'V','V_out = V_in × R₂/(R₁ + R₂).')
rep(3,f)
# p-4-4 waves
def f():
    f_,lam=ri(100,1000),round(R.uniform(0.2,3),2)
    T('p-4-4',1,f'f = {f_} Hz, λ = {lam} m. Speed (3 s.f.)?',f_*lam,'m/s','v = fλ.')
rep(3,f)
def f():
    n1,n2,th=1.0,pk(1.33,1.5,1.6),pk(20,30,40,50)
    T('p-4-4',2,f'Light enters a medium n = {n2} from air at {th}°. Angle of refraction (3 s.f.)?',math.degrees(math.asin(math.sin(math.radians(th))/n2)),'°','n₁ sin θ₁ = n₂ sin θ₂.')
rep(4,f)
def f():
    d,lam=pk(1/300,1/500,1/600),pk(500,589,633)
    dm=d/1000;th=math.degrees(math.asin(lam*1e-9/dm))
    T('p-4-4',2,f'A grating with {int(round(1/d))} lines per mm, λ = {lam} nm. Angle of the first order (3 s.f.)?',th,'°','d sin θ = nλ.')
rep(3,f)
def f():
    L,f_=round(R.uniform(0.3,1.2),2),ri(100,500)
    T('p-4-4',3,f'A string {L} m long vibrates at its fundamental of {f_} Hz. Find the wave speed (3 s.f.).',2*L*f_,'m/s','λ = 2L.')
rep(3,f)
def f():
    lines,lam=pk(300,500,600),pk(500,589,633)
    d=1e-3/lines;nmax=int(d/(lam*1e-9))
    T('p-4-4',3,f'Grating {lines} lines/mm, λ = {lam} nm. Highest order visible?',nmax,'','n ≤ d/λ, round down.',0)
rep(3,f)
def f():
    I0,r=ri(20,100),pk(2,3,4)
    T('p-4-4',3,f'Intensity is {I0} W m⁻² at 1 m from a point source. Find it at {r} m (3 s.f.).',I0/r**2,'W m⁻²','Inverse square law.')
rep(2,f)
# p-4-5 quantum
def f():
    lam=ri(300,700)
    T('p-4-5',1,f'Photon energy at {lam} nm (eV, 3 s.f.)?',h*c/(lam*1e-9)/e,'eV','E = hc/λ, divide by e.')
rep(4,f)
def f():
    phi,lam=pk(2.3,2.9,4.3,4.7),pk(200,250,300)
    T('p-4-5',2,f'Work function {phi} eV, light λ = {lam} nm. Max KE of photoelectrons (eV, 3 s.f.)?',h*c/(lam*1e-9)/e-phi,'eV','KEmax = hf − φ.')
rep(4,f)
def f():
    V=pk(100,500,1000,5000)
    p=math.sqrt(2*me*e*V)
    T('p-4-5',3,f'Electrons accelerated through {V} V. de Broglie wavelength (× 10⁻¹¹ m, 3 s.f.)?',h/p/1e-11,'× 10⁻¹¹ m','λ = h/√(2meV).')
rep(4,f)
def f():
    phi=pk(2.3,2.9,4.3)
    T('p-4-5',2,f'Threshold frequency for work function {phi} eV (× 10¹⁴ Hz, 3 s.f.)?',phi*e/h/1e14,'× 10¹⁴ Hz','f₀ = φ/h.')
rep(3,f)
def f():
    P,lam=pk(1,5,10),pk(450,550,650)
    T('p-4-5',3,f'A {P} mW laser emits λ = {lam} nm. Photons per second (× 10¹⁵, 3 s.f.)?',P*1e-3/(h*c/(lam*1e-9))/1e15,'× 10¹⁵','N = P/E_photon.')
rep(3,f)
# p-5-1 thermal
def f():
    m,cc,dT=round(R.uniform(0.2,3),1),pk(4200,900,390,2100),ri(5,40)
    T('p-5-1',1,f'Heat {m} kg (c = {cc} J kg⁻¹ K⁻¹) by {dT} K. Energy (3 s.f.)?',m*cc*dT,'J','E = mcΔθ.')
rep(4,f)
def f():
    tc=ri(-50,150)
    T('p-5-1',1,f'Convert {tc} °C to kelvin.',tc+273,'K','Add 273.',0)
rep(2,f)
def f():
    P,t,m,dT=ri(50,200),ri(60,600),round(R.uniform(0.3,2),1),ri(5,30)
    T('p-5-1',2,f'A {P} W heater warms {m} kg by {dT} K in {t} s. Find c (no losses, 3 s.f.).',P*t/(m*dT),'J kg⁻¹ K⁻¹','Pt = mcΔθ.')
rep(3,f)
def f():
    T_=ri(250,600)
    T('p-5-1',2,f'Mean KE of a gas molecule at {T_} K (× 10⁻²¹ J, 3 s.f.)?',1.5*kB*T_/1e-21,'× 10⁻²¹ J','KE = 3/2 kT.')
rep(3,f)
def f():
    p1,V1,T1,T2=ri(100,200),ri(1,5),ri(280,320),ri(350,500)
    T('p-5-1',3,f'Gas at {p1} kPa, {T1} K is heated at constant volume to {T2} K. New pressure (3 s.f.)?',p1*T2/T1,'kPa','p/T constant.')
rep(3,f)
def f():
    T_,M=ri(250,500),pk(0.028,0.032,0.004)
    T('p-5-1',3,f'r.m.s. speed of molecules of molar mass {M} kg mol⁻¹ at {T_} K (3 s.f.)?',math.sqrt(3*Rg*T_/M),'m/s','½m c² = 3/2 kT → c = √(3RT/M).')
rep(4,f)
def f():
    m,L,cc,dT=round(R.uniform(0.1,0.5),2),3.34e5,4200,ri(10,40)
    T('p-5-1',3,f'Energy to melt {m} kg of ice at 0 °C and warm it to {dT} °C (L = 3.34 × 10⁵, c = 4200). kJ, 3 s.f.?',(m*L+m*cc*dT)/1000,'kJ','mL + mcΔθ.')
rep(3,f)
# p-5-2 circular
def f():
    T_=round(R.uniform(0.5,5),1)
    T('p-5-2',1,f'Period {T_} s. Angular velocity (3 s.f.)?',2*math.pi/T_,'rad/s','ω = 2π/T.')
rep(3,f)
def f():
    m,v,r=round(R.uniform(0.1,2),1),ri(2,20),round(R.uniform(0.5,5),1)
    T('p-5-2',2,f'{m} kg at {v} m/s in a circle of radius {r} m. Centripetal force (3 s.f.)?',m*v*v/r,'N','F = mv²/r.')
rep(4,f)
def f():
    r,rpm=round(R.uniform(0.1,0.5),2),pk(33,45,78,1200)
    w=rpm*2*math.pi/60
    T('p-5-2',2,f'A point {r} m from the centre of a disc spinning at {rpm} rpm. Find its speed (3 s.f.).',w*r,'m/s','v = ωr.')
rep(3,f)
def f():
    r=round(R.uniform(0.5,2),1)
    T('p-5-2',3,f'Minimum speed at the top of a vertical circle of radius {r} m for the string to stay taut (3 s.f.)?',math.sqrt(g*r),'m/s','mg = mv²/r.')
rep(4,f)
def f():
    m,r,v=ri(800,1500),ri(30,100),ri(10,25)
    T('p-5-2',3,f'A {m} kg car goes over a hump-backed bridge of radius {r} m at {v} m/s. Find the normal reaction at the top (3 s.f.).',m*(g-v*v/r),'N','mg − R = mv²/r.')
rep(3,f)
# p-5-3 SHM
def f():
    f_,A=round(R.uniform(0.5,5),1),round(R.uniform(0.02,0.2),2)
    T('p-5-3',1,f'SHM: f = {f_} Hz, A = {A} m. Max acceleration (3 s.f.)?',(2*math.pi*f_)**2*A,'m s⁻²','a = ω²A.')
rep(3,f)
def f():
    L=round(R.uniform(0.2,2),2)
    T('p-5-3',1,f'Simple pendulum length {L} m. Period (3 s.f.)?',2*math.pi*math.sqrt(L/g),'s','T = 2π√(L/g).')
rep(3,f)
def f():
    f_,A,x=round(R.uniform(0.5,3),1),0.10,pk(0.03,0.05,0.06,0.08)
    w=2*math.pi*f_
    T('p-5-3',2,f'SHM: f = {f_} Hz, A = 0.10 m. Speed at x = {x} m (3 s.f.)?',w*math.sqrt(A*A-x*x),'m/s','v = ω√(A² − x²).')
rep(4,f)
def f():
    m,k=round(R.uniform(0.1,1),2),ri(10,100)
    T('p-5-3',2,f'Mass {m} kg on a spring k = {k} N/m. Frequency (3 s.f.)?',1/(2*math.pi)*math.sqrt(k/m),'Hz','f = (1/2π)√(k/m).')
rep(3,f)
def f():
    m,f_,A=round(R.uniform(0.1,1),2),round(R.uniform(0.5,3),1),round(R.uniform(0.02,0.1),2)
    T('p-5-3',3,f'{m} kg oscillates in SHM, f = {f_} Hz, A = {A} m. Total energy (mJ, 3 s.f.)?',0.5*m*(2*math.pi*f_)**2*A*A*1000,'mJ','E = ½mω²A².')
rep(4,f)
def f():
    A,f_,t=round(R.uniform(0.02,0.1),2),round(R.uniform(0.5,2),1),round(R.uniform(0.1,0.4),2)
    T('p-5-3',3,f'x = A cos(ωt), A = {A} m, f = {f_} Hz. Displacement at t = {t} s (cm, 3 s.f.)?',A*math.cos(2*math.pi*f_*t)*100,'cm','Radians mode!',1)
rep(3,f)
# p-5-4 gravity
def f():
    m1,m2,r=ri(50,100),ri(50,100),round(R.uniform(0.5,3),1)
    T('p-5-4',1,f'Force between {m1} kg and {m2} kg, {r} m apart (× 10⁻⁷ N, 3 s.f.)?',G*m1*m2/r**2/1e-7,'× 10⁻⁷ N','F = Gm₁m₂/r².')
rep(3,f)
def f():
    M,r=pk((6.0e24,6.4e6),(6.4e23,3.4e6),(7.3e22,1.7e6)),None
    T('p-5-4',1,f'Surface g for M = {sci(M[0])} kg, r = {sci(M[1])} m (3 s.f.)?',G*M[0]/M[1]**2,'N/kg','g = GM/r².')
rep(3,f)
def f():
    hh=pk(400,800,2000,20000)
    r=6.4e6+hh*1000;M=6.0e24
    T('p-5-4',2,f'Orbital period of a satellite {hh} km above Earth (M = 6.0 × 10²⁴ kg, R = 6400 km). Hours, 3 s.f.?',2*math.pi*math.sqrt(r**3/(G*M))/3600,'h','T² = 4π²r³/GM.')
rep(4,f)
def f():
    M,r=6.0e24,6.4e6
    k=pk(2,3,4)
    T('p-5-4',2,f'Gravitational potential at {k}R from Earth’s centre (M = 6.0 × 10²⁴ kg, R = 6.4 × 10⁶ m). MJ/kg, 3 s.f.?',-G*M/(k*r)/1e6,'MJ/kg','V = −GM/r.')
rep(3,f)
def f():
    M,r=pk((6.0e24,6.4e6),(6.4e23,3.4e6)),None
    T('p-5-4',3,f'Escape velocity for M = {sci(M[0])} kg, R = {sci(M[1])} m (km/s, 3 s.f.)?',math.sqrt(2*G*M[0]/M[1])/1000,'km/s','½mv² = GMm/R.')
rep(3,f)
def f():
    m=ri(100,2000);M,R0=6.0e24,6.4e6;h1=pk(300,500,1000)
    T('p-5-4',3,f'Energy to lift a {m} kg satellite from Earth’s surface to {h1} km altitude (GJ, 3 s.f.)?',G*M*m*(1/R0-1/(R0+h1*1000))/1e9,'GJ','ΔE = GMm(1/R₁ − 1/R₂).')
rep(4,f)
# p-5-5 astro
def f():
    lm=ri(300,900)
    T('p-5-5',1,f'Wien: λmax = {lm} nm. Surface temperature (3 s.f.)?',2.9e-3/(lm*1e-9),'K','T = 2.9 × 10⁻³/λmax.')
rep(3,f)
def f():
    d=ri(10,500)
    T('p-5-5',1,f'Recession speed of a galaxy {d} Mpc away (H₀ = 70 km s⁻¹ Mpc⁻¹)?',70*d,'km/s','v = H₀d.',0)
rep(3,f)
def f():
    p=round(R.uniform(0.05,0.8),2)
    T('p-5-5',2,f'Parallax angle {p} arcseconds. Distance (pc, 3 s.f.)?',1/p,'pc','d = 1/p.')
rep(3,f)
def f():
    l0,dl=pk(656.3,486.1,434.0),round(R.uniform(1,15),1)
    T('p-5-5',2,f'A line at {l0} nm is observed at {l0+dl:.1f} nm. Recession speed (× 10⁶ m/s, 3 s.f.)?',dl/l0*c/1e6,'× 10⁶ m/s','Δλ/λ = v/c.')
rep(3,f)
def f():
    T_,r=ri(3000,20000),pk(0.5,1,2,5)
    Rs=6.96e8*r
    T('p-5-5',3,f'Luminosity of a star with T = {T_} K and radius {r} solar radii (R☉ = 6.96 × 10⁸ m). × 10²⁶ W, 3 s.f.?',4*math.pi*Rs**2*5.67e-8*T_**4/1e26,'× 10²⁶ W','L = 4πr²σT⁴.')
rep(4,f)
def f():
    H=pk(65,70,75)
    T('p-5-5',3,f'Estimate the age of the universe from H₀ = {H} km s⁻¹ Mpc⁻¹ (1 Mpc = 3.09 × 10²² m). Billion years, 3 s.f.?',(3.09e22/(H*1000))/3.15e7/1e9,'× 10⁹ years','t ≈ 1/H₀ in seconds.')
rep(3,f)
def f():
    E1,E2=pk((-13.6,-3.4),(-3.4,-1.51),(-13.6,-1.51))
    T('p-5-5',3,f'Electron drops from {E2} eV to {E1} eV. Wavelength of photon emitted (nm, 3 s.f.)?',h*c/((E2-E1)*e)*1e9,'nm','λ = hc/ΔE.')
rep(3,f)
# p-6-1 capacitors
def f():
    C,V=ri(10,1000),round(R.uniform(1,12),1)
    T('p-6-1',1,f'Charge on {C} µF at {V} V (mC, 3 s.f.)?',C*V/1000,'mC','Q = CV.')
rep(3,f)
def f():
    C1,C2=ri(10,100),ri(10,100)
    T('p-6-1',2,f'{C1} µF and {C2} µF in series. Combined capacitance (µF, 3 s.f.)?',1/(1/C1+1/C2),'µF','1/C = 1/C₁ + 1/C₂.')
rep(3,f)
def f():
    C,V=ri(100,4700),ri(3,24)
    T('p-6-1',1,f'Energy stored in {C} µF at {V} V (3 s.f.)?',0.5*C*1e-6*V*V,'J','½CV².')
rep(3,f)
def f():
    R_,C,t=ri(1,100),ri(10,1000),round(R.uniform(0.1,5),1)
    tau=R_*1e3*C*1e-6
    T('p-6-1',3,f'{C} µF discharges through {R_} kΩ. Fraction of charge left after {t} s (3 s.f.)?',math.exp(-t/tau),'','Q/Q₀ = e^(−t/RC).')
rep(4,f)
def f():
    R_,C,fr=ri(1,100),ri(10,1000),pk(0.5,0.25,0.1)
    tau=R_*1e3*C*1e-6
    T('p-6-1',3,f'{C} µF discharges through {R_} kΩ. Time for the pd to fall to {fr} of its initial value (3 s.f.)?',-tau*math.log(fr),'s','t = −RC ln(V/V₀).')
rep(4,f)
def f():
    A,d=round(R.uniform(0.01,0.1),3),round(R.uniform(0.5,3),1)
    T('p-6-1',2,f'Parallel plates: area {A} m², gap {d} mm, air. Capacitance (pF, 3 s.f.)?',e0*A/(d/1000)*1e12,'pF','C = ε₀A/d.')
rep(3,f)
# p-6-2 electric fields
def f():
    Q,r=round(R.uniform(1,9),1),round(R.uniform(0.05,0.5),2)
    T('p-6-2',1,f'Field strength {r} m from a {Q} µC point charge (× 10⁵ N/C, 3 s.f.)?',Q*1e-6/(4*math.pi*e0*r*r)/1e5,'× 10⁵ N/C','E = Q/4πε₀r².')
rep(3,f)
def f():
    q1,q2,r=ri(1,9),ri(1,9),round(R.uniform(0.05,0.5),2)
    T('p-6-2',2,f'Force between {q1} µC and {q2} µC, {r} m apart (3 s.f.)?',q1*q2*1e-12/(4*math.pi*e0*r*r),'N','Coulomb’s law.')
rep(4,f)
def f():
    Q,r=round(R.uniform(1,9),1),round(R.uniform(0.05,0.5),2)
    T('p-6-2',2,f'Electric potential {r} m from a {Q} nC charge (3 s.f.)?',Q*1e-9/(4*math.pi*e0*r),'V','V = Q/4πε₀r.')
rep(3,f)
def f():
    V=pk(100,500,1000,2000)
    T('p-6-2',3,f'Electron accelerated from rest through {V} V. Final speed (× 10⁷ m/s, 3 s.f.)?',math.sqrt(2*e*V/me)/1e7,'× 10⁷ m/s','eV = ½mv².')
rep(4,f)
def f():
    V,d,L,u=ri(100,500),0.02,0.05,pk(2e7,3e7)
    E=V/d;acc=e*E/me;t=L/u
    T('p-6-2',3,f'An electron enters between plates ({V} V, 2.0 cm apart, 5.0 cm long) at {u/1e7:g} × 10⁷ m/s parallel to the plates. Vertical deflection on leaving (mm, 3 s.f.)?',0.5*acc*t*t*1000,'mm','a = eV/(md), t = L/u, y = ½at².')
rep(3,f)
# p-6-3 electromagnetism
def f():
    B_,I,L=round(R.uniform(0.05,0.5),2),round(R.uniform(0.5,5),1),round(R.uniform(0.05,0.5),2)
    T('p-6-3',1,f'Force on {L} m of wire, {I} A, perpendicular to {B_} T (3 s.f.)?',B_*I*L,'N','F = BIL.')
rep(3,f)
def f():
    B_,v=round(R.uniform(0.01,0.5),2),ri(1,9)*1e5
    T('p-6-3',1,f'Force on a proton at {v/1e5:g} × 10⁵ m/s perpendicular to {B_} T (× 10⁻¹⁵ N, 3 s.f.)?',B_*e*v/1e-15,'× 10⁻¹⁵ N','F = BQv.')
rep(3,f)
def f():
    N_,B1,A,t=ri(50,500),round(R.uniform(0.1,0.8),2),round(R.uniform(0.001,0.01),3),round(R.uniform(0.05,0.5),2)
    T('p-6-3',2,f'A {N_}-turn coil of area {A} m² in {B1} T is pulled out of the field in {t} s. Average emf (3 s.f.)?',N_*B1*A/t,'V','ε = NΔΦ/Δt.')
rep(4,f)
def f():
    Np,Ns,Vp=ri(100,2000),ri(20,500),pk(230,120,12)
    T('p-6-3',2,f'Transformer {Np}:{Ns} turns, primary {Vp} V. Secondary voltage (3 s.f.)?',Vp*Ns/Np,'V','Vs/Vp = Ns/Np.')
rep(3,f)
def f():
    B_,V=round(R.uniform(0.001,0.01),4),pk(100,200,500)
    v=math.sqrt(2*e*V/me)
    T('p-6-3',3,f'Electrons accelerated through {V} V enter {B_*1000:g} mT at right angles. Radius of path (cm, 3 s.f.)?',me*v/(e*B_)*100,'cm','v from eV = ½mv², then r = mv/BQ.')
rep(4,f)
def f():
    B_,L,v=round(R.uniform(0.1,0.5),2),round(R.uniform(0.1,1),1),ri(2,10)
    T('p-6-3',3,f'A {L} m rod moves at {v} m/s perpendicular to {B_} T. Induced emf (3 s.f.)?',B_*L*v,'V','ε = BLv.')
rep(3,f)
# p-6-4 nuclear
def f():
    t12,t=ri(2,30),None
    n=pk(2,3,4);t=t12*n
    T('p-6-4',1,f'Half-life {t12} days. Fraction left after {t} days?',0.5**n,'','(½)ⁿ.',0)
rep(3,f)
def f():
    t12=pk(5.27,8.0,30.0,1600)
    T('p-6-4',2,f'Half-life {t12} years. Decay constant (y⁻¹, 3 s.f.)?',math.log(2)/t12,'y⁻¹','λ = ln 2/t½.')
rep(3,f)
def f():
    A0,t12,t=ri(200,900),ri(2,10),ri(3,20)
    T('p-6-4',2,f'Activity {A0} Bq, half-life {t12} h. Activity after {t} h (3 s.f.)?',A0*math.exp(-math.log(2)/t12*t),'Bq','A = A₀e^(−λt).')
rep(4,f)
def f():
    dm=round(R.uniform(0.01,0.3),3)
    T('p-6-4',2,f'Mass defect {dm} u. Binding energy (MeV, 3 s.f.)? (1 u = 931.5 MeV)',dm*931.5,'MeV','× 931.5.')
rep(3,f)
def f():
    t12,N0=pk((5730,'carbon-14'),(28.8,'Sr-90')),None
    fr=pk(0.25,0.4,0.6,0.8)
    T('p-6-4',3,f'A sample of {t12[1]} (half-life {t12[0]} y) has {int(fr*100)}% of its original activity. Age (y, 3 s.f.)?',-math.log(fr)/(math.log(2)/t12[0]),'y','t = ln(A₀/A)/λ.')
rep(4,f)
def f():
    m=round(R.uniform(1,10),1);M=pk((235,7.04e8*365*24*3600,'U-235'),(239,24100*3.15e7,'Pu-239'))
    Nn=m/1000/(M[0]*1.661e-27);lam=math.log(2)/M[1]
    T('p-6-4',3,f'Activity of {m} g of {M[2]} (half-life {M[1]/3.15e7:.3g} y; 1 y = 3.15 × 10⁷ s). MBq, 3 s.f.?',lam*Nn/1e6,'MBq','N = m/(A × u), A = λN.')
rep(3,f)
# p-6-5 medical
def f():
    mu,x=round(R.uniform(0.1,1),2),round(R.uniform(0.5,5),1)
    T('p-6-5',1,f'X-ray attenuation μ = {mu} cm⁻¹. Fraction transmitted through {x} cm (3 s.f.)?',math.exp(-mu*x),'','I/I₀ = e^(−μx).')
rep(4,f)
def f():
    mu=round(R.uniform(0.1,1),2)
    T('p-6-5',2,f'Half-value thickness for μ = {mu} cm⁻¹ (cm, 3 s.f.)?',math.log(2)/mu,'cm','x½ = ln 2/μ.')
rep(3,f)
def f():
    rho,v=pk((1000,1500),(1060,1580),(1900,4080)),None
    T('p-6-5',1,f'Acoustic impedance: ρ = {rho[0]} kg m⁻³, c = {rho[1]} m/s (× 10⁶ kg m⁻² s⁻¹, 3 s.f.)?',rho[0]*rho[1]/1e6,'× 10⁶','Z = ρc.')
rep(3,f)
def f():
    Z1,Z2=pk((1.5,1.7),(1.6,7.8),(0.0004,1.6)),None
    T('p-6-5',3,f'Intensity reflection coefficient between Z₁ = {Z1[0]} and Z₂ = {Z1[1]} (× 10⁶ units). (3 s.f.)?',((Z1[1]-Z1[0])/(Z1[1]+Z1[0]))**2,'','(Z₂ − Z₁)²/(Z₂ + Z₁)².')
rep(4,f)
def f():
    t,v=ri(20,200),1540
    T('p-6-5',3,f'An ultrasound echo returns after {t} µs in tissue (c = 1540 m/s). Depth of the boundary (cm, 3 s.f.)?',v*t*1e-6/2*100,'cm','Distance = ct/2.')
rep(4,f)
def f():
    f_,v=pk(2,3.5,5),1540
    T('p-6-5',2,f'Ultrasound at {f_} MHz in tissue (c = 1540 m/s). Wavelength (mm, 3 s.f.)?',v/(f_*1e6)*1000,'mm','λ = c/f.')
rep(3,f)
