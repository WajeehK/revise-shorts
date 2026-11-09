@spec Edexcel 9MA0 Pure topic 8: 8.1–8.10 (fundamental theorem, indefinite and definite integrals, areas, standard integrals, substitution, by parts, partial fractions, differential equations)
@intro Integration is the reverse of differentiation. It finds areas, totals from rates, and solutions to differential equations. This topic covers the standard integrals, the main techniques (substitution, by parts and partial fractions), and how to set up and solve differential equations.
# The basics
- **Fundamental theorem of calculus:** integration reverses differentiation, $\int f'(x)\,dx=f(x)+c$.
- $\int x^n\,dx=\frac{x^{n+1}}{n+1}+c$, for $n\neq-1$.
- **Definite integral:** $\int_a^bf(x)\,dx=F(b)-F(a)$, which gives the signed area under the curve.
!fig m-area The definite integral as an area under a curve
- Area that lies **below** the $x$-axis gives a negative integral. Integrate each part separately and add their magnitudes.
- The **area between two curves** is $\int_a^b(\text{top}-\text{bottom})\,dx$.
:::ex Area between a curve and a line
Q: Find the area enclosed by $y=x^2$ and $y=2x$.
1. They meet where $x^2=2x$, so at $x=0$ and $x=2$.
2. Area $=\int_0^2(2x-x^2)\,dx=\left[x^2-\frac{x^3}{3}\right]_0^2=4-\frac83$.
A: $\frac43$
:::
:::ex Area partly below the axis
Q: Find the total area between $y=x(x-2)$ and the $x$-axis, for $0\le x\le3$.
1. The curve is below the axis for $0<x<2$. $\int_0^2(x^2-2x)\,dx=\left[\frac{x^3}{3}-x^2\right]_0^2=-\frac43$.
2. $\int_2^3(x^2-2x)\,dx=(9-9)-(\frac83-4)=\frac43$.
A: Total area $=\frac43+\frac43=\frac83$. A single integral from 0 to 3 would wrongly give 0.
:::
# Standard integrals (A level)
| $f(x)$ | $\int f(x)\,dx$ |
|---|---|
| $e^{kx}$ | $\frac1ke^{kx}+c$ |
| $\frac1x$ | $\ln|x|+c$ |
| $\cos kx$ | $\frac1k\sin kx+c$ |
| $\sin kx$ | $-\frac1k\cos kx+c$ |
| $\sec^2kx$ | $\frac1k\tan kx+c$ |
| $\frac{f'(x)}{f(x)}$ | $\ln|f(x)|+c$ |
- Use identities first. For example, $\sin^2x=\frac12(1-\cos2x)$, and $\tan^2x=\sec^2x-1$.
# Techniques (A level)
- **Substitution:** change the variable, and remember to change $dx$ and the limits as well.
- **By parts:** $\int u\frac{dv}{dx}\,dx=uv-\int v\frac{du}{dx}\,dx$. Choose $u$ to be the factor that gets simpler when differentiated, such as $x$ or $\ln x$.
- **Partial fractions:** split the fraction first, then integrate each term as a log.
:::ex By parts
Q: Find $\int xe^{2x}\,dx$.
1. $u=x$, so $u'=1$. $v'=e^{2x}$, so $v=\frac12e^{2x}$.
2. $\frac12xe^{2x}-\int\frac12e^{2x}\,dx$.
A: $\frac12xe^{2x}-\frac14e^{2x}+c$
:::
:::ex Substitution
Q: Use $u=1+x^2$ to find $\int_0^1\dfrac{2x}{(1+x^2)^2}\,dx$.
1. $du=2x\,dx$. The limits change: $x=0$ gives $u=1$, and $x=1$ gives $u=2$.
2. $\int_1^2u^{-2}\,du=\left[-\frac1u\right]_1^2=-\frac12+1$.
A: $\frac12$
:::
:::ex Partial fractions
Q: Find $\int\dfrac{5x+1}{(x-1)(x+2)}\,dx$.
1. $\dfrac{5x+1}{(x-1)(x+2)}=\dfrac{2}{x-1}+\dfrac{3}{x+2}$.
A: $2\ln|x-1|+3\ln|x+2|+c$
:::
## Choosing a technique
- Is it a standard result, or the **reverse chain rule**, where the derivative of an "inside" function is sitting outside? For example, $\int 2x\cos(x^2)\,dx=\sin(x^2)+c$.
- Is it a **product** of two different types of function, such as $x\sin x$ or $x^2e^x$? Use integration by parts, possibly twice.
- Is it a **rational function** with a factorisable denominator? Use partial fractions. If the top has the same or higher degree than the bottom, divide first.
- Is a substitution suggested, or does it simplify a root or a power? Then substitute.
# The trapezium rule
!fig m-trapezium The trapezium rule approximates the area with strips
:::eq
$$\int_a^by\,dx\approx\frac h2\left[y_0+2(y_1+\dots+y_{n-1})+y_n\right],\qquad h=\frac{b-a}{n}$$
:::
- It **overestimates** for a convex curve and **underestimates** for a concave one. More strips give a better approximation.
- Integration is the limit of a sum: $\int_a^by\,dx=\lim_{\delta x\to0}\sum y\,\delta x$.
# Differential equations (A level)
- **Separation of variables:** rearrange to $\int\frac1{g(y)}\,dy=\int f(x)\,dx$, integrate both sides, and use the initial conditions to find $c$.
:::ex Separating variables
Q: Solve $\dfrac{dy}{dx}=2xy$, given that $y=3$ when $x=0$.
1. $\int\frac1y\,dy=\int2x\,dx$, so $\ln|y|=x^2+c$.
2. $y=Ae^{x^2}$, and $y(0)=3$ gives $A=3$.
A: $y=3e^{x^2}$
:::
- **Forming a differential equation:** translate the words carefully. "The rate of change of $V$ is inversely proportional to $\sqrt V$" becomes $\frac{dV}{dt}=\frac{k}{\sqrt V}$. Decide the sign of $k$ from whether the quantity is increasing or decreasing.
- **Modelling with differential equations:** "the rate of decrease is proportional to $N$" becomes $\frac{dN}{dt}=-kN$. Interpret the solution in context, and comment on its limitations.
:::warn
- Forgetting $+c$ in indefinite integrals.
- Leaving the old limits in place after a substitution.
- Writing $\int\frac1x\,dx=\ln x$ without the modulus when $x$ can be negative.
:::
:::tip
- Check any indefinite integral by differentiating your answer.
:::
:::sum
- $\int x^n\,dx=\frac{x^{n+1}}{n+1}+c$; definite integrals give areas.
- Standard integrals; reverse chain rule; substitution, by parts and partial fractions.
- Trapezium rule, and integration as the limit of a sum.
- Separable differential equations and modelling.
:::
