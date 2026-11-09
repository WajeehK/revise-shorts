@spec Edexcel 9MA0 Mechanics topic 9: 9.1 moments; equilibrium of rigid bodies, including rods on supports, tilting, ladders and non-uniform rods
@intro A moment measures the turning effect of a force. Taking moments lets us solve problems with beams, rods, see-saws and ladders. In equilibrium, both the forces and the moments must balance.
# Moments
:::eq
$$\text{moment}=F\times d_\perp$$
:::
- $d_\perp$ is the **perpendicular** distance from the pivot to the line of action of the force. Moments are measured in N m, and their sense is clockwise or anticlockwise.
- For a force at an angle, use either $F\sin\theta\times d$ or $F\times d\sin\theta$.
!fig k-moments-beam Forces and moments on a horizontal beam
# Equilibrium of a rigid body
- **Resultant force = 0** (resolve in two directions) **and** **resultant moment = 0** about any point.
- A **uniform** rod has its weight acting at its midpoint. A **non-uniform** rod has its centre of mass at an unknown point, which you may need to find.
- Take moments about a point where an unknown force acts, so that force is eliminated.
:::ex Beam on two supports
Q: A uniform 6 m plank of mass 20 kg rests on supports at A (0 m) and B (5 m). A 50 kg child stands 4 m from A. Find the reactions.
1. Moments about A: $R_B\times5=20g\times3+50g\times4=260g$, so $R_B=52g=509.6$ N.
2. Vertically: $R_A+R_B=70g$, so $R_A=18g=176.4$ N.
A: $R_A=176$ N and $R_B=510$ N
:::
# Tilting
- When a rod is **on the point of tilting** about a support, the reaction at the **other** support is **zero**.
:::ex On the point of tilting
Q: In the plank example, how far beyond B can the child stand before the plank tilts?
1. On the point of tilting about B, $R_A=0$.
2. Moments about B: the plank's weight acts 2 m to the left of B, so $20g\times2=50g\times x$.
A: $x=0.8$ m beyond B, which is 5.8 m from A.
:::
:::ex Non-uniform rod
Q: A non-uniform 4 m rod of weight 60 N is suspended horizontally by two vertical strings at its ends. The tensions are 25 N and 35 N. Find the position of its centre of mass.
1. Moments about the 25 N end: $35\times4=60x$.
A: $x=2.33$ m from the end with the 25 N tension.
:::
## Rods held by strings at an angle
- If a rod is held by a string at an angle, resolve the tension into horizontal and vertical components. Only the component **perpendicular to the rod** produces a moment about a point on the rod.
- A **hinge** (or pivot) exerts a reaction with both horizontal and vertical components, $X$ and $Y$. Take moments about the hinge to eliminate both of them at once.
# Ladders and rods with friction (A level)
!fig k-ladder Forces on a ladder against a wall
- A ladder leaning against a **smooth wall** on **rough ground** has: weight at its centre, a normal reaction from the ground $R$, friction at the ground $F$ (towards the wall), and a normal reaction from the wall $S$ (perpendicular to the wall).
- Resolve horizontally ($F=S$) and vertically ($R=W$), then take moments about the foot of the ladder.
:::ex Ladder
Q: A uniform 4 m ladder of weight $W$ rests against a smooth wall at 60° to the ground. Find the least coefficient of friction needed for equilibrium.
1. Moments about the foot: $S\times4\sin60°=W\times2\cos60°$, so $S=\frac{W}{2\tan60°}=0.289W$.
2. $F=S$ and $R=W$, so we need $\mu\ge\frac FR=0.289$.
A: $\mu_{\min}=\frac{1}{2\sqrt3}\approx0.289$
:::
:::warn
- Using the distance along the rod instead of the perpendicular distance when a force is at an angle.
- Forgetting the weight of the rod.
- Giving friction at the wall when the wall is described as smooth.
:::
:::tip
- Taking moments about a point where two unknown forces meet removes both of them in one step.
:::
:::sum
- Moment = $F\times d_\perp$.
- Equilibrium: no resultant force and no resultant moment.
- Uniform rods have their weight at the midpoint; on the point of tilting, the other reaction is 0.
- Ladders: resolve both ways and take moments; friction is limited by $F\le\mu R$.
:::
