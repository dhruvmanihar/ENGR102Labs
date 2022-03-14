# temp then v,u,h,s in that order
temp = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260]

volume = [0.0009977, 0.0009996, 0.0010057, 0.0010149, 0.0010267,
          0.0010410, 0.0010576, 0.0010769, 0.0010988, 0.0011240,
          0.0011531, 0.0011868, 0.0012268, 0.0012755]



# inputs
user_temp = float(input("Enter a temperature between 0 and 260 deg C: "))
print("Properties at {} deg C are:".format(user_temp))

# conditions
for i in range(len(temp)):
    one = float(temp[i])
    two = float(temp[i + 1])
    if user_temp >= one and user_temp <= two:
        break

#volume (v) (aaron)
vi= volume[i]
vf= volume[i+1]
ti= one
tf= two
given_t= user_temp
v = ((vf-vi)/(tf-ti))*(given_t-tf)+vf


