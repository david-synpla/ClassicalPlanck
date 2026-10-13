# Study 3 — number of allowed normal modes

## Question

Will adding more permitted modes bring all fluctuation ratios `R_n` toward the target of 1?

Two checks were performed.

### First check — original discrete normalization

Same numerical parameters, `N=8,12,20,32,48,64`. This changes total physical mass/cutoff, so is primarily a numerical sensitivity check.

| Modes | Full median R | R_1 | R_2 |
|---:|---:|---:|---:|
| 8 | 1.549 | 11.46 | 3.48 |
| 12 | 1.311 | 8.48 | 3.14 |
| 20 | 1.175 | 8.25 | 2.84 |
| 32 | 1.054 | 7.87 | 2.98 |
| 48 | 1.023 | 6.93 | 2.89 |
| 64 | 1.012 | 6.93 | 2.70 |

The median approaches 1; original low modes do not.

### Second check — fixed-total-mass continuum cutoff

Held string length and total mass constant, used `omega_n=n omega_1`, `phi_n(x)=sqrt(2)sin(n pi x)`, and a smooth particle contact profile with spectral overlap `exp[-0.5(n pi*0.05)^2]`. Repeated with three random seeds per configuration.

| Modes | Full median R | First-six median R |
|---:|---:|---:|
| 12 | 2.37 | 5.29 |
| 20 | 1.18 | 5.08 |
| 32 | 1.01 | 5.26 |
| 48 | 1.01 | 5.36 |
| 64 | 1.00 | 5.32 |

R_2 stayed around 10–12; R_6 around 2.5–2.7. R_1 is especially noisy because its temperature susceptibility can be very small. The fixed-mass result is more relevant to a mode-cutoff limit.

## Explanation

High-frequency modes are weakly excited by colored forcing and smooth contact, so `U_0,n` becomes small. For the linear bath, `R_n=1+2U_0,n/T`. Adding many almost thermal high-frequency modes pushes the **all-mode median** toward 1 mechanically, while the first modes do not change appreciably.

## Conclusion

Increasing spectral resolution does not establish the Planck fluctuation relation. Mode-by-mode checks, fixed physical normalization and replicated seeds are mandatory.
