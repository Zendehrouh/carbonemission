import matplotlib.pyplot as plt
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.charts import Bar
from bokeh.palettes import inferno,plasma, viridis
from bokeh.models import Legend
import itertools
import numpy as np

def plot_co2emission_year_matplotlib(column_order, df):
    x = df.loc[df['Column_Order'] == column_order, 'YYYYMM']
    y = df.loc[ df['Column_Order'] == column_order, "Value"]
    plt.figure(figsize=(8,8))
    plt.plot(x,y)
    plt.xlabel('Time (Monthly)')
    if column_order == 1:
        plt.ylabel('Coal Electric Power Sector CO2 Emissions')
    elif column_order == 2:
        plt.ylabel('Natural Gas Electric Power Sector CO2 Emissions')
    elif column_order == 3:
        plt.ylabel('Distillate Fuel, Including Kerosene-Type Jet Fuel, Oil Electric Power Sector CO2 Emissions')
    elif column_order == 4:
        plt.ylabel('Petroleum Coke Electric Power Sector CO2 Emissions')
    elif column_order == 5:
        plt.ylabel('Residual Fuel Oil Electric Power Sector CO2 Emissions')
    elif column_order == 6:
        plt.ylabel('Petroleum Electric Power Sector CO2 Emissions')
    elif column_order == 7:
        plt.ylabel('eothermal Energy Electric Power Sector CO2 Emissions')
    elif column_order == 8:
        plt.ylabel('Non-Biomass Waste Electric Power Sector CO2 Emissions')
    elif column_order == 9:
        plt.ylabel('Total Energy Electric Power Sector CO2 Emissions')
            
    plt.show()    
    return 


######################################################################################

def plot_co2emission_year_together_matplotlib(ls , df):
    ls.sort()
    dict ={ '1' : 'Coal Electric Power Sector CO2 Emissions', 
'2' : 'Natural Gas Electric Power Sector CO2 Emissions', 
'3' : 'Distillate Fuel, Including Kerosene-Type Jet Fuel, Oil Electric Power Sector CO2 Emissions',
'4' : 'Petroleum Coke Electric Power Sector CO2 Emissions',
'5' : 'Residual Fuel Oil Electric Power Sector CO2 Emissions',
'6' : 'Petroleum Electric Power Sector CO2 Emissions',
'7' : 'Geothermal Energy Electric Power Sector CO2 Emissions',
'8' : 'Non-Biomass Waste Electric Power Sector CO2 Emissions',
'9' : 'Total Energy Electric Power Sector CO2 Emissions'}
    n = np.size(ls)
    i=0
    plt.figure(figsize=(8,8))
    while i < n:
        plt.plot( df.loc[df['Column_Order'] == ls[i], 'YYYYMM'] , df.loc[ df['Column_Order'] == ls[i], "Value"], label =  dict[str(ls[i])])
        i=i+1
    plt.xlabel('Time (Monthly)')
    plt.ylabel('Million Metric Tons of Carbon Dioxide')
    plt.legend(loc='best', bbox_to_anchor=(0.5, -0.1))    
    plt.show()    
    return    
########################################################################################
def plot_co2emission_year_bokeh(column_order, df):   
    x = df.loc[df['Column_Order'] == column_order, 'YYYYMM']
    y = df.loc[ df['Column_Order'] == column_order, "Value"]
    TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select,lasso_select"
    output_notebook()
    fig = figure( width =600, height= 600, x_axis_type="datetime", tools= TOOLS)
    fig.line(x,y)
    fig.xaxis.axis_label = 'Time (Monthly)'
    if column_order == 1:
        fig.yaxis.axis_label = 'Coal Electric Power Sector CO2 Emissions'
    elif column_order == 2:
        fig.yaxis.axis_label = 'Natural Gas Electric Power Sector CO2 Emissions'
    elif column_order == 3:
        fig.yaxis.axis_label = 'Distillate Fuel, Including Kerosene-Type Jet Fuel, Oil Electric Power Sector CO2 Emissions'
    elif column_order == 4:
        fig.yaxis.axis_label = 'Petroleum Coke Electric Power Sector CO2 Emissions'
    elif column_order == 5:
        fig.yaxis.axis_label = 'Residual Fuel Oil Electric Power Sector CO2 Emissions'
    elif column_order == 6:
        fig.yaxis.axis_label = 'Petroleum Electric Power Sector CO2 Emissions'
    elif column_order == 7:
        fig.yaxis.axis_label = 'eothermal Energy Electric Power Sector CO2 Emissions'
    elif column_order == 8:
        fig.yaxis.axis_label = 'Non-Biomass Waste Electric Power Sector CO2 Emissions'
    elif column_order == 9:
        fig.yaxis.axis_label = 'Total Energy Electric Power Sector CO2 Emissions'
    show(fig)
    return

########################################################################################

########################################################################################
def plot_co2emission_year_together_bokeh(ls, df):
    ls.sort()
    dict ={ '1' : 'Coal Electric Power Sector CO2 Emissions', 
'2' : 'Natural Gas Electric Power Sector CO2 Emissions', 
'3' : 'Distillate Fuel, Including Kerosene-Type Jet Fuel, Oil Electric Power Sector CO2 Emissions',
'4' : 'Petroleum Coke Electric Power Sector CO2 Emissions',
'5' : 'Residual Fuel Oil Electric Power Sector CO2 Emissions',
'6' : 'Petroleum Electric Power Sector CO2 Emissions',
'7' : 'Geothermal Energy Electric Power Sector CO2 Emissions',
'8' : 'Non-Biomass Waste Electric Power Sector CO2 Emissions',
'9' : 'Total Energy Electric Power Sector CO2 Emissions'}
    n = np.size(ls)
    color = plasma(n)
    i=0
    TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select,lasso_select"
    output_notebook()
    fig = figure( width =900, height= 900, x_axis_type="datetime", tools= TOOLS)
    while i < n:
        fig.line( df.loc[df['Column_Order'] == ls[i], 'YYYYMM'] , df.loc[ df['Column_Order'] == ls[i], "Value"], legend=dict[str(ls[i])], color=color[i] )
        i=i+1
    fig.xaxis.axis_label = 'Time (Monthly)'
    fig.yaxis.axis_label = 'Million Metric Tons of Carbon Dioxide'
    show(fig)    
    return  
##########################################################################################
def plot_CO2_per_source_bar_matplotlib(df):
    CO2_per_source = df.groupby(["Description"])['Value'].sum().sort_values()
    plt.figure(figsize=(8,8))
    plt.bar(np.arange(len(CO2_per_source)), CO2_per_source, align = 'center', alpha = 0.9, width=0.7)
    plt.xticks( np.arange(len(CO2_per_source)), CO2_per_source.index, rotation ='vertical')
    plt.title('CO2 emission per source')
    plt.ylabel('Million Metric Tons of Carbon Dioxide')
    plt.show()
    return
#########################################################################################
def plot_CO2_per_source_bar_bokeh(df):
    output_notebook()
    CO2_per_source = df.groupby(["Description"])['Value'].sum().sort_values()
    p = Bar(CO2_per_source, title = 'CO2 emission per source',  width=700, legend =None)
    p.yaxis.axis_label = 'Million Metric Tons of CO2'
    show(p)
    return