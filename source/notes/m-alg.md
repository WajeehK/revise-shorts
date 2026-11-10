@spec Edexcel 9MA0 Pure topic 2: 2.1–2.11 (indices and surds, quadratics, simultaneous equations, inequalities, polynomials and the factor theorem, graphs and transformations, partial fractions, functions, modelling)
@intro Algebra is the toolkit for the whole course. This topic covers indices and surds, quadratics and the discriminant, simultaneous equations and inequalities, polynomials, sketching and transforming graphs, the modulus function, partial fractions, and composite and inverse functions.
# Indices and surds
:::eq
$$a^m\times a^n=a^{m+n}\qquad (a^m)^n=a^{mn}\qquad a^{-n}=\frac1{a^n}\qquad a^{\frac{m}{n}}=\left(\sqrt[n]{a}\right)^m$$
:::
- **Rationalising** the denominator: multiply $\frac{1}{a+\sqrt b}$ by $\frac{a-\sqrt b}{a-\sqrt b}$, which uses the difference of two squares.
:::ex Rationalising
Q: Simplify $\dfrac{4}{3-\sqrt5}$.
1. Multiply the top and bottom by $3+\sqrt5$.
2. The denominator becomes $9-5=4$.
A: $3+\sqrt5$
:::
# Quadratics
- **Completing the square:** $ax^2+bx+c=a(x+\frac{b}{2a})^2+c-\frac{b^2}{4a}$. This gives the turning point.
- **Discriminant:** $b^2-4ac>0$ gives two real roots; $=0$ gives one repeated root; $<0$ gives no real roots.
- Equations that are quadratic in a function of $x$ can be solved the same way. For example, $x^4-5x^2+4=0$ becomes $u^2-5u+4=0$ with $u=x^2$.
:::ex Using the discriminant
Q: Find the values of $k$ for which $x^2+kx+9=0$ has no real roots.
1. We need $k^2-36<0$.
A: $-6<k<6$
:::
# Simultaneous equations and inequalities
- For a linear and a quadratic equation, use **substitution**. The discriminant of the resulting quadratic tells you whether the line crosses, touches or misses the curve.
- **Quadratic inequalities:** find the critical values, sketch the graph, and read off the region. For example, $x^2-x-6<0\Rightarrow(x-3)(x+2)<0\Rightarrow-2<x<3$.
- Regions on graphs: use a dashed line for $<$ or $>$, and a solid line for $\le$ or $\ge$.
# Polynomials and the factor theorem
- **Factor theorem:** if $f(a)=0$, then $(x-a)$ is a factor of $f(x)$.
- Use algebraic division, or comparing coefficients, to find the remaining quadratic factor.
:::ex Factorising a cubic
Q: Fully factorise $f(x)=x^3-2x^2-5x+6$.
1. $f(1)=1-2-5+6=0$, so $(x-1)$ is a factor.
2. Dividing gives $f(x)=(x-1)(x^2-x-6)$.
A: $f(x)=(x-1)(x-3)(x+2)$
:::
# Graphs and transformations
- Know the shapes of cubics, quartics, the reciprocal graphs $y=\frac{k}{x}$ and $y=\frac{k}{x^2}$ (with their asymptotes), and $y=|f(x)|$.
- **Proportion:** $y\propto x$ is a straight line through the origin; $y\propto\frac1x$ is a reciprocal curve.
!fig m-transl Translations of a graph
!fig m-stretch Stretches of a graph
| Transformation | Effect |
|---|---|
| $y=f(x)+a$ | translation by $a$ upwards |
| $y=f(x+a)$ | translation by $a$ to the **left** |
| $y=af(x)$ | vertical stretch, scale factor $a$ |
| $y=f(ax)$ | horizontal stretch, scale factor $\frac1a$ |
| $y=-f(x)$ / $y=f(-x)$ | reflection in the $x$-axis / the $y$-axis |
# The modulus function (A level)
!fig m-reflect-mod The modulus graph reflects the negative parts of the curve in the x-axis
- $y=|f(x)|$ reflects the parts below the $x$-axis up above it. $y=f(|x|)$ reflects the part for $x\ge0$ in the $y$-axis.
- To solve $|2x-1|=x+4$, consider both $2x-1=x+4$ and $-(2x-1)=x+4$, and check each solution. This gives $x=5$ or $x=-1$.
# Partial fractions (A level)
:::eq
$$\frac{px+q}{(x-a)(x-b)}=\frac{A}{x-a}+\frac{B}{x-b}\qquad\frac{\dots}{(x-a)(x-b)^2}=\frac{A}{x-a}+\frac{B}{x-b}+\frac{C}{(x-b)^2}$$
:::
:::ex Partial fractions
Q: Express $\dfrac{5x+1}{(x-1)(x+2)}$ in partial fractions.
1. $5x+1=A(x+2)+B(x-1)$.
2. At $x=1$: $6=3A$, so $A=2$. At $x=-2$: $-9=-3B$, so $B=3$.
A: $\dfrac{2}{x-1}+\dfrac{3}{x+2}$
:::
# Functions (A level)
:::def
**Function:** a mapping in which each input has exactly one output. It can be one-to-one or many-to-one.
**Composite function:** $fg(x)=f(g(x))$; apply $g$ first.
**Inverse function:** $f^{-1}$ undoes $f$. It exists only for one-to-one functions. The domain of $f^{-1}$ is the range of $f$, and its graph is the reflection of $y=f(x)$ in $y=x$.
:::
:::ex Inverse function
Q: Let $f(x)=\dfrac{3x+1}{x-2}$ for $x>2$. Find $f^{-1}(x)$.
1. Let $y=\frac{3x+1}{x-2}$. Then $y(x-2)=3x+1$, so $xy-3x=2y+1$.
2. $x=\frac{2y+1}{y-3}$.
A: $f^{-1}(x)=\dfrac{2x+1}{x-3}$ for $x>3$, because the range of $f$ is $f(x)>3$.
:::
- **Modelling:** use functions in context, for example an exponential model or a quadratic for a projectile, and comment on the model's limitations.
# Inequalities graphically and in set notation
- To interpret an inequality graphically, sketch both sides as graphs. The solution of $f(x)>g(x)$ is the set of $x$ values where the curve $y=f(x)$ lies **above** $y=g(x)$. Find the critical values where the graphs cross.
- Inequalities with brackets and fractions: expand or multiply through first. With a fraction such as $\frac{1}{x}<2$, multiply both sides by $x^2$ (which is always positive) rather than by $x$.
- Express solutions in set notation: $\{x:-2<x<3\}$ for one interval, and $\{x:x<-2\}\cup\{x:x>3\}$ for two separate regions.
- Regions in the plane: for $y>x^2-4$ and $y<x+2$, shade the region between the curves. A dashed line means a strict inequality; a solid line means $\le$ or $\ge$.
- **Manipulating polynomials.** Expanding brackets, collecting like terms, factorisation and simple algebraic division are the basic skills; the factor theorem says that if $f(a)=0$ then $(x-a)$ is a factor.
:::warn
- For $y=f(x+a)$, moving the graph to the right. It moves to the **left**.
- Dividing an inequality by a negative number without reversing the sign.
- Forgetting to state the domain of an inverse function.
:::
:::tip
- For any "sketch" question, label the intercepts, the turning points and the asymptotes with their equations.
:::
:::sum
- Index laws and rationalising; completing the square and the discriminant.
- Factor theorem; transformations; the modulus function.
- Partial fractions, including repeated factors; composite and inverse functions.
:::
