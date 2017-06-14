#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 14:35:33 2017

@author: Boxuan Li
"""
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
    
    gdd=[]
    for i in range(1,365,31):
        gdd.append(gdd_tot(df_rename['Mean Temp (Â°C)'][0:i]))
    
    return gdd