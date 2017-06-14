#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 11:08:45 2017

@author: Bharathi

"""
import Plot_min_max as PM
import Plot_GDD as PDD
import Plot_gdd_Q2_1 as Q2



stationid1 = 50092
stationid2 = 50089
stationid3 = 6842
year = 2015

#calling min_max function
PM.plot_min_max(stationid1, year)
PM.plot_min_max(stationid2, year)
PM.plot_min_max(stationid3, year)

#calling gdd plot
PDD.plot_gdd(stationid1, 2015)
PDD.plot_gdd(stationid1, 2014)
PDD.plot_gdd(stationid1, 2013)
PDD.plot_gdd(stationid1, 2012)


#Section 2, question 1
#Q2.plot_gdd_Q2_1(stationid1, 2015)
#Q2.plot_gdd_Q2_1(stationid2, 2015)
#Q2.plot_gdd_Q2_1(stationid3, 2015)




print("main file run successful") 