## m-proof
### Key ideas
- **Proof by deduction:** start from known facts and use logical steps to reach the statement in general.
- **Proof by exhaustion:** split into a finite set of cases and check every one (e.g. $n$ even / $n$ odd, or $n \equiv 0,1,2 \pmod 3$).
- **Disproof by counter-example:** a single case where the statement fails is enough.
- **Proof by contradiction:** assume the statement is false, then show this leads to something impossible.
### Useful forms
- Even: $2k$; odd: $2k+1$; consecutive integers: $n,\ n+1$; rational: $\frac{a}{b}$ with $a,b \in \mathbb{Z}$, $b \neq 0$, no common factors.
- Completing the square proves positivity: $x^2-6x+10=(x-3)^2+1>0$ for all real $x$.
### Classic proofs
- **$\sqrt{2}$ is irrational:** assume $\sqrt2=\frac ab$ in lowest terms. Then $a^2=2b^2$, so $a$ is even, $a=2c$, giving $b^2=2c^2$, so $b$ is even too, contradicting "lowest terms".
- **Infinitely many primes:** assume finitely many, $p_1,\dots,p_n$. Then $N=p_1p_2\cdots p_n+1$ leaves remainder 1 when divided by every $p_i$. So $N$ is prime or has a prime factor not in the list. Contradiction.
### Worked example
Prove that the sum of any three consecutive integers is divisible by 3.
$$n+(n+1)+(n+2)=3n+3=3(n+1)$$
$3(n+1)$ is a multiple of 3, so the result holds for all integers $n$.
### Exam tips
> Write a concluding sentence that restates what has been proved, e.g. "…therefore it is divisible by 3".
- In contradiction proofs, state clearly what you are assuming and where the contradiction is.
- A list of examples is **not** a proof (unless it is exhaustion over *all* cases).

## m-alg
### Indices and surds
- $a^m a^n=a^{m+n}$, $\ (a^m)^n=a^{mn}$, $\ a^{-n}=\frac1{a^n}$, $\ a^{\frac mn}=(\sqrt[n]a)^m$.
- Rationalise: $\dfrac{1}{\sqrt a+\sqrt b}=\dfrac{\sqrt a-\sqrt b}{a-b}$.
### Quadratics
- Discriminant $b^2-4ac$: $>0$ two real roots, $=0$ one repeated root, $<0$ no real roots.
- Completed square $a(x+p)^2+q$ gives the turning point $(-p,\,q)$.
$$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$
### Inequalities
- For a quadratic inequality, find the critical values and sketch. E.g. $x^2-x-6<0 \Rightarrow -2<x<3$.
- Multiplying or dividing by a negative number reverses the inequality sign.
### Polynomials
- **Factor theorem:** $f(a)=0 \iff (x-a)$ is a factor.
- Algebraic division (or comparing coefficients) gives the other factor.
### Functions
- Composite $fg(x)=f(g(x))$: apply $g$ first.
- Inverse $f^{-1}$: swap $x$ and $y$ and rearrange. Its graph is the reflection of $f$ in $y=x$. Domain of $f^{-1}$ = range of $f$.
- Modulus: solve $|f(x)|=k$ using $f(x)=\pm k$, and check graphically.
- Transformations: $f(x)+a$ is up $a$; $f(x+a)$ is left $a$; $af(x)$ stretches vertically by factor $a$; $f(ax)$ stretches horizontally by factor $\frac1a$.
!fig m-transl
!fig m-stretch
!fig m-reflect-mod
### Partial fractions
$$\frac{5x+1}{(x-1)(x+2)}=\frac{A}{x-1}+\frac{B}{x+2}$$
Put $x=1$: $6=3A$, so $A=2$. Put $x=-2$: $-9=-3B$, so $B=3$.
- For a repeated factor $(x-a)^2$ use $\frac{A}{x-a}+\frac{B}{(x-a)^2}$.
### Exam tips
> For "show that" questions, every step must be visible. Don't jump straight to the given answer.
- State the domain and range when asked about $f^{-1}$. Many marks are lost here.

