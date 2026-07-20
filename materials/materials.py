from dataclasses import dataclass

@dataclass
class Material:
    name: str
    
    reflectivity: float
    absorptivity: float
    emissivity: float
    
    density: float # kg/m^3
    
    maxTemperature: float # Kelvin
    colour: str = 'white' # default colour is white
    
    @property
    def temperature(self):
        return self.maxTemperature