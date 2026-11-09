@spec Edexcel 9MA0 Pure topic 6: 6.1–6.7 (exponential functions, e, logarithms, laws of logs, solving equations, linearising data, modelling growth and decay)
@intro Exponential functions model anything that grows or decays at a rate proportional to its size: populations, money, radioactive decay and cooling. Logarithms are the inverse of exponentials, and they let us solve equations where the unknown is in the power.
# Exponential functions
- $y=a^x$ (with $a>0$) passes through $(0,1)$, has the $x$-axis as an asymptote, and is always positive.
- **The number $e$** (about 2.718) is special because the gradient of $y=e^{kx}$ is $ke^{kx}$. The rate of change is proportional to the value.
!fig m-exp-ln y = eˣ and y = ln x are reflections of each other in y = x
- $y=\ln x$ is the inverse of $y=e^x$. Its domain is $x>0$, it passes through $(1,0)$, and the $y$-axis is an asymptote.
## Transformations of exponential graphs
- $y=e^{-x}$ is the reflection of $y=e^x$ in the $y$-axis, so it shows decay.
- $y=Ae^{kx}+c$ has a horizontal asymptote at $y=c$, and it crosses the $y$-axis at $(0,A+c)$. When you sketch it, always label the asymptote with its equation and give the intercept.
- $y=\ln(x+a)$ is a translation of $y=\ln x$ by $a$ to the left. Its vertical asymptote moves to $x=-a$.
# Laws of logarithms
:::eq
$$a^x=b\Leftrightarrow x=\log_ab\qquad\log_a(xy)=\log_ax+\log_ay\qquad\log_a\frac xy=\log_ax-\log_ay\qquad\log_ax^k=k\log_ax$$
:::
- Useful facts: $\log_aa=1$ and $\log_a1=0$.
:::ex Using the laws
Q: Solve $\log_2(x+1)+\log_2(x-1)=3$.
1. $\log_2((x+1)(x-1))=3$, so $x^2-1=8$.
2. $x=\pm3$. But $x-1>0$, so reject $-3$.
A: $x=3$
:::
# Solving exponential equations
- Take logs of both sides, or rearrange so you can use $\ln$.
:::ex Unknown in the power
Q: Solve $3^{2x-1}=20$.
1. $(2x-1)\ln3=\ln20$, so $2x-1=2.727$.
A: $x=1.86$ (3 s.f.)
:::
:::ex Disguised quadratic
Q: Solve $e^{2x}-5e^x+6=0$.
1. Let $u=e^x$. Then $u^2-5u+6=0$, so $u=2$ or $u=3$.
A: $x=\ln2$ or $x=\ln3$
:::
# Linearising data with logs
| Model | Plot | Gradient | Intercept |
|---|---|---|---|
| $y=ax^n$ | $\log y$ against $\log x$ | $n$ | $\log a$ |
| $y=kb^x$ | $\log y$ against $x$ | $\log b$ | $\log k$ |
:::ex Finding a model
Q: A graph of $\log_{10}y$ against $x$ is a straight line with gradient $0.301$ and intercept $0.699$. Find the model.
1. $\log_{10}y=0.699+0.301x$, so $y=10^{0.699}\times(10^{0.301})^x$.
A: $y=5\times2^x$
:::
# Modelling growth and decay
- A growth model is $N=N_0e^{kt}$ with $k>0$; a decay model has $k<0$. The initial value is $N_0$, and the rate of change is $\frac{dN}{dt}=kN$.
- **Limitations:** real populations cannot grow forever (resources run out), so the model is only valid over a limited range of time.
:::ex Population
Q: A population is modelled by $P=200e^{0.04t}$, where $t$ is in years. When does it first reach 500, and what is its rate of growth then?
1. $e^{0.04t}=2.5$, so $t=\frac{\ln2.5}{0.04}=22.9$ years.
2. $\frac{dP}{dt}=0.04P=0.04\times500$.
A: After about 22.9 years; the rate of growth is then 20 per year.
:::
:::ex Half-life
Q: The mass of a radioactive sample is $m=40e^{-0.02t}$ grams, where $t$ is in days. Find the half-life.
1. Set $20=40e^{-0.02t}$. Then $e^{-0.02t}=0.5$.
2. $-0.02t=\ln0.5$, so $t=\frac{\ln2}{0.02}$.
A: The half-life is about 34.7 days. It does not depend on the starting mass, which is a key property of exponential decay.
:::
## Comparing and refining models
- If the predictions of a model drift away from the data, suggest a refinement. For example, add a constant term (say, a population that levels off at a maximum value), or use a different rate for different time periods.
- When a question asks you to "interpret" a constant, explain its meaning in context. For example, in $T=20+60e^{-0.1t}$, the 20 is the room temperature that the liquid cools towards, and the 60 is the initial temperature difference.
:::warn
- Writing $\log(x+y)=\log x+\log y$. That is **false**.
- Forgetting to reject solutions that make a log argument negative or zero.
- Confusing $\ln$ and $\log_{10}$ when reading off the gradient of a graph.
:::
:::tip
- "Initial value" means substituting $t=0$. "Rate of change" means differentiating.
- In modelling questions, always comment on limitations or the validity of the model when asked to evaluate it.
:::
:::sum
- $y=a^x$ and $y=e^x$; $\ln$ is the inverse of $e^x$.
- Laws of logs; solving $a^x=b$ by taking logs.
- Linearise with log graphs: $y=ax^n$ or $y=kb^x$.
- Growth and decay models, $N=N_0e^{kt}$, and their limitations.
:::
