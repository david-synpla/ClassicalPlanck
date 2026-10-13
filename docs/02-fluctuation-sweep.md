# Study 2 — parameter-space search for R ≈ 1

## Target

`R_n = (Var_T(E_n)-Var_0(E_n))/(T^2 d<E_n>/dT)` with `k_B=1`.

Central derivative at `T=0.12` from runs at `T=0.06, 0.18`; separate baseline at `T=0`. The original `variance_ratio_median` represented **Var(E)/mean(E)^2, not R**. This follow-up computed R directly.

## Correlation-time and feedback sweep

Median R across 12 modes:

| Colored-bath correlation time | Feedback 0 | Feedback 1 | Feedback 3 |
|---:|---:|---:|---:|
| 0.20 | 1.433 | 1.448 | 1.506 |
| 0.65 | 1.348 | 1.346 | 1.426 |
| 1.50 | 1.310 | 1.291 | 1.367 |

Increasing correlation time lowers the median, but low-mode ratios may worsen.

## Forcing/impact amplitude sweep, three independent seeds

| Regime | Impact J | Active-force sigma_F | Median R | Fundamental R_1 |
|---|---:|---:|---:|---:|
| Weak | 0.12 | 0.06 | 1.026 ± 0.006 | 1.31 ± 0.04 |
| Original | 0.48 | 0.30 | 1.316 ± 0.009 | 8.73 ± 0.45 |
| Strong | 0.80 | 0.60 | 2.215 ± 0.023 | 45.6 ± 17.2 |

Sample SD over three independent seeds, not formal uncertainty intervals. The large first-mode ratios may also be unstable when the finite-difference thermal derivative is small.

The extended correlation-time sweep to `tau_c=20` did **not** continue to R=1; median values level around 1.25 for long correlation times.

Across 300 mode-level records from a 5×5 amplitude grid, observed R values were highly correlated (`r≈0.979`) with `1+2 U_0/T`. This is a numerical correlation, not proof for the nonlinear walker.

## The exact linear Gaussian limit

For bath-only linear dynamics, stationary covariance has the form `C(T)=C_0+T K^{-1}`, where `K=diag(omega^2,1)`. Hence `<E>=U_0+T` and

```math
R=1+\frac{2U_0}{T}.
```

If `U_0>0`, R cannot be 1 for this limit. Observed approach to R=1 is primarily the trivial disappearance of nonthermal excitation.

**Do not optimize solely by the median across modes.** Report low-mode ratios and zero-temperature energies independently.
