# Binomial $X\sim B(n,p)$
- Conditions: fixed $n$; independent trials; two outcomes; constant $p$.
$$P(X=r)=\binom nr p^r(1-p)^{n-r}$$
- Use cumulative tables or a calculator: $P(X\ge r)=1-P(X\le r-1)$.
# Normal $X\sim N(\mu,\sigma^2)$
- Symmetric bell curve. About 68% of values lie within $1\sigma$, 95% within $2\sigma$, and 99.7% within $3\sigma$. The points of inflection are at $\mu\pm\sigma$.
- Standardise: $Z=\frac{X-\mu}\sigma\sim N(0,1)$.
- Normal approximation to $B(n,p)$ when $n$ is large and $p\approx0.5$: $\mu=np$, $\sigma^2=np(1-p)$. Use a continuity correction, e.g. $P(X\le 10)\to P(Y<10.5)$.
!fig s-normal
# Worked example
$X\sim N(50,4^2)$ with $P(X>a)=0.1$: $\frac{a-50}{4}=1.2816$, so $a=55.1$.
# Worked example (binomial)
$X\sim B(20,0.3)$. Then $P(X=5)=\binom{20}{5}(0.3)^5(0.7)^{15}=0.179$, and $P(X\ge5)=1-P(X\le4)=1-0.238=0.762$.
# Common mistakes
- Treating $P(X<5)$ as $P(X\le5)$ for a binomial: for discrete distributions, $P(X<5)=P(X\le4)$.
- Entering $\sigma^2$ into the calculator where it wants $\sigma$.
- For a normal distribution $P(X=a)=0$, so $<$ and $\le$ give the same answer; for a binomial they do not.
# Exam tips
> Remember the variance is $\sigma^2$: $N(50,16)$ means $\sigma=4$.
- Discrete distribution: probabilities sum to 1.
