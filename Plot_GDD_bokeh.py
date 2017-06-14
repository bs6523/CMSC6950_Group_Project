#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: gsahans (gs3041)
"""
import gdd_Cal as GD
import numpy as np
from bokeh import plotting



def plot_gdd():

    stationid1 = 50092
    stationid2 = 50089
    stationid3 = 6842

    gdd1 = GD.gdd_cal_accum(stationid1, 2015)
    gdd2 = GD.gdd_cal_accum(stationid2, 2014)
    gdd3 = GD.gdd_cal_accum(stationid3, 2013)

    plot=plotting.figure(title="Plot GDD")
    plot.xaxis.axis_label = 'Year/Time'
    plot.yaxis.axis_label = 'Accumlated GDD'

    x_data=np.linspace(1,13,12)

    plot.line(x_data,gdd1, legend="2015", line_color = "red")

    plot.line(x_data,gdd2, legend="2015", line_color = "blue")
    plot.circle(x_data,gdd2, legend="2014", line_color = "blue")

    plot.line(x_data,gdd3, legend="2015", line_color = "green")
    plot.triangle(x_data,gdd3, legend="2013", line_color = "green")


    plotting.show(plot)
