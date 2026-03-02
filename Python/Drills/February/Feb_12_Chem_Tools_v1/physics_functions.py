import math as m
import physics_constants as const

def calc_wavelength(n_initial, n_final):
    wavelength = 1 / (
        const.rydberg_const * (
            (1 / n_initial**2) - (1 / n_final**2)))
    return wavelength

def calc_n_final(wavelength, n_initial):
    wavelength_meters = wavelength*10**-9
    n_final = m.sqrt(
        1/(
            -(
                (1/(wavelength_meters*const.rydberg_const)) - (1/n_initial**2)
                )))
    return n_final

def calc_n_initial(wavelength, n_final):
    wavelength_meters = wavelength*10**-9
    n_initial = m.sqrt(
        1/(
            (1/(wavelength_meters*const.rydberg_const)) - (1/n_final**2)))
    return n_initial