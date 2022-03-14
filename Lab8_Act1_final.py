# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Mariana Sanchez
#               Aaron Garcia
#               Dhruv Manihar
#               Ethan Nguyen
# Section:      514
# Assignment:   Lab 8
# Date:         29 10 2021
#
# temp then v,u,h,s in that order
temp = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260]

volume = [0.0009977, 0.0009996, 0.0010057, 0.0010149, 0.0010267,
          0.0010410, 0.0010576, 0.0010769, 0.0010988, 0.0011240,
          0.0011531, 0.0011868, 0.0012268, 0.0012755]

internal_e = [0.04, 83.61, 166.92, 250.29, 333.82, 417.65,
              501.91, 586.80, 672.55, 759.47, 847.92, 938.39,
              1031.6, 1128.5]

enthalpy = [5.03, 88.61, 171.95, 255.36, 338.96, 422.85,
            507.19, 592.18, 678.04, 765.09, 853.68, 944.32,
            1037.7, 1134.9]

entropy = [0.0001, 0.2954, 0.5705, 0.8287, 1.0723, 1.3034, 1.5236,
           1.7344, 1.9374, 2.1338, 2.3251, 2.5127, 2.6983, 2.8841]

# inputs
user_temp = float(input("Enter a temperature between 0 and 260 deg C: "))
print("Properties at {} deg C are:".format(user_temp))

# conditions
for i in range(len(temp)):
    one = float(temp[i])
    two = float(temp[i + 1])
    if user_temp >= one and user_temp <= two:
        break

# volume (v)
vi = volume[i]
vf = volume[i + 1]
ti = one
tf = two
given_t = user_temp
v = ((vf - vi) / (tf - ti)) * (given_t - tf) + vf

# internal energy (u)
ei = internal_e[i]
ef = internal_e[i + 1]
ti = one
tf = two
given_t = user_temp
u = ((ef - ei) / (tf - ti)) * (given_t - tf) + ef

# enthalpy (h)
thi = enthalpy[i]
thf = enthalpy[i + 1]
ti = one
tf = two
given_t = user_temp
h = ((thf - thi) / (tf - ti)) * (given_t - tf) + thf

# entropy (s)
tri = entropy[i]
trf = entropy[i + 1]
ti = one
tf = two
given_t = user_temp
s = ((trf - tri) / (tf - ti)) * (given_t - tf) + trf

# print statements
print('Specific volume (m^3/kg): {:.7f}'.format(v))
print('Specific internal energy (kJ/kg): {:.2f}'.format(u))
print('Specific enthalpy (kJ/kg): {:.2f}'.format(h))
print('Specific entropy (kJ/kgK): {:.4f}'.format(s))
