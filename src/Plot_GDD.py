#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:14:11 2017

@author: Bharathi
"""
# This code plots the accumulated gdd over the selected canadian cities

import gdd_Cal as GD
from matplotlib import pylab as plt
import numpy as np
import download_data as DW

def plot_gdd(stationid, year):

    Citi_name, df_rename = DW.download(stationid, year)

    gdd = GD.gdd_cal_accum(stationid, year)
    figure_name = "Fig_GDD_{}.png".format(stationid)

    x = np.linspace(1,13,12)
    fig= plt.figure(num=1, figsize=(10,6))
    plt.title("accumulated GDD "+ Citi_name)
    plt.plot(x,gdd, label = year)
    plt.xlabel("Year/Time")
    plt.ylabel("accumulated GDD")
    plt.legend(bbox_to_anchor=(1, 1), loc=1)

    fig.savefig("../plots/"+figure_name) #for saving figure 
    #plt.show()
