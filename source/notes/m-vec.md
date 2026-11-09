@spec Edexcel 9MA0 Pure topic 10: 10.1 vectors in 2D and 3D; 10.2 magnitude and direction; 10.3 vector addition and scalar multiplication; 10.4 position vectors and distance; 10.5 geometric problems and modelling
@intro A vector has both size and direction. Vectors describe displacements, velocities and forces, and they make geometry problems (parallel lines, midpoints, ratios) almost mechanical.
# Notation and basics
!fig m-vectors Adding vectors tip to tail
- In 2D, a vector can be written as $\begin{pmatrix}a\\b\end{pmatrix}=a\mathbf i+b\mathbf j$. In 3D, $\mathbf k$ is added.
- **Magnitude:** $|\mathbf a|=\sqrt{a^2+b^2+c^2}$.
- A **unit vector** has magnitude 1: $\hat{\mathbf a}=\frac{\mathbf a}{|\mathbf a|}$.
- **Direction:** in 2D, the angle with $\mathbf i$ is $\tan^{-1}\frac ba$. In 3D, the angle with the $x$-axis satisfies $\cos\theta_x=\frac{a}{|\mathbf a|}$.
- For a magnitude $r$ at angle $\theta$ to $\mathbf i$, the vector is $r\cos\theta\,\mathbf i+r\sin\theta\,\mathbf j$.
:::ex Magnitude and unit vector
Q: Find the magnitude of $\mathbf a=2\mathbf i-3\mathbf j+6\mathbf k$, and a unit vector in its direction.
1. $|\mathbf a|=\sqrt{4+9+36}=7$.
A: $\hat{\mathbf a}=\frac17(2\mathbf i-3\mathbf j+6\mathbf k)$
:::
- **Equal vectors** have the same magnitude and the same direction, wherever they are drawn. **Negative vectors** have the same magnitude but the opposite direction: $\overrightarrow{BA}=-\overrightarrow{AB}$.
# Adding vectors and scalar multiples
- Add and subtract vectors component by component. Multiplying by a scalar $k$ scales the length and keeps (or reverses) the direction.
- Vectors $\mathbf a$ and $\mathbf b$ are **parallel** if $\mathbf b=k\mathbf a$ for some scalar $k$.
- If $\lambda\mathbf a+\mu\mathbf b=\mathbf 0$, and $\mathbf a$ and $\mathbf b$ are non-parallel, then $\lambda=\mu=0$. This lets you **compare coefficients** in geometry proofs.
# Position vectors and distance
- The **position vector** of $A$ is $\overrightarrow{OA}=\mathbf a$. Then $\overrightarrow{AB}=\mathbf b-\mathbf a$.
- The distance $AB$ is $|\mathbf b-\mathbf a|$, which in 3D is $\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}$.
- The **midpoint** of $AB$ has position vector $\frac12(\mathbf a+\mathbf b)$.
- The point dividing $AB$ in the ratio $m:n$ has position vector $\mathbf a+\frac{m}{m+n}(\mathbf b-\mathbf a)$.
:::ex Distance in 3D
Q: Find the distance between $A(1,2,-1)$ and $B(4,-2,11)$.
1. $\overrightarrow{AB}=(3,-4,12)$.
A: $|AB|=\sqrt{9+16+144}=13$
:::
# Geometric problems
:::ex Proving points are collinear
Q: $\overrightarrow{OA}=\mathbf a$ and $\overrightarrow{OB}=\mathbf b$. $P$ divides $AB$ in the ratio $1:2$, and $\overrightarrow{OQ}=2\mathbf a+\mathbf b$. Show that $O$, $P$ and $Q$ are collinear.
1. $\overrightarrow{OP}=\mathbf a+\frac13(\mathbf b-\mathbf a)=\frac23\mathbf a+\frac13\mathbf b=\frac13(2\mathbf a+\mathbf b)$.
2. So $\overrightarrow{OQ}=3\overrightarrow{OP}$. The two vectors are parallel, and they share the point $O$.
A: $O$, $P$ and $Q$ lie on a straight line, with $OP:PQ=1:2$.
:::
:::ex Comparing coefficients
Q: $\overrightarrow{OX}=\lambda(\mathbf a+\mathbf b)$ and also $\overrightarrow{OX}=\mathbf a+\mu(\mathbf b-\mathbf a)$, where $\mathbf a$ and $\mathbf b$ are not parallel. Find $\lambda$ and $\mu$.
1. Coefficients of $\mathbf a$: $\lambda=1-\mu$. Coefficients of $\mathbf b$: $\lambda=\mu$.
2. So $\mu=1-\mu$, which gives $\mu=\frac12$.
A: $\lambda=\mu=\frac12$, so $X$ is the midpoint of $AB$.
:::
:::ex Finding a fourth vertex
Q: $A(1,0,2)$, $B(3,1,5)$ and $C(4,-2,1)$ are three vertices of the parallelogram $ABCD$. Find $D$.
1. In a parallelogram, $\overrightarrow{AD}=\overrightarrow{BC}=(1,-3,-4)$.
2. $\mathbf d=\mathbf a+\overrightarrow{BC}$.
A: $D=(2,-3,-2)$
:::
## Strategy for geometry problems
- Draw a clear diagram and label the known vectors.
- Express every required vector as a route through known points. For example, $\overrightarrow{MN}=\overrightarrow{MO}+\overrightarrow{ON}$.
- If a point lies on a line, introduce a scalar parameter ($\lambda$ or $\mu$) for "some fraction of the way along".
- Write the same vector in two different ways, then compare the coefficients of the non-parallel base vectors.
# Modelling with vectors
- In mechanics, forces, velocities and accelerations are vectors. The resultant force is the vector sum of the forces, and Newton's second law becomes $\mathbf F=m\mathbf a$.
- Position at time $t$ with constant velocity: $\mathbf r=\mathbf r_0+t\mathbf v$.
:::ex Ship moving with constant velocity
Q: A ship starts at $(2\mathbf i+3\mathbf j)$ km and moves with velocity $(4\mathbf i-\mathbf j)$ km h⁻¹. Find its position and its distance from the origin after 2 hours.
1. $\mathbf r=(2+8)\mathbf i+(3-2)\mathbf j=10\mathbf i+\mathbf j$.
A: Its position is $10\mathbf i+\mathbf j$, at a distance of $\sqrt{101}\approx10.0$ km.
:::
:::warn
- Writing $\overrightarrow{AB}=\mathbf a-\mathbf b$. It is **end minus start**: $\mathbf b-\mathbf a$.
- Confusing a position (a point) with a displacement (a vector between two points).
- Giving a direction without saying which axis the angle is measured from.
:::
:::tip
- To prove that points are collinear, show that two vectors are scalar multiples of each other **and** that they share a common point.
:::
:::sum
- Magnitude $\sqrt{a^2+b^2+c^2}$; unit vector $\frac{\mathbf a}{|\mathbf a|}$.
- Parallel vectors: $\mathbf b=k\mathbf a$. $\overrightarrow{AB}=\mathbf b-\mathbf a$; midpoint $\frac12(\mathbf a+\mathbf b)$.
- Vectors are used for geometry proofs and for modelling forces and motion.
:::
