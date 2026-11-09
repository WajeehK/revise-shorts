@spec Edexcel 9MA0 Mechanics topic 7: 7.1 language of kinematics; 7.2 graphs; 7.3 constant acceleration (suvat, including vectors); 7.4 calculus for variable acceleration; 7.5 projectiles
@intro Kinematics describes motion using displacement, velocity, acceleration and time. This topic covers motion graphs, the constant-acceleration equations, vertical motion under gravity, calculus for variable acceleration, and projectiles.
# Language and graphs
- **Distance** and **speed** are scalars. **Displacement**, **velocity** and **acceleration** are vectors. Average velocity = displacement ÷ time.
!fig k-suvat-vt Velocity–time graph: the gradient is acceleration and the area is displacement
- On a displacement–time graph, the **gradient is velocity**.
- On a velocity–time graph, the **gradient is acceleration** and the **area is displacement**. Area below the axis counts as negative displacement.
:::ex Velocity–time graph
Q: A car accelerates uniformly from rest to 12 m s⁻¹ in 4 s, travels at 12 m s⁻¹ for 10 s, then decelerates uniformly to rest in 6 s. Find the total distance.
1. Area = trapezium = $\frac12(10+20)\times12$.
A: 180 m
:::
# Constant acceleration (suvat)
:::eq
$$v=u+at\qquad s=ut+\tfrac12at^2\qquad s=\tfrac12(u+v)t\qquad v^2=u^2+2as\qquad s=vt-\tfrac12at^2$$
:::
- For **vertical motion under gravity**, $a=-9.8$ m s⁻² if up is taken as positive.
- **Vector form** (A level): $\mathbf v=\mathbf u+\mathbf at$ and $\mathbf r=\mathbf ut+\frac12\mathbf at^2$.
:::ex Ball thrown upwards
Q: A ball is thrown up at 14 m s⁻¹ from 2 m above the ground. Find its maximum height above the ground, and when it lands.
1. At the top, $v=0$: $0=196-19.6s$, so $s=10$ m. The maximum height is 12 m above the ground.
2. On landing, $s=-2$: $-2=14t-4.9t^2$, so $4.9t^2-14t-2=0$, which gives $t=\frac{14+\sqrt{196+39.2}}{9.8}$.
A: 12 m, and it lands after 2.99 s.
:::
## Two-particle problems
- When two objects move at the same time, write an expression for each one's displacement, using the **same time variable**, and set them equal to find when they meet. If one object starts later, its time is $t-t_0$.
:::ex Overtaking
Q: Car A passes a point at a constant 15 m s⁻¹. At that moment, car B starts from rest at the same point and accelerates at 2 m s⁻². When does B catch A?
1. A travels $s_A=15t$, and B travels $s_B=t^2$.
2. $t^2=15t$, so $t=15$ s ($t=0$ is the start).
A: After 15 s, when both have travelled 225 m.
:::
# Variable acceleration (calculus)
:::eq
$$v=\frac{ds}{dt}\qquad a=\frac{dv}{dt}=\frac{d^2s}{dt^2}\qquad s=\int v\,dt\qquad v=\int a\,dt$$
:::
- Find the constants of integration from the initial conditions. The maximum displacement occurs where $v=0$.
- In vector form (A level), differentiate or integrate the $\mathbf i$ and $\mathbf j$ components separately.
:::ex Calculus kinematics
Q: $v=6t-3t^2$ m s⁻¹. Find the acceleration at $t=2$, and the displacement from $t=0$ to $t=2$.
1. $a=6-6t$, so at $t=2$, $a=-6$ m s⁻².
2. $s=\int_0^2(6t-3t^2)\,dt=[3t^2-t^3]_0^2=12-8$.
A: $a=-6$ m s⁻² and $s=4$ m
:::
- **When to use calculus:** if the acceleration (or velocity) is given as a function of $t$, the suvat equations do not apply. Look for phrases like "at time $t$ seconds, the velocity is…".
- To find the **distance** travelled (rather than the displacement) when the particle changes direction, find where $v=0$, integrate each part separately, and add the magnitudes.
# Projectiles (A level)
- Treat the horizontal and vertical motions separately. Horizontally, the velocity $u\cos\theta$ is **constant**. Vertically, the initial velocity is $u\sin\theta$ and $a=-g$.
- Time of flight (back to the same level): $\frac{2u\sin\theta}{g}$. Maximum height: $\frac{u^2\sin^2\theta}{2g}$. Range: $\frac{u^2\sin2\theta}{g}$, which is greatest when $\theta=45°$.
:::ex Projectile
Q: A ball is kicked at 20 m s⁻¹ at 30° above the horizontal. Find its time of flight and its range.
1. $u_y=10$ m s⁻¹, so $t=\frac{2\times10}{9.8}=2.04$ s.
2. $u_x=17.32$ m s⁻¹, so the range $=17.32\times2.04$.
A: 2.04 s and 35.3 m
:::
:::warn
- Mixing up signs. Choose a positive direction and keep to it.
- Using suvat with variable acceleration. Use calculus instead.
- Forgetting the starting height in vertical-motion problems.
:::
:::tip
- Write "s = , u = , v = , a = , t = " and fill in the known values. Pick the equation that leaves out the unknown you don't need.
:::
:::sum
- On graphs: gradient and area.
- suvat for constant acceleration, including vectors; $g=9.8$ m s⁻² downwards.
- Calculus for variable acceleration.
- Projectiles: the horizontal and vertical components are independent.
:::