## m-coord
### Straight lines
- Gradient $m=\frac{y_2-y_1}{x_2-x_1}$; line $y-y_1=m(x-x_1)$.
- Parallel lines have equal gradients. Perpendicular lines have $m_1m_2=-1$.
- Midpoint $\left(\frac{x_1+x_2}2,\frac{y_1+y_2}2\right)$; distance $\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$.
### Circles
$$(x-a)^2+(y-b)^2=r^2$$
- Centre $(a,b)$, radius $r$. Complete the square to convert $x^2+y^2+2fx+2gy+c=0$.
- A tangent is perpendicular to the radius at the point of contact.
- A perpendicular from the centre to a chord bisects the chord.
- The angle in a semicircle is $90^\circ$, so a right-angled triangle's hypotenuse is a diameter.
- Line meets circle: substitute, then use the discriminant ($>0$ two points, $=0$ tangent, $<0$ none).
!fig m-circle
### Parametric equations
- $x=f(t)$, $y=g(t)$. To get the Cartesian form, eliminate $t$, e.g. using $\sin^2t+\cos^2t=1$.
- Example: $x=3\cos t$, $y=3\sin t$ gives $x^2+y^2=9$.
### Worked example
Find the tangent to $x^2+y^2-4x+6y-12=0$ at $(5,1)$.
Centre $(2,-3)$, so the radius gradient is $\frac{1-(-3)}{5-2}=\frac43$. The tangent gradient is $-\frac34$:
$$y-1=-\tfrac34(x-5)\ \Rightarrow\ 3x+4y-19=0$$
### Exam tips
- Give the line in the form the question asks for (e.g. $ax+by+c=0$ with integers).
- Watch your signs: in $(x-a)^2$ the centre is at $+a$.

## m-seq
### Binomial expansion
$$(a+b)^n=\sum_{r=0}^{n}\binom nr a^{n-r}b^r$$
- For any rational $n$: $(1+x)^n=1+nx+\frac{n(n-1)}{2!}x^2+\dots$, valid for $|x|<1$.
- For $(a+bx)^n$, first take out $a^n$: $a^n\left(1+\frac bax\right)^n$, valid for $|x|<\left|\frac ab\right|$.
### Arithmetic sequences
$$u_n=a+(n-1)d$$
$$S_n=\tfrac n2\left[2a+(n-1)d\right]=\tfrac n2(a+l)$$
### Geometric sequences
$$u_n=ar^{n-1}$$
$$S_n=\frac{a(1-r^n)}{1-r}$$
$$S_\infty=\frac a{1-r}\ \ (|r|<1)$$
### Other sequences
- Recurrence $u_{n+1}=f(u_n)$: increasing, decreasing or **periodic** (repeats with some order $k$).
- Sigma notation: $\sum_{r=1}^{n}1=n$. Watch the start value.
### Worked example
A geometric series has $u_2=12$ and $S_\infty=64$. Find $r$.
$ar=12$ and $\frac a{1-r}=64$, so $12=64r(1-r)$. This gives $16r^2-16r+3=0$, i.e. $(4r-1)(4r-3)=0$, so $r=\frac14$ or $r=\frac34$.
### Exam tips
> Always state the validity range of a binomial expansion with a non-integer or negative $n$.
- When solving $S_n>k$ by logs, dividing by $\ln r$ with $r<1$ flips the inequality.

