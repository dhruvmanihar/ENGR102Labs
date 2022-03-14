# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 10b_Act2
# Date: 11/17/2021


open ('CLLWeatherData.csv', 'w')
from math import *
import numpy as np
import matplotlib.pyplot as plt


weatherdata = open("CLLWeatherData.csv", "r")
da = list(weatherdata)
da = da[1:len(da)]

# settings for the graphs
date = []
month = []
precipitation = []
precipitation1 = []
averagewindspeed = []
averagetemperature = []
mintemp = []
maxtemp = []
min_month = []
max_month = []

# create lists for the variables in doc
for h in range(0, len(da)):
    i = da[h]
    count = 0
    ind = []
    for x in range(len(i)):
        if i[x] == "," or i[x] == "\n":
            count += 1
            ind.append(x)
            if count == 1:
                s = i[0:x]
                date.append(s)
            if count == 2:
                s = i[ind[count - 2] + 1:x]
                averagewindspeed.append(float(s))
            if count == 3:
                s = i[ind[count - 2] + 1:x]
                precipitation.append(float(s))
            if count == 4:
                s = i[ind[count - 2] + 1:x]
                averagetemperature.append(float(s))
            if count == 5:
                s = i[ind[count - 2] + 1:x]
                maxtemp.append(float(s))
            if count == 6:
                s = i[ind[count - 2] + 1:x]
                mintemp.append(float(s))


# if else statements to get the data for months
def append(month, date):
    for i in range(len(date)):

        if date[i][:2] == "1/":
            month.append("1")
        elif date[i][:2] == "2/":
            month.append("2")
        elif date[i][:2] == "3/":
            month.append("3")
        elif date[i][:2] == "4/":
            month.append("4")
        elif date[i][:2] == "5/":
            month.append("5")
        elif date[i][:2] == "6/":
            month.append("6")
        elif date[i][:2] == "7/":
            month.append("7")
        elif date[i][:2] == "8/":
            month.append("8")
        elif date[i][:2] == "9/":
            month.append("9")
        elif date[i][:2] == "10":
            month.append("10")
        elif date[i][:2] == "11":
            month.append("11")
        elif date[i][:2] == "12":
            month.append("12")


append(month, date)

# average for months
month1_min, month2_min, month3_min, month4_min, month5_min, month6_min, month7_min, month8_min, month9_min, month10_min, month11_min, month12_min = [], [], [], [], [], [], [], [], [], [], [], []
month1_max, month2_max, month3_max, month4_max, month5_max, month6_max, month7_max, month8_max, month9_max, month10_max, month11_max, month12_max = [], [], [], [], [], [], [], [], [], [], [], []


# min

# create a list of values for each month
def min_temp_month():
    # getting data by months
    for i in range(len(date)):

        if date[i][:2] == "1/":
            month1_min.append(mintemp[i])

        elif date[i][:2] == "2/":
            month2_min.append(mintemp[i])

        elif date[i][:2] == "3/":
            month3_min.append(mintemp[i])

        elif date[i][:2] == "4/":
            month4_min.append(mintemp[i])

        elif date[i][:2] == "5/":
            month5_min.append(mintemp[i])

        elif date[i][:2] == "6/":
            month6_min.append(mintemp[i])

        elif date[i][:2] == "7/":
            month7_min.append(mintemp[i])

        elif date[i][:2] == "8/":
            month8_min.append(mintemp[i])

        elif date[i][:2] == "9/":
            month9_min.append(mintemp[i])

        elif date[i][:2] == "10":
            month10_min.append(mintemp[i])

        elif date[i][:2] == "11":
            month11_min.append(mintemp[i])

        elif date[i][:2] == "12":
            month12_min.append(mintemp[i])


min_temp_month()


# calculate sum of values for lists
def sumofcalculation(month1_min):
    count = 0
    for i in range(len(month1_min)):
        count += month1_min[i]

    count = count / (len(month1_min))
    min_month.append(count)


