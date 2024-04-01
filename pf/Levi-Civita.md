# Levi-Civita

In three dimensions, the Levi-Civita symbol is defined by:
$$
\varepsilon _{ijk} = 
\begin{cases}
+1	&	\text{if $(i,j,k)$ is $(1,2,3)$, $(2,3,1)$ or $(3,1,2)$}\\
-1	&	\text{if $(i,j,k)$ is $(3,2,1)$, $(2,1,3)$ or $(2,1,3)$}\\
\;\;\,0&\text{if $i=j$, $i=k$ or $k=i$}
\end{cases}
$$
That is, $\varepsilon_{ijk}$ is $1$ if $(i,j,k)$ is an even permutation of $(1,2,3)$, $−1$ if it is an odd permutation, and $0$​ if any index is repeated.

## Properties

### Product

$$
\begin{aligned}
\varepsilon _{ijk}\varepsilon _{lmn}
&=\begin{vmatrix}
\delta _{il}&\delta _{im}&\delta _{in}\\
\delta _{jl}&\delta _{jm}&\delta _{jn}\\
\delta _{kl}&\delta _{km}&\delta _{kn}
\end{vmatrix}\\[6pt]
&=\delta _{il} \left(\delta _{jm}\delta _{kn}-\delta _{jn}\delta _{km}\right)
	-\delta _{im} \left(\delta _{jl}\delta _{kn}-\delta _{jn}\delta _{kl}\right) 
	+\delta _{in} \left(\delta _{jl}\delta _{km}-\delta _{jm}\delta _{kl}\right).
\end{aligned}
$$

### Special cases

$$
\sum _{i=1}^{3}\varepsilon _{ijk}\varepsilon _{imn}=\delta _{jm}\delta _{kn}-\delta _{jn}\delta _{km}
$$

**Proof**

Using the properties of product
$$
\begin{aligned}
\sum _{i=1}^{3}\varepsilon _{ijk}\varepsilon _{imn} 
&= \sum _{i=1}^{3}\begin{vmatrix}
\delta _{ii}&\delta _{im}&\delta _{in}\\
\delta _{ji}&\delta _{jm}&\delta _{jn}\\
\delta _{ki}&\delta _{km}&\delta _{kn}
\end{vmatrix}\\[6pt]
&= \sum _{i=1}^{3}\bigg(\delta _{ii} \left(\delta _{jm}\delta _{kn}-\delta _{jn}\delta _{km}\right)
	-\delta _{im} \left(\delta _{ji}\delta _{kn}-\delta _{jn}\delta _{ki}\right) 
	+\delta _{in} \left(\delta _{ji}\delta _{km}-\delta _{jm}\delta _{ki}\right)\bigg)\\
&= \left(\delta _{jm}\delta _{kn}-\delta _{jn}\delta _{km}\right)  \sum _{i=1}^{3}\delta _{ii}
	+ \sum _{i=1}^{3}\bigg(-\delta _{im} \left(\delta _{ji}\delta _{kn}-\delta _{jn}\delta _{ki}\right) 
	+\delta _{in} \left(\delta _{ji}\delta _{km}-\delta _{jm}\delta _{ki}\right)\bigg)\\
&= 3\cdot\left(\delta _{jm}\delta _{kn}-\delta _{jn}\delta _{km}\right)
	+ \sum _{i=1}^{3}\left(
	-\delta _{im}\delta _{ji}\delta _{kn} + \delta _{im}\delta _{jn}\delta _{ki} 
	+\delta _{in}\delta _{ji}\delta _{km} - \delta _{in}\delta _{jm}\delta _{ki}
	\right)\\[6pt]
&= 3\cdot\left(\delta _{jm}\delta _{kn}-\delta _{jn}\delta _{km}\right)
	-\delta _{jm}\delta _{kn} + \delta _{km}\delta _{jn}
	+\delta _{jn}\delta _{km} - \delta _{kn}\delta _{jm}\\[6pt]
&= 3\cdot\left(\delta _{jm}\delta _{kn}-\delta _{jn}\delta _{km}\right)
	-2\delta _{jm}\delta _{kn} + 2\delta _{km}\delta _{jn}\\[6pt]
&= \delta _{jm}\delta _{kn}-\delta _{km}\delta _{jn}
\end{aligned}
$$
