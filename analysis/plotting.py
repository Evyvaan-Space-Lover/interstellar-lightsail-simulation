import matplotlib.pyplot as plt
import numpy as np

plt.style.use("dark_background")

def setupPlot(title, xlabel, ylabel):
    fig, ax = plt.subplots(figsize=(10, 5.5))
    
    fig.patch.set_facecolor('#0d1117')
    ax.set_facecolor('#161b22')
    
    ax.set_title(title, fontsize=16, weight='bold', pad=20, color='white')
    
    ax.set_xlabel(xlabel, color='white')
    ax.set_ylabel(ylabel, color='white')
    ax.tick_params(colors='white')
    
    ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)
    
    for spine in ax.spines.values():
        spine.set_color('#6e7681')
    
    ax.tick_params(colors='white')
    
    return fig, ax


def plotForceHistory(sail):
    if len(sail.history['force']) == 0:
        print("No force history to plot.")
        return
    
    t = np.array(sail.history['time'])
    F= np.array(sail.history['force'])
    
    fig, ax = setupPlot("Force vs Time", "Time (s)", "Force (N)")
    
    ax.plot(t, F[:, 0], label='Force X', color='cyan')
    ax.plot(t, F[:, 1], label='Force Y', color='magenta')
    ax.plot(t, F[:, 2], label='Force Z', color='yellow')
    
    legend = ax.legend(frameon=True)
    legend.get_frame().set_facecolor('#21262d')
    legend.get_frame().set_edgecolor('#30363d')
    
    plt.tight_layout()
    plt.show()


def plotForceMagnitude(sail):
    if len(sail.history['force']) == 0:
        print("No force history to plot.")
        return
    
    t = np.array(sail.history['time'])
    F= np.array(sail.history['force'])
    magnitude = np.linalg.norm(F, axis=1)
    
    fig, ax = setupPlot("Force Magnitude vs Time", "Time (s)", "Force Magnitude (N)")
    
    ax.plot(t, magnitude, linewidth=3, color="#58a6ff", label='Force Magnitude')
    
    ax.fill_between(t, magnitude, alpha=0.25, color='#58A6FF')
    
    peak = np.argmax(magnitude)
    
    ax.scatter(t[peak], magnitude[peak], s=80, color='#FF7B72', zorder=5, label=f"Peak = {magnitude[peak]:.3e} N")
    
    legend = ax.legend(frameon=True)
    legend.get_frame().set_facecolor("#21262d")
    legend.get_frame().set_edgecolor("#30363d")
    
    plt.tight_layout()
    plt.show()

def plotPositionHistory(sail):
    if len(sail.history['position']) == 0:
        print("No position history to plot.")
        return
    
    t = np.array(sail.history["time"])
    pos = np.array(sail.history["position"])
    
    fig, ax = setupPlot("Position vs Time", "Time (s)", "Position (m)")
    
    ax.plot(t, pos[:,0], linewidth=2.5, color='#58a6ff', label='X Position')
    ax.plot(t, pos[:,1], linewidth=2.5, color='#3fb950', label='Y Position')
    ax.plot(t, pos[:,2], linewidth=2.5, color='#f79166', label='Z Position')
    
    legend = ax.legend(frameon=True)
    legend.get_frame().set_facecolor('#21262d')
    legend.get_frame().set_edgecolor('#30363d')
    
    plt.tight_layout()
    plt.show()

def plotVelocityHistory(sail):
    if len(sail.history['velocity']) == 0:
        print("No velocity history to plot.")
        return
    
    t = np.array(sail.history["time"])
    vel = np.array(sail.history["velocity"])
    
    fig, ax = setupPlot("Velocity vs Time", "Time (s)", "Velocity (m/s)")
    
    ax.plot(t, vel[:,0], linewidth=2.5, color='#58a6ff', label='X Velocity')
    ax.plot(t, vel[:,1], linewidth=2.5, color='#3fb950', label='Y Velocity')
    ax.plot(t, vel[:,2], linewidth=2.5, color='#f79166', label='Z Velocity')
    
    legend = ax.legend(frameon=True)
    legend.get_frame().set_facecolor('#21262d')
    legend.get_frame().set_edgecolor('#30363d')
    
    plt.tight_layout()
    plt.show()

