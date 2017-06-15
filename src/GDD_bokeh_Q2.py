#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author gsahans

"""
#This code shows the bokeh plot showing GDD over selected canadian cities

import gdd_Cal as GD
import numpy as np
from bokeh import plotting
import os
import download_data as DW


def plot_gdd(stationid):

    Citi_name, temp = DW.download(stationid, 2014)

    gdd1 = GD.gdd_cal(stationid, 2015)
    gdd2 = GD.gdd_cal(stationid, 2014)
    gdd3 = GD.gdd_cal(stationid, 2013)
    gdd4 = GD.gdd_cal(stationid, 2016)

    figure_name = "Bokeh_GDD_{}.html".format(stationid)
    bok_title="GDD PLOT {}".format(Citi_name)

    plot=plotting.figure(title=bok_title)
    plot.xaxis.axis_label = 'Year/Time'
    plot.yaxis.axis_label = 'Accumlated GDD'

    x_data=np.linspace(1,13,12)

    plot.line(x_data,gdd1, legend="2015", line_color = "red")

    plot.line(x_data,gdd2, legend="2015", line_color = "blue")
    plot.circle(x_data,gdd2, legend="2014", line_color = "blue")

    plot.line(x_data,gdd3, legend="2015", line_color = "green")
    plot.triangle(x_data,gdd3, legend="2013", line_color = "green")

    plot.line(x_data,gdd4, legend="2016", line_color = "orange")

    plotting.output_file(os.path.dirname(os.path.realpath(__file__)) + "/../plots/"+ figure_name, title=bok_title)
    plotting.show(plot)
