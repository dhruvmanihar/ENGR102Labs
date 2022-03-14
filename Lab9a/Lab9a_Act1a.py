# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Mariana Sanchez
#               Aaron Garcia
#               Dhruv Manihar
#               Ethan Nguyen
# Section:      514
# Assignment:   Lab 9a_1a
# Date:         11 8 2021
#


# opening files to read it
passport_files = open("Lab9a_input.txt", "r")

pass_read = passport_files.read()

pass_split = pass_read.split("\n\n")
# opening files to write
valid_pass = 0
new_file = open("Lab9a_Act1a_vaild.txt", "w")
# checking if it's valid
passport_files.close()
for i in pass_split:
    if "byr" in i:
        if "iyr" in i:
            if "eyr" in i:
                if "hgt" in i:
                    if "hcl" in i:
                        if "ecl" in i:
                            if "pid" in i:
                                valid_pass += 1
                                new_file.write(i)
                                new_file.write("\n")

print("There are", valid_pass ,"valid passports")

new_file.close()

