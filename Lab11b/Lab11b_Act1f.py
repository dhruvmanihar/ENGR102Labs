# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 11b_Act1f
# Date: 11/27/2021


#partf function
def partf(time, distance):
    #empty velocities list
    velocities = []
    #lopp appends new values
    for i in range(1, len(time)):
        velocities.append((distance[i] - distance[i - 1]) / (time[i] - time[i - 1]))
    return velocities


times = [1, 3, 5, 7]
distances = [25, 29, 35, 70]
print(partf(times, distances))
