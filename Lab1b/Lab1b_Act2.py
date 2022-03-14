# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 1b_Act1
# Date: 09/08/2021

from math import *

#A: Calculate the force in Newtons applied to an object with mass 2 kg and acceleration 5 m/s^2

print("Force is", 2*5, "N")

#B: Calculate the wavelength of x-rays scattering from a crystal lattice with a distance between
#crystal layers of 0.025 nm, scattering angle of 25 degrees, and first order diffraction

print("Wavelength is", 2*.025*sin(radians(25)), "nm")

#C: Calculate how much Radon-222 is left after 5 days of radioactive decay given an initial
# amount of 3 g and a half-life of 3.8 days.

print("Radon-222 left is", 3*(2**(-5/3.8)), "g")

#D: Calculate the pressure of 5 moles of an ideal gas with a volume of 0.15 m^3, and temperature of 425 K.

print("Pressure is", (5*425*8.314)/(150), "kPa")

