"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.
def generate_data(seed):
    """
    Generate simulated temperature readings from two sensors and timestamps.

    Creates synthetic data for two temperature sensors with specified mean and 
    standard deviation, along with uniformly-distributed timestamps.

    Parameters
    ----------
    seed : int
        Random seed for reproducibility. Typically the last 4 digits of a Drexel ID.

    Returns
    -------
    sensor_a : ndarray
        Temperature readings from Sensor A, shape (200,), dtype float64.
        Mean 25°C, standard deviation 3°C.
    sensor_b : ndarray
        Temperature readings from Sensor B, shape (200,), dtype float64.
        Mean 27°C, standard deviation 4.5°C.
    timestamps : ndarray
        Uniformly-distributed timestamps, shape (200,), dtype float64.
        Range [0, 10] seconds.
    """
    rng = np.random.default_rng(seed=seed)
    
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=200)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=200)
    timestamps = rng.uniform(low=0.0, high=10.0, size=200)
    
    return sensor_a, sensor_b, timestamps

# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.
def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """
    Plot sensor temperature readings as a scatter plot on the given Axes.

    Draws temperature readings from two sensors against time as overlaid scatter plots
    with distinct colors. Modifies the Axes object in place.

    Parameters
    ----------
    sensor_a : ndarray
        Temperature readings from Sensor A, shape (200,), dtype float64.
    sensor_b : ndarray
        Temperature readings from Sensor B, shape (200,), dtype float64.
    timestamps : ndarray
        Time values in seconds, shape (200,), dtype float64.
    ax : matplotlib.axes.Axes
        Axes object to draw on. Modified in place.

    Returns
    -------
    None
    """
    ax.scatter(timestamps, sensor_a, color='blue', alpha=0.6, label='Sensor A', s=30)
    ax.scatter(timestamps, sensor_b, color='orange', alpha=0.6, label='Sensor B', s=30)
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Sensor Temperature Readings Over Time')
    ax.legend()
    ax.grid(True, alpha=0.3)

# Create plot_histogram(sensor_a, sensor_b, ax) that draws the histogram
# from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.
def plot_histogram(sensor_a, sensor_b, ax):
    """
    Plot overlaid histograms of sensor temperature distributions on the given Axes.

    Draws overlaid histograms with vertical dashed lines at each sensor's mean.
    Modifies the Axes object in place.

    Parameters
    ----------
    sensor_a : ndarray
        Temperature readings from Sensor A, shape (200,), dtype float64.
    sensor_b : ndarray
        Temperature readings from Sensor B, shape (200,), dtype float64.
    ax : matplotlib.axes.Axes
        Axes object to draw on. Modified in place.

    Returns
    -------
    None
    """
    ax.hist(sensor_a, bins=30, alpha=0.5, label='Sensor A', color='blue')
    ax.hist(sensor_b, bins=30, alpha=0.5, label='Sensor B', color='orange')
    
    mean_a = np.mean(sensor_a)
    mean_b = np.mean(sensor_b)
    ax.axvline(mean_a, color='blue', linestyle='--', linewidth=2, label=f'Mean A: {mean_a:.2f}°C')
    ax.axvline(mean_b, color='orange', linestyle='--', linewidth=2, label=f'Mean B: {mean_b:.2f}°C')
    
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Frequency')
    ax.set_title('Temperature Distribution: Sensor A vs Sensor B')
    ax.legend()
    ax.grid(True, alpha=0.3)