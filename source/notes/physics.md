## p-1
### Planning and implementing
- **Independent variable:** the one you change. **Dependent variable:** the one you measure. **Control variables:** kept constant.
- Choose instruments with a suitable **resolution**, the smallest change they can show (e.g. a micrometer reads to 0.01 mm).
- Repeat readings and take the mean, discarding anomalies. Check for zero errors.
### Analysis
- **Accuracy:** how close a value is to the true value. **Precision:** how close repeated readings are to each other.
- **Random errors** cause scatter; reduce them by repeating and averaging. **Systematic errors** shift every reading the same way (e.g. a zero error); they are not reduced by repeating.
- Straight-line graphs: compare with $y=mx+c$. Take the gradient from a large triangle.
- Log graphs: if $y=kx^n$, then $\lg y=n\lg x+\lg k$, so the gradient is $n$.
!fig p-errorbars
### Evaluation
- Percentage difference from the accepted value: $\frac{|\text{exp}-\text{accepted}|}{\text{accepted}}\times100\%$.
- Error bars show the uncertainty. Worst-fit lines give the uncertainty in the gradient.
### Exam tips
> "Suggest an improvement": be specific, e.g. "use a data-logger with a light gate to remove human reaction time", not just "be more accurate".

## p-2-1
### SI base units
- kg, m, s, A, K, mol (also cd). Every other unit is derived from these, e.g. N = kg m s⁻², J = kg m² s⁻², V = kg m² s⁻³ A⁻¹, C = A s.
### Prefixes
- p $10^{-12}$, n $10^{-9}$, μ $10^{-6}$, m $10^{-3}$, c $10^{-2}$, k $10^{3}$, M $10^{6}$, G $10^{9}$, T $10^{12}$.
### Homogeneity
- An equation is homogeneous if both sides have the same base units. This is necessary for the equation to be correct, but not sufficient (numerical constants such as $\frac12$ can't be checked this way).
### Worked example
Check that $E_k=\frac12mv^2$ is homogeneous: $\text{kg}\,(\text{m s}^{-1})^2=\text{kg m}^2\text{s}^{-2}=\text{J}$ ✓.
### Estimation
- Mass of an adult ≈ 70 kg; walking speed ≈ 1.5 m s⁻¹; height of a room ≈ 2.5 m; power of a kettle ≈ 2 kW.
### Exam tips
> Convert everything to base SI units before substituting into equations. Squared prefixes trip people up: $1\text{ cm}^2=10^{-4}\text{ m}^2$.

## p-2-2
### Uncertainties
- **Absolute uncertainty:** e.g. $(2.40\pm0.05)\text{ m}$. **Percentage uncertainty** $=\frac{\Delta x}{x}\times100\%$.
- Adding or subtracting quantities: **add the absolute** uncertainties.
- Multiplying or dividing: **add the percentage** uncertainties.
- Powers: $y=x^n$ gives (% in $y$) $= n\times$(% in $x$).
- Uncertainty from repeat readings: $\pm\frac12\times$range.
- From a graph: $\%\text{ uncertainty}=\frac{|\text{best}-\text{worst gradient}|}{\text{best gradient}}\times100\%$.
### Worked example
Diameter $d=(0.50\pm0.01)$ mm is a 2% uncertainty, so the area $A=\frac{\pi d^2}{4}$ has uncertainty $2\times2\%=4\%$.
Resistivity $\rho=\frac{RA}{L}$ with $R$ ±3% and $L$ ±1%: the total is $3+4+1=8\%$.
### Significant figures
- Give the final answer to the same number of s.f. as the least precise data.
- The uncertainty in a mean is about half the range of the repeat readings. Anomalies are excluded before averaging.
### Exam tips
> Quote the final uncertainty to 1 (or 2) significant figures, and match the decimal places of the value to it.

## p-2-3
### Scalars and vectors
- **Scalar:** magnitude only (mass, speed, energy, distance). **Vector:** magnitude and direction (force, velocity, displacement, acceleration, momentum).
### Combining vectors
- Two perpendicular vectors: $R=\sqrt{F_1^2+F_2^2}$, at angle $\theta=\tan^{-1}\frac{F_2}{F_1}$.
- Non-perpendicular: use a scale drawing, or the cosine rule ($R^2=a^2+b^2-2ab\cos C$).
- Equilibrium of three coplanar forces: they form a **closed triangle**.
### Resolving
$$F_x=F\cos\theta,\qquad F_y=F\sin\theta$$
- On a slope at $\theta$: the component of weight along the slope is $mg\sin\theta$; perpendicular to it is $mg\cos\theta$.
### Worked example
A 12 N force acts at $30^\circ$ above the horizontal: $F_x=12\cos30^\circ=10.4$ N and $F_y=6.0$ N.
### Exam tips
> Make sure the angle you use is the one between the force and the direction you are resolving along.

## p-3-1
### Definitions
- **Displacement** $s$: distance in a given direction. **Velocity** $v=\frac{\Delta s}{\Delta t}$. **Acceleration** $a=\frac{\Delta v}{\Delta t}$.
- Graphs: the gradient of $s$–$t$ is velocity; the gradient of $v$–$t$ is acceleration; the area under $v$–$t$ is displacement.
!fig p-vt-graph
### suvat (constant acceleration)
$$v=u+at$$
$$s=\tfrac12(u+v)t$$
$$s=ut+\tfrac12at^2$$
$$v^2=u^2+2as$$
### Free fall and projectiles
- Free fall: $g=9.81\text{ m s}^{-2}$. Measure $g$ with light gates, a trapdoor and electromagnet, or video.
- Projectiles: horizontal and vertical motion are **independent**. Horizontal velocity is constant (no air resistance); vertical acceleration is $g$.
- **Stopping distance** = thinking distance ($v\times$ reaction time) + braking distance.
!fig p-projectile
### Worked example
A ball is kicked horizontally at $8.0\text{ m s}^{-1}$ off a 20 m cliff. Vertically: $20=\frac12(9.81)t^2$, so $t=2.02$ s. Horizontal distance: $8.0\times2.02=16$ m.
### Exam tips
> List your s, u, v, a, t values first, and take one direction as positive (e.g. up = +, so $a=-9.81$).
- Doubling the speed doubles the thinking distance but **quadruples** the braking distance.

## p-3-2
### Forces
- $F=ma$; weight $W=mg$. **Drag** increases with speed. **Terminal velocity** is reached when drag + upthrust = weight, so $a=0$.
- **Upthrust** $=$ weight of fluid displaced $=\rho Vg$ (Archimedes).
- Pressure $p=\frac FA$. In a fluid, $p=h\rho g$.
!fig p-slope-fbd
!fig p-terminal
### Moments and equilibrium
- Moment $=F\times d_\perp$. **Couple:** torque $=F\times$ perpendicular separation of the two forces.
- **Principle of moments:** in equilibrium, the sum of clockwise moments equals the sum of anticlockwise moments, and the resultant force is zero.
- **Centre of mass:** the point where the weight appears to act.
!fig p-moments
### Worked example
A 500 g object is fully submerged in water ($\rho=1000\text{ kg m}^{-3}$) with volume $2.0\times10^{-4}\text{ m}^3$. Upthrust $=1000\times2.0\times10^{-4}\times9.81=1.96$ N, so its apparent weight is $4.91-1.96=2.95$ N.
### Exam tips
> Free-body diagrams: label every force, and draw each arrow from the point where the force acts.

## p-3-3
### Work done
$$W=Fx\cos\theta$$
- **Work done** is the energy transferred when a force moves an object; it equals the force × the distance moved **in the direction of the force**.
- 1 joule is the work done when a force of 1 N moves its point of application 1 m in the direction of the force.
- A force at right angles to the motion ($\theta=90^\circ$) does no work, e.g. the normal reaction on a horizontal floor or a centripetal force.
!fig p-work-angle
- The area under a force–displacement graph is the work done.
### Kinetic and potential energy
$$E_k=\tfrac12mv^2,\qquad \Delta E_p=mg\Delta h$$
- $E_k=\frac12mv^2$ comes from $W=Fs$ with $F=ma$ and $v^2=2as$.
- $mg\Delta h$ is valid near the Earth's surface, where $g$ is constant.
### Conservation of energy
- **Principle of conservation of energy:** energy cannot be created or destroyed; it can only be transferred from one form to another. The total energy of a closed system is constant.
- With no air resistance, a falling object's loss of $E_p$ equals its gain in $E_k$: $mgh=\frac12mv^2$, so $v=\sqrt{2gh}$ (independent of mass).
- With resistive forces: loss of $E_p$ = gain in $E_k$ + work done against friction or drag.
### Power and efficiency
$$P=\frac{W}{t}=Fv$$
$$\text{efficiency}=\frac{\text{useful output energy (or power)}}{\text{total input energy (or power)}}\times100\%$$
- **Power** is the rate of doing work (rate of energy transfer); $1\text{ W}=1\text{ J s}^{-1}$.
- $P=Fv$ follows from $P=\frac{F\Delta x}{\Delta t}$. At top speed, the driving force equals the resistive forces.
### Worked examples
A car with a 30 kW engine has a top speed of $25\text{ m s}^{-1}$. The resistive force is $F=\frac Pv=\frac{30000}{25}=1200$ N.
A 0.50 kg ball is dropped from 8.0 m and lands at $11\text{ m s}^{-1}$. Loss of $E_p=0.50\times9.81\times8.0=39.2$ J; gain in $E_k=\frac12\times0.50\times11^2=30.3$ J. Work done against air resistance $=39.2-30.3=9.0$ J, so the average drag is $\frac{9.0}{8.0}=1.1$ N.
A motor lifts a 20 kg load through 3.0 m in 4.0 s, taking 250 W from the supply. Useful power $=\frac{20\times9.81\times3.0}{4.0}=147$ W, so the efficiency is $\frac{147}{250}=59\%$.
### Common mistakes
- Using the total distance instead of the distance **along the force** (use $\cos\theta$).
- Using mass instead of weight in $W=Fx$ (weight = $mg$).
- Writing efficiency greater than 100%, or forgetting to square $v$ in $E_k$.
### Exam tips
> In energy questions, write the energy statement in words first ("loss of GPE = gain in KE + work against drag"), then substitute. It earns method marks even if the arithmetic slips.

## p-3-4
### Springs
- **Hooke's law:** $F=kx$ (up to the limit of proportionality).
- Elastic potential energy $E=\frac12Fx=\frac12kx^2$, the area under the $F$–$x$ graph.
- Series springs: $\frac1k=\frac1{k_1}+\frac1{k_2}$. Parallel springs: $k=k_1+k_2$.
!fig p-force-ext
### Materials
$$\sigma=\frac FA,\qquad \varepsilon=\frac xL,\qquad E=\frac\sigma\varepsilon$$
- Young modulus unit: Pa. Find it from the gradient of the linear part of the stress–strain graph.
- **Elastic deformation:** returns to its original shape. **Plastic:** permanent extension.
- **Ductile** (copper): large plastic region. **Brittle** (glass): breaks with no plastic deformation. **Polymeric** (rubber): loading and unloading curves differ (hysteresis); the area between them is energy lost as heat.
- **UTS:** the maximum stress a material can withstand.
!fig p-stress-strain
### Exam tips
> Determining $E$ for a wire: use a long wire (larger extension), measure the diameter with a micrometer in several places, and use the gradient of the stress–strain graph.

## p-3-5
### Newton's laws
- **N1:** a body stays at rest or at constant velocity unless a resultant force acts.
- **N2:** $F=\frac{\Delta p}{\Delta t}$, which gives $F=ma$ for constant mass.
- **N3:** when A exerts a force on B, B exerts an equal and opposite force of the same type on A.
### Momentum
$$p=mv,\qquad \text{impulse}=F\Delta t=\Delta p$$
- Impulse is the area under the $F$–$t$ graph (unit N s).
- Momentum is **conserved** in a closed system.
- **Elastic collision:** kinetic energy is also conserved. **Inelastic collision:** some kinetic energy is transferred to other forms.
!fig p-collision
### Worked example
A 2.0 kg trolley at $3.0\text{ m s}^{-1}$ hits a stationary 1.0 kg trolley and they stick together: $6.0=3.0v$, so $v=2.0\text{ m s}^{-1}$. Kinetic energy goes from 9.0 J to 6.0 J, so the collision is inelastic.
### Exam tips
> Momentum is a vector, so give a sign to each direction. Airbags and crumple zones increase $\Delta t$, which reduces the force for the same $\Delta p$.

## p-4-1
### Charge and current
$$I=\frac{\Delta Q}{\Delta t}$$
- 1 C is the charge passing a point when 1 A flows for 1 s. Elementary charge $e=1.60\times10^{-19}$ C, so charge is **quantised**.
- **Kirchhoff's 1st law:** the current into a junction equals the current out (conservation of charge).
- In metals, the charge carriers are electrons. In electrolytes, they are ions.
### Mean drift velocity
$$I=Anev$$
- $n$ is the number density of charge carriers. Metals have $n\approx10^{28}\text{ m}^{-3}$, so $v$ is tiny (about mm s⁻¹). Semiconductors have a much smaller $n$.
### Worked example
$I=2.0$ A in copper ($n=8.5\times10^{28}$) with $A=1.0\times10^{-6}\text{ m}^2$: $v=\frac{2.0}{1.0\times10^{-6}\times8.5\times10^{28}\times1.6\times10^{-19}}=1.5\times10^{-4}\text{ m s}^{-1}$.
### Exam tips
> If a wire narrows, the current is the same, so a smaller $A$ means the drift velocity increases.

## p-4-2
### Definitions
- **p.d.** $V=\frac WQ$: energy transferred from electrical to other forms per unit charge. **e.m.f.** $\varepsilon=\frac WQ$: energy transferred to electrical form per unit charge.
- Energy gained by an electron accelerated through $V$: $eV=\frac12mv^2$.
- Resistance $R=\frac VI$. **Ohm's law:** $I\propto V$ for a metallic conductor at constant temperature.
### I–V characteristics
- Resistor: a straight line through the origin. Filament lamp: a curve (resistance rises as it gets hotter). Diode: conducts only in forward bias, above about 0.6 V. LED: about 2 V.
- **NTC thermistor:** resistance falls as temperature rises. **LDR:** resistance falls as light intensity rises.
!fig p-iv
### Resistivity and power
$$R=\frac{\rho L}{A}$$
$$P=VI=I^2R=\frac{V^2}{R},\qquad W=VIt$$
- 1 kWh $=3.6\times10^6$ J. Cost = kWh × price per kWh.
### Exam tips
> Resistivity is a property of the **material**; resistance depends on its dimensions too. For a metal, $\rho$ rises with temperature.

## p-4-3
### Circuit rules
- **Kirchhoff's 2nd law:** around any loop, the sum of e.m.f.s equals the sum of p.d.s (conservation of energy).
- Series: $R=R_1+R_2+\dots$ Parallel: $\frac1R=\frac1{R_1}+\frac1{R_2}+\dots$
!fig p-series-parallel
### Internal resistance
$$\varepsilon=I(R+r),\qquad V=\varepsilon-Ir$$
- "Lost volts" $=Ir$. A graph of $V$ against $I$ has gradient $-r$ and $y$-intercept $\varepsilon$.
### Potential divider
$$V_{out}=\frac{R_2}{R_1+R_2}V_{in}$$
- With an LDR or thermistor in place of $R_2$, $V_{out}$ responds to light or temperature (sensor circuits).
- A potentiometer gives a continuously variable output.
!fig p-potdiv
### Worked example
$\varepsilon=6.0$ V, $r=0.50\ \Omega$, $R=5.5\ \Omega$: $I=\frac{6.0}{6.0}=1.0$ A, so the terminal p.d. is $V=5.5$ V.
### Exam tips
> An ideal voltmeter has infinite resistance; an ideal ammeter has zero resistance. In potential-divider questions, say what happens to $R$, then to $V_{out}$, and why.

## p-4-4
### Wave basics
$$v=f\lambda,\qquad f=\frac1T$$
- **Progressive waves** transfer energy. **Transverse waves** oscillate perpendicular to the direction of travel; **longitudinal** waves oscillate parallel to it.
- **Phase difference** $=\frac{x}{\lambda}\times360^\circ$. Intensity $I=\frac PA$, and $I\propto A^2$.
- Only transverse waves can be **polarised**: their oscillations are restricted to one plane. Crossed polarising filters (or a metal grille for microwaves) block the wave.
!fig p-wave
### Electromagnetic waves
- All travel at $c=3.00\times10^8\text{ m s}^{-1}$ in a vacuum. Order: radio, micro, IR, visible (400–700 nm), UV, X-ray, γ.
- **Refraction:** $n=\frac cv$; $n_1\sin\theta_1=n_2\sin\theta_2$. Total internal reflection when $\theta>C$, where $\sin C=\frac1n$ (going into air).
### Superposition and stationary waves
- **Coherent sources:** constant phase difference. Path difference $n\lambda$ gives constructive interference; $(n+\frac12)\lambda$ gives destructive.
- **Young's double slit:** $\lambda=\frac{ax}{D}$. **Grating:** $d\sin\theta=n\lambda$.
- **Stationary waves** form from two waves of the same frequency travelling in opposite directions. Node-to-node distance $=\frac\lambda2$. They store energy rather than transferring it.
- Pipe closed at one end: $L=\frac\lambda4$ for the fundamental. String or open pipe: $L=\frac\lambda2$.
!fig p-interference
!fig p-stationary
### Exam tips
> In Young's slits, $a$ is the slit separation, $x$ is the fringe spacing, and $D$ is the slit-to-screen distance. Measure across several fringes and divide.

## p-4-5
### Photons
$$E=hf=\frac{hc}{\lambda}$$
- 1 eV $=1.60\times10^{-19}$ J. LEDs can be used to find $h$: $eV_0=\frac{hc}\lambda$.
!fig p-energy-levels
### Photoelectric effect
$$hf=\phi+KE_{max}$$
- The **threshold frequency** is $f_0=\frac\phi h$. Below it, no electrons are emitted, however intense the light.
- A higher intensity means more photons per second, so more electrons, but **not** a higher $KE_{max}$.
- Emission is instantaneous and one-to-one (one photon, one electron). This is evidence for the particle nature of light.
!fig p-photoelectric
### Wave–particle duality
$$\lambda=\frac hp=\frac h{mv}$$
- Electron diffraction through graphite is evidence that particles behave as waves (spacing ≈ λ).
### Worked example
UV of wavelength 200 nm falls on a metal with $\phi=4.5$ eV. $E=\frac{6.63\times10^{-34}\times3.0\times10^8}{200\times10^{-9}}=9.9\times10^{-19}\text{ J}=6.2$ eV, so $KE_{max}=1.7$ eV.
### Exam tips
> Convert between eV and J carefully. Wave theory can't explain the threshold frequency; only the photon model can.

## p-5-1
### Temperature and phases
- Thermal equilibrium: no net flow of energy between objects. $T(\text{K})=\theta(^\circ\text{C})+273$. Absolute zero (0 K) is the lowest possible internal energy.
- **Internal energy:** the sum of the random kinetic and potential energies of the particles.
- During a change of phase, $T$ stays constant: the potential energy changes, not the kinetic energy.
### Specific heat and latent heat
$$Q=mc\Delta\theta,\qquad Q=mL$$
- $c$ in J kg⁻¹ K⁻¹; $L_f$ for fusion and $L_v$ for vaporisation, in J kg⁻¹.
!fig p-heating
### Ideal gases
$$pV=nRT=NkT$$
- Assumptions: a large number of identical molecules moving randomly; negligible molecular volume; elastic collisions; no forces between molecules except during collisions; collision time much less than the time between collisions.
$$pV=\tfrac13Nm\overline{c^2},\qquad \tfrac12m\overline{c^2}=\tfrac32kT$$
- $k=\frac R{N_A}=1.38\times10^{-23}\text{ J K}^{-1}$. The r.m.s. speed is $\sqrt{\overline{c^2}}$.
- Boyle's law: $pV$ is constant at constant $T$.
### Worked example
Mean KE of a molecule at 300 K: $\frac32\times1.38\times10^{-23}\times300=6.2\times10^{-21}$ J.
### Exam tips
> Always use kelvin in gas equations. $n$ is in moles; $N$ is the number of molecules.

## p-5-2
### Circular motion
$$\omega=\frac{2\pi}{T}=2\pi f,\qquad v=\omega r$$
$$a=\frac{v^2}r=\omega^2r,\qquad F=\frac{mv^2}r=m\omega^2r$$
- 1 radian is the angle subtended by an arc equal in length to the radius.
- Constant speed but **changing velocity**, so it is accelerating towards the centre. The centripetal force is provided by something real (tension, gravity, friction, a reaction force).
!fig p-circular
### Vertical circles
- At the top: $T+mg=\frac{mv^2}r$. At the bottom: $T-mg=\frac{mv^2}r$.
- Minimum speed at the top (string just slack): $v=\sqrt{gr}$.
### Worked example
A 0.20 kg mass on a 0.50 m string moves at $3.0\text{ m s}^{-1}$ in a horizontal circle (on a table): $F=\frac{0.20\times9.0}{0.50}=3.6$ N.
### Common mistakes
- Using degrees in $v=\omega r$: angles must be in radians.
- Saying an object in uniform circular motion is in equilibrium. Its velocity is changing, so there is a resultant force towards the centre.
- At the top of a vertical circle the weight helps provide the centripetal force, so the tension is smallest there.
### Exam tips
> Centripetal force is **not** an extra force on the free-body diagram. It is the resultant of the real forces.

## p-5-3
### SHM
$$a=-\omega^2x$$
- SHM: the acceleration is proportional to the displacement and directed towards the equilibrium position.
$$x=A\cos\omega t$$
$$v=\pm\omega\sqrt{A^2-x^2},\qquad v_{max}=\omega A$$
- The period is independent of amplitude (isochronous). Pendulum: $T=2\pi\sqrt{\frac Lg}$. Mass–spring: $T=2\pi\sqrt{\frac mk}$.
- Energy swaps between KE and PE; the total is constant ($\propto A^2$) without damping.
!fig p-shm
### Damping and resonance
- **Light damping:** the amplitude decays gradually. **Critical damping:** returns to equilibrium in the shortest time without oscillating. **Heavy damping:** returns slowly.
- **Forced oscillations:** resonance happens when the driving frequency equals the natural frequency, giving maximum amplitude. Damping lowers and broadens the peak (and shifts it slightly lower).
### Worked example
$A=0.050$ m, $f=2.0$ Hz: $\omega=4\pi$, so $v_{max}=0.63\text{ m s}^{-1}$ and $a_{max}=\omega^2A=7.9\text{ m s}^{-2}$.
### Exam tips
> Use $x=A\sin\omega t$ if timing starts at equilibrium, and $\cos$ if it starts at maximum displacement. Set your calculator to radians.

## p-5-4
### Fields
$$g=\frac Fm,\qquad g=-\frac{GM}{r^2}$$
- Field lines are radial for a point mass and uniform close to the Earth's surface. $G=6.67\times10^{-11}\text{ N m}^2\text{kg}^{-2}$.
- Newton's law: $F=-\frac{GMm}{r^2}$, which is attractive.
!fig p-gfield
### Orbits
- Kepler 1: elliptical orbits with the Sun at one focus. Kepler 2: equal areas in equal times. Kepler 3: $T^2\propto r^3$.
$$T^2=\frac{4\pi^2}{GM}r^3,\qquad v=\sqrt{\frac{GM}r}$$
- **Geostationary orbit:** $T=24$ h, above the equator, moving in the same direction as the Earth spins.
### Potential
$$V_g=-\frac{GM}r,\qquad E=-\frac{GMm}r$$
- Potential is the work done per unit mass to bring a mass from infinity to that point. It is negative.
- Escape velocity: $v=\sqrt{\frac{2GM}r}$.
- The area under a force–distance graph is the work done (change in potential energy).
### Exam tips
> $r$ is measured from the **centre** of the planet, so add the planet's radius to the height of the orbit.

## p-5-5
### Stars
- Life cycle: nebula, protostar, main sequence (H fusion). Low-mass stars become red giants, then white dwarfs. High-mass stars become red supergiants, then a supernova, leaving a neutron star or black hole.
- **Chandrasekhar limit:** $1.44M_\odot$; electron degeneracy pressure supports a white dwarf below it.
- HR diagram: luminosity against temperature (temperature *decreasing* to the right).
### Radiation
$$\lambda_{max}T=\text{constant}\ (2.9\times10^{-3}\text{ m K})$$
$$L=4\pi r^2\sigma T^4$$
- Energy levels: $\Delta E=hf$. Emission and absorption line spectra. Grating: $d\sin\theta=n\lambda$.
### Cosmology
- Units: 1 AU (Earth–Sun distance), 1 ly, 1 pc ≈ $3.1\times10^{16}$ m. Parallax: $p(\text{arcsec})=\frac1{d(\text{pc})}$.
- Doppler: $\frac{\Delta\lambda}\lambda\approx\frac vc$. **Hubble's law** $v=H_0d$; the age of the universe is about $\frac1{H_0}$.
- Cosmological principle: the universe is isotropic and homogeneous on large scales. Evidence for the Big Bang: the CMB (about 2.7 K) and galactic redshift. Dark matter and dark energy.
### Exam tips
> Convert $H_0$ from km s⁻¹ Mpc⁻¹ to s⁻¹ before computing the age: $1\text{ Mpc}=3.1\times10^{22}$ m.

## p-6-1
### Key definitions
- **Capacitance:** the charge stored per unit potential difference, $C=\frac QV$. Unit: the farad, $1\text{ F}=1\text{ C V}^{-1}$. Typical values are µF (10⁻⁶) to nF (10⁻⁹).
- A capacitor has two conducting plates separated by an insulator (the dielectric). Charge $+Q$ builds on one plate and $-Q$ on the other; no charge flows through the gap.
### Combining capacitors
$$\text{parallel: } C=C_1+C_2+\dots\qquad\text{series: } \frac1C=\frac1{C_1}+\frac1{C_2}+\dots$$
- These are the **opposite** of the resistor rules. In series each capacitor stores the same charge $Q$; in parallel each has the same p.d.
- Parallel-plate capacitor: $C=\frac{\varepsilon_0\varepsilon_rA}{d}$, so a larger area or a smaller gap gives a larger capacitance.
### Energy stored
$$W=\tfrac12QV=\tfrac12CV^2=\frac{Q^2}{2C}$$
- The area under a $V$–$Q$ graph (a straight line through the origin) is the energy stored.
- When a battery charges a capacitor it does work $QV$, but only $\frac12QV$ is stored; the other half is dissipated as heat in the resistance of the circuit.
### Charging and discharging
!fig p-cap-circuit
$$\tau=RC$$
$$\text{discharge: } x=x_0e^{-t/RC}\quad(x = Q,\ V\text{ or }I)$$
$$\text{charging: } V=V_0\left(1-e^{-t/RC}\right)$$
$$Q=Q_0\left(1-e^{-t/RC}\right),\quad I=I_0e^{-t/RC}$$
- After one time constant ($t=RC$) a discharging capacitor has $e^{-1}=37\%$ of its starting value; a charging one has reached 63% of its final value.
- **Constant-ratio property:** in equal time intervals the value falls by the same fraction, e.g. the time to halve is always $t_{1/2}=RC\ln2\approx0.69RC$.
- Taking logs of the discharge equation: $\ln V=\ln V_0-\frac{t}{RC}$, so a graph of $\ln V$ against $t$ is a straight line with gradient $-\frac1{RC}$.
- The area under an $I$–$t$ graph is the charge that has flowed.
!fig p-discharge
!fig p-charging
### Modelling by iteration
- Over a small time step $\Delta t$: $\Delta Q=-\frac{Q}{RC}\Delta t$. Repeating this in a spreadsheet gives the exponential decay; smaller $\Delta t$ gives a more accurate model.
### Worked examples
$C=470\ \mu$F and $R=10$ kΩ give $\tau=470\times10^{-6}\times10\times10^3=4.7$ s. The time for the p.d. to halve is $t=RC\ln2=3.3$ s.
A 2200 µF capacitor is charged to 12 V. Energy stored: $W=\frac12CV^2=\frac12\times2200\times10^{-6}\times144=0.16$ J. Charge: $Q=CV=0.026$ C.
The p.d. across a discharging capacitor falls from 9.0 V to 3.0 V in 5.0 s. Then $\frac{3}{9}=e^{-5/RC}$, so $RC=\frac{5.0}{\ln3}=4.6$ s.
### Uses
- Flash guns and defibrillators (release stored energy quickly), back-up power for memory, smoothing a rectified supply, and timing circuits (choose $RC$).
### Common mistakes
- Forgetting to convert µF to F (×10⁻⁶) and kΩ to Ω (×10³).
- Using the resistor rules for capacitors in series and parallel.
- Thinking the current is constant: it is largest at the start and decays exponentially in **both** charging and discharging (it reverses direction on discharge).
### Exam tips
> If the question gives the time for the value to fall to a fraction, rearrange using natural logs: $t=RC\ln\frac{x_0}{x}$. Show the log step clearly for method marks.

## p-6-2
### Key definitions
- **Electric field:** a region in which a charged object experiences a force.
- **Electric field strength** $E$: the force per unit **positive** charge, $E=\frac Fq$. Units: N C⁻¹ (equivalent to V m⁻¹). It is a vector, pointing in the direction of the force on a positive charge.
- Field lines go from + to −; closer lines mean a stronger field.
!fig p-efield-radial
### Coulomb's law (point charges)
$$F=\frac{Qq}{4\pi\varepsilon_0r^2},\qquad E=\frac{Q}{4\pi\varepsilon_0r^2}$$
- Inverse-square law: doubling $r$ quarters the force. A charged sphere behaves as if its charge were at its centre (for points outside it).
- Like charges repel and unlike charges attract. $\varepsilon_0=8.85\times10^{-12}\text{ F m}^{-1}$ is the permittivity of free space.
### Uniform fields
$$E=\frac Vd$$
- Between parallel plates the field is uniform (equally spaced parallel lines), except near the edges.
!fig p-efield-plates
- A charged particle entering at right angles to a uniform field has a constant force $F=qE$ perpendicular to its velocity, so it follows a **parabola**: constant velocity along the plates, constant acceleration $a=\frac{qE}m$ across them.
!fig p-electron-deflect
- Work done moving a charge through a p.d.: $W=qV$. An electron accelerated through $V$ gains $E_k=eV$.
### Electric potential
$$V=\frac{Q}{4\pi\varepsilon_0r},\qquad E_p=qV=\frac{Qq}{4\pi\varepsilon_0r}$$
- **Electric potential** at a point: the work done per unit positive charge in bringing a small test charge from infinity to that point. It is zero at infinity, positive near a positive charge and negative near a negative charge.
- **Equipotentials** are surfaces of constant potential; they are perpendicular to field lines, and no work is done moving along one.
- Field strength is the potential gradient: $E=-\frac{\Delta V}{\Delta r}$. The area under an $E$–$r$ graph is the change in potential.
- Capacitance of an isolated sphere of radius $R$: $C=4\pi\varepsilon_0R$.
### Comparison with gravitational fields
- Both are inverse-square, both have $\frac1r$ potentials, and both field strengths are force per unit (mass or charge).
- Gravity acts on mass and is **always attractive** (so $V_g$ is always negative). Electric forces act on charge and can attract or repel.
- Electric forces between particles are vastly stronger: for two protons, the electric force is about $10^{36}$ times the gravitational force.
### Worked examples
Force between charges of $+2.0\ \mu$C and $-3.0\ \mu$C, 0.10 m apart: $F=\frac{2.0\times10^{-6}\times3.0\times10^{-6}}{4\pi\times8.85\times10^{-12}\times0.10^2}=5.4$ N, attractive.
Plates 4.0 cm apart with a p.d. of 2000 V: $E=\frac{2000}{0.040}=5.0\times10^4\text{ V m}^{-1}$. Force on an electron: $F=eE=1.60\times10^{-19}\times5.0\times10^4=8.0\times10^{-15}$ N.
### Common mistakes
- Forgetting to square $r$ in Coulomb's law, or to convert cm to m and µC to C.
- Using $E=\frac Vd$ for a point charge: it applies only to a uniform field.
- Mixing up $E$ (field strength) with $E_p$ (potential energy) and $V$ (potential).
### Exam tips
> Keep signs on charges when calculating potential, but use magnitudes for the size of a force and state its direction (attract or repel) in words.

## p-6-3
### Magnetic forces
$$F=BIL\sin\theta,\qquad F=BQv$$
- Fleming's left-hand rule: First finger = Field, seCond finger = Current, thuMb = Motion.
- 1 T is the field that exerts 1 N on 1 m of wire carrying 1 A perpendicular to the field.
- A charged particle in a field moves in a circle: $r=\frac{mv}{BQ}$. **Velocity selector:** $v=\frac EB$.
!fig p-bfield-circle
### Electromagnetic induction
$$\phi=BA\cos\theta,\qquad \varepsilon=-\frac{\Delta(N\phi)}{\Delta t}$$
- Faraday: the induced e.m.f. equals the rate of change of flux linkage. Lenz: the induced current opposes the change that caused it.
- Transformers: $\frac{n_s}{n_p}=\frac{V_s}{V_p}=\frac{I_p}{I_s}$ (if 100% efficient).
### Worked examples
A 0.050 m length of wire carries 3.0 A at right angles to a 0.20 T field: $F=BIL=0.20\times3.0\times0.050=0.030$ N.
A coil of 200 turns and area $4.0\times10^{-4}$ m² is in a 0.15 T field, which falls to zero in 0.020 s. Change of flux linkage $=200\times0.15\times4.0\times10^{-4}=0.012$ Wb-turns, so $\varepsilon=\frac{0.012}{0.020}=0.60$ V.
### Common mistakes
- Using the right hand for Fleming's motor rule. The **left** hand gives the force; the current direction is conventional current (opposite to electron flow).
- Forgetting that a charged particle moving **parallel** to $B$ feels no force ($\sin0^\circ=0$).
- Confusing flux $\phi$ (Wb) with flux density $B$ (T).
### Exam tips
> Flux linkage $N\phi$ has units Wb (or Wb-turns). Step-up transformers increase $V$ and reduce $I$ for transmission, giving smaller $I^2R$ losses.

## p-6-4
### The nucleus
- Rutherford α-scattering: most pass straight through (atom mostly empty space); a few are deflected through large angles (small, dense, positive nucleus).
- Radius $R=r_0A^{1/3}$ with $r_0\approx1.2$ fm. Nuclear density is constant (about $10^{17}\text{ kg m}^{-3}$).
- **Strong nuclear force:** attractive up to about 3 fm, repulsive below about 0.5 fm.
### Particles
- Hadrons (baryons qqq, mesons q q̄) feel the strong force; leptons (e, μ, ν) do not.
- Quarks: u $+\frac23e$, d $-\frac13e$, s $-\frac13e$. Proton uud, neutron udd.
- β⁻ decay: $d\to u+e^-+\bar\nu_e$. β⁺ decay: $u\to d+e^++\nu_e$ (weak interaction).
### Radioactivity
$$A=\lambda N,\qquad N=N_0e^{-\lambda t},\qquad \lambda t_{1/2}=\ln2$$
- α: 2p2n, highly ionising, stopped by paper. β: stopped by a few mm of aluminium. γ: reduced by lead.
### Binding energy
$$\Delta E=\Delta mc^2$$
- Mass defect: the mass of the separated nucleons minus the mass of the nucleus. Binding energy per nucleon peaks at Fe-56. Fusion of light nuclei and fission of heavy ones both release energy.
- 1 u $=931.5$ MeV.
!fig p-binding
### Exam tips
> Fission reactors: the moderator slows neutrons (elastic collisions), control rods absorb neutrons, and the coolant removes heat.

## p-6-5
### X-rays
- Produced when fast electrons hit a tungsten target (about 1% efficiency). Attenuation: $I=I_0e^{-\mu x}$.
- Mechanisms: simple scatter (1–20 keV), photoelectric effect (< 100 keV), Compton scattering (0.5–5 MeV), pair production (> 1.02 MeV).
- Contrast media (barium, iodine) have a high atomic number $Z$, so they absorb strongly. CAT scans build a 3D image from slices taken by a rotating X-ray tube.
### Nuclear medicine
- Tracers such as technetium-99m (γ emitter, 6 h half-life). Gamma camera: collimator, scintillator, photomultiplier tubes.
- **PET:** a β⁺ tracer (e.g. F-18 in FDG). Annihilation produces two 511 keV γ photons in opposite directions.
### Ultrasound
- Above 20 kHz, produced with the piezoelectric effect. A-scan and B-scan. Doppler for blood flow: $\Delta f=\frac{2fv\cos\theta}c$.
- Acoustic impedance $Z=\rho c$. Reflected fraction: $\frac{I_r}{I_0}=\frac{(Z_2-Z_1)^2}{(Z_2+Z_1)^2}$. Gel is used to match impedance, because air–skin reflects almost everything.
### Exam tips
> Compare techniques by resolution, ionising risk, cost and what they image (bone/soft tissue/function).
