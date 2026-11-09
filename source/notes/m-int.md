# Standard results
$$\int x^n\,dx=\frac{x^{n+1}}{n+1}+c\ (n\neq-1)$$
$$\int\frac1x\,dx=\ln|x|+c$$
$$\int e^{kx}dx=\tfrac1ke^{kx}+c$$
$$\int\cos kx\,dx=\tfrac1k\sin kx+c$$
$$\int\sin kx\,dx=-\tfrac1k\cos kx+c$$
- $\int\frac{f'(x)}{f(x)}dx=\ln|f(x)|+c$, and $\int\sec^2kx\,dx=\frac1k\tan kx+c$.
# Techniques
- **Substitution:** change $dx$ **and** the limits.
- **By parts:** $\int u\frac{dv}{dx}dx=uv-\int v\frac{du}{dx}dx$. Choose $u$ to be the factor that simplifies when differentiated (but take $u=\ln x$).
- **Partial fractions** for rational functions.
- Trig identities, e.g. $\cos^2x=\frac12(1+\cos2x)$.
# Areas and differential equations
- The area between curve and $x$-axis is $\int_a^b y\,dx$. Regions below the axis give negative values, so split them up.
- Area between curves: $\int(\text{top}-\text{bottom})\,dx$.
- Separable DE: $\frac{dy}{dx}=f(x)g(y) \Rightarrow \int\frac1{g(y)}dy=\int f(x)\,dx$. Use the initial conditions to find $c$.
- Trapezium rule: $\int_a^b y\,dx\approx\frac h2\left[y_0+2(y_1+\dots+y_{n-1})+y_n\right]$, where $h=\frac{b-a}n$.
!fig m-area
!fig m-trapezium
# Worked example
$\displaystyle\int_1^e x\ln x\,dx$: take $u=\ln x$, $v'=x$. Then
$$\left[\tfrac{x^2}2\ln x\right]_1^e-\int_1^e\tfrac x2\,dx=\tfrac{e^2}2-\tfrac{e^2-1}4=\tfrac{e^2+1}4$$
# Exam tips
> Don't forget $+c$ on indefinite integrals, and the modulus in $\ln|x|$.
- Trapezium rule: an overestimate if the curve is convex, an underestimate if concave.
