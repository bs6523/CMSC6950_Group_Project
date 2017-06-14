#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 10:24:25 2017

@author: Bharathi
"""

import gdd_Cal as GD
from matplotlib import pylab as plt
import numpy as np


def plot_gdd_Q2_1(stationid, year):
    
    gdd = GD.gdd_cal(stationid, year)
    figure_name = "Fig_GDD_{}.png".format(stationid)
    
    
    x = np.linspace(1,13,12)
    fig= plt.figure(num=1, figsize=(10,6))
    plt.title("GDD")
    plt.plot(x,gdd, label = year)
    plt.xlabel("Month")
    plt.ylabel("GDD")
    plt.plot(x,gdd, label = year)
    plt.legend(bbox_to_anchor=(1, 1), loc=1)
    
    fig.savefig(figure_name) #for saving figure 
   # plt.xticks(np.arange(1,12,1))
