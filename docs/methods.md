# Methods, estimators and limitations

- **Classical model:** fixed-end 1D modes with normalized mass, damped harmonic dynamics, thermal white noise, external colored Ornstein–Uhlenbeck forcing, and intermittent particle impacts.
- **Thermal control:** the white-noise coefficient is matched to viscous damping to recover equipartition.
- **Integrator:** the original simulation advanced the linear stochastic between-bounce state by Gaussian transition matrices and applied discrete nonlinear walker impacts; modal energies were sampled at multiple times within each bounce.
- **Observable:** `R_n(T)=[Var_T(E_n)-Var_0(E_n)]/[T^2(d<E_n>/dT)]`, `k_B=1`.
- **Derivative:** central finite difference using T=0.06 and 0.18 about T=0.12. This is a susceptibility estimate, not a direct response-theory calculation.
- **Variance:** computed from stationary-sample modal energies; autocorrelation can reduce effective sample size substantially.
- **Burn-in:** first impacts discarded before collecting the stationarity statistics.
- **Seeds:** repeated across selected parameter combinations, not every grid cell.
- **Interpretation:** ratios become ill-conditioned when the susceptibility is small; report derivatives and absolute variances along with ratios.
- **Spectral comparisons:** a fit to `a omega/(exp(b omega)-1)` is an empirical shape comparison, not a derived partition function. The full Planck result also contains `hbar omega/2`.
- **Model limits:** no explicit parametric Faraday drive, no true fluid hydrodynamics, no quantized energy states; in the original normalized discrete sweep adding modes also alters physical discretization.
- **Reproducibility:** the archived source and raw outputs need importing; files presently in this repository are the analytical control and documented numerical summaries.
