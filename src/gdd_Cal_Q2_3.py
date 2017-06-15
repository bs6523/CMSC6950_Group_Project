#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 14:35:33 2017

@author: Boxuan Li
"""
import numpy as np
import download_data as DW
import math


def gdd_tot_SB(mean, tbase):
     temp = 0.0
     for i in mean:
         if i < tbase:
             temp = temp + 0.0
         elif not math.isnan(i) :
             temp = temp + (i - tbase)
     return temp
     
def gdd_cal_accum_SB(stationid, year, tbase):
   
    Citi_name, df_rename = DW.download(stationid, year)
    
    gdd=[]
    for i in range(1,365,31):
        gdd.append(gdd_tot_SB(df_rename['Mean Temp (Â°C)'][0:i], tbase))
    
    return gdd 