## m-trig
### Basics
- Radians: $\pi\text{ rad}=180^\circ$. Arc length $s=r\theta$; sector area $A=\frac12r^2\theta$ ($\theta$ in radians).
- Small angles: $\sin\theta\approx\theta$, $\tan\theta\approx\theta$, $\cos\theta\approx1-\frac{\theta^2}2$.
- Sine rule $\frac a{\sin A}=\frac b{\sin B}$ (watch for the ambiguous case). Cosine rule $a^2=b^2+c^2-2bc\cos A$. Area $\frac12ab\sin C$.
!fig m-unit-circle
!fig m-trig-graphs
!fig m-cast
### Identities
$$\sin^2\theta+\cos^2\theta=1$$
$$1+\tan^2\theta=\sec^2\theta$$
$$1+\cot^2\theta=\csc^2\theta$$
$$\sin(A\pm B)=\sin A\cos B\pm\cos A\sin B$$
$$\cos(A\pm B)=\cos A\cos B\mp\sin A\sin B$$
$$\sin2A=2\sin A\cos A$$
$$\cos2A=1-2\sin^2A=2\cos^2A-1$$
$$\tan2A=\frac{2\tan A}{1-\tan^2A}$$
### Harmonic form
$a\sin\theta+b\cos\theta=R\sin(\theta+\alpha)$, where $R=\sqrt{a^2+b^2}$ and $\tan\alpha=\frac ba$.
- Max value $R$, min value $-R$. Use it to solve equations and find extrema.
### Inverse trig
- $\arcsin$: domain $[-1,1]$, range $[-\frac\pi2,\frac\pi2]$. $\arccos$: range $[0,\pi]$. $\arctan$: range $(-\frac\pi2,\frac\pi2)$.
### Worked example
Solve $2\cos^2x=1+\sin x$ for $0\le x<2\pi$.
$2(1-\sin^2x)=1+\sin x \Rightarrow 2\sin^2x+\sin x-1=0 \Rightarrow (2\sin x-1)(\sin x+1)=0$.
So $\sin x=\frac12$, giving $x=\frac\pi6,\frac{5\pi}6$; or $\sin x=-1$, giving $x=\frac{3\pi}2$.
### Exam tips
> Check the interval and units (degrees or radians). Find **all** solutions using the CAST diagram or the graph's symmetry.
- Never divide both sides by $\sin x$: you lose the solutions where $\sin x=0$. Factorise instead.

## m-exp
### Key facts
- $y=a^x$ passes through $(0,1)$. $y=e^x$ has gradient equal to its value: $\frac d{dx}e^{kx}=ke^{kx}$.
- $\log_a x=n \iff a^n=x$; $\ln x=\log_e x$.
$$\log a+\log b=\log ab$$
$$\log a-\log b=\log\tfrac ab$$
$$k\log a=\log a^k$$
- Change of base: $\log_a x=\frac{\ln x}{\ln a}$.
!fig m-exp-ln
### Modelling
- Growth/decay: $N=N_0e^{kt}$ ($k>0$ growth, $k<0$ decay).
- **Linearising:** if $y=ax^n$ then $\log y=\log a+n\log x$ (gradient $n$, intercept $\log a$). If $y=kb^x$ then $\log y=\log k+x\log b$.
### Worked example
Solve $3^{2x}-4\cdot3^x+3=0$.
Let $u=3^x$: $u^2-4u+3=0$, so $u=1$ or $u=3$, giving $x=0$ or $x=1$.
### Exam tips
> In modelling questions, interpret the constants in context (e.g. $N_0$ is the initial value) and comment on limitations of the model.
- $\ln(a+b)\neq\ln a+\ln b$. This is a very common error.
- $e^x>0$ for all $x$, so reject any solution that needs $e^x\le0$.

## m-diff
### Rules
$$\frac{d}{dx}x^n=nx^{n-1}$$
$$\frac{d}{dx}e^{kx}=ke^{kx}$$
$$\frac{d}{dx}\ln x=\frac1x$$
$$\frac{d}{dx}\sin kx=k\cos kx$$
$$\frac{d}{dx}\cos kx=-k\sin kx$$
$$\frac{d}{dx}\tan kx=k\sec^2kx$$
- **Chain rule:** $\frac{dy}{dx}=\frac{dy}{du}\cdot\frac{du}{dx}$. **Product rule:** $(uv)'=u'v+uv'$. **Quotient rule:** $\left(\frac uv\right)'=\frac{u'v-uv'}{v^2}$.
- First principles: $f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$.
### Applications
- Tangent gradient $f'(a)$; normal gradient $-\frac1{f'(a)}$.
- Stationary points where $f'(x)=0$: $f''>0$ minimum, $f''<0$ maximum.
- Points of inflection: $f''(x)=0$ **and** $f''$ changes sign. Concave where $f''<0$, convex where $f''>0$.
- Increasing where $f'(x)>0$.
!fig m-tangent-normal
!fig m-stationary
### Implicit and parametric
- Implicit: differentiate each term w.r.t. $x$, so $\frac d{dx}y^2=2y\frac{dy}{dx}$ and $\frac d{dx}(xy)=y+x\frac{dy}{dx}$.
- Parametric: $\frac{dy}{dx}=\dfrac{dy/dt}{dx/dt}$.
- Connected rates: $\frac{dV}{dt}=\frac{dV}{dr}\cdot\frac{dr}{dt}$.
### Worked example
$y=x^2e^{3x}$: $\ \frac{dy}{dx}=2xe^{3x}+3x^2e^{3x}=xe^{3x}(2+3x)$.
### Exam tips
> For the nature of a stationary point you must show the $f''$ value (or the sign change) and state the conclusion.
- In optimisation, check that the answer makes sense (e.g. a length must be positive).

