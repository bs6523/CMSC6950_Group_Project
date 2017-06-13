#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 10:40:11 2017

@author: Bharathi
#plot file
"""

def plot_min_max(stationid, year):
    
    Citi_name, df_rename = download(stationid, year)
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
    plt.show()
    
    
    

stationid1 = 50092
stationid2 = 50089
stationid3 = 6842
year = 2015

plot_min_max(stationid1, year)

