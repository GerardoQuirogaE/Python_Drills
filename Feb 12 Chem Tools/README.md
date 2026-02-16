# Chem Tools

This folder contains Python scripts for calculating energy transitions in atoms using the Rydberg formula. It allows users to compute the wavelength of emitted or absorbed light and the corresponding initial or final energy levels.

| File | Description |
|------|-------------|
| `energy_transition_function.py` | Interactive script that prompts the user to calculate either the wavelength, lower energy level, or higher energy level based on inputs. Uses functions from `physics_functions.py`. |
| `physics_constants.py` | Stores physical constants used in calculations, currently contains the Rydberg constant. |
| `physics_functions.py` | Contains functions to compute wavelength, initial energy level, and final energy level from the Rydberg formula. Used by `energy_transition_function.py`. |
