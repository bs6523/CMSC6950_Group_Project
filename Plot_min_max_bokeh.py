#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 10:40:11 2017

@author: Boxuan Li
#plot file
"""
from matplotlib import pylab as plt
import numpy as np
import download_data as DW
from bokeh import plotting

def plot_min_max(stationid, year):
    
    #calling the download function and geting the table and citi name
    Citi_name, df_rename = DW.download(stationid, year)

    y = df_rename['Max Temp (Â°C)']
    y2 = df_rename['Min Temp (Â°C)']
    
    #creating Figure name


    print(Citi_name)
    
     

    plot1=plotting.figure(title = "Min/Max Temp Plot")
    plot1.xaxis.axis_label = 'Days'
    plot1.yaxis.axis_label = 'Temperature'
    
    x_data=np.linspace(0,365,365)
    
    
    plot1.line(x_data,y, legend="Max Temperature", line_color = "red")
    plot1.line(x_data,y2, legend="Min Temperature", line_color = "blue")
    plot1.circle(x_data,y2 , line_color = "blue")
    

    
    
    plotting.show(plot1)