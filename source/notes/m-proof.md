@spec Edexcel 9MA0 Pure topic 1: 1.1 proof by deduction, exhaustion and counter-example; 1.2 proof by contradiction
@intro A proof is a logical argument that shows a statement is always true. A-level Maths uses four methods: deduction, exhaustion, counter-example and contradiction.
# The language of proof
- **Notation:** $\Rightarrow$ (implies), $\Leftarrow$ (is implied by), $\Leftrightarrow$ (if and only if), $\in$ (is an element of), $\therefore$ (therefore).
- **Integers:** an even number is $2n$, an odd number is $2n+1$, and consecutive integers are $n$ and $n+1$, where $n\in\mathbb{Z}$.
- A **rational** number can be written as $\frac{a}{b}$, where $a,b$ are integers, $b\neq0$, and $\frac{a}{b}$ is in its simplest form.
- Finish every proof with a concluding sentence that restates what has been shown.
# Proof by deduction
- Start from known facts and use algebra to reach the result, step by step.
:::ex Proof by deduction
Q: Prove that the sum of any three consecutive integers is a multiple of 3.
1. Let the integers be $n$, $n+1$ and $n+2$.
2. Their sum is $3n+3=3(n+1)$.
3. $n+1$ is an integer, so the sum is a multiple of 3.
A: The sum of any three consecutive integers is a multiple of 3. ∎
:::
:::ex Completing the square in a proof
Q: Prove that $x^2-6x+10>0$ for all real $x$.
1. $x^2-6x+10=(x-3)^2+1$.
2. $(x-3)^2\ge0$ for all real $x$, so $(x-3)^2+1\ge1>0$.
A: $x^2-6x+10>0$ for all real $x$. ∎
:::
# Proof by exhaustion
- Split the problem into a finite number of cases and prove each one. For example, consider $n$ even and $n$ odd, or test every value in a small set.
:::ex Proof by exhaustion
Q: Prove that $n^2+n$ is even for every integer $n$.
1. If $n$ is even, $n=2k$, then $n^2+n=4k^2+2k=2(2k^2+k)$, which is even.
2. If $n$ is odd, $n=2k+1$, then $n^2+n=(2k+1)(2k+2)=2(2k+1)(k+1)$, which is even.
A: Both cases give an even number, so $n^2+n$ is always even. ∎
:::
# Disproof by counter-example
- A single example where the statement fails is enough to **disprove** it.
:::ex Counter-example
Q: Disprove the statement "$2^n-1$ is prime for every positive integer $n$".
1. Try small values: $n=1$ gives $1$, which is not prime.
2. Or $n=4$ gives $15=3\times5$.
A: $n=4$ gives 15, which is not prime, so the statement is false.
:::
# Proof by contradiction (A level)
- Assume the **opposite** of what you want to prove, then show that this assumption leads to a contradiction.
:::ex √2 is irrational
Q: Prove that $\sqrt2$ is irrational.
1. Assume that $\sqrt2=\frac{a}{b}$, where $a,b$ are integers with no common factors.
2. Then $2b^2=a^2$, so $a^2$ is even, so $a$ is even. Let $a=2k$.
3. Then $2b^2=4k^2$, so $b^2=2k^2$, so $b$ is even too.
4. So $a$ and $b$ have a common factor of 2, which is a contradiction.
A: Therefore $\sqrt2$ is irrational. ∎
:::
:::ex Infinitely many primes
Q: Prove that there are infinitely many primes.
1. Assume that there are finitely many primes, $p_1,p_2,\dots,p_n$.
2. Let $N=p_1p_2\cdots p_n+1$. Dividing $N$ by any $p_i$ leaves a remainder of 1.
3. So $N$ is either prime, or it has a prime factor not in the list. Either way, this contradicts the assumption.
A: There are infinitely many primes. ∎
:::
:::warn
- Checking a few examples and calling it a proof. Examples can only **disprove**; exhaustion works only when every case is covered.
- Using the same letter for two different integers. For example, odd numbers should be $2m+1$ and $2n+1$, not both $2n+1$.
- Leaving out the concluding statement.
:::
:::tip
- For a contradiction proof, state the assumption clearly at the start ("Assume, for contradiction, that…") and name the contradiction explicitly at the end.
:::
:::sum
- Deduction: logical algebraic steps from known facts.
- Exhaustion: cover every case.
- Counter-example: one failure disproves a statement.
- Contradiction: assume the opposite and reach an impossibility. Examples are √2 being irrational and there being infinitely many primes.
:::
