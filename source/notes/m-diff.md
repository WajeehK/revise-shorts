@spec Edexcel 9MA0 Pure topic 7: 7.1–7.6 (first principles, standard derivatives, chain/product/quotient rules, tangents and normals, stationary points, convexity, implicit and parametric differentiation, connected rates of change)
@intro Differentiation measures how fast one quantity changes compared with another, which is the gradient of a curve. This topic covers the derivative from first principles, the standard results and rules, and their uses: tangents, stationary points, convexity and rates of change.
# The derivative
- The **gradient of a curve** at a point is the gradient of the tangent there.
- **Differentiation from first principles:**
$$f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$$
:::ex First principles
Q: Prove from first principles that the derivative of $x^2$ is $2x$.
1. $\frac{(x+h)^2-x^2}{h}=\frac{2xh+h^2}{h}=2x+h$.
2. As $h\to0$, this tends to $2x$.
A: $\frac{d}{dx}(x^2)=2x$ ∎
:::
# Standard derivatives
| $f(x)$ | $f'(x)$ |
|---|---|
| $x^n$ | $nx^{n-1}$ |
| $e^{kx}$ | $ke^{kx}$ |
| $\ln x$ | $\frac1x$ |
| $a^{kx}$ | $ka^{kx}\ln a$ |
| $\sin kx$ | $k\cos kx$ |
| $\cos kx$ | $-k\sin kx$ |
| $\tan kx$ | $k\sec^2kx$ |
- The derivatives of $\sec x$, $\csc x$ and $\cot x$ are given in the formula booklet.
- The trig results are only true when $x$ is in **radians**. They are proved from first principles using the small-angle approximations, which hold only in radians.
- **Rewrite before differentiating.** Turn roots into powers and split fractions: for example, $\frac{3}{\sqrt x}=3x^{-1/2}$, and $\frac{x^2+1}{x}=x+x^{-1}$.
# Chain, product and quotient rules (A level)
:::eq
$$\frac{dy}{dx}=\frac{dy}{du}\frac{du}{dx}\qquad (uv)'=u'v+uv'\qquad\left(\frac uv\right)'=\frac{u'v-uv'}{v^2}$$
:::
:::ex Product rule
Q: Differentiate $y=x^2e^{3x}$.
1. Let $u=x^2$ and $v=e^{3x}$. Then $u'=2x$ and $v'=3e^{3x}$.
A: $\dfrac{dy}{dx}=2xe^{3x}+3x^2e^{3x}=xe^{3x}(2+3x)$
:::
# Tangents, normals and stationary points
!fig m-tangent-normal The tangent and the normal at a point on a curve
- **Tangent:** $y-y_1=m(x-x_1)$, with $m=f'(x_1)$. The **normal** has gradient $-\frac1m$.
- **Stationary points** are where $\frac{dy}{dx}=0$. If $\frac{d^2y}{dx^2}>0$ it is a **minimum**; if $\frac{d^2y}{dx^2}<0$ it is a **maximum**. If it equals 0, check the gradient on either side.
- A function is **increasing** where $f'(x)>0$ and decreasing where $f'(x)<0$.
- A curve is **concave** where $f''(x)<0$ and **convex** where $f''(x)>0$. A **point of inflection** is where $f''(x)$ changes sign.
!fig m-stationary Maximum, minimum and inflection points
:::ex Stationary points
Q: Find and classify the stationary points of $y=x^3-3x^2-9x+5$.
1. $\frac{dy}{dx}=3x^2-6x-9=3(x-3)(x+1)=0$, so $x=3$ or $x=-1$.
2. $\frac{d^2y}{dx^2}=6x-6$. At $x=3$ this is $12>0$, so a minimum, at $(3,-22)$. At $x=-1$ this is $-12<0$, so a maximum, at $(-1,10)$.
A: Maximum at $(-1,10)$ and minimum at $(3,-22)$.
:::
# Implicit and parametric differentiation (A level)
- **Implicit:** differentiate every term with respect to $x$, using $\frac{d}{dx}(y^n)=ny^{n-1}\frac{dy}{dx}$ and the product rule for terms like $xy$.
- **Parametric:** $\dfrac{dy}{dx}=\dfrac{dy/dt}{dx/dt}$.
:::ex Implicit
Q: Find $\frac{dy}{dx}$ for $x^2+xy+y^2=7$, and the gradient at $(1,2)$.
1. $2x+y+x\frac{dy}{dx}+2y\frac{dy}{dx}=0$.
2. $\frac{dy}{dx}=-\frac{2x+y}{x+2y}$. At $(1,2)$ this is $-\frac45$.
A: $\dfrac{dy}{dx}=-\dfrac{2x+y}{x+2y}$, and the gradient is $-\frac45$.
:::
# Connected rates of change (A level)
- Link the rates with the chain rule, e.g. $\frac{dV}{dt}=\frac{dV}{dr}\times\frac{dr}{dt}$.
:::ex Expanding balloon
Q: A spherical balloon's volume increases at 50 cm³ s⁻¹. How fast is the radius increasing when $r=5$ cm?
1. $V=\frac43\pi r^3$, so $\frac{dV}{dr}=4\pi r^2=100\pi$.
2. $\frac{dr}{dt}=\frac{50}{100\pi}$.
A: $\frac{1}{2\pi}\approx0.159$ cm s⁻¹
:::
:::ex Optimisation
Q: A rectangular field is fenced on three sides with 100 m of fencing, and a wall forms the fourth side. Find the maximum area.
1. Let the two sides perpendicular to the wall be $x$. Then the side parallel to it is $100-2x$, and $A=x(100-2x)=100x-2x^2$.
2. $\frac{dA}{dx}=100-4x=0$, so $x=25$. Since $\frac{d^2A}{dx^2}=-4<0$, this is a maximum.
A: The maximum area is $25\times50=1250$ m².
:::
- Real-world uses: maximising area or profit, and minimising cost or material. Always check that your answer is a maximum or minimum, and that it makes sense in context.
# Constructing differential equations (A level)
- A rate of change statement becomes a differential equation. "The rate of growth of a population $P$ is proportional to its size" gives $\frac{dP}{dt}=kP$.
- In kinematics, $\frac{dv}{dt}$ is acceleration: "the deceleration is proportional to the square of the speed" gives $\frac{dv}{dt}=-kv^2$.
- In economics, modelling the relationship between price and demand: "the rate of change of demand $D$ with price $p$ is inversely proportional to $p$" gives $\frac{dD}{dp}=-\frac{k}{p}$.
- Pure mathematics examples: "the gradient at any point is twice the $x$ coordinate times $y$" gives $\frac{dy}{dx}=2xy$.
- **Rational powers.** Differentiate $x^n$ for any rational $n$, with constant multiples, sums and differences: $\frac{d}{dx}\left(4x^{\frac32}-3x^{-1}\right)=6x^{\frac12}+3x^{-2}$.
:::warn
- Forgetting the $\frac{dy}{dx}$ when differentiating $y$ terms implicitly.
- Using degrees when differentiating trig functions. Calculus always needs **radians**.
- Classifying a point with $f''(x)=0$ as a point of inflection without checking for a sign change.
:::
:::tip
- For optimisation questions: write the quantity in terms of a single variable, differentiate, set the result to 0, solve, then confirm with the second derivative.
:::
:::sum
- First principles: $f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$.
- Standard derivatives; the chain, product and quotient rules.
- Tangents, normals, stationary points and convexity.
- Implicit and parametric differentiation; connected rates of change.
:::
