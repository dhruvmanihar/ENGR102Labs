# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Mariana Sanchez
#               Aaron Garcia
#               Dhruv Manihar
#               Ethan Nguyen
# Section:      514
# Assignment:   Lab 5a_2
# Date:         10 2 2021
#

#all input variables
sex = input('Enter your sex (M/F): ')
age = int(input('Enter your age (years): '))
smoke = input('Do you smoke cigarettes (Y/N)? ')
cholesterol = int(input('Enter your total cholesterol (mg/dL): '))
hdl = int(input('Enter your HDL cholesterol (mg/dL): '))
bp = int(input('Enter your systolic BP (mmHg): '))
medication = input('Are you taking blood pressure medication (Y/N)? ')
points = 0
risk = ''

#if else blocks
if 20 <= age <= 79:
    if sex == 'M' or sex == 'm':  # if sex is male
        if age < 35:
            points -= 9
            if smoke == 'Y' or smoke == 'y':
                points += 8
            else:
                points += 0
            if cholesterol < 160:
                points += 0
            elif cholesterol < 200:
                points += 4
            elif cholesterol < 240:
                points += 7
            elif cholesterol < 280:
                points += 9
            else:
                points += 11
        elif age < 40:
            points -= 4
            if smoke == 'Y' or smoke == 'y':
                points += 8
            else:
                points += 0
            if cholesterol < 160:
                points += 0
            elif cholesterol < 200:
                points += 4
            elif cholesterol < 240:
                points += 7
            elif cholesterol < 280:
                points += 9
            else:
                points += 11
        elif age < 45:
            points += 0
            if smoke == 'Y' or smoke == 'y':
                points += 5
            else:
                points += 0
            if cholesterol < 160:
                points += 0
            elif cholesterol < 200:
                points += 3
            elif cholesterol < 240:
                points += 5
            elif cholesterol < 280:
                points += 6
            else:
                points += 8
        elif age < 50:
            points += 3
            if smoke == 'Y' or smoke == 'y':
                points += 5
            else:
                points += 0
            if cholesterol < 160:
                points += 0
            elif cholesterol < 200:
                points += 3
            elif cholesterol < 240:
                points += 5
            elif cholesterol < 280:
                points += 6
            else:
                points += 8
        elif age < 55:
            points += 6
            if smoke == 'Y' or smoke == 'y':
                points += 3
            else:
                points += 0
            if cholesterol < 160:
                points += 0
            elif cholesterol < 200:
                points += 2
            elif cholesterol < 240:
                points += 3
            elif cholesterol < 280:
                points += 4
            else:
                points += 5
        elif age < 60:
            points += 8
            if smoke == 'Y' or smoke == 'y':
                points += 3
            else:
                points += 0
            if cholesterol < 160:
                points += 0
            elif cholesterol < 200:
                points += 2
            elif cholesterol < 240:
                points += 3
            elif cholesterol < 280:
                points += 4
            else:
                points += 5
        elif age < 65:
            points += 10
            if smoke == 'Y' or smoke == 'y':
                points += 1
            else:
                points += 0
            if cholesterol < 160:
                points += 0
            elif cholesterol < 200:
                points += 1
            elif cholesterol < 240:
                points += 1
            elif cholesterol < 280:
                points += 2
            else:
                points += 3
        elif age < 70:
            points += 11
            if smoke == 'Y' or smoke == 'y':
                points += 1
            else:
                points += 0
            if cholesterol < 160:
                points += 0
            elif cholesterol < 200:
                points += 1
            elif cholesterol < 240:
                points += 1
            elif cholesterol < 280:
                points += 2
            else:
                points += 3
        elif age < 75:
            points += 12
            if smoke == 'Y' or smoke == 'y':
                points += 1
            else:
                points += 0
            if cholesterol < 160:
                points += 0
            elif cholesterol < 200:
                points += 0
            elif cholesterol < 240:
                points += 0
            elif cholesterol < 280:
                points += 1
            else:
                points += 1
        else:
            points += 13
            if smoke == 'Y' or smoke == 'y':
                points += 1
            else:
                points += 0
            if cholesterol < 160:
                points += 0
            elif cholesterol < 200:
                points += 0
            elif cholesterol < 240:
                points += 0
            elif cholesterol < 280:
                points += 1
            else:
                points += 1
        # HDL calculations
        if hdl < 40:
            points += 2
        elif hdl < 50:
            points += 1
        elif hdl < 60:
            points += 0
        else:
            points -= 1
        # Systolic BP Calculations
        if bp < 120:
            points += 0
        elif bp < 130:
            if medication == 'Y' or medication == 'y':
                points += 1
            else:
                points += 0
        elif bp < 140:
            if medication == 'Y' or medication == 'y':
                points += 2
            else:
                points += 1
        elif bp < 160:
            if medication == 'Y' or medication == 'y':
                points += 2
            else:
                points += 1
        else:
            if medication == 'Y' or medication == 'y':
                points += 3
            else:
                points += 2
        # risk calculation
        if points < 0:
            risk = "<1%"
        elif points < 5:
            risk = "1%"
        elif points < 7:
            risk = "2%"
        elif points == 7:
            risk = "3%"
        elif points == 8:
            risk = "4%"
        elif points == 9:
            risk = "5%"
        elif points == 10:
            risk = "6%"
        elif points == 11:
            risk = "8%"
        elif points == 12:
            risk = "10%"
        elif points == 13:
            risk = "12%"
        elif points == 14:
            risk = "16%"
        elif points == 15:
            risk = "20%"
        elif points == 16:
            risk = "25%"
        else:
            risk = ">30%"
    else:  # If sex is female
        if age < 35:
            points += -7
            if smoke == 'Y' or smoke == 'y':
                points += 9
            if cholesterol < 160:
                points += 0
            elif cholesterol < 200:
                points += 4
            elif cholesterol < 240:
                points += 8
            elif cholesterol < 280:
                points += 11
            else:
                points += 13
        elif age < 40:
            points += -3
            if smoke == 'Y' or smoke == 'y':
                points += 9
            if cholesterol < 160:
                points += 0
            elif cholesterol < 200:
                points += 4
            elif cholesterol < 240:
                points += 8
            elif cholesterol < 280:
                points += 11
            else:
                points += 13
        elif age < 45:
            points += 0
            if smoke == 'Y' or smoke == 'y':
                points += 7
            if cholesterol < 160:
                points += 0
            elif cholesterol < 200:
                points += 3
            elif cholesterol < 240:
                points += 6
            elif cholesterol < 280:
                points += 8
            else:
                points += 10
        elif age < 50:
            points += 3
            if smoke == 'Y' or smoke == 'y':
                points += 7
            if cholesterol < 160:
                points += 0
            elif cholesterol < 200:
                points += 3
            elif cholesterol < 240:
                points += 6
            elif cholesterol < 280:
                points += 8
            else:
                points += 10
        elif age < 55:
            points += 6
            if smoke == 'Y' or smoke == 'y':
                points += 4
            if cholesterol < 160:
                points += 0
            elif cholesterol < 200:
                points += 2
            elif cholesterol < 240:
                points += 4
            elif cholesterol < 280:
                points += 5
            else:
                points += 7
        elif age < 60:
            points += 8
            if smoke == 'Y' or smoke == 'y':
                points += 4
            if cholesterol < 160:
                points += 0
            elif cholesterol < 200:
                points += 2
            elif cholesterol < 240:
                points += 4
            elif cholesterol < 280:
                points += 5
            else:
                points += 7
        elif age < 65:
            points += 10
            if smoke == 'Y' or smoke == 'y':
                points += 2
            if cholesterol < 160:
                points += 0
            elif cholesterol < 200:
                points += 1
            elif cholesterol < 240:
                points += 2
            elif cholesterol < 280:
                points += 3
            else:
                points += 4
        elif age < 70:
            points += 12
            if smoke == 'Y' or smoke == 'y':
                points += 2
            if cholesterol < 160:
                points += 0
            elif cholesterol < 200:
                points += 1
            elif cholesterol < 240:
                points += 2
            elif cholesterol < 280:
                points += 3
            else:
                points += 4
        elif age < 75:
            points += 14
            if smoke == 'Y' or smoke == 'y':
                points += 1
            if cholesterol < 160:
                points += 0
            elif cholesterol < 240:
                points += 1
            else:
                points += 2
        else:
            points += 16
            if smoke == 'Y' or smoke == 'y':
                points += 1
            if cholesterol < 160:
                points += 0
            elif cholesterol < 240:
                points += 1
            else:
                points += 2
        # HDL calculations
        if hdl < 40:
            points += 2
        elif hdl < 50:
            points += 1
        elif hdl < 60:
            points += 0
        else:
            points -= 1
        # Systolic BP Calculations
        if bp < 120:
            points += 0
        elif bp < 130:
            if medication == 'Y' or medication == 'y':
                points += 3
            else:
                points += 1
        elif bp < 140:
            if medication == 'Y' or medication == 'y':
                points += 4
            else:
                points += 2
        elif bp < 160:
            if medication == 'Y' or medication == 'y':
                points += 5
            else:
                points += 3
        else:
            if medication == 'Y' or medication == 'y':
                points += 6
            else:
                points += 4
        # risk calculation
        if points < 9:
            risk = "<1%"
        elif points < 13:
            risk = "1%"
        elif points < 15:
            risk = "2%"
        elif points == 15:
            risk = "3%"
        elif points == 16:
            risk = "4%"
        elif points == 17:
            risk = "5%"
        elif points == 18:
            risk = "6%"
        elif points == 19:
            risk = "8%"
        elif points == 20:
            risk = "11%"
        elif points == 21:
            risk = "14%"
        elif points == 22:
            risk = "17%"
        elif points == 23:
            risk = "22%"
        elif points == 24:
            risk = "27%"
        else:
            risk = ">30%"
    print('Your 10-year risk of a heart attack is', risk)
else:
    # not in range
    print('Invalid age entered')

