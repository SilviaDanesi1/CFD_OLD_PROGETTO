# Intro
So we can have heat transfer due to:
  - irradiation (Not our case)
  - conduction  (Not our case, is for still elements)
  - convection  (Definetly our case)

Convection can be splitted in:
  - forced conv
  - mixed conv
  - natural conv
We can deduct in wich case we are in thanks to the Richardson's adimensional parameter $\Ri = \frac{\Gr}{\Re^2}$, $\Gr =\frac{|g|*k_{pf}*|T_{f}-T_{p}|*D_{car}^3}{\mu^2_{f}}$, that represents the ratio between bouiancy forces against viscuos forces.

Another dinstiction can be made in:
  - External convection
  - Internal convection
*The book at this point explain the thermal BL and fluid's BL*

## Newtons's eq for estimate of thermal coefficent *h*
$$ frac{\partial Q''}{\partial t} = - h (T_p - T_f) $$
Where:
  - $Q''_p$ thermal flux projected along the normal (Exiting the body)
  - $T_p$  is the temperature of the wall
  - $T_f$ is an adequate temperature to describe the fluid, usually is either:
    - $T_m$  the mean T in the region of interest, (T of the infinitesimal volume would be an appropriate choise in this sense I think)
    - $T_inf$ as the temperature of the fluid far from the heat source (Reservoire T, out of our model I  would say)
  - $h$ is the coefficent hiding all the completìxity of the problem, is generally function of the fluid and flow properties, has to be guessed trough soe adimensional parameters, the most helpful are:
    - $Nu = \frac{h Dcar}{\lambda_f}$ that represents the ratio between convective heat transfer and condctive heat transfer ($\lambda_f$ is the cond heat transf parameter)
    - $Re$
    - $Pr = \frac{\mu_f c_f}{\lambda_f}$ with the meaning of transport of momentum against trnsport of heat
    - The earlier descriebed Grashof parameter
    - $Pe = Re Pr$ That represents the avvection agaimst diffusion contribution to the heat flux

There are some analitical ways to get h, but all of them are out of our study case, BUT we may find help in the $\epsilon$-NTU model, but is defined and works for 2 fluid heat exchanger, so our case would be out of interest in my understanding, here's the link to [WIKI](https://en.wikipedia.org/wiki/NTU_method) in any case.   

## The $\epsilon$ - NTU method

Starting from the efficency parameter $\epsilon = \frac{Q°_B}{hA_h(T_B-T_inf)}$, NTU  is defined as _Number of unit of transport_, we also know that we can define $\epsilon = \frac{Q°}{C°_min(T_{hi} - T_{ci})}$, so we can get $Q°$ as function of $\epsilon$ and obtain epsilon from diagrams at the change in of NTU, coming from experimentaal datas.

Even tho it may look useful I couldn't find anything related to our problem, so I would just rely on the datas form CFD and try to understand the solver.

Peace.
