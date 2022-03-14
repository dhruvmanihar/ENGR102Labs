# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Mariana Sanchez
#               Aaron Garcia
#               Dhruv Manihar
#               Ethan Nguyen
# Section:      514
# Assignment:   Lab 11a_1
# Date:         11 21 2021
#


def readfile(saussage):
    global Ilovecats
    Ilovecats = []
    with open(str(saussage), 'r') as files:
        reading = files.readlines()
        for i in range(len(reading)-1):
            splitread = reading[i+1].strip('\n')
            splitread = splitread.split(',')
            splitread = [int(splitread[0]), int(splitread[1])]
            Ilovecats += [splitread]



    return Ilovecats # first function will return ilovecats

#second function
def cross(soy_sayse, y):
    global crossp
    crossp = (float(soy_sayse[0]) * float(y[1])) - (float(soy_sayse[1]) * float(y[0]))
    return crossp

def shoelace(soy_sayse): #3rd function
    global itsactuallynotthathard
    itsactuallynotthathard = 0
    soy_sayse += [soy_sayse[0]]
    for u in range(len(soy_sayse)-1):
        global c
        global v
        c = soy_sayse[u]
        v = soy_sayse[u+1]
        cross(c, v)

        itsactuallynotthathard += crossp
    itsactuallynotthathard /= 2
    return itsactuallynotthathard





def main():


    global saussage
    saussage = input('Please enter the filename: ')
    readfile(saussage)
    shoelace(Ilovecats)
    print('The area of the polygon is', itsactuallynotthathard)

if __name__ == '__main__':
    main()
