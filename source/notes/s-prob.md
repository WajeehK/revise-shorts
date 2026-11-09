@spec Edexcel 9MA0 Statistics topic 3: 3.1 mutually exclusive and independent events, Venn and tree diagrams; 3.2 set notation and conditional probability; 3.3 modelling with probability
@intro Probability measures how likely an event is, on a scale from 0 to 1. This topic covers Venn and tree diagrams, mutually exclusive and independent events, set notation and conditional probability.
# Basics and Venn diagrams
- $P(A')=1-P(A)$, and $P(A\cup B)=P(A)+P(B)-P(A\cap B)$.
!fig s-venn Venn diagram with two overlapping events
- **Set notation:** $A\cap B$ means "A and B"; $A\cup B$ means "A or B (or both)"; $A'$ means "not A".
:::def
**Mutually exclusive events:** events that cannot happen together, so $P(A\cap B)=0$ and $P(A\cup B)=P(A)+P(B)$.
**Independent events:** one event does not affect the probability of the other, so $P(A\cap B)=P(A)\times P(B)$.
:::
:::ex Testing independence
Q: $P(A)=0.4$, $P(B)=0.5$ and $P(A\cup B)=0.7$. Are $A$ and $B$ independent?
1. $P(A\cap B)=0.4+0.5-0.7=0.2$.
2. $P(A)P(B)=0.4\times0.5=0.2$.
A: They are equal, so $A$ and $B$ are independent.
:::
# Tree diagrams
!fig s-tree Tree diagram for two events
- **Multiply** along the branches, and **add** the results for different routes that lead to the same outcome.
- Without replacement, the probabilities on the second set of branches change.
:::ex Without replacement
Q: A bag has 5 red and 3 blue counters. Two are taken without replacement. Find the probability that they are different colours.
1. $P(RB)=\frac58\times\frac37=\frac{15}{56}$, and $P(BR)=\frac38\times\frac57=\frac{15}{56}$.
A: $\frac{30}{56}=\frac{15}{28}$
:::
## "At least one" questions
- "At least one" is usually easiest via the complement: $P(\text{at least one})=1-P(\text{none})$. This avoids having to list every route through a tree diagram.
:::ex At least one six
Q: A fair die is rolled 4 times. Find the probability of at least one six.
1. $P(\text{no sixes})=\left(\frac56\right)^4=0.4823$.
A: $1-0.4823=0.518$
:::
# Conditional probability (A level)
:::eq
$$P(A\mid B)=\frac{P(A\cap B)}{P(B)}$$
:::
- $P(A\mid B)$ means the probability of $A$ given that $B$ has happened. It restricts the sample space to $B$.
- If $A$ and $B$ are independent, then $P(A\mid B)=P(A)$.
- Use two-way tables, Venn diagrams or tree diagrams. On a tree diagram, the second-stage branches are conditional probabilities.
:::ex Medical test
Q: 2% of people have a disease. A test detects it 95% of the time, but gives a false positive for 10% of healthy people. Given a positive result, find the probability that the person has the disease.
1. $P(+)=0.02\times0.95+0.98\times0.10=0.019+0.098=0.117$.
2. $P(D\mid+)=\frac{0.019}{0.117}$.
A: About $0.162$. Most positive results are false, because the disease is rare.
:::
:::ex From a two-way table
Q: Of 120 students, 50 study physics, 40 study chemistry, and 15 study both. A student is chosen at random. Given that they study chemistry, find the probability that they study physics.
1. $P(P\cap C)=\frac{15}{120}$ and $P(C)=\frac{40}{120}$.
A: $P(P\mid C)=\frac{15}{40}=\frac38$
:::
## Conditional probability in Venn diagrams
- For $P(A\mid B)$, look **only inside circle $B$**. The answer is the part of $B$ that is also in $A$, divided by the whole of $B$.
- For three events, the same idea applies. Fill in the central region (all three) first, then the regions where pairs overlap, then the rest.
# Modelling with probability
- Probability models make assumptions, for example that outcomes are equally likely or that events are independent. A good answer comments on whether these assumptions are realistic in context, for example whether a coin is really fair, or whether one person's choice really doesn't affect another's.
- Compare an experiment's relative frequencies with the model's predicted probabilities. A large difference suggests the model needs refining.
:::warn
- Confusing "mutually exclusive" (they can't both happen) with "independent" (one doesn't affect the other).
- Adding probabilities along a branch of a tree. Multiply along branches, and add across them.
- Dividing by the wrong event in a conditional probability. Divide by the event that is **given**.
:::
:::tip
- In a Venn diagram, fill in the intersection first, then work outwards. Check that everything adds up to 1.
:::
:::sum
- Addition rule; $P(A')=1-P(A)$.
- Mutually exclusive: $P(A\cap B)=0$. Independent: $P(A\cap B)=P(A)P(B)$.
- Tree and Venn diagrams; $P(A\mid B)=\frac{P(A\cap B)}{P(B)}$.
- Probability models rely on assumptions that should be checked.
:::