def plotAccelerationHistory(sail):
    if len(sail.history['force']) == 0:
        print("No force history to plot.")
        return
    
    t = np.array(sail.history["time"])
    F = np.array(sail.history["force"])
    
    acceleration = F / sail.mass
    
    fig, ax = setupPlot("Acceleration vs Time", "Time (s)", "Acceleration (m/s\u00B2)")
    
    ax.plot(t, acceleration[:,0], linewidth=2.5, color='#58a6ff', label='X acceleration')
    ax.plot(t, acceleration[:,1], linewidth=2.5, color='#3fb950', label='Y acceleration')
    ax.plot(t, acceleration[:,2], linewidth=2.5, color='#f79166', label='Z acceleration')
    
    legend = ax.legend(frameon=True)
    legend.get_frame().set_facecolor('#21262d')
    legend.get_frame().set_edgecolor('#30363d')
    
    plt.tight_layout()
    plt.show()

def plotAngularVelocityHistory(sail):
    if len(sail.history['angularVelocity']) == 0:
        print("No angular velocity history to plot.")
        return
    
    t = np.array(sail.history["time"])
    omega = np.array(sail.history["angularVelocity"])

    fig, ax = setupPlot("Angular Velocity vs Time", "Time (s)", "Angular Velocity (rad/s)")
    
    ax.plot(t, omega[:,0], linewidth=2.5, color='#58a6ff', label='X \u03A9')
    ax.plot(t, omega[:,1], linewidth=2.5, color='#3fb950', label='Y \u03A9')
    ax.plot(t, omega[:,2], linewidth=2.5, color='#f79166', label='Z \u03A9')
    
    legend = ax.legend(frameon=True)
    legend.get_frame().set_facecolor('#21262d')
    legend.get_frame().set_edgecolor('#30363d')
    
    plt.tight_layout()
    plt.show()

def plotTemperatureHistory(sail):
    if len(sail.history['maxTemperature']) == 0:
        print("No temperature history to plot.")
        return
    
    t = np.array(sail.history["time"])
    Tmax = np.array(sail.history["maxTemperature"])
    Tavg = np.array(sail.history["averageTemperature"])

    fig, ax = setupPlot("Temperature vs Time", "Time (s)", "Temperature (K)")
    
    ax.plot(t, Tmax, linewidth=2.5, color='#58a6ff', label='Maximum Temperature')
    ax.plot(t, Tavg, linewidth=2.5, color='#3fb950', label='Average Temperature')
    
    ax.fill_between(t, Tavg, Tmax, color="#FF7B72", alpha=0.2)
    
    legend = ax.legend(frameon=True)
    legend.get_frame().set_facecolor('#21262d')
    legend.get_frame().set_edgecolor('#30363d')
    
    plt.tight_layout()
    plt.show()

def plotTemperatureHistogram(sail):
    if len(sail.history['maxTemperature']) == 0:
        print("No temperature history to plot.")
        return
    
    temperatures = np.array(sail.temperatureMap)

    fig, ax = setupPlot("Temperature Distribution", "Temperature (K)", "Number Of Elements (Mesh Cells)")
    
    ax.hist(temperatures, bins=30, color='#ff7b72', edgecolor='white', linewidth=0.5, alpha=0.85)
    
    mean = np.mean(temperatures)
    
    ax.axvline(mean, color="#58a6ff", linestyle='--', linewidth=2, label=f"Mean = {mean:.2f} K")
    
    legend = ax.legend(frameon=True)
    legend.get_frame().set_facecolor('#21262d')
    legend.get_frame().set_edgecolor('#30363d')
    
    plt.tight_layout()
    plt.show()