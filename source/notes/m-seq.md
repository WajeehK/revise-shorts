# Binomial expansion
$$(a+b)^n=\sum_{r=0}^{n}\binom nr a^{n-r}b^r$$
- For any rational $n$: $(1+x)^n=1+nx+\frac{n(n-1)}{2!}x^2+\dots$, valid for $|x|<1$.
- For $(a+bx)^n$, first take out $a^n$: $a^n\left(1+\frac bax\right)^n$, valid for $|x|<\left|\frac ab\right|$.
# Arithmetic sequences
$$u_n=a+(n-1)d$$
$$S_n=\tfrac n2\left[2a+(n-1)d\right]=\tfrac n2(a+l)$$
# Geometric sequences
$$u_n=ar^{n-1}$$
$$S_n=\frac{a(1-r^n)}{1-r}$$
$$S_\infty=\frac a{1-r}\ \ (|r|<1)$$
# Other sequences
- Recurrence $u_{n+1}=f(u_n)$: increasing, decreasing or **periodic** (repeats with some order $k$).
- Sigma notation: $\sum_{r=1}^{n}1=n$. Watch the start value.
# Worked example
A geometric series has $u_2=12$ and $S_\infty=64$. Find $r$.
$ar=12$ and $\frac a{1-r}=64$, so $12=64r(1-r)$. This gives $16r^2-16r+3=0$, i.e. $(4r-1)(4r-3)=0$, so $r=\frac14$ or $r=\frac34$.
# Exam tips
> Always state the validity range of a binomial expansion with a non-integer or negative $n$.
- When solving $S_n>k$ by logs, dividing by $\ln r$ with $r<1$ flips the inequality.
