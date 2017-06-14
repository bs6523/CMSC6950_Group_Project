#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 11:08:45 2017

@author: Bharathi

"""
import Plot_min_max as PM
import Plot_GDD as PDD



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


print("main file run successful") 