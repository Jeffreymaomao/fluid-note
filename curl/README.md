

Curl is an operation, which when applied to a vector field, quantifies the *circulation* of that field.

> **Concept of Circulation：**
>
> *Circulation* is the integral of a vector field over a closed path.

Specifically, the circulation of the vector field $\vec{F}$ over the closed path $C$ is
$$
\oint_{C} \vec{F} \cdot  d\vec{\ell}
$$
If the path $C$ shrinks to it’s smallest possible, the integral in one sense is zero, since the arc length of $C$ is zero in this limit. 

But if we calculate the circulation per unit area, the result may be a non-trivial value, that is 
$$
\lim_{A\to 0}\frac{\displaystyle\oint_C \vec{F} \cdot  d\vec{\ell}}{A}
$$
and we may choosing the direction of curl to be the normal vector $\vec{n}$ of infinitesmal path, one can define the curl is given by
$$
\operatorname{curl} \vec{F} = \lim_{A\to 0} \frac{\displaystyle \oint_{C}\vec{F} \cdot d\vec{\ell}}{\abs{A}},
$$
where the line integral is calculated along the boundary $C$ of the area $A$.

---

