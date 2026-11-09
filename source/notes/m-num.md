@spec Edexcel 9MA0 Pure topic 9: 9.1 locating roots by sign change; 9.2 iteration; 9.3 Newton–Raphson; 9.4 numerical integration; 9.5 applications
@intro Many equations cannot be solved exactly, so we use numerical methods to approximate their roots to any accuracy we need. This topic covers sign changes, fixed-point iteration, the Newton–Raphson method and their limitations.
# Locating roots by a change of sign
- If $f(x)$ is **continuous** on $[a,b]$, and $f(a)$ and $f(b)$ have opposite signs, then there is at least one root between $a$ and $b$.
- **When this fails:** a repeated root (the curve touches the axis without crossing it), several roots in the interval that cancel out the sign change, or a discontinuity such as an asymptote (e.g. $f(x)=\frac1x$ changes sign across $x=0$ but has no root there).
:::ex Showing a root lies in an interval
Q: Show that $f(x)=x^3-2x-5$ has a root between 2 and 3.
1. $f(2)=8-4-5=-1<0$.
2. $f(3)=27-6-5=16>0$.
A: There is a change of sign and $f$ is continuous, so there is a root in $(2,3)$.
:::
- **To show that a root is correct to a given accuracy,** for example $\alpha=2.09$ to 2 d.p., check the sign of $f(2.085)$ and $f(2.095)$. A sign change between these bounds confirms the rounding.
# Fixed-point iteration
- Rearrange $f(x)=0$ into the form $x=g(x)$, then iterate $x_{n+1}=g(x_n)$ from a starting value $x_0$.
- The sequence **converges** if $|g'(x)|<1$ near the root. Convergence can be a **staircase** (when $0<g'<1$) or a **cobweb** (when $-1<g'<0$) on the diagram of $y=x$ and $y=g(x)$.
- A different rearrangement may **diverge**, even with the same starting value.
:::ex Iteration
Q: Use $x_{n+1}=\sqrt[3]{2x_n+5}$ with $x_0=2$ to find the root of $x^3-2x-5=0$ to 3 d.p.
1. $x_1=\sqrt[3]{9}=2.0801$, $x_2=2.0924$, $x_3=2.0942$, $x_4=2.0945$, $x_5=2.0945$.
2. Check: $f(2.0945)<0$ and $f(2.0955)>0$.
A: $x=2.095$ (3 d.p.)
:::
# The Newton–Raphson method
!fig m-newton Newton–Raphson follows the tangent down to the x-axis
:::eq
$$x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}$$
:::
- Geometrically, each step follows the **tangent** at $x_n$ down to where it crosses the $x$-axis.
- **Failure:** if $f'(x_n)$ is close to 0 (near a stationary point), the tangent is almost horizontal, so the next estimate jumps far away. If $f'(x_n)=0$, the method cannot be used at all.
:::ex Newton–Raphson
Q: Use Newton–Raphson with $x_0=2$ on $f(x)=x^3-2x-5$ to find $x_1$ and $x_2$.
1. $f'(x)=3x^2-2$, so $x_1=2-\frac{-1}{10}=2.1$.
2. $f(2.1)=0.061$ and $f'(2.1)=11.23$, so $x_2=2.1-0.00543=2.0946$.
A: $x_1=2.1$ and $x_2=2.0946$, which converges much faster than fixed-point iteration.
:::
# Numerical integration and applications
- The **trapezium rule** gives an approximate value for a definite integral (see the Integration topic). Increasing the number of strips improves the accuracy.
- **Applications:** use these methods when an equation comes from a model and cannot be solved algebraically. Examples are the time when two populations are equal, or when a projectile hits a sloped hill.
- Always interpret the root in context, and give an appropriate level of accuracy.
:::ex Using a root in context
Q: The height of a ball is $h=20-5t^2+\ln(t+1)$. Show that it lands between $t=2.0$ and $t=2.1$.
1. $h(2.0)=20-20+\ln3=1.10>0$.
2. $h(2.1)=20-22.05+\ln3.1=-0.92<0$.
A: There is a sign change and $h$ is continuous, so the ball lands (h = 0) for $2.0<t<2.1$.
:::
:::warn
- Concluding "root found" from a sign change without stating that the function is **continuous**.
- Rounding the intermediate iterates too early. Keep full calculator values, using the ANS key.
- Using a Newton–Raphson start point near a turning point.
:::
:::tip
- Learn the conclusion sentence: "There is a change of sign and $f$ is continuous on the interval, therefore there is a root in the interval."
- On a staircase or cobweb diagram, start on the $x$-axis at $x_0$, go vertically to the curve, then horizontally to $y=x$, and repeat.
:::
:::sum
- A sign change on a continuous function gives a root. Watch for repeated roots and asymptotes.
- Iteration $x_{n+1}=g(x_n)$ converges if $|g'|<1$; it shows as a staircase or cobweb.
- Newton–Raphson: $x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}$. It fails if $f'\approx0$.
:::
