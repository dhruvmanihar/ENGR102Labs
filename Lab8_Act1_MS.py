# temp then v,u,h,s in that order
temp = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260]


enthalpy = [5.03, 88.61, 171.95, 255.36, 338.96, 422.85,
            507.19, 592.18, 678.04, 765.09, 853.68, 944.32,
            1037.7, 1134.9]



# inputs
user_temp = float(input("Enter a temperature between 0 and 260 deg C: "))
print("Properties at {} deg C are:".format(user_temp))

# conditions
for i in range(len(temp)):
    one = float(temp[i])
    two = float(temp[i + 1])
    if user_temp >= one and user_temp <= two:
        break

#enthalpy (h) (mariana)
thi= enthalpy[i]
thf= enthalpy[i+1]
ti= one
tf= two
given_t= user_temp
h = ((thf-thi)/(tf-ti))*(given_t-tf)+thf

