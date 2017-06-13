#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 14:35:33 2017

@author: Boxuan Li
"""

import os
import urllib.request
import sys
import pandas as pd
from matplotlib import pylab as plt
import numpy as np
import download_data as DW
import math





def gdd_tot(mean):
     temp = 0.0
     for i in mean:
         if i < 10.0:
             temp = temp + 0.0
         elif not math.isnan(i) :
             temp = temp + (i - 10.0)
     return temp



def gdd_cal(stationid, year):
    Citi_name, df_rename = DW.download(stationid, year)
    
    a=[]
    
    x = np.linspace(0,12,12)
    
    
    for i in range(1,365,31):
        a.append(gdd_tot(df_rename['Mean Temp (Â°C)'][0:i]))
    
    
    #a.append(gdd_tot(df_rename['Mean Temp (Â°C)'][0:31]))
    #a.append(gdd_tot(df_rename['Mean Temp (Â°C)'][0:59]))
    #a.append(gdd_tot(df_rename['Mean Temp (Â°C)'][0:90]))
    #a.append(gdd_tot(df_rename['Mean Temp (Â°C)'][0:120]))
    #a.append(gdd_tot(df_rename['Mean Temp (Â°C)'][0:151]))
    #a.append(gdd_tot(df_rename['Mean Temp (Â°C)'][0:181]))
    
    #a.append(gdd_tot(df_rename['Mean Temp (Â°C)'][0:212]))
    #a.append(gdd_tot(df_rename['Mean Temp (Â°C)'][0:243]))
    #a.append(gdd_tot(df_rename['Mean Temp (Â°C)'][0:273]))
    #a.append(gdd_tot(df_rename['Mean Temp (Â°C)'][0:304]))
   # a.append(gdd_tot(df_rename['Mean Temp (Â°C)'][0:334]))
   # a.append(gdd_tot(df_rename['Mean Temp (Â°C)'][0:365]))
    
   
    plt.plot(x,a)
    plt.xticks(np.arange(1,12,1))
    

    return a

             
    



stationid1 = 50092
stationid2 = 50089
stationid3 = 6842
year = 2015
print("temp is:")
print(gdd_cal(stationid1, year))
print(gdd_cal(stationid2, year))
print(gdd_cal(stationid3, year))

print("temp end:")