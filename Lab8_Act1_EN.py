# temp then v,u,h,s in that order
temp = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260]


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


#entropy (s) (ethan)
tri= entropy[i]
trf= entropy[i+1]
ti= one
tf= two
given_t= user_temp
s = ((trf-tri)/(tf-ti))*(given_t-tf)+trf
