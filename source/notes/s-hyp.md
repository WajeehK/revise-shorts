@spec Edexcel 9MA0 Statistics topic 5: 5.1 language of hypothesis testing; 5.2 binomial tests and critical regions; 5.3 tests for correlation (PMCC) and for the mean of a normal distribution
@intro A hypothesis test uses sample data to decide whether there is enough evidence to reject a claim about a population. This topic covers the language of testing, binomial tests and critical regions, and (at A level) tests for correlation and for a normal mean.
# The language of hypothesis testing
:::def
**Null hypothesis ($H_0$):** the assumption that is believed to be true unless there is evidence against it, e.g. $H_0:p=0.3$.
**Alternative hypothesis ($H_1$):** what we accept if $H_0$ is rejected. It can be one-tailed ($p>0.3$ or $p<0.3$) or two-tailed ($p\neq0.3$).
**Test statistic:** the value calculated from the sample, used to make the decision.
**Significance level ($\alpha$):** the probability threshold for rejecting $H_0$, e.g. 5%.
**Critical region:** the set of values of the test statistic that lead to rejecting $H_0$. The **critical value** is the first value inside it.
**Actual significance level:** the true probability of rejecting $H_0$ when it is true, which is the probability of the critical region.
**p-value:** the probability of a result at least as extreme as the one observed, assuming $H_0$ is true.
:::
# Binomial tests
1. Define the variable and write $H_0$ and $H_1$ in terms of the **population parameter** $p$.
2. Assume $H_0$ is true, so $X\sim B(n,p_0)$.
3. Work out the probability of the observed value or a more extreme one, or find the critical region.
4. Compare it with $\alpha$ (or with $\frac\alpha2$ in each tail for a two-tailed test).
5. Conclude **in context**, without overclaiming: "There is sufficient evidence at the 5% level to suggest that…"
:::ex One-tailed test
Q: A coin is suspected of being biased towards heads. In 20 flips it gives 15 heads. Test at the 5% level.
1. $H_0:p=0.5$ and $H_1:p>0.5$. Under $H_0$, $X\sim B(20,0.5)$.
2. $P(X\ge15)=1-P(X\le14)=0.0207$.
3. $0.0207<0.05$, so reject $H_0$.
A: There is sufficient evidence at the 5% level that the coin is biased towards heads.
:::
!fig s-crit Critical regions in the tails of a distribution
:::ex Critical region, two-tailed
Q: Find the critical region for testing $H_0:p=0.3$ against $H_1:p\neq0.3$ with $n=20$ at the 10% level (5% in each tail), and give the actual significance level.
1. Lower tail: $P(X\le2)=0.0355$ and $P(X\le3)=0.1071$, so the lower region is $X\le2$.
2. Upper tail: $P(X\ge10)=0.0480$ and $P(X\ge9)=0.1133$, so the upper region is $X\ge10$.
A: The critical region is $X\le2$ or $X\ge10$. The actual significance level is $0.0355+0.0480=0.0835$ (8.35%).
:::
# Testing correlation (A level)
- $H_0:\rho=0$, against $H_1:\rho>0$, $\rho<0$ or $\rho\neq0$, where $\rho$ is the population PMCC.
- Compare the sample $r$ with the **critical value** from tables, for the given $n$ and significance level.
:::ex PMCC test
Q: For 10 pairs of data, $r=0.62$. Test for positive correlation at the 5% level, where the critical value is 0.5494.
1. $H_0:\rho=0$ and $H_1:\rho>0$.
2. $0.62>0.5494$, so $r$ is in the critical region.
A: Reject $H_0$. There is evidence of positive correlation between the variables.
:::
# Testing a normal mean (A level)
- If $X\sim N(\mu,\sigma^2)$, then the sample mean is $\bar X\sim N\left(\mu,\frac{\sigma^2}{n}\right)$.
:::ex Mean test
Q: Bags are meant to weigh 500 g, with $\sigma=8$ g. A sample of 16 bags has mean 496 g. Test at the 5% level whether the mean weight has decreased.
1. $H_0:\mu=500$ and $H_1:\mu<500$. Under $H_0$, $\bar X\sim N(500,\frac{64}{16})=N(500,2^2)$.
2. $P(\bar X\le496)=P(Z\le-2)=0.0228$.
3. $0.0228<0.05$, so reject $H_0$.
A: There is evidence at the 5% level that the mean weight has decreased.
:::
:::warn
- Writing hypotheses in terms of $X$ or $\bar x$. They must use **parameters** ($p$, $\mu$ or $\rho$).
- Using $P(X=15)$ instead of $P(X\ge15)$. The test always uses the tail probability.
- Saying "$H_0$ is proved true" or "proves the coin is biased". Tests give evidence, not proof.
:::
:::tip
- For a two-tailed test, halve the significance level for each tail and check both ends.
- Always give a two-part conclusion: a statistical statement (reject or do not reject $H_0$) and an interpretation in context.
:::
:::sum
- $H_0$ and $H_1$ concern population parameters; tests are one- or two-tailed.
- Binomial tests use tail probabilities. Critical regions have an actual significance level.
- PMCC test: compare $r$ with the critical value.
- Normal mean test: $\bar X\sim N(\mu,\frac{\sigma^2}{n})$.
:::