## m-int
### Standard results
$$\int x^n\,dx=\frac{x^{n+1}}{n+1}+c\ (n\neq-1)$$
$$\int\frac1x\,dx=\ln|x|+c$$
$$\int e^{kx}dx=\tfrac1ke^{kx}+c$$
$$\int\cos kx\,dx=\tfrac1k\sin kx+c$$
$$\int\sin kx\,dx=-\tfrac1k\cos kx+c$$
- $\int\frac{f'(x)}{f(x)}dx=\ln|f(x)|+c$, and $\int\sec^2kx\,dx=\frac1k\tan kx+c$.
### Techniques
- **Substitution:** change $dx$ **and** the limits.
- **By parts:** $\int u\frac{dv}{dx}dx=uv-\int v\frac{du}{dx}dx$. Choose $u$ to be the factor that simplifies when differentiated (but take $u=\ln x$).
- **Partial fractions** for rational functions.
- Trig identities, e.g. $\cos^2x=\frac12(1+\cos2x)$.
### Areas and differential equations
- The area between curve and $x$-axis is $\int_a^b y\,dx$. Regions below the axis give negative values, so split them up.
- Area between curves: $\int(\text{top}-\text{bottom})\,dx$.
- Separable DE: $\frac{dy}{dx}=f(x)g(y) \Rightarrow \int\frac1{g(y)}dy=\int f(x)\,dx$. Use the initial conditions to find $c$.
- Trapezium rule: $\int_a^b y\,dx\approx\frac h2\left[y_0+2(y_1+\dots+y_{n-1})+y_n\right]$, where $h=\frac{b-a}n$.
!fig m-area
!fig m-trapezium
### Worked example
$\displaystyle\int_1^e x\ln x\,dx$: take $u=\ln x$, $v'=x$. Then
$$\left[\tfrac{x^2}2\ln x\right]_1^e-\int_1^e\tfrac x2\,dx=\tfrac{e^2}2-\tfrac{e^2-1}4=\tfrac{e^2+1}4$$
### Exam tips
> Don't forget $+c$ on indefinite integrals, and the modulus in $\ln|x|$.
- Trapezium rule: an overestimate if the curve is convex, an underestimate if concave.

## m-num
### Locating roots
- If $f$ is continuous on $[a,b]$ and $f(a)$, $f(b)$ have opposite signs, there is a root in $(a,b)$.
- It can fail if $f$ has an asymptote in the interval, or if there are two roots close together.
### Iteration
- Rearrange $f(x)=0$ to $x=g(x)$ and iterate $x_{n+1}=g(x_n)$.
- It converges if $|g'(x)|<1$ near the root. Staircase diagram if $g'>0$, cobweb if $g'<0$.
### Newton–Raphson
$$x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}$$
- It fails if $f'(x_n)\approx0$ (tangent nearly horizontal), or if the start value is far from the root.
!fig m-newton
### Worked example
$f(x)=x^3-2x-5$, $x_0=2$: $f(2)=-1$ and $f'(2)=10$, so $x_1=2.1$.
To show a root is $2.09$ to 2 d.p., check that $f(2.085)$ and $f(2.095)$ have opposite signs.
### Exam tips
> To justify accuracy, use the sign change on the **bounds** ($\pm0.005$ for 2 d.p.), then conclude in words.

