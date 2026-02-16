import physics_functions as Pcalc

def calc_energy_transition():
    print("\nWhat are you looking for?")
    unknown = int(input("Wavelength(1), Lower Energy Level(2) or Higher Energy Level(3):\n"))
    if unknown == 1:
        n_init = float(input("What is the lower energy level: "))
        n_fin = float(input("What is the higher energy level: "))
        result_in_meters = Pcalc.calc_wavelength(n_init, n_fin)
        result = result_in_meters*10**9
        print(f"Wavelength is {result:.3f} nm")

    elif unknown == 2:
        wavelength = float(input("Whats the wavelength in nm: "))
        n_fin = float(input("What is the higher energy level: "))
        result = Pcalc.calc_n_initial(wavelength, n_fin)
        print(f"Lower Energy Level is {result:.3f}")
    
    elif unknown == 3:
        wavelength = float(input("Whats the wavelength in nm: "))
        n_init = float(input("What is the lower energy level: "))
        result = Pcalc.calc_n_final(wavelength, n_init)
        print(f"Higher Energy Level is {result:.3f}")

if __name__ == "__main__":
    calc_energy_transition()