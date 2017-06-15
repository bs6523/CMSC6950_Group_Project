#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 10:40:11 2017

@author: Bharathi
#plot file
"""
from matplotlib import pylab as plt
import numpy as np
import download_data as DW

def plot_min_max(stationid, year):
    
    #calling the download function and geting the table and citi name
    Citi_name, df_rename = DW.download(stationid, year)


    fig= plt.figure(num=1, figsize=(15,6))
    x = np.linspace(0,365,365)
    
    y = df_rename['Max Temp (Â°C)']
    y2 = df_rename['Min Temp (Â°C)']
    
    #creating Figure name
    figure_name = "Fig_{}_{}.png".format(stationid, year)

    plt.plot(x,y,label="Max Temperature")
    plt.plot(x,y2,label="Min Temperature")
    
    plt.legend(bbox_to_anchor=(1, 1), loc=1)
    plt.xticks(np.arange(0,365,10)) 
    plt.title(Citi_name, color = "red", size = 15)
    plt.xlabel('Days', color = "green")
    plt.ylabel('Temperature',color = "green")
    
    fig.savefig(figure_name) #for saving figure 
    plt.show()
    