## m-vec
### Basics
- $\mathbf a=x\mathbf i+y\mathbf j+z\mathbf k$; magnitude $|\mathbf a|=\sqrt{x^2+y^2+z^2}$; unit vector $\frac{\mathbf a}{|\mathbf a|}$.
- $\overrightarrow{AB}=\mathbf b-\mathbf a$. Parallel vectors are scalar multiples of each other.
- Position vector of a point dividing $AB$ in the ratio $m:n$: $\mathbf a+\frac m{m+n}(\mathbf b-\mathbf a)$.
- Direction angle with the $x$-axis: $\cos\theta_x=\frac x{|\mathbf a|}$.
!fig m-vectors
### Geometry
- Collinear points: show $\overrightarrow{AB}=k\overrightarrow{BC}$ and that they share a point.
- In 2D, a vector at bearing/angle $\theta$ to $\mathbf i$ with magnitude $r$ is $r\cos\theta\,\mathbf i+r\sin\theta\,\mathbf j$.
### Worked example
$A(1,2,3)$ and $B(4,6,3)$: $\overrightarrow{AB}=3\mathbf i+4\mathbf j$, so $|AB|=5$ and the unit vector is $\frac15(3\mathbf i+4\mathbf j)$.
### Exam tips
> Show vector working clearly in column or $\mathbf{ijk}$ form. In proofs, state the conclusion (e.g. "hence $ABCD$ is a parallelogram").

## s-samp
### Key terms
- **Population:** the whole group. **Census:** observe every member. **Sample:** a subset.
- **Sampling frame:** a list of the members of the population.
### Methods
- **Simple random:** every sample of size $n$ is equally likely (random numbers or lottery).
- **Systematic:** every $k$-th item from a list, with a random start; $k=\frac Nn$.
- **Stratified:** sample from each stratum in proportion to its size, e.g. $\frac{80}{200}\times30=12$.
- **Quota:** the interviewer fills quotas for each group. Non-random, so it may be biased, but no frame is needed.
- **Opportunity:** whoever is available. Easy, but unlikely to be representative.
### Large data set
- Know the Edexcel LDS: weather data from UK and overseas stations, 1987 and 2015. "tr" means trace (under 0.05 mm of rain). Look out for n/a values.
### Exam tips
> When criticising a method, refer to the **context** (e.g. "only people at the gym at 9 am are sampled, so it is not representative").
- Stratified and quota sampling both use groups. Stratified is random within each group; quota is not.

## s-data
### Measures
$$\bar x=\frac{\sum x}n$$
$$\sigma^2=\frac{\sum x^2}n-\bar x^2=\frac{S_{xx}}n$$
- Median and quartiles for grouped data come from interpolation. IQR $=Q_3-Q_1$.
- Coding $y=\frac{x-a}b$: $\bar y=\frac{\bar x-a}b$ and $\sigma_y=\frac{\sigma_x}b$.
### Diagrams
- **Histogram:** frequency density $=\frac{\text{frequency}}{\text{class width}}$; area is proportional to frequency.
- **Box plots:** outliers are usually below $Q_1-1.5\times\text{IQR}$ or above $Q_3+1.5\times\text{IQR}$.
- Cumulative frequency: plot at the **upper class boundaries**.
!fig s-boxplot
### Correlation and regression
- PMCC $r$ lies between $-1$ and $1$. Correlation does not imply causation.
- Regression line $y=a+bx$: interpret $b$ as the change in $y$ per unit of $x$. Only predict within the data range (interpolation).
### Exam tips
> When comparing distributions, compare a **location** (median or mean) and a **spread** (IQR or s.d.), both **in context**.
- Use the median and IQR when there are outliers or skew.

## s-prob
### Rules
$$P(A\cup B)=P(A)+P(B)-P(A\cap B)$$
- Mutually exclusive: $P(A\cap B)=0$. Independent: $P(A\cap B)=P(A)P(B)$.
$$P(A\mid B)=\frac{P(A\cap B)}{P(B)}$$
- Independence also means $P(A\mid B)=P(A)$.
### Tools
- **Venn diagrams:** fill from the centre outwards.
- **Tree diagrams:** multiply along branches and add between outcomes. The second-stage branches are conditional.
- Two-way tables.
!fig s-venn
### Worked example
$P(A)=0.4$, $P(B)=0.5$, $P(A\cup B)=0.7$. Then $P(A\cap B)=0.2=0.4\times0.5$, so $A$ and $B$ are independent.
$P(A\mid B)=\frac{0.2}{0.5}=0.4$.
### Worked example 2 (tree diagram)
A bag has 3 red and 2 blue counters. Two are taken without replacement. Find $P(\text{second red}\mid\text{first blue})$ and $P(\text{both same colour})$.
- $P(R_2\mid B_1)=\frac34$.
- $P(\text{same})=\frac35\cdot\frac24+\frac25\cdot\frac14=\frac{6}{20}+\frac{2}{20}=\frac25$.
- Without replacement, the second-stage probabilities change, so the events are **not** independent.
!fig s-tree
### Exam tips
> To prove independence, show a numerical equality such as $P(A\cap B)=P(A)\times P(B)$ and state the conclusion.