sumofcalculation(month1_min)
sumofcalculation(month2_min)
sumofcalculation(month3_min)
sumofcalculation(month4_min)
sumofcalculation(month5_min)
sumofcalculation(month6_min)
sumofcalculation(month7_min)
sumofcalculation(month8_min)
sumofcalculation(month9_min)
sumofcalculation(month10_min)
sumofcalculation(month11_min)
sumofcalculation(month12_min)


# max for lists of values of months
def max_temp_month():
    # getting data by months
    for i in range(len(date)):
        if date[i][:2] == "1/":
            month1_max.append(maxtemp[i])

        elif date[i][:2] == "2/":
            month2_max.append(maxtemp[i])

        elif date[i][:2] == "3/":
            month3_max.append(maxtemp[i])

        elif date[i][:2] == "4/":
            month4_max.append(maxtemp[i])

        elif date[i][:2] == "5/":
            month5_max.append(maxtemp[i])

        elif date[i][:2] == "6/":
            month6_max.append(maxtemp[i])

        elif date[i][:2] == "7/":
            month7_max.append(maxtemp[i])

        elif date[i][:2] == "8/":
            month8_max.append(maxtemp[i])

        elif date[i][:2] == "9/":
            month9_max.append(maxtemp[i])

        elif date[i][:2] == "10":
            month10_max.append(maxtemp[i])

        elif date[i][:2] == "11":
            month11_max.append(maxtemp[i])

        elif date[i][:2] == "12":
            month12_max.append(maxtemp[i])


max_temp_month()


# calculate sum of values for lists
def sumofcalculation(month1_max):
    count = 0
    for i in range(len(month1_max)):
        count += month1_max[i]

    count = count / (len(month1_max))

    max_month.append(count)


sumofcalculation(month1_max)
sumofcalculation(month2_max)
sumofcalculation(month3_max)
sumofcalculation(month4_max)
sumofcalculation(month5_max)
sumofcalculation(month6_max)
sumofcalculation(month7_max)
sumofcalculation(month8_max)
sumofcalculation(month9_max)
sumofcalculation(month10_max)
sumofcalculation(month11_max)
sumofcalculation(month12_max)

# setting up the bar chart
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
monthactual = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
ax.bar(month, averagetemperature, color='olive')
plt.title('Average Temperature by Month')
plt.xlabel('Precipitation, in')
plt.ylabel("Average Temprature, F")
l2 = plt.plot(monthactual, max_month, color="red", label="High T")
l1 = plt.plot(monthactual, min_month, color="b", label="Low T")
plt.legend(bbox_to_anchor=(0, 1), loc="upper left", borderaxespad=0.)
plt.show()

# setting up the line graph
ax1 = plt.subplot()
l1, = ax1.plot(averagewindspeed, color='blue')
ax2 = ax1.twinx()
l2, = ax2.plot(averagetemperature, color='red')
plt.ylabel("Average Temprature, F")
ax1.set_ylabel("Average Wind Speed, mph")
plt.title("Average Temperature and Wind Speed")
plt.legend([l1, l2], ["Wind Avg", "Temp Avg"])
plt.show()

# for loop o get rid of 0 values
for i in range(len(precipitation)):

    if precipitation[i] != 0:
        precipitation1.append(precipitation[i])

# setting up the histogram graph
plt.num_bins = 100
n, bins, patches = plt.hist(precipitation1, plt.num_bins, facecolor='blue', alpha=1)
plt.title("Histogram of precipitation")
plt.ylabel("Number of Days")
plt.xlabel("Precipitation, in")
plt.ylim([0, 50])
plt.show()

# setting up the scatter plot
plt.scatter([mintemp], [averagewindspeed], marker='o', s=10, color="black");
plt.xlabel('Minimum Temperature, F')
plt.ylabel("Average Wind Speed, mph")
plt.title("Average Wind Speed vs Minimum Temperature")
plt.show()
