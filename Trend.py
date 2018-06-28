import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def Trend(Column_order, df, trend_length):
    dict ={ '1' : 'Coal Electric Power Sector CO2 Emissions', 
'2' : 'Natural Gas Electric Power Sector CO2 Emissions', 
'3' : 'Distillate Fuel, Including Kerosene-Type Jet Fuel, Oil Electric Power Sector CO2 Emissions',
'4' : 'Petroleum Coke Electric Power Sector CO2 Emissions',
'5' : 'Residual Fuel Oil Electric Power Sector CO2 Emissions',
'6' : 'Petroleum Electric Power Sector CO2 Emissions',
'7' : 'Geothermal Energy Electric Power Sector CO2 Emissions',
'8' : 'Non-Biomass Waste Electric Power Sector CO2 Emissions',
'9' : 'Total Energy Electric Power Sector CO2 Emissions'}
    
    mo_ave=df.loc[ df['Column_Order'] == Column_order , "Value"].rolling( window=12).mean()
    plt.figure(figsize=(9,8))
    plt.plot(df.loc[ df['Column_Order'] == Column_order, "YYYYMM"], df.loc[ df['Column_Order'] == Column_order, "Value"], color='red', label = dict[str(Column_order)] )
    plt.plot(df.loc[ df['Column_Order'] == Column_order, "YYYYMM"],mo_ave, color = 'blue', label ='CO2 emision trend (moving average)')
    plt.xlabel('Time (Monthly)')
    plt.ylabel('Million Metric Tons of Carbon Dioxide')
    plt.legend(loc='best')
    plt.show()
    return
