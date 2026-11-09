# Rules
$$\frac{d}{dx}x^n=nx^{n-1}$$
$$\frac{d}{dx}e^{kx}=ke^{kx}$$
$$\frac{d}{dx}\ln x=\frac1x$$
$$\frac{d}{dx}\sin kx=k\cos kx$$
$$\frac{d}{dx}\cos kx=-k\sin kx$$
$$\frac{d}{dx}\tan kx=k\sec^2kx$$
- **Chain rule:** $\frac{dy}{dx}=\frac{dy}{du}\cdot\frac{du}{dx}$. **Product rule:** $(uv)'=u'v+uv'$. **Quotient rule:** $\left(\frac uv\right)'=\frac{u'v-uv'}{v^2}$.
- First principles: $f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$.
# Applications
- Tangent gradient $f'(a)$; normal gradient $-\frac1{f'(a)}$.
- Stationary points where $f'(x)=0$: $f''>0$ minimum, $f''<0$ maximum.
- Points of inflection: $f''(x)=0$ **and** $f''$ changes sign. Concave where $f''<0$, convex where $f''>0$.
- Increasing where $f'(x)>0$.
!fig m-tangent-normal
!fig m-stationary
# Implicit and parametric
- Implicit: differentiate each term w.r.t. $x$, so $\frac d{dx}y^2=2y\frac{dy}{dx}$ and $\frac d{dx}(xy)=y+x\frac{dy}{dx}$.
- Parametric: $\frac{dy}{dx}=\dfrac{dy/dt}{dx/dt}$.
- Connected rates: $\frac{dV}{dt}=\frac{dV}{dr}\cdot\frac{dr}{dt}$.
# Worked example
$y=x^2e^{3x}$: $\ \frac{dy}{dx}=2xe^{3x}+3x^2e^{3x}=xe^{3x}(2+3x)$.
# Exam tips
> For the nature of a stationary point you must show the $f''$ value (or the sign change) and state the conclusion.
- In optimisation, check that the answer makes sense (e.g. a length must be positive).
