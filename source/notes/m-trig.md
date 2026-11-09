# Basics
- Radians: $\pi\text{ rad}=180^\circ$. Arc length $s=r\theta$; sector area $A=\frac12r^2\theta$ ($\theta$ in radians).
- Small angles: $\sin\theta\approx\theta$, $\tan\theta\approx\theta$, $\cos\theta\approx1-\frac{\theta^2}2$.
- Sine rule $\frac a{\sin A}=\frac b{\sin B}$ (watch for the ambiguous case). Cosine rule $a^2=b^2+c^2-2bc\cos A$. Area $\frac12ab\sin C$.
!fig m-unit-circle
!fig m-trig-graphs
!fig m-cast
# Identities
$$\sin^2\theta+\cos^2\theta=1$$
$$1+\tan^2\theta=\sec^2\theta$$
$$1+\cot^2\theta=\csc^2\theta$$
$$\sin(A\pm B)=\sin A\cos B\pm\cos A\sin B$$
$$\cos(A\pm B)=\cos A\cos B\mp\sin A\sin B$$
$$\sin2A=2\sin A\cos A$$
$$\cos2A=1-2\sin^2A=2\cos^2A-1$$
$$\tan2A=\frac{2\tan A}{1-\tan^2A}$$
# Harmonic form
$a\sin\theta+b\cos\theta=R\sin(\theta+\alpha)$, where $R=\sqrt{a^2+b^2}$ and $\tan\alpha=\frac ba$.
- Max value $R$, min value $-R$. Use it to solve equations and find extrema.
# Inverse trig
- $\arcsin$: domain $[-1,1]$, range $[-\frac\pi2,\frac\pi2]$. $\arccos$: range $[0,\pi]$. $\arctan$: range $(-\frac\pi2,\frac\pi2)$.
# Worked example
Solve $2\cos^2x=1+\sin x$ for $0\le x<2\pi$.
$2(1-\sin^2x)=1+\sin x \Rightarrow 2\sin^2x+\sin x-1=0 \Rightarrow (2\sin x-1)(\sin x+1)=0$.
So $\sin x=\frac12$, giving $x=\frac\pi6,\frac{5\pi}6$; or $\sin x=-1$, giving $x=\frac{3\pi}2$.
# Exam tips
> Check the interval and units (degrees or radians). Find **all** solutions using the CAST diagram or the graph's symmetry.
- Never divide both sides by $\sin x$: you lose the solutions where $\sin x=0$. Factorise instead.
