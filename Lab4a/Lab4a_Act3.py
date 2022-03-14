# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Mariana Sanchez
#               Aaron Garcia
#               Dhruv Manihar
#               Ethan Nguyen
# Section:      514
# Assignment:   Lab 4a_3
# Date:         09 24 2021
#

########### Part A ###########

a_string = input("Enter True or False for a: ") 
b_string = input("Enter True or False for b: ") 
c_string = input("Enter True or False for c: ")  
a = a_string == 'True' or a_string == 'T' or a_string == 't' 
b = b_string == 'True' or b_string == 'T' or b_string == 't' 
c = c_string == 'True' or c_string == 'T' or c_string == 't' 
########### Part B ########### 

print('a and b and c:', a and b and c)
print('a or b or c:', a or b or c) 

########### Part C ########### 

print('XOR:',a ^ b) 
print('Odd number:',a ^ b ^ c)

########### Part D ########### 

print('Complex 1:', (not(a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)) 
print('Complex 2:', (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b)))))
print('Simple 1:',(not (b and (a or c)))) 
print('Simple 2:',(a or (not b and c))) 
