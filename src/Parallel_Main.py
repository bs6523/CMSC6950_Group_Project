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
import GDD_bokeh_Q2 as Q2_B
import Plot_GDD_bokeh_Q2_3 as Q2_3
from bokeh import plotting
import time


start = time.time()

stationid1 = 50092
stationid2 = 50089
stationid3 = 6842
stationid4 = 27378
year = 2015

x1=[stationid1, stationid2, stationid3]
y1=[2015, 2014, 2013, 2012]
x2=[stationid1, stationid2, stationid3, stationid4]

#......................................
#calling min_max function
def P_func1(x1):
        PM.plot_min_max(x1, year)


#......................................
#bokeh
def P_func2(x1):
        PM_B.plot_min_max(x1, year)


#......................................
#calling gdd plot
def P_func3(y1):
        PDD.plot_gdd(stationid1, y1)

#......................................
#2nd set for bokeh
def P_func4(x2):
        PDD_B.plot_gdd(x2)


# SECTION 2
#.....................................
#Section 2, question 1
def P_func5(x2):
        Q2_B.plot_gdd(x2)


#Section 2, question 3
def P_func6(x2):
	Q2_3.plot_gdd(x2)



#  MULTI PROCESSING EXECUTION
#......................................

Par_comp = Pool(5)                      # number of processes
Par_comp.map(P_func1, x1)
Par_comp.map(P_func2, x1)
Par_comp.map(P_func3, y1)
Par_comp.map(P_func4, x2)
Par_comp.map(P_func5, x2)
Par_comp.map(P_func6, x2)






stop = time.time()
print("measured Runtime: {:.3f} seconds".format(stop-start))
print(20*"-"+"\n")


print("main file run successful")
