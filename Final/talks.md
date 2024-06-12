# Rotation of The Fluid Flow

Author: Chang-Mao Yang



---

## Rotation 

What is the rotation of a particle? First we look at a particle in a space $\mathbb{R}^2$

<u>Fig</u>



---

However, if we add a coordinate

<u>Fig</u>

And define the magnitude angular velocity to be 
$$
\omega = \lim_{t_1 \to t_2}\frac{\theta(t_2) - \theta(t_1)}{t_2 - t_1} = \frac{d\theta}{dt}
$$

---

Notice that, the velocity can be calculated in Polar coordinate $\vec{r} = r\cos\theta\hat{e}_{x}+ r\sin\theta\hat{e}_y$
$$
\begin{aligned}
\vec{v} &= \frac{d\vec{r}}{dt} = \frac{d}{dt}\left(r\left(\cos\theta\hat{e}_{x}+ \sin\theta\hat{e}_y\right)\right)\\
&= \frac{dr}{dt} \left(\cos\theta\hat{e}_x + \sin\theta\hat{e}_y\right) + r\left(-\sin\theta\hat{e}_x + \cos\theta\hat{e}_y\right)\frac{d\theta}{dt}\\
&= \frac{dr}{dt}\hat{e}_r + r\frac{d\theta}{dt}\hat{e}_\theta
\end{aligned}
$$
Extending the space to $z$ component, we define the angular velocity for a particle on the $xy$-plane in $\mathbb{R}^3$
$$
\vec{\omega} = \frac{\hat{e}_r\times \vec{v}}{r} 
= \frac{r(\hat{e}_{r}\times\hat{e}_\theta)}{r}\frac{d\theta}{dt}
= \frac{d\theta}{dt} \hat{e}_z
$$

where $\hat{e}_r$, $\hat{e}_\theta$ and $\hat{e}_z$ are the orthonormal basis of cylinder coordinate.

---

Now, consider the particle in $\mathbb{R}^3$ and we still using position vector $\vec{r}$ rather than the $r$-component vector, since $\hat{e}_r = \vec{r}/r$, we also can write 
$$
\vec{\omega}  = \frac{\hat{e}_r\times \vec{v}}{r} = \frac{\vec{r}\times\vec{v}}{r^2}
$$

---

Then, how about a group of particles?
$$
\tilde{\Omega} = \frac{1}{n}\sum_{i=1}^{n}\vec{\omega}_i = \sum_{i=1}^{n}\frac{\vec{r}_i\times\vec{v}}{\lVert \vec{r}_i\lVert^2}
$$
so using the mean of angular velocity can not be a good approximation.

---

There are two different way to describe how fluid flow.

- Path line
- Stream line



---

A more intuitive way to describe how a group of particles rotate, is to place a marker is these particles. 

---

Consider a fluid flow,

<u>Fig</u>

---

Using a example 
$$
\vec{u}(x,y) = (y^3 - 9y) \hat{e}_x + (x^3 - 9x)\hat{e}_y
$$

---

After we solving the system of non-linear differential equations, we have the path line. 

---

Also calculate the curl of vector field $\operatorname{curl} \vec{u} = \partial_{x}(x^3-9x) - \partial_{y}(y^3-9y)=3(x^3-y^2)$, and make a contour





#### Referece

- https://courses.ansys.com/wp-content/uploads/2019/05/FluidKinematics-Lesson3-FlowRotation-Handout.pdf
- https://www.ess.uci.edu/~yu/class/ess228/lecture.4.circulation.2017.pdf
- https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/d18774dd8a3f24001bf3d502fef7f854_MIT18_02SC_MNotes_v4.3.pdf
- https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/6/3494/files/2014/04/Circulation-and-flux-handout-14akcjb.pdf