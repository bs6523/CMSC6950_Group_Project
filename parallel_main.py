#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from multiprocessing import Pool

"""
Created on Tue Jun 13 11:08:45 2017

@author: augustine and team members

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


start = time.time()                 # start timer



stationid1 = 50092
stationid2 = 50089
stationid3 = 6842
year = 2015

#--------------------------------
#calling min_max function_plot_save, bokehplot_of_min_max and gddplot
x1=[stationid1, stationid2, stationid3]
y1=[2015, 2014, 2013, 2012]

def P_func1(x1):
	PM.plot_min_max(x1, year)

def P_func2(x1):
	PM_B.plot_min_max(x1, year)

def P_func3(y1):
	PDD.plot_gdd(stationid1, y1)




Par_comp = Pool(1)
Par_comp.map(P_func1, x1)
Par_comp.map(P_func2, x1)
Par_comp.map(P_func3, y1)







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
