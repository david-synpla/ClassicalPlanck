# Study 1 — baseline active-bath string and walker

A fixed-end 1D mass–spring string is expanded into 12 normal modes. In normalized coordinates,

```math
E_n=\frac12(P_n^2+\omega_n^2 Q_n^2),\qquad
\omega_n=\frac{\sin[n\pi/(2(N+1))]}{\sin[\pi/(2(N+1))]}.
```

Between impacts, each mode has damping, thermal Langevin noise and independent colored Ornstein–Uhlenbeck force:

```math
dQ_n=P_n\,dt,\quad dP_n=(-\omega_n^2 Q_n-2\gamma_n P_n+F_n)dt+\sqrt{4\gamma_n T}\,dW_n,
```

```math
dF_n=-F_n\,dt/\tau_c+\sqrt{2\sigma_F^2/\tau_c}\,dB_n.
```

A particle impacting at `X_j` changes modal momentum by `J_j phi_n(X_j)` and receives a horizontal kick proportional to local wave slope, with optional walker noise and drag. Random impact amplitudes and horizontal agitation are included.

## Baseline experiments

12 modes, baseline `T=0.12`, 90,000 impacts with 12,000 discarded in the main run. Four equally spaced within-period samples avoid relying solely on pre/post-impact energies.

- Thermal-only control: modal means within 1.6% of `T`, median variance over `T^2` = 1.004.
- Full model: first-mode mean energy = 0.6097, twelfth = 0.1356.
- Full model: `R_1=8.13`, `R_2=3.12`, high modes around 1.28–1.32.
- Two-parameter thermal Planck-shape fit to modal means: logarithmic RMS discrepancy 0.274, versus 0.443 for a flat fit. This is **not** a true Planck equilibrium.
- The original nine-case sensitivity study varied `tau_c={0.2,0.65,1.5}` and feedback `{0,1,3}`.

A continuous Gaussian classical mode can exhibit `Var(E)/<E>^2≈1`. It remains classical; this must not be conflated with the excess-variance test.

## Analytical bath-only benchmark

With `a=1/tau_c` and no impacts,

```math
\langle E_n\rangle=T+\frac{\sigma_F^2(\gamma_n+a)}{2\gamma_n(\omega_n^2+2\gamma_n a+a^2)}.
```

The simulated means agreed with the formula within approximately 3% across the modes.

Further details: [methods](methods.md).
