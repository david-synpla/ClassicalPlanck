# ClassicalPlanck

Numerical exploration of whether a **classical fixed-end 1D string**, driven by a thermal bath, an independent active bath and a bouncing wave-coupled particle, can produce the Planck modal-energy law or the proposed excess-variance fluctuation identity.

**Status: exploratory negative result.** The model produces non-equipartition modal spectra and sometimes a superficially Planck-like thermal spectral shape, but it has not produced the Planck distribution or the sought identity with nonzero background energy.

## Research question

Each normal mode has energy

```math
E_n = (P_n^2 + \omega_n^2 Q_n^2)/2
```

in normalized mass units. The proposed criterion is

```math
R_n = \frac{\mathrm{Var}_T(E_n)-\mathrm{Var}_{T=0}(E_n)}
{k_B T^2\, \partial_T \langle E_n\rangle}=1.
```

Simulations use dimensionless units with `k_B=1`. This criterion is **not** the ordinary Gaussian oscillator identity `Var(E)/mean(E)^2 ≈ 1`; the latter is observed in classical thermal oscillators and cannot be taken as evidence of Planck statistics.

## Studies

- [Baseline model and findings](docs/01-baseline.md) — Langevin bath, colored active forcing, bouncing walker and modal spectra.
- [Parameter-space follow-up](docs/02-fluctuation-sweep.md) — corrected excess-variance ratios across noise correlation, impact strength and feedback.
- [Mode-count convergence](docs/03-mode-convergence.md) — controlled checks at 8–64 modes, including fixed-total-mass continuum cutoff.
- [Methods and caveats](docs/methods.md) — estimators, controls and interpretations.
- [Key data](data/summary.csv) — concise numerical summary of representative runs.
- [Analytical control](scripts/linear_bath_control.py) — dependency-free formula for linear bath mean energy and ratio.

The full original numerical simulation scripts, notebooks, charts, and CSV tables were created in an earlier experimental session, but **have not yet been imported into this repository**. The present repository is a documented research index and analytical control, not a claim that all original Monte Carlo computations can already be reproduced from it.

## Main findings

1. A thermal-only Langevin bath agrees with classical equipartition (`<E_n>≈T`).
2. Colored active noise and impacts preferentially excite low-frequency modes.
3. In the full 12-mode case, `R_1≈8.13`; other modes also deviate from 1.
4. Weakening the nonthermal drive makes many ratios tend to 1, but also removes the intended finite zero-temperature background.
5. Adding modes makes the all-mode median tend to 1 **without** making the first six modes tend to 1.

## Scope

This is a stylized **1D string / stroboscopic walker**, not a full Faraday-wave / walking-droplet simulation. There is no built-in quantum energy discretization, Planck bath spectrum, or prescribed frequency-dependent impulse. A fit to a Planck-shaped curve is descriptive, not a derivation of Planck thermodynamics.

See [Next experiments](docs/04-next-experiments.md).

## Citation / provenance

Exploratory calculations developed in ChatGPT with the user on 13 October 2026. Numerical estimates are finite-sample simulation outputs, not established universal laws. Full Monte Carlo provenance and artifacts should be added before any external scientific use.
