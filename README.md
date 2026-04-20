<!-- 
Section list:
- Overview
- Requirements
- Installation
- Usage
- Output
- AI Tools Used and Disclosure
-->

# Lab 3: Sensor Analysis Plots

## Overview

This project generates synthetic temperature readings from two sensors and creates visualization plots to compare their distributions. The script produces a multi-panel figure with three subplots: a scatter plot of readings over time, an overlaid histogram of temperature distributions, and side-by-side box plots for statistical comparison.

## Requirements

- Python 3.8 or later
- NumPy
- Matplotlib

## Installation

1. **Activate the ece105 Conda environment:**
   \\\ash
   conda activate ece105
   \\\

2. **Install dependencies** (if not already installed in the environment):
   \\\ash
   conda install numpy matplotlib
   \\\
   
   Or using Mamba (faster alternative):
   \\\ash
   mamba install numpy matplotlib
   \\\

## Usage

Run the script from the command line:

\\\ash
python generate_plots.py
\\\

The script will:
1. Generate synthetic sensor data (200 temperature readings from each sensor, plus 200 timestamps).
2. Create a 1×3 subplot figure with scatter plot, histogram, and box plot visualizations.
3. Save the figure as \sensor_analysis.png\ at 150 DPI.

## Output

- **sensor_analysis.png**: A 3-panel matplotlib figure saved to the current directory.
  - **Left panel (Scatter Plot):** Temperature readings vs. time for both sensors.
  - **Middle panel (Histogram):** Overlaid temperature distributions with mean lines.
  - **Right panel (Box Plot):** Side-by-side box plots with overall mean reference line.

## AI Tools Used and Disclosure

<!-- Placeholder: Add details about AI tools, models, and how they were used in this project. -->

