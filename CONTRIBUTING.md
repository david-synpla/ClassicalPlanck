# Contributing and research practices

Keep model assumptions separate from results and interpretations.

- Add a reproducible script and random seed for every new numerical claim.
- Keep physical parameters fixed when varying only the mode cutoff; clearly state whether a discrete-lattice or fixed-continuum model is used.
- Preserve per-mode energies and variances, particularly the first six modes; a falling full-spectrum median is not enough.
- Compare thermal control, active-noise-only, impact-only and fully coupled dynamics.
- Quote both the thermal susceptibility and excess variance; mark undefined/ill-conditioned ratios.
- Report parameter ranges, run duration, burn-in, solver, uncertainty from multiple seeds and raw data.
- Do not label a fitted Planck-like shape as a derived Planck law.
- Keep the original exploratory scripts and datasets unmodified when they are imported; record revised versions separately.

Quick analytical check:

```sh
python scripts/linear_bath_control.py
python -m unittest discover -s tests -v
```
