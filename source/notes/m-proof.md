# Key ideas
- **Proof by deduction:** start from known facts and use logical steps to reach the statement in general.
- **Proof by exhaustion:** split into a finite set of cases and check every one (e.g. $n$ even / $n$ odd, or $n \equiv 0,1,2 \pmod 3$).
- **Disproof by counter-example:** a single case where the statement fails is enough.
- **Proof by contradiction:** assume the statement is false, then show this leads to something impossible.
# Useful forms
- Even: $2k$; odd: $2k+1$; consecutive integers: $n,\ n+1$; rational: $\frac{a}{b}$ with $a,b \in \mathbb{Z}$, $b \neq 0$, no common factors.
- Completing the square proves positivity: $x^2-6x+10=(x-3)^2+1>0$ for all real $x$.
# Classic proofs
- **$\sqrt{2}$ is irrational:** assume $\sqrt2=\frac ab$ in lowest terms. Then $a^2=2b^2$, so $a$ is even, $a=2c$, giving $b^2=2c^2$, so $b$ is even too, contradicting "lowest terms".
- **Infinitely many primes:** assume finitely many, $p_1,\dots,p_n$. Then $N=p_1p_2\cdots p_n+1$ leaves remainder 1 when divided by every $p_i$. So $N$ is prime or has a prime factor not in the list. Contradiction.
# Worked example
Prove that the sum of any three consecutive integers is divisible by 3.
$$n+(n+1)+(n+2)=3n+3=3(n+1)$$
$3(n+1)$ is a multiple of 3, so the result holds for all integers $n$.
# Exam tips
> Write a concluding sentence that restates what has been proved, e.g. "…therefore it is divisible by 3".
- In contradiction proofs, state clearly what you are assuming and where the contradiction is.
- A list of examples is **not** a proof (unless it is exhaustion over *all* cases).
