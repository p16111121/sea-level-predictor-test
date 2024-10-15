import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv(r"epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))  # Set figure size
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label='Data', color='blue')

    # Create first line of best fit (all data)
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = pd.Series(range(df["Year"].min(), 2051))  # From the min year in df to 2050
    sea_level_prediction = slope * years_extended + intercept
    plt.plot(years_extended, sea_level_prediction, color='red', label='Line of Best Fit (All Data)')

    # Create second line of best fit (2000 onward)
    df_filtered = df[df["Year"] >= 2000]
    slope, intercept, r_value, p_value, std_err = linregress(df_filtered["Year"], df_filtered["CSIRO Adjusted Sea Level"])
    years_extended_filtered = pd.Series(range(2000, 2051))  # From 2000 to 2050
    sea_level_prediction_filtered = slope * years_extended_filtered + intercept
    plt.plot(years_extended_filtered, sea_level_prediction_filtered, color='green', label='Line of Best Fit (2000 onward)')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    plt.grid()

    # Save plot
    plt.savefig('sea_level_plot.png')

    # Show the plot
    plt.show()

    # Return the current axis for testing (DO NOT MODIFY)
    return plt.gca()
