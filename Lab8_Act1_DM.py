# temp then v,u,h,s in that order
temp = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260]


internal_e = [0.04, 83.61, 166.92, 250.29, 333.82, 417.65,
              501.91, 586.80, 672.55, 759.47, 847.92, 938.39,
              1031.6, 1128.5]


# inputs
user_temp = float(input("Enter a temperature between 0 and 260 deg C: "))
print("Properties at {} deg C are:".format(user_temp))

# conditions
for i in range(len(temp)):
    one = float(temp[i])
    two = float(temp[i + 1])
    if user_temp >= one and user_temp <= two:
        break

#internal energy calculations

ei= internal_e[i]
ef= internal_e[i+1]
ti= one
tf= two
given_t= user_temp
u = ((ef-ei)/(tf-ti))*(given_t-tf)+ef
