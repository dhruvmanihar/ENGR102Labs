# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 2b_Act1
# Date: 09/13/2021

from math import *

#A: Calculate the force in Newtons applied to an object with mass 2 kg and acceleration 5 m/s^2

object_mass = 2
object_acceleration = 5
object_force = object_mass*object_acceleration
print("Force is", object_force , "N")

#B: Calculate the wavelength of x-rays scattering from a crystal lattice with a distance between
#crystal layers of 0.025 nm, scattering angle of 25 degrees, and first order diffraction

angle = radians(25)
distance = .025
wavelength = 2*distance*sin(angle)
print("Wavelength is", wavelength, "nm")

#C: Calculate how much Radon-222 is left after 5 days of radioactive decay given an initial
# amount of 3 g and a half-life of 3.8 days.

initialAmount = 3
time = 5
halfLife = 3.8
elementLeft = initialAmount*(2**(-time/halfLife))
print("Radon-222 left is", elementLeft, "g")

#D: Calculate the pressure of 5 moles of an ideal gas with a volume of 0.15 m^3, and temperature of 425 K.

moles = 5
temp = 425
gas_constant = 8.314
volume = 150
pressure = (moles*temp*gas_constant)/volume
print("Pressure is", pressure, "kPa")