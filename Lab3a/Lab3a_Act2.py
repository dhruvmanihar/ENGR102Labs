# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Mariana Sanchez
#               Aaron Garcia
#               Dhruv Manihar
#               Ethan Nguyen
# Section:      514
# Assignment:   Lab 3a_2
# Date:         09 15 2021
#

#interpolate function
def interpolate():
    t1 = int(input("Enter time 1: "))
    x1 = int(input("Enter the x position of the object at time 1: "))
    y1 = int(input("Enter the y position of the object at time 1: "))
    z1 = int(input("Enter the z position of the object at time 1: "))
    t2 = int(input("Enter time 2: "))
    x2 = int(input("Enter the x position of the object at time 2: "))
    y2 = int(input("Enter the y position of the object at time 2: "))
    z2 = int(input("Enter the z position of the object at time 2: "))
    print()
    dt = (t2 - t1) / 4
    time_list = [t1, t1 + dt, t1 + (2 * dt), t1 + (3 *dt), t2]
    mean_x = (x2 - x1) / (t2 -t1)
    mean_y = (y2 - y1) / (t2 -t1)
    mean_z = (z2 - z1) / (t2 -t1)
    for t in time_list:
        x = x1 + (mean_x * (t - t1))
        y = y1 + (mean_y * (t - t1))
        z = z1 + (mean_z * (t - t1))
        solution = "At time {:.1f} seconds the object is at ({:.2f}, {:.2f}, {:.2f})"
        print(solution.format(t, x, y, z))

#function call
interpolate()
