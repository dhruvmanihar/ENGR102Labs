# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 11b_Act1b
# Date: 11/27/2021


#Define the partb() function.
def partb(facility_names, operation_cost, production_value):

    #empty profitability list
    profitability = []

    #loop that appends into profitability
    for i in range(len(operation_cost)):

        value = production_value[i] - operation_cost[i]

        profitability.append(value)

    maxValue = max(profitability)

    maxIndex = profitability.index(maxValue)

    return facility_names[maxIndex], profitability[maxIndex]
