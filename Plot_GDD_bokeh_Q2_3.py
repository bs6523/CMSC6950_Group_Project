#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Boxuan Li
"""
import gdd_Cal as GD
import gdd_Cal_Q2_3 as GDQ23
import numpy as np
from bokeh import plotting



def plot_gdd():

    stationid1 = 50092
    stationid2 = 50089
    stationid3 = 6842

    gdd1 = GDQ23.gdd_cal_accum_SB(stationid1, 2015, 15)
    gdd2 = GDQ23.gdd_cal_accum_SB(stationid2, 2014, 15)
    gdd3 = GDQ23.gdd_cal_accum_SB(stationid3, 2013, 15)

    plot=plotting.figure(title="Plot GDD for Q2_3")
    plot.xaxis.axis_label = 'Year/Time'
    plot.yaxis.axis_label = 'Accumlated GDD'

    x_data=np.linspace(1,13,12)

    plot.line(x_data,gdd1, legend="2015", line_color = "red")

    plot.line(x_data,gdd2, legend="2015", line_color = "blue")
    plot.circle(x_data,gdd2, legend="2014", line_color = "blue")

    plot.line(x_data,gdd3, legend="2015", line_color = "green")
    plot.triangle(x_data,gdd3, legend="2013", line_color = "green")


    plotting.show(plot)
