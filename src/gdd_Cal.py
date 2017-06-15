#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 14:35:33 2017
@authors: Boxuan Li
        
"""
import sys
import numpy as np
import download_data as DW
import math

#input_file = sys.argv[1]
#tbase = sys.argv[2]
#tupper = sys.argv[3]

tbase=10

def gdd_tot(mean):
     temp = 0.0
     for i in mean:
         if i < tbase:
             temp = temp + 0.0
         elif not math.isnan(i) :
             temp = temp + (i - 10.0)
     return temp

def gdd_cal_accum(stationid, year):
   
    Citi_name, df_rename = DW.download(stationid, year)
    
    gdd=[]
    for i in range(1,365,31):
        gdd.append(gdd_tot(df_rename['Mean Temp (Â°C)'][0:i]))
    
    return gdd

def gdd_cal(stationid, year):
   
    Citi_name, df_rename = DW.download(stationid, year)
    
    gdd=[]
    
    gdd.append(gdd_tot(df_rename['Mean Temp (Â°C)'][0:30]))
    gdd.append(gdd_tot(df_rename['Mean Temp (Â°C)'][30:60]))
    gdd.append(gdd_tot(df_rename['Mean Temp (Â°C)'][60:90]))
    gdd.append(gdd_tot(df_rename['Mean Temp (Â°C)'][90:120]))
    gdd.append(gdd_tot(df_rename['Mean Temp (Â°C)'][120:150]))
    gdd.append(gdd_tot(df_rename['Mean Temp (Â°C)'][150:180]))
        
    gdd.append(gdd_tot(df_rename['Mean Temp (Â°C)'][180:210]))
    gdd.append(gdd_tot(df_rename['Mean Temp (Â°C)'][210:240]))
    gdd.append(gdd_tot(df_rename['Mean Temp (Â°C)'][240:270]))
    gdd.append(gdd_tot(df_rename['Mean Temp (Â°C)'][270:300]))
    gdd.append(gdd_tot(df_rename['Mean Temp (Â°C)'][300:330]))
    gdd.append(gdd_tot(df_rename['Mean Temp (Â°C)'][330:364]))
    
    return gdd
