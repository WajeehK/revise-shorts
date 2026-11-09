@spec Edexcel 9MA0 Pure topic 4: 4.1 binomial expansion; 4.2–4.8 sequences, sigma notation, arithmetic and geometric series, modelling
@intro Sequences and series are lists of numbers and their sums. This topic covers the binomial expansion (for positive and for fractional or negative powers), arithmetic and geometric series, and sequences defined by recurrence relations.
# Binomial expansion
:::eq
$$(a+b)^n=a^n+\binom n1a^{n-1}b+\binom n2a^{n-2}b^2+\dots+b^n,\qquad\binom nr=\frac{n!}{r!(n-r)!}$$
:::
- For any rational $n$ (A level), the expansion below is valid when $|x|<1$:
$$(1+x)^n=1+nx+\frac{n(n-1)}{2!}x^2+\frac{n(n-1)(n-2)}{3!}x^3+\dots$$
- For $(a+bx)^n$, first take out $a^n$: $(a+bx)^n=a^n\left(1+\frac{b}{a}x\right)^n$. The expansion is then valid for $|x|<\left|\frac ab\right|$.
:::ex Positive integer power
Q: Find the coefficient of $x^3$ in $(2+3x)^5$.
1. The term is $\binom53\,2^2(3x)^3$.
2. $10\times4\times27=1080$.
A: $1080$
:::
:::ex Negative power
Q: Expand $(1-2x)^{-1/2}$ up to the $x^2$ term, and state when it is valid.
1. $n=-\frac12$, and $x$ is replaced by $-2x$.
2. $1+(-\tfrac12)(-2x)+\frac{(-\frac12)(-\frac32)}{2}(4x^2)$.
A: $1+x+\frac32x^2$, valid for $|x|<\frac12$
:::
# Sequences
- A sequence can be given by a **position-to-term** rule, $u_n=f(n)$, or by a **recurrence relation**, $u_{n+1}=f(u_n)$.
- Sequences can be **increasing**, **decreasing** or **periodic**. For example, $u_{n+1}=\frac{1}{u_n}$ has period 2.
- **Sigma notation:** $\sum_{r=1}^n u_r$ means the sum of $u_1$ to $u_n$.
:::ex Recurrence relation
Q: A sequence is defined by $u_1=2$ and $u_{n+1}=3u_n-k$. Given that $u_3=10$, find $k$.
1. $u_2=6-k$.
2. $u_3=3(6-k)-k=18-4k=10$.
A: $k=2$
:::
- A recurrence relation $u_{n+1}=f(u_n)$ needs a **starting value** before you can work out any terms. If the sequence converges to a limit $L$, then $L=f(L)$, which gives an equation you can solve for $L$.
- A sequence is **increasing** if $u_{n+1}>u_n$ for all $n$, and **decreasing** if $u_{n+1}<u_n$ for all $n$. To show that a sequence is increasing, show that $u_{n+1}-u_n>0$.
# Arithmetic series
:::eq
$$u_n=a+(n-1)d\qquad S_n=\frac n2\left(2a+(n-1)d\right)=\frac n2(a+l)$$
:::
:::ex Arithmetic series
Q: Find the sum of the integers from 1 to 100 that are multiples of 3.
1. These are $3,6,\dots,99$, which is $33$ terms.
2. $S=\frac{33}{2}(3+99)$.
A: $1683$
:::
- **Proof of $S_n$:** write the sum forwards and backwards, then add them. Each pair adds to $2a+(n-1)d$, and there are $n$ pairs.
# Geometric series
- **Recognising the type:** if the **difference** between consecutive terms is constant, the sequence is arithmetic. If the **ratio** of consecutive terms is constant, it is geometric. Check this before choosing a formula, because using the wrong one is a common way to lose all the marks.
:::eq
$$u_n=ar^{n-1}\qquad S_n=\frac{a(1-r^n)}{1-r}\qquad S_\infty=\frac{a}{1-r}\ \ (|r|<1)$$
:::
- A geometric series is **convergent** if $|r|<1$.
- **Proof of $S_n$:** work out $S_n-rS_n$; all the terms cancel except two.
:::ex Geometric series
Q: A geometric series has first term 8 and sum to infinity 12. Find $r$, and the smallest $n$ for which $S_n>11.9$.
1. $\frac{8}{1-r}=12$, so $r=\frac13$.
2. $S_n=12(1-(\tfrac13)^n)>11.9$, so $(\tfrac13)^n<\frac{1}{120}$.
3. Taking logs: $n>\frac{\ln120}{\ln3}=4.36$.
A: $r=\frac13$ and $n=5$
:::
:::ex Modelling with a geometric sequence
Q: A car worth £18 000 loses 15% of its value each year. After how many whole years is it first worth less than £5000?
1. Its value after $n$ years is $18000(0.85)^n$.
2. $18000(0.85)^n<5000$ gives $(0.85)^n<0.2778$.
3. $n>\dfrac{\ln0.2778}{\ln0.85}=7.88$.
A: After 8 years.
:::
- **Proof of $S_\infty$:** when $|r|<1$, $r^n\to0$ as $n\to\infty$, so $S_n\to\frac{a}{1-r}$.
- **Modelling:** salaries that rise by a fixed amount each year form an arithmetic sequence; compound interest and depreciation form geometric sequences.
:::warn
- Forgetting to raise $b$ to the power as well, e.g. writing $3x^3$ instead of $(3x)^3$.
- Using $S_\infty$ when $|r|\ge1$.
- Using $n$ terms when the question asks for the term number. Check whether you need $u_n$ or $S_n$.
- Forgetting the validity condition for non-integer expansions.
:::
:::tip
- Show your working when finding $n$ from an inequality, then check the integer either side, because the question usually asks for a whole number.
- With inequalities involving $r^n$, take logs. If $r<1$, $\ln r$ is negative, so the inequality flips when you divide by it.
:::
:::sum
- Binomial expansion: $\binom nr$ for positive integers $n$; the general series, valid for $|x|<1$, for other $n$.
- AP: $u_n=a+(n-1)d$, $S_n=\frac n2(2a+(n-1)d)$.
- GP: $u_n=ar^{n-1}$, $S_n=\frac{a(1-r^n)}{1-r}$, $S_\infty=\frac a{1-r}$.
- Recurrence relations; sequences can be increasing, decreasing or periodic.
:::
