class: center, middle
background-image: url(img2.jpg) 
background-size: contain

### A PROJECT FOR CALCULATING GROWING DEGREE DAYS (GDD) IN CANADA
     
---

### Abstract 
    
---

### Introduction
The Growing Degree Day, or GDD, is a heat index that can be used to predict when a crop will reach maturity. Each day’s GDD is calculated by subtracting a reference temperature, which varies with plant species, from the daily mean temperature.
The reference temperature for a given plant is the temperature below which its development slows or stops. For example, cool season plants, have a reference temperature of 40 degrees fahrenheit while warm season plants, have a reference temperature of 50 degrees fahrenheit.
The development of plants depends on the accumulation of heat and since cool season plants have a lower reference temperature, they accumulate GDDs faster than warm season plants.

The base temperature is that temperature below which plant growth is zero. GDs are calculated each day as maximum temperature plus the minimum temperature divided by 2 (or the mean temperature), minus the base temperature. GDUs are accumulated by adding each day’s GDs contribution as the season progresses.
---
    
### GDD
To calculate the GDD, we had to use maximum temperature plus the minimum temperature divided by 2 (or the mean temperature), minus the base temperature.

The code below is for calculating GDD:


import numpy as np
import download_data as DW
import math



def gdd_tot(mean):
     temp = 0.0
     for i in mean:
         if i < 10.0:
             temp = temp + 0.0
         elif not math.isnan(i) :
             temp = temp + (i - 10.0)
     return temp

---

### Data Visualization


<img src="/home/solidbay/group_project/Fig1.png" width="720" height="402"/>


---

### Data Visualization

<img src="/home/solidbay/group_project/Fig2.png" width="720" height="402"/>

---

### Data Visualization

<img src="/home/solidbay/group_project/Fig3.png" width="720" height="402"/>


---

### Data Visualization


<img src="/home/solidbay/group_project/Fig4.png" width="720" height="402"/>



  
