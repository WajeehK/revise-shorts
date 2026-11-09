# Locating roots
- If $f$ is continuous on $[a,b]$ and $f(a)$, $f(b)$ have opposite signs, there is a root in $(a,b)$.
- It can fail if $f$ has an asymptote in the interval, or if there are two roots close together.
# Iteration
- Rearrange $f(x)=0$ to $x=g(x)$ and iterate $x_{n+1}=g(x_n)$.
- It converges if $|g'(x)|<1$ near the root. Staircase diagram if $g'>0$, cobweb if $g'<0$.
# Newton–Raphson
$$x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}$$
- It fails if $f'(x_n)\approx0$ (tangent nearly horizontal), or if the start value is far from the root.
!fig m-newton
# Worked example
$f(x)=x^3-2x-5$, $x_0=2$: $f(2)=-1$ and $f'(2)=10$, so $x_1=2.1$.
To show a root is $2.09$ to 2 d.p., check that $f(2.085)$ and $f(2.095)$ have opposite signs.
# Exam tips
> To justify accuracy, use the sign change on the **bounds** ($\pm0.005$ for 2 d.p.), then conclude in words.