## s-dist
### Binomial $X\sim B(n,p)$
- Conditions: fixed $n$; independent trials; two outcomes; constant $p$.
$$P(X=r)=\binom nr p^r(1-p)^{n-r}$$
- Use cumulative tables or a calculator: $P(X\ge r)=1-P(X\le r-1)$.
### Normal $X\sim N(\mu,\sigma^2)$
- Symmetric bell curve. About 68% of values lie within $1\sigma$, 95% within $2\sigma$, and 99.7% within $3\sigma$. The points of inflection are at $\mu\pm\sigma$.
- Standardise: $Z=\frac{X-\mu}\sigma\sim N(0,1)$.
- Normal approximation to $B(n,p)$ when $n$ is large and $p\approx0.5$: $\mu=np$, $\sigma^2=np(1-p)$. Use a continuity correction, e.g. $P(X\le 10)\to P(Y<10.5)$.
!fig s-normal
### Worked example
$X\sim N(50,4^2)$ with $P(X>a)=0.1$: $\frac{a-50}{4}=1.2816$, so $a=55.1$.
### Worked example (binomial)
$X\sim B(20,0.3)$. Then $P(X=5)=\binom{20}{5}(0.3)^5(0.7)^{15}=0.179$, and $P(X\ge5)=1-P(X\le4)=1-0.238=0.762$.
### Common mistakes
- Treating $P(X<5)$ as $P(X\le5)$ for a binomial: for discrete distributions, $P(X<5)=P(X\le4)$.
- Entering $\sigma^2$ into the calculator where it wants $\sigma$.
- For a normal distribution $P(X=a)=0$, so $<$ and $\le$ give the same answer; for a binomial they do not.
### Exam tips
> Remember the variance is $\sigma^2$: $N(50,16)$ means $\sigma=4$.
- Discrete distribution: probabilities sum to 1.

## s-hyp
### Method
1. State $H_0$ and $H_1$ in terms of the parameter ($p$, $\mu$ or $\rho$).
2. Choose the significance level (e.g. 5%). For a two-tailed test, put $2.5\%$ in each tail.
3. Under $H_0$, find the probability of the observed value or more extreme (or find the critical region).
4. Compare, then **conclude in context**.
### Binomial test
- $H_0: p=0.3$, $H_1: p>0.3$. With $X\sim B(20,0.3)$, test $P(X\ge x_{\text{obs}})$.
- Critical region: the set of values that leads to rejecting $H_0$. The actual significance level is $P(\text{in CR}\mid H_0)$.
### Normal mean
$$\bar X\sim N\!\left(\mu,\frac{\sigma^2}n\right)$$
$$Z=\frac{\bar x-\mu}{\sigma/\sqrt n}$$
!fig s-crit
### Correlation
- $H_0:\rho=0$, $H_1:\rho>0$ (or $<0$, or $\neq0$). Compare $r$ with the critical value from the table.
### Exam tips
> Write the conclusion with no certainty words: "There is sufficient evidence at the 5% level to suggest that the proportion has increased."

## k-units
### SI units
- Base units: m (length), kg (mass), s (time). Derived: N = kg m s⁻², J = N m, W = J s⁻¹.
- Convert carefully: $1\text{ km h}^{-1}=\frac{1000}{3600}\text{ m s}^{-1}$.
### Modelling assumptions
- **Particle:** mass at one point; ignore size and rotation.
- **Rod:** rigid, has length but no thickness. **Lamina:** flat.
- **Light:** massless. **Inextensible:** constant length, so connected objects have equal acceleration.
- **Smooth:** no friction. **Rough:** friction acts.
- $g=9.8\text{ m s}^{-2}$ unless stated. Give answers to 2–3 s.f. when $g=9.8$ is used.
### Exam tips
> When a question asks you to "state an assumption", link it to the effect it has, e.g. "treat the ball as a particle, so air resistance is ignored".

