#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 10:40:11 2017

@author: Bharathi
#plot file
"""

import os
import urllib.request
import sys
import pandas as pd
from matplotlib import pylab as plt
import numpy as np
import download_data as DW
def plot_min_max(stationid, year):
    
    Citi_name, df_rename = DW.download(stationid, year)
    #obs2 = download(stationid2, year)
    #obs3 = download(stationid3, year)

    fig= plt.figure(num=1, figsize=(15,6))
    x = np.linspace(0,365,365)
    
    y = df_rename['Max Temp (Â°C)']
    y2 = df_rename['Min Temp (Â°C)']

    plt.plot(x,y,label="Max Temperature")
    plt.plot(x,y2,label="Min Temperature")
    plt.legend(bbox_to_anchor=(1, 1), loc=1)
    plt.xticks(np.arange(0,365,10)) 
    plt.title(Citi_name, color = "red", size = 15)
    plt.xlabel('Days', color = "green")
    plt.ylabel('Temperature',color = "green")
    plt.savefig(citi_name)
    plt.show()
   


stationid1 = 50092
stationid2 = 50089
stationid3 = 6842
year = 2015


    

plot_min_max(stationid1, year)
fig = plt.gcf()
fig.canvas.set_window_title('Figure 1')
plt.savefig('Figure1.png')
plt.clf()


plot_min_max(stationid2, year)
fig = plt.gcf()
fig.canvas.set_window_title('Figure 2')
plt.savefig('Figure2.png')
plt.clf()


plot_min_max(stationid3, year)
fig = plt.gcf()
fig.canvas.set_window_title('Figure 3')
plt.savefig('Figure3.png')
plt.clf()
