# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Mariana Sanchez
#               Aaron Garcia
#               Dhruv Manihar
#               Ethan Nguyen
# Section:      514
# Assignment:   Lab 9a_1b
# Date:         11 8 2021
#


outfile = "Lab9a_Act1b_valid.txt"
passports = []
validPassports = []

# Open the input file and format the data into lists
with open("Lab9a_input.txt") as inputFile:
    current = []
    line = inputFile.readline().strip()
    while line != "":
        current += [line]
        line = inputFile.readline().strip()
        if (line == ""):
            passports += [current]
            current = []
            line = inputFile.readline().strip()

# Check for valid passports
for i in passports:
    # Declare variable to use to check if passport is valid
    values = []
    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False

    # Break inputs into individual values
    for line in i:
        values += line.split(" ")

    # Check that all neccesary values are there
    # values are formatted "xxx:yyyyy" where x is the value name and y is the value
    for v in values:
        if v[0:3] == 'byr':
            year = int(v[4:])
            if year >= 1920 and year <= 2005 and len(v[4:]) == 4:
                byr = True
        elif v[0:3] == 'iyr':
            year = int(v[4:])
            if year >= 2011 and year <= 2021 and len(v[4:]) == 4:
                iyr = True
        elif v[0:3] == 'eyr':
            year = int(v[4:])
            if year >= 2021 and year <= 2031 and len(v[4:]) == 4:
                eyr = True
        elif v[0:3] == 'hgt':
            try:
                num = int(v[4:-2])
                unit = v[-2:]
                if unit == "in" and (num >= 59 and num <= 76):
                    hgt = True
                elif unit == "cm" and (num >= 150 and num <= 193):
                    hgt = True
                else:
                    pass
            except:
                pass
        elif v[0:3] == 'ecl':
            if (len(v[4:]) == 3) and (
                    str(v[4:]) == 'amb' or str(v[4:]) == 'blu' or str(v[4:]) == 'brn' or str(v[4:]) == 'gry' or str(
                    v[4:]) == 'grn' or str(v[4:]) == 'hzl' or str(v[4:]) == 'oth'):
                ecl = True
        elif v[0:3] == 'hcl':
            if v[4] == "#" and len(v[5:]) == 6:
                valid = True
                for x in range(6):
                    c = str(v[5 + x]).casefold()
                    try:
                        int(c)
                    except:
                        if not (c == "a" or c == "b" or c == "c" or c == "d" or c == "e" or c == "f"):
                            valid = False
                if valid:
                    hcl = True
        elif v[0:3] == 'pid':
            if (len(v[4:]) == 9):
                try:
                    x = int(v[4:])
                    pid = True
                except:
                    pass

    # If the passport is valid, add it to valid passports
    if (byr and iyr and eyr and hgt and hcl and ecl and pid):
        validPassports += [i]

# Print console output
print(f"There are {len(validPassports)} valid passports")

with open(outfile, 'w') as output:
    for i in validPassports:
        for line in i:
            output.write(line + "\n")
        output.write("\n")
