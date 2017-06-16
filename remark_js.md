class: center, middle
background-image: url(img2.jpg) 
background-size: contain
   
### A PROJECT FOR CALCULATING GROWING DEGREE DAYS (GDD) IN CANADA
             
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
### Plot Code

<img src="/home/solidbay/group_project/PlotCode.png" width="720" height="402"/>

---

### Data Visualization


<img src="/home/solidbay/group_project/Fig_50089_2015.png" width="720" height="402"/>

---

### Data Visualization
<img src="/home/solidbay/group_project/Fig_50092_2015.png" width="720" height="402"/>

---

Bharathi

<img src="/home/solidbay/group_project/1.png" width="720" height="402"/>

---



<img src="/home/solidbay/group_project/2.png" width="720" height="402"/>

---

<img src="/home/solidbay/group_project/3.png" width="720" height="602"/>

---
Boxuan Li


<img src="/home/solidbay/group_project/Page1.png" width="720" height="402"/>

---

<img src="/home/solidbay/group_project/Page2_1.png" width="720" height="402"/>

---

<img src="/home/solidbay/group_project/Page2_2.png" width="720" height="402"/>


---

<img src="/home/solidbay/group_project/Page3.png" width="720" height="402"/>


---

Gdd Plot

<iframe src=https://github.com/bs6523/CMSC6950_Group_Project/blob/master/plots/Bokeh_GDD_50089.html></iframe>


GDD over Tbase
```html
<iframe src=https://github.com/bs6523/CMSC6950_Group_Project/blob/master/plots/Bokeh_GDD_tbase50092.html></iframe>
```
---

### Data Visualization

<iframe src="https://github.com/bs6523/CMSC6950_Group_Project/blob/master/plots/Bokeh_Min-Max_50089.html" width="720" height="602"></iframe>

---

### Min-Max

<iframe src="https://github.com/bs6523/CMSC6950_Group_Project/blob/master/plots/Bokeh_Min-Max_6842.html">
</iframe>

---
###Gdd accumulated

<iframe src="https://github.com/bs6523/CMSC6950_Group_Project/blob/master/plots/Bokeh_GDD-Accum_27378.html"></iframe>


---

### Gdd Plot

<iframe src="https://github.com/bs6523/CMSC6950_Group_Project/blob/master/plots/Bokeh_GDD_50089.html"></iframe>

---
###GDD over Tbase
<iframe src="https://github.com/bs6523/CMSC6950_Group_Project/blob/master/plots/Bokeh_GDD_tbase50092.html"></iframe>






  
