import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress # 用來執行線性回歸分析，返回斜率、截距、相關係數等統計量

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize = (10,6))
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'], label = 'Data', color = 'blue', alpha = 0.6)

    # Create first line of best fit
    slope_all, intercept_all, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level']) # 進行線性回歸
    years_extended = pd.Series(range(1880, 2051)) # 生成一個從 1880 到 2050 的年份序列
    sea_levels_all = slope_all * years_extended + intercept_all # 使用斜率和截距計算對應年份的 y 軸數值，生成擬合線數據
    plt.plot(years_extended, sea_levels_all, label='Best fit (1880-2050)', color='red')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000] # 篩選年份大於等於 2000 的數據，接下來同上
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    sea_levels_recent = slope_recent * years_recent + intercept_recent
    plt.plot(years_recent, sea_levels_recent, label='Best fit (2000-2050)', color='green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()