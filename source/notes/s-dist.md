@spec Edexcel 9MA0 Statistics topic 4: 4.1 discrete distributions and the binomial distribution; 4.2 the normal distribution; 4.3 choosing a distribution and the normal approximation to the binomial
@intro A probability distribution lists the probability of every possible outcome. This topic covers discrete distributions, the binomial distribution, and (at A level) the normal distribution for continuous data.
# Discrete random variables
- A **discrete random variable** $X$ takes a countable set of values, and $\sum P(X=x)=1$.
- A distribution can be given as a table or a formula. The **discrete uniform distribution** gives every outcome the same probability, as for a fair die.
:::ex Finding an unknown probability
Q: $P(X=x)=kx$ for $x=1,2,3,4$. Find $k$, and $P(X\ge3)$.
1. $k(1+2+3+4)=1$, so $k=\frac1{10}$.
2. $P(X\ge3)=\frac{3+4}{10}$.
A: $k=0.1$ and $P(X\ge3)=0.7$
:::
# The binomial distribution
- $X\sim B(n,p)$ models the number of successes in $n$ trials when:
1. there is a fixed number of trials, $n$;
2. each trial has two outcomes (success or failure);
3. the probability of success, $p$, is constant;
4. the trials are independent.
:::eq
$$P(X=r)=\binom nr p^r(1-p)^{n-r}$$
:::
- Use the calculator's **binomial cumulative distribution function** for $P(X\le r)$. For other cases, $P(X\ge r)=1-P(X\le r-1)$.
:::ex Binomial
Q: $X\sim B(20,0.3)$. Find $P(X=5)$ and $P(X>8)$.
1. $P(X=5)=\binom{20}{5}(0.3)^5(0.7)^{15}=0.1789$.
2. $P(X>8)=1-P(X\le8)=1-0.8867$.
A: $0.179$ and $0.113$
:::
- The **mean** (expected number of successes) of $B(n,p)$ is $np$. This is useful for checking whether an answer is reasonable, and for setting up the normal approximation later.
- **Criticising a binomial model:** in context, the probability might not really be constant (for example, a player gets tired), or the trials might not be independent (for example, faults that come in batches). Say which condition fails and why.
# The normal distribution (A level)
!fig s-normal Normal distribution curve with mean μ and standard deviation σ
- $X\sim N(\mu,\sigma^2)$ is **symmetric** and bell-shaped, centred on the mean $\mu$. The points of inflection are at $\mu\pm\sigma$.
- About **68%** of values lie within $1\sigma$ of the mean, **95%** within $2\sigma$, and **99.7%** within $3\sigma$.
- **Standardising:** $Z=\frac{X-\mu}{\sigma}$ gives $Z\sim N(0,1)$.
- **Inverse normal:** given a probability, find the value. Use standardising to find an unknown $\mu$ or $\sigma$.
:::ex Normal probabilities
Q: Heights are distributed $N(170,8^2)$ cm. Find $P(160<X<180)$ and the height exceeded by 10% of people.
1. Use the normal CDF: $P(160<X<180)=0.7887$.
2. Inverse normal: $P(X>h)=0.1$, so $h=170+1.2816\times8$.
A: $0.789$, and $h=180.3$ cm
:::
:::ex Finding σ
Q: $X\sim N(50,\sigma^2)$ and $P(X<56)=0.9$. Find $\sigma$.
1. $\frac{56-50}{\sigma}=1.2816$.
A: $\sigma=4.68$
:::
- **Using the normal as a model:** check that the data are roughly symmetric, and that about 95% of values lie within $2\sigma$ of the mean. A normal model gives a small probability to impossible values (such as negative heights), so it is only an approximation.
- For a **continuous** variable, $P(X=a)=0$, so $P(X<a)=P(X\le a)$. This is unlike discrete distributions, where the difference matters.
# Choosing a distribution and the normal approximation
- Use the binomial for counts of successes, and the normal for continuous measurements that are symmetric about a mean.
- When $n$ is large and $p$ is close to $0.5$, $B(n,p)$ can be approximated by $N(np,\,np(1-p))$, using a **continuity correction**. For example, $P(X\le20)$ becomes $P(Y<20.5)$.
:::ex Normal approximation
Q: $X\sim B(100,0.4)$. Use a normal approximation to estimate $P(X\le35)$.
1. $\mu=40$ and $\sigma^2=24$, so $\sigma=4.899$.
2. $P(Y<35.5)=P\left(Z<\frac{35.5-40}{4.899}\right)=P(Z<-0.9186)$.
A: About $0.179$
:::
:::warn
- Using $P(X\le r)$ when the question says "fewer than $r$". That means $P(X\le r-1)$.
- Entering the **variance** as $\sigma$ on the calculator. $N(\mu,\sigma^2)$ gives the variance, so take its square root.
- Forgetting the continuity correction.
:::
:::tip
- Before calculating, write the distribution out in full, for example "Let $X$ be the number of faulty bulbs; $X\sim B(20,0.05)$." Defining the variable earns a method mark and keeps your working clear.
- In "state assumptions" questions, list the binomial conditions **in context** (for example, "each seed germinates independently").
:::
:::sum
- $\sum P=1$; discrete uniform.
- $B(n,p)$: fixed $n$, two outcomes, constant $p$, independent trials.
- $N(\mu,\sigma^2)$: symmetric; 68/95/99.7 rule; $Z=\frac{X-\mu}{\sigma}$.
- Normal approximation to $B(n,p)$, with a continuity correction.
:::
