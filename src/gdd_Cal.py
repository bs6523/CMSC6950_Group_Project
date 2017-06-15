#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 14:35:33 2017

@authors: Boxuan Li and team members
        
"""
import sys
import numpy as np
import download_data as DW
import math

File_name = sys.argv[1]
tbase = sys.argv[2]
tupper = sys.argv[3]


def gdd_tot_SB(mean, tbase):
     temp = 0.0
     for i in mean:
         if i < tbase:
             temp = temp + 0.0
         elif not math.isnan(i) :
             temp = temp + (i - tbase)
     return temp
     
def gdd_Q1_3(File_name, tbase, tupper):
   
    data = pd.read_csv('Data_csv/'+File_name, skiprows=25, sep=",", encoding="ISO-8859-1")
    
    gdd=[]
    for i in range(1,365,31):
        gdd.append(gdd_tot_SB(data['Mean Temp (Â°C)'][0:i], tbase))
    
return gdd 
