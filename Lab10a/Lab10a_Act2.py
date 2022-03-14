# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Mariana Sanchez
#               Aaron Garcia
#               Dhruv Manihar
#               Ethan Nguyen
# Section:      514
# Assignment:   Lab 10a_2
# Date:         11 15 2021
#
# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material


from sympy import*
from sympy.plotting import (plot, plot_parametric)
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
x = symbols('x', real = True)
f1 = 6
f2 = 2
eq1 = (1/(4*f1))*x**2
eq2 = (1/(4*f2))*x**2
first = plot(eq1,(x,-2,2),show = False)
second = plot(eq2,(x,-2,2),show = False)
first.extend(second)
plt.title('parabolas')
first.show()


y = (2*x**3) + (3*x**2) - (11*x) - (6)
plot(y,(x,-4,4))


#import
import numpy as np
import matplotlib.pyplot as plt
from math import *


#create/format sin and cos graph
a = np.arange(-2*pi, 2*pi)
b = np.sin(a)
c = np.arange(-2*pi, 2*pi)
d = np.cos(a)
plt.subplot(2 ,1, 1)
plt.plot(a,b, label = "sin function")
plt.title('Sin Graph')
plt.legend(loc = 1)
plt.subplot(2, 1, 2)
plt.plot(c,d, label = "cos function" , c = 'red')
plt.title ('Cos Graph')
plt.legend (loc = 1)
plt.show()