## k-kin
### Constant acceleration (suvat)
$$v=u+at$$
$$s=ut+\tfrac12at^2$$
$$s=\tfrac12(u+v)t$$
$$v^2=u^2+2as$$
$$s=vt-\tfrac12at^2$$
- Vector form: $\mathbf v=\mathbf u+\mathbf at$, $\mathbf r=\mathbf ut+\frac12\mathbf at^2$.
### Graphs
- $v$–$t$ graph: gradient is acceleration; area is displacement.
!fig k-suvat-vt
### Variable acceleration
$$v=\frac{ds}{dt}$$
$$a=\frac{dv}{dt}=\frac{d^2s}{dt^2}$$
$$s=\int v\,dt$$
$$v=\int a\,dt$$
### Projectiles
- Horizontal: $u\cos\theta$ is constant. Vertical: $u\sin\theta$, with $a=-g$.
- Time of flight (to the same level): $\frac{2u\sin\theta}g$. Max height: $\frac{u^2\sin^2\theta}{2g}$.
### Worked example
A ball is thrown at $20\text{ m s}^{-1}$ and $30^\circ$ above the horizontal. Vertical $u_y=10$, so it is at the top at $t=\frac{10}{9.8}=1.02\text{ s}$. The range on level ground is $20\cos30^\circ\times2.04=35.3\text{ m}$.
### Common mistakes
- Using suvat when acceleration is not constant: use calculus instead.
- Forgetting that $g$ acts on the vertical motion only; horizontal velocity is constant in a projectile.
- At the highest point the vertical velocity is zero, not the speed.
### Exam tips
> Choose and state a positive direction. Most suvat sign errors come from mixing directions.

## k-force
### Newton's laws
- N1: constant velocity unless a resultant force acts. N2: $F=ma$. N3: equal and opposite forces on **different** bodies.
- Weight $W=mg$. On a slope at angle $\alpha$: $mg\sin\alpha$ down the slope, $mg\cos\alpha$ into the slope.
### Friction
$$F\le\mu R$$
- Limiting equilibrium or moving: $F=\mu R$. Friction opposes the motion (or the tendency to move).
!fig k-incline
### Connected particles
- Over a smooth pulley: same tension on both sides of a light string; same acceleration if the string is inextensible.
- Write $F=ma$ for each particle separately (or for the whole system if moving together).
!fig k-pulley
### Worked example
A 3 kg block on a rough horizontal table ($\mu=0.2$) is pulled by a string over a pulley to a hanging 2 kg mass.
For the 2 kg mass: $2g-T=2a$. For the block: $T-0.2(3g)=3a$. Adding gives $2g-0.6g=5a$, so $a=2.74\text{ m s}^{-2}$ and $T=14.1\text{ N}$.
### Exam tips
> Draw a large force diagram for every body. Resolve parallel and perpendicular to the slope.

## k-mom
### Moments
$$\text{moment}=F\times d_\perp$$
- $d_\perp$ is the perpendicular distance from the pivot to the line of action. Unit: N m.
- Equilibrium: resultant force $=0$ **and** total clockwise moment = total anticlockwise moment about **any** point.
- Uniform rod: its weight acts at the centre.
- "About to tilt" about a support: the reaction at the **other** support is $0$.
- Ladder problems: resolve vertically and horizontally, then take moments about the foot. Use $F\le\mu R$.
!fig k-ladder
!fig k-moments-beam
### Worked example
A uniform 4 m plank of mass 20 kg rests on supports at end A and at B, 3 m from A. How far beyond B can a 50 kg person stand before the plank tips?
On the point of tipping about B, $R_A=0$. Taking moments about B: $20g\times1=50g\times d$, so $d=0.4\text{ m}$ beyond B (3.4 m from A).
### Exam tips
> Take moments about a point where an unknown force acts, which removes it from the equation.
