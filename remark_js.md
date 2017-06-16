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



<img src="/home/solidbay/group_project/1.png" width="720" height="402"/>

---



<img src="/home/solidbay/group_project/2.png" width="720" height="402"/>

---

<img src="/home/solidbay/group_project/3.png" width="720" height="602"/>

---


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

<iframe src=https://github.com/bs6523/CMSC6950_Group_Project/blob/master/plots/Bokeh_GDD_tbase50092.html></iframe>

---

Data Visualization:

<iframe src="https://github.com/bs6523/CMSC6950_Group_Project/blob/master/plots/Bokeh_Min-Max_50089.html"></iframe>

---

Min-Max:

<iframe src="https://github.com/bs6523/CMSC6950_Group_Project/blob/master/plots/Bokeh_Min-Max_6842.html">
</iframe>

---

Gdd accumulated:

<iframe src="https://github.com/bs6523/CMSC6950_Group_Project/blob/master/plots/Bokeh_GDD-Accum_27378.html"></iframe>


---

Gdd Plot:

<iframe src="https://github.com/bs6523/CMSC6950_Group_Project/blob/master/plots/Bokeh_GDD_50089.html"></iframe>

---
GDD over Tbase:

<iframe src="https://github.com/bs6523/CMSC6950_Group_Project/blob/master/plots/Bokeh_GDD_tbase50092.html"></iframe>

---

The “main.py” which executes the core task, question 1 of secondary task and question 3 of secondary task, primarily spends it's time downloading data, computing GDD and plotting.


Fortunately the task can be parallelized based on cities and years.

x1=[stationid1, stationid2, stationid3]

y1=[2015, 2014, 2013, 2012]

x2=[stationid1, stationid2, stationid3, stationid4]

###calling min_max function

P_func1(x1)  

###bokeh

P_func2(x1)

###calling gdd plot

P_func3(y1)

###2nd set for bokeh

P_func4(x2)

###Section 2, question 1

def P_func5(x2)

###Section 2, question 3

def P_func6(x2)      

---

###  MULTI PROCESSING EXECUTION

<img src="/home/solidbay/Group_Project/CMSC6950_Group_Project/processor_1.png" width="720" height=""/>



<img src="/home/solidbay/Group_Project/CMSC6950_Group_Project/processor1.png" width="720" height="220"/>

---

<img src="/home/solidbay/Group_Project/CMSC6950_Group_Project/processor.png" width="720" height="402"/>



---

### Mark Down-to_Slide HTML Hosting on Github

<img src="/home/solidbay/Group_Project/CMSC6950_Group_Project/slide1.png" width="720" height="402"/>


<img src="/home/solidbay/Group_Project/CMSC6950_Group_Project/slide2.png" width="720" height="402"/>

 




  
