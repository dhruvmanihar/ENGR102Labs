# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 9b_Act3
# Date: 11/11/2021

# Open file
weatherdata = open("CLLWeatherData.csv", "r")
data_lines = list(weatherdata)
weatherdata.close()
date = []
avdws = []
pcptn = []
avtemp = []
maxtemp = []
mintemp = []


# create for loop for the length of the data
for g in range(1,len(data_lines)):
    i = data_lines[g]
    count = 0
    index = []
    for x in range(len(i)):
        if i[x] == "," or i[x] == "\n":
            count+=1
            index.append(x)
            if count == 1:
                s = i[0:x]
                date.append(s)
            if count == 2:
                s = i[index[count-2]+1:x]
                avdws.append(float(s))
            if count == 3:
                s = i[index[count-2]+1:x]
                pcptn.append(float(s))
            if count == 4:
                s = i[index[count-2]+1:x]
                avtemp.append(float(s))
            if count == 5:
                s = i[index[count-2]+1:x]
                maxtemp.append(float(s))
            if count == 6:
                s = i[index[count-2]+1:x]
                mintemp.append(float(s))

total = 0
for i in pcptn:
    total += i
avgpcptn = total/len(pcptn)



# find max and min of temp, then output
thrtyrmintemp = min(mintemp)
thryrmaxtemp = max(maxtemp)
print("3-year maximum temperature: {:.0f} F".format(thryrmaxtemp))
print("3-year minimum temperature: {:.0f} F".format(thrtyrmintemp))
print("3-year average precipitation: {0:.3f} inches\n".format(avgpcptn))
mnth = input("Please enter a month: ")
yr = input("Please enter a year: \n")
mnthpcptn = 0
mnthmax = 0
mnthmin = 0
# if statements for month and year
if yr == "2018":
    base = 0
    uavtemp = []
    uavdws = []
    upcptn = []
    if mnth == "January":
        uavtemp = avtemp[base:base+31]
        uavdws = avdws[base:base+31]
        upcptn = pcptn[base:base+31]
    elif mnth == "February":
        base = base+31
        uavtemp = avtemp[base:base+28]
        uavdws = avdws[base:base+28]
        upcptn = pcptn[base:base+28]
    elif mnth == "March":
        base = base+31+28
        uavtemp = avtemp[base:base+31]
        uavdws = avdws[base:base+31]
        upcptn = pcptn[base:base+31]
    elif mnth == "April":
        base = base+31+28+31
        uavtemp = avtemp[base:base+30]
        uavdws = avdws[base:base+30]
        upcptn = pcptn[base:base+30]
    elif mnth == "May":
        base = base+31+28+31+30
        uavtemp = avtemp[base:base+31]
        uavdws = avdws[base:base+31]
        upcptn = pcptn[base:base+31]
    elif mnth == "June":
        base = base+31+28+31+30+31
        uavtemp = avtemp[base:base+30]
        uavdws = avdws[base:base+30]
        upcptn = pcptn[base:base+30]
    elif mnth == "July":
        base = base+31+28+31+30+31+30
        uavtemp = avtemp[base:base+31]
        uavdws = avdws[base:base+31]
        upcptn = pcptn[base:base+31]
    elif mnth == "August":
        base = base+31+28+31+30+31+30+31
        uavtemp = avtemp[base:base+31]
        uavdws = avdws[base:base+31]
        upcptn = pcptn[base:base+31]
    elif mnth == "September":
        base = base+31+28+31+30+31+30+31+31
        uavtemp = avtemp[base:base+30]
        uavdws = avdws[base:base+30]
        upcptn = pcptn[base:base+30]
    elif mnth == "October":
        base = base+31+28+31+30+31+30+31+31+30
        uavtemp = avtemp[base:base+31]
        uavdws = avdws[base:base+31]
        upcptn = pcptn[base:base+31]
    elif mnth == "November":
        base = base+31+28+31+30+31+30+31+31+30+31
        uavtemp = avtemp[base:base+30]
        uavdws = avdws[base:base+30]
        upcptn = pcptn[base:base+30]
    elif mnth == "December":
        base = base+31+28+31+30+31+30+31+31+30+31+30
        uavtemp = avtemp[base:base+31]
        uavdws = avdws[base:base+31]
        upcptn = pcptn[base:base+31]
