import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    years_extended = pd.Series(range(df['Year'].min(), 2051))
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    sea_level_predicted = intercept + slope * years_extended
    plt.plot(years_extended, sea_level_predicted)

    # Create second line of best fit
    df_filtered = df[df['Year'] >= 2000]
    slope_filtered, intercept_filtered, r_value_filtered, p_value_filtered, std_err_filtered = linregress(df_filtered['Year'], df_filtered['CSIRO Adjusted Sea Level'])
    years_filtered_extended = pd.Series(range(df_filtered['Year'].min(), 2051))
    sea_level_predicted_filtered = intercept_filtered + slope_filtered * years_filtered_extended
    plt.plot(years_filtered_extended, sea_level_predicted_filtered)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()