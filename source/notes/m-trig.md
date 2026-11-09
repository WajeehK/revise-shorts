@spec Edexcel 9MA0 Pure topic 5: 5.1–5.9 (sine and cosine rules, radians, small-angle approximations, trig graphs, reciprocal and inverse functions, identities, compound and double angles, R-form, solving equations, proof and modelling)
@intro Trigonometry runs from triangle calculations at GCSE all the way to identities and R-form at A level. This topic covers each stage: triangles, radians, graphs, reciprocal and inverse functions, identities, compound angles and solving equations.
# Triangles
:::eq
$$\frac{a}{\sin A}=\frac{b}{\sin B}\qquad a^2=b^2+c^2-2bc\cos A\qquad\text{Area}=\tfrac12ab\sin C$$
:::
- Use the **sine rule** when you know a side and its opposite angle. Use the **cosine rule** when you have two sides and the included angle, or all three sides.
- **Ambiguous case:** when you use the sine rule to find an angle, $\sin\theta=k$ has two possible solutions, $\theta$ and $180°-\theta$. Check whether both give a valid triangle.
:::ex Cosine rule
Q: In triangle $ABC$, $b=7$, $c=5$ and $A=60°$. Find $a$.
1. $a^2=49+25-2(7)(5)(\tfrac12)=39$.
A: $a=\sqrt{39}\approx6.24$
:::
# Radians, arcs and sectors
- $\pi$ radians $=180°$. In radians, **arc length** is $s=r\theta$ and **sector area** is $A=\frac12r^2\theta$.
- **Small-angle approximations** (A level, with $\theta$ in radians): $\sin\theta\approx\theta$, $\tan\theta\approx\theta$ and $\cos\theta\approx1-\frac{\theta^2}{2}$.
:::ex Segment area
Q: A sector has radius 6 cm and angle $\frac{\pi}{3}$. Find the area of the segment cut off by the chord.
1. Sector area $=\frac12(36)\frac\pi3=6\pi$.
2. Triangle area $=\frac12(36)\sin\frac\pi3=9\sqrt3$.
A: $6\pi-9\sqrt3\approx3.26$ cm²
:::
# Graphs and exact values
!fig m-unit-circle The unit circle defines sin and cos for any angle
!fig m-trig-graphs Graphs of sin, cos and tan
- $\sin$ and $\cos$ have period $360°$ ($2\pi$); $\tan$ has period $180°$, with asymptotes at $90°$, $270°$, and so on.
- Learn the exact values: $\sin30°=\frac12$, $\sin45°=\frac{\sqrt2}{2}$, $\sin60°=\frac{\sqrt3}{2}$, $\tan45°=1$ and $\tan60°=\sqrt3$.
!fig m-cast The CAST diagram shows which ratios are positive in each quadrant
# Reciprocal and inverse functions (A level)
:::def
**Secant, cosecant, cotangent:** $\sec x=\frac1{\cos x}$, $\csc x=\frac1{\sin x}$, $\cot x=\frac1{\tan x}$.
**Inverse functions:** $\arcsin$ and $\arccos$ take inputs in $[-1,1]$, and $\arctan$ takes any real input. Their ranges are restricted to $[-\frac\pi2,\frac\pi2]$, $[0,\pi]$ and $(-\frac\pi2,\frac\pi2)$ respectively.
:::
# Identities
:::eq
$$\sin^2x+\cos^2x=1\qquad\tan x=\frac{\sin x}{\cos x}\qquad1+\tan^2x=\sec^2x\qquad1+\cot^2x=\csc^2x$$
$$\sin(A\pm B)=\sin A\cos B\pm\cos A\sin B\qquad\cos(A\pm B)=\cos A\cos B\mp\sin A\sin B$$
$$\sin2A=2\sin A\cos A\qquad\cos2A=\cos^2A-\sin^2A=2\cos^2A-1=1-2\sin^2A$$
:::
- **R-form:** $a\sin x+b\cos x=R\sin(x+\alpha)$, where $R=\sqrt{a^2+b^2}$ and $\tan\alpha=\frac ba$. This gives the maximum and minimum values (which are $\pm R$) and makes equations easy to solve.
:::ex R-form
Q: Write $3\sin x+4\cos x$ as $R\sin(x+\alpha)$, and give its maximum value.
1. $R=\sqrt{9+16}=5$.
2. $R\cos\alpha=3$ and $R\sin\alpha=4$, so $\tan\alpha=\frac43$ and $\alpha=53.1°$.
A: $5\sin(x+53.1°)$, which has a maximum of 5, when $x=36.9°$.
:::
# Solving equations
1. Use identities to rewrite the equation in terms of a single trig function, often as a quadratic.
2. Find the principal value with the calculator's inverse function.
3. Use the graph or CAST to find every solution in the given range. Adjust the range first if the angle is $2x$ or $x+30°$.
:::ex Quadratic in cos
Q: Solve $2\sin^2x=3\cos x$ for $0\le x<360°$.
1. $2(1-\cos^2x)=3\cos x$, so $2\cos^2x+3\cos x-2=0$.
2. $(2\cos x-1)(\cos x+2)=0$. $\cos x=-2$ is impossible, so $\cos x=\frac12$.
A: $x=60°$ or $x=300°$
:::
:::ex Double angle
Q: Solve $\sin2x=\sin x$ for $0\le x\le2\pi$.
1. $2\sin x\cos x-\sin x=0$, so $\sin x(2\cos x-1)=0$.
2. $\sin x=0$ gives $0,\pi,2\pi$. $\cos x=\frac12$ gives $\frac\pi3,\frac{5\pi}3$.
A: $x=0,\frac\pi3,\pi,\frac{5\pi}3,2\pi$
:::
- **Proving identities:** start with the more complicated side and work towards the other side. Never treat the identity as an equation by doing the same thing to both sides.
- **Modelling:** tides, daylight hours and Ferris wheels can be modelled with $h=a+b\sin(\omega t+c)$. The amplitude is $b$, the period is $\frac{2\pi}{\omega}$, and the mean level is $a$.
:::warn
- Dividing both sides by $\sin x$ or $\cos x$. This **loses solutions**, so factorise instead.
- Using degree mode when the question is in radians, or the other way round.
- Stopping at the principal value. Look for every solution in the range.
:::
:::tip
- If the angle is $2x$, double the range (e.g. $0\le2x<720°$), solve for $2x$, then halve the answers.
- The formula booklet gives the compound-angle formulae, but you must know the double-angle forms and the Pythagorean identities by heart.
:::
:::sum
- Sine and cosine rules; area $=\frac12ab\sin C$.
- Radians: $s=r\theta$, $A=\frac12r^2\theta$; small-angle approximations.
- Graphs, exact values and CAST; sec, cosec, cot and the inverse functions.
- Identities, compound and double angles, and R-form; solve by factorising and finding all solutions.
:::
