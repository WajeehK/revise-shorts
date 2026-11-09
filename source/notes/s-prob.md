# Rules
$$P(A\cup B)=P(A)+P(B)-P(A\cap B)$$
- Mutually exclusive: $P(A\cap B)=0$. Independent: $P(A\cap B)=P(A)P(B)$.
$$P(A\mid B)=\frac{P(A\cap B)}{P(B)}$$
- Independence also means $P(A\mid B)=P(A)$.
# Tools
- **Venn diagrams:** fill from the centre outwards.
- **Tree diagrams:** multiply along branches and add between outcomes. The second-stage branches are conditional.
- Two-way tables.
!fig s-venn
# Worked example
$P(A)=0.4$, $P(B)=0.5$, $P(A\cup B)=0.7$. Then $P(A\cap B)=0.2=0.4\times0.5$, so $A$ and $B$ are independent.
$P(A\mid B)=\frac{0.2}{0.5}=0.4$.
# Worked example 2 (tree diagram)
A bag has 3 red and 2 blue counters. Two are taken without replacement. Find $P(\text{second red}\mid\text{first blue})$ and $P(\text{both same colour})$.
- $P(R_2\mid B_1)=\frac34$.
- $P(\text{same})=\frac35\cdot\frac24+\frac25\cdot\frac14=\frac{6}{20}+\frac{2}{20}=\frac25$.
- Without replacement, the second-stage probabilities change, so the events are **not** independent.
!fig s-tree
# Exam tips
> To prove independence, show a numerical equality such as $P(A\cap B)=P(A)\times P(B)$ and state the conclusion.
