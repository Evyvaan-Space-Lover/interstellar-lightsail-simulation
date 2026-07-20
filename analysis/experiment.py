import pandas as pd

class Experiment:
    def __init__(self):
        self.results = []
    
    def addResult(self, geometry, material, force, torque, maxTemp, avgTemp):
        self.results.append({
            "Geometry": geometry,
            "Material": material,
            
            "Force X": force[0],
            "Force Y": force[1],
            "Force Z": force[2],
            
            "Torque X": torque[0],
            "Torque Y": torque[1],
            "Torque Z": torque[2],
            
            "Max Temperature": maxTemp,
            "Average Temperature": avgTemp
        })
    
    def dataframe(self):
        return pd.DataFrame(self.results)
    
    def exportCSV(self, filename):
        self.dataframe().to_csv(filename, index=False)
        
        print(f"Results exported to {filename}")