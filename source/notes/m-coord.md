@spec Edexcel 9MA0 Pure topic 3: 3.1 straight lines; 3.2 circles; 3.3 parametric equations; 3.4 parametric modelling
@intro Coordinate geometry describes lines and curves with equations. This topic covers straight lines (including parallel and perpendicular lines), circles and their properties, and curves defined by parametric equations.
# Straight lines
:::eq
$$m=\frac{y_2-y_1}{x_2-x_1}\qquad y-y_1=m(x-x_1)\qquad ax+by+c=0$$
:::
- **Parallel** lines have equal gradients. **Perpendicular** lines have $m_1m_2=-1$.
- Midpoint $=\left(\frac{x_1+x_2}{2},\frac{y_1+y_2}{2}\right)$, and distance $=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$.
- Straight-line models: interpret the gradient as a rate, and the intercept as a starting value.
:::ex Perpendicular bisector
Q: Find the perpendicular bisector of the segment joining $A(1,2)$ and $B(5,6)$.
1. The midpoint is $(3,4)$, and the gradient of $AB$ is $\frac{4}{4}=1$.
2. The perpendicular gradient is $-1$, so $y-4=-(x-3)$.
A: $y=-x+7$
:::
# Circles
:::eq
$$(x-a)^2+(y-b)^2=r^2\quad\text{centre }(a,b),\ \text{radius }r$$
:::
!fig m-circle Circle with centre (a, b) and radius r
- To find the centre and radius from $x^2+y^2+2fx+2gy+c=0$, **complete the square** for both $x$ and $y$.
- **Circle properties:** the angle in a semicircle is a right angle; the perpendicular from the centre to a chord bisects the chord; a tangent is perpendicular to the radius at the point of contact.
- A line meets a circle in 2, 1 (a tangent) or 0 points. Substitute and use the discriminant.
:::ex Centre and radius
Q: Find the centre and radius of $x^2+y^2-6x+4y-12=0$.
1. $(x-3)^2-9+(y+2)^2-4-12=0$.
2. $(x-3)^2+(y+2)^2=25$.
A: The centre is $(3,-2)$ and the radius is $5$.
:::
:::ex Tangent to a circle
Q: Find the tangent to $(x-3)^2+(y+2)^2=25$ at the point $(6,2)$.
1. The gradient of the radius from $(3,-2)$ to $(6,2)$ is $\frac43$.
2. The tangent's gradient is $-\frac34$, so $y-2=-\frac34(x-6)$.
A: $3x+4y-26=0$
:::
:::ex Does the line meet the circle?
Q: Show that the line $y=x+10$ does not meet the circle $x^2+y^2=25$.
1. Substitute: $x^2+(x+10)^2=25$, which simplifies to $2x^2+20x+75=0$.
2. The discriminant is $400-4(2)(75)=400-600=-200<0$.
A: There are no real solutions, so the line does not meet the circle.
:::
## Finding a circle through three points
- The centre lies on the **perpendicular bisector** of every chord. Find the perpendicular bisectors of two chords; they meet at the centre.
- If two of the points form a **diameter** (that is, the triangle has a right angle at the third point), the centre is the midpoint of that diameter. This is a quick shortcut worth checking for first.
- Then the radius is the distance from the centre to any of the points.
# Parametric equations (A level)
- A curve can be defined by $x=f(t)$ and $y=g(t)$, where $t$ is the parameter.
- To convert to a **Cartesian** equation, eliminate $t$. Use substitution, or an identity such as $\sin^2t+\cos^2t=1$.
- The domain and range of the Cartesian form come from the range of $t$.
:::ex Parametric to Cartesian
Q: A curve has $x=3\cos t$ and $y=2\sin t$. Find its Cartesian equation.
1. $\cos t=\frac{x}{3}$ and $\sin t=\frac y2$.
2. Use $\cos^2t+\sin^2t=1$.
A: $\dfrac{x^2}{9}+\dfrac{y^2}{4}=1$, an ellipse.
:::
:::ex Intersection with an axis
Q: The curve $x=t^2-1$, $y=2t+3$ meets the $y$-axis. Find the points.
1. On the $y$-axis $x=0$, so $t^2=1$ and $t=\pm1$.
2. $t=1$ gives $y=5$; $t=-1$ gives $y=1$.
A: $(0,5)$ and $(0,1)$
:::
## Sketching parametric curves
- Make a table of values of $t$, $x$ and $y$, and plot the points in order of increasing $t$. Add arrows to show the direction.
- Find where the curve crosses the axes by setting $x=0$ or $y=0$ and solving for $t$.
- To find the intersection with a line, substitute the parametric expressions into the line's equation, solve for $t$, and then work out $x$ and $y$.
- **Modelling with parametric equations:** for a projectile, $x=ut\cos\theta$ and $y=ut\sin\theta-\frac12gt^2$. The parameter is time, and you can find the range by setting $y=0$.
:::warn
- Misreading the sign of the centre. $(x+2)^2$ means the centre has $x=-2$.
- Forgetting to take the square root to find $r$ from $r^2$.
- Not restricting the Cartesian domain when $t$ is restricted.
:::
:::tip
- A sketch helps in almost every circle question. Mark the centre, the radius and any right angles.
:::
:::sum
- Lines: $y-y_1=m(x-x_1)$; perpendicular lines have $m_1m_2=-1$.
- Circles: $(x-a)^2+(y-b)^2=r^2$; complete the square; tangent ⟂ radius.
- Parametric equations: eliminate $t$ to get a Cartesian equation; use them to model motion.
:::
