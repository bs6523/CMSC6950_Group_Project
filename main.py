#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Jun 13 11:08:45 2017

@author: Bharathi , gsahans

"""
import Plot_min_max as PM
import Plot_min_max_bokeh as PM_B
import Plot_GDD as PDD
import Plot_GDD_bokeh as PDD_B
import Plot_gdd_Q2_1 as Q2
import GDD_bokeh_Q2 as Q2_B
import Plot_GDD_bokeh_Q2_3 as Q2_3
from bokeh import plotting
import time


start = time.time()

stationid1 = 50092
stationid2 = 50089
stationid3 = 6842
year = 2015

start = time.time()

#--------------------------------
#calling min_max function
PM.plot_min_max(stationid1, year)
PM.plot_min_max(stationid2, year)
PM.plot_min_max(stationid3, year)

#bokeh
PM_B.plot_min_max(stationid1, year)
PM_B.plot_min_max(stationid2, year)
PM_B.plot_min_max(stationid3, year)
#-----------------------------------

#----------------------------------
#calling gdd plot
PDD.plot_gdd(stationid1, 2015)
PDD.plot_gdd(stationid1, 2014)
PDD.plot_gdd(stationid1, 2013)
PDD.plot_gdd(stationid1, 2012)


#bokeh
PDD_B.plot_gdd()
#----------------------------------
#Section 2, question 1
#Q2.plot_gdd_Q2_1(stationid1, 2015)
#Q2.plot_gdd_Q2_1(stationid2, 2015)
#Q2.plot_gdd_Q2_1(stationid3, 2015)
Q2_B.plot_gdd()

# Section 2, question 3
Q2_3.plot_gdd()

stop = time.time()                  # stop timer
print("measured Runtime: {:.3f} seconds".format(stop-start))
print(20*"-"+"\n")




print("main file run successful")
