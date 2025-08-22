import math

# 1. Hydrostatic Pressure
def hydrostatic_pressure(depth, density, g=9.81):
    return density * g * depth / 1e6  # Pressure in MPa

# 2. Oil Formation Volume Factor (simplified correlation)
def oil_fvf(api, temp_f):
    return 0.972 + 1.47e-4 * (temp_f - 60) + (1.25e-4 * api)

class Fluid:
    def __init__(self, name, density):
        self.name = name
        self.density_value = density

    # Method
    def density(self):
        return self.density_value

class Oil(Fluid):
    def __init__(self, api, density):
        super().__init__("Oil", density)
        self.api = api

    # Polymorphism: override density method
    def density(self):
        return 141.5 / (131.5 + self.api) * 1000  # kg/m3 approx.

class Gas(Fluid):
    def __init__(self, density, z_factor=0.9):
        super().__init__("Gas", density)
        self.z = z_factor

    def density(self):
        return self.density_value * self.z

class Water(Fluid):
    def __init__(self, density=1000):
        super().__init__("Water", density)

if __name__ == "__main__":
    # Function examples
    print("Hydrostatic Pressure at 2000 m depth:", hydrostatic_pressure(2000, 1000), "MPa")
    print("Oil FVF (API=35, Temp=180F):", oil_fvf(35, 180))

    # Class & Methods
    oil = Oil(api=35, density=850)
    gas = Gas(density=0.8)
    water = Water()

    # Polymorphism demonstration
    fluids = [oil, gas, water]
    for f in fluids:
        print(f"{f.name} Density: {f.density():.2f} kg/m3")