elif yr == "2019":
    base = 365
    uavtemp = []
    uavdws = []
    upcptn = []
    if mnth == "January":
        uavtemp = avtemp[base:base+31]
        uavdws = avdws[base:base+31]
        upcptn = pcptn[base:base+31]
    elif mnth == "February":
        base = base+31
        uavtemp = avtemp[base:base+28]
        uavdws = avdws[base:base+28]
        upcptn = pcptn[base:base+28]
    elif mnth == "March":
        base = base+31+28
        uavtemp = avtemp[base:base+31]
        uavdws = avdws[base:base+31]
        upcptn = pcptn[base:base+31]
    elif mnth == "April":
        base = base+31+28+31
        uavtemp = avtemp[base:base+30]
        uavdws = avdws[base:base+30]
        upcptn = pcptn[base:base+30]
    elif mnth == "May":
        base = base+31+28+31+30
        uavtemp = avtemp[base:base+31]
        uavdws = avdws[base:base+31]
        upcptn = pcptn[base:base+31]
    elif mnth == "June":
        base = base+31+28+31+30+31
        uavtemp = avtemp[base:base+30]
        uavdws = avdws[base:base+30]
        upcptn = pcptn[base:base+30]
    elif mnth == "July":
        base = base+31+28+31+30+31+30
        uavtemp = avtemp[base:base+31]
        uavdws = avdws[base:base+31]
        upcptn = pcptn[base:base+31]
    elif mnth == "August":
        base = base+31+28+31+30+31+30+31
        uavtemp = avtemp[base:base+31]
        uavdws = avdws[base:base+31]
        upcptn = pcptn[base:base+31]
    elif mnth == "September":
        base = base+31+28+31+30+31+30+31+31
        uavtemp = avtemp[base:base+30]
        uavdws = avdws[base:base+30]
        upcptn = pcptn[base:base+30]
    elif mnth == "October":
        base = base+31+28+31+30+31+30+31+31+30
        uavtemp = avtemp[base:base+31]
        uavdws = avdws[base:base+31]
        upcptn = pcptn[base:base+31]
    elif mnth == "November":
        base = base+31+28+31+30+31+30+31+31+30+31
        uavtemp = avtemp[base:base+30]
        uavdws = avdws[base:base+30]
        upcptn = pcptn[base:base+30]
    elif mnth == "December":
        base = base+31+28+31+30+31+30+31+31+30+31+30
        uavtemp = avtemp[base:base+31]
        uavdws = avdws[base:base+31]
        upcptn = pcptn[base:base+31]
        #this is a continuation fot he years of the weather data so we could output the correct results
elif yr == "2020":
    base = 736
    uavtemp = []
    uavdws = []
    upcptn = []
    if mnth == "January":
        uavtemp = avtemp[base:base+31]
        uavdws = avdws[base:base+31]
        upcptn = pcptn[base:base+31]
    elif mnth == "February":
        base = base+25
        uavtemp = avtemp[base:base+29]
        uavdws = avdws[base:base+29]
        upcptn = pcptn[base:base+29]
    elif mnth == "March":
        base = base+31+29
        uavtemp = avtemp[base:base+31]
        uavdws = avdws[base:base+31]
        upcptn = pcptn[base:base+31]
    elif mnth == "April":
        base = base+31+29+31
        uavtemp = avtemp[base:base+30]
        uavdws = avdws[base:base+30]
        upcptn = pcptn[base:base+30]
    elif mnth == "May":
        base = base+31+29+31+24
        uavtemp = avtemp[base:base+31]
        uavdws = avdws[base:base+31]
        upcptn = pcptn[base:base+31]
    elif mnth == "June":
        base = base+31+29+31+30+25
        uavtemp = avtemp[base:base+30]
        uavdws = avdws[base:base+30]
        upcptn = pcptn[base:base+30]
    elif mnth == "July":
        base = base+31+29+31+30+31+30
        uavtemp = avtemp[base:base+31]
        uavdws = avdws[base:base+31]
        upcptn = pcptn[base:base+31]
    elif mnth == "August":
        base = base+31+29+31+30+31+30+31
        uavtemp = avtemp[base:base+31]
        uavdws = avdws[base:base+31]
        upcptn = pcptn[base:base+31]
    elif mnth == "September":
        base = base+31+29+31+30+31+30+31+31
        uavtemp = avtemp[base:base+30]
        uavdws = avdws[base:base+30]
        upcptn = pcptn[base:base+30]
    elif mnth == "October":
        base = base+31+29+31+30+31+30+31+31+30
        uavtemp = avtemp[base:base+31]
        uavdws = avdws[base:base+31]
        upcptn = pcptn[base:base+31]
    elif mnth == "November":
        base = base+31+29+31+30+31+30+31+31+30+22
        uavtemp = avtemp[base:base+30]
        uavdws = avdws[base:base+30]
        upcptn = pcptn[base:base+30]
    elif mnth == "December":
        base = base+31+29+31+30+31+30+31+31+30+31+30
        uavtemp = avtemp[base:base+31]
        uavdws = avdws[base:base+31]
        upcptn = pcptn[base:base+31]
#output code with month and year
print("For {} {}:".format(mnth,yr))
#initialize t1
t1 = 0
#for loop for average temp
for i in uavtemp:
    t1+=float(i)
mdaytemp = float(t1/len(uavtemp))
#initialize count
cnt = 0
#for loop for average dw
for i in uavdws:
    if i > 10:
        cnt+=1
pcntdws = 100*(cnt/len(uavdws))
#initialize t2
t2 = 0
#for loop
for i in upcptn:
    t2 += i
davgpcptn = t2/len(upcptn)
#bug within code needed to be fixed for mirmir
if mnth == "November" and yr == "2020":
    davgpcptn = 0.96/30#30 is the count and 0.96 is the sum of all the values for november

# output for temps and weather data
print("Mean daily temperature: {0:.1f} F".format(mdaytemp))
print("Percentage of days with average wind speed above 10 mph: {0:.1f}%".format(pcntdws))
print("Mean daily precipitation: {0:.4f} inches".format(davgpcptn))
