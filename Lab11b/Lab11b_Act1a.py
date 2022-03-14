# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dhruv Manihar
# Section: 514
# Assignment: 11b_Act1a
# Date: 11/27/2021


from math import * # value of PI
def parta(boxLength,boxWidth,boxHeight,holeRadius):
    area = boxLength * boxWidth * boxHeight # calculate area
    hole = (pi * holeRadius ** 2) * boxHeight # volume of cylinder
    if holeRadius * 2 < 1 and holeRadius < boxWidth:
        vleft = area - hole
        return vleft
    elif holeRadius >= sqrt((1/2) ** 2 + (boxWidth/2)**2):
        return 0
    else:
        boxWidthSegment = holeRadius - boxWidth/2
        boxLengthSegment = holeRadius - 1/2
        WidthPiece = holeRadius ** 2 * acos(1-(boxWidthSegment/holeRadius))-(holeRadius-boxWidthSegment) * sqrt(holeRadius ** 2 -(holeRadius-boxWidthSegment) ** 2)
        LengthPiece = holeRadius ** 2 * acos(1-(boxLengthSegment/holeRadius))-(holeRadius-boxLengthSegment) * sqrt(holeRadius ** 2 -(holeRadius-boxLengthSegment) ** 2)
        actual = ((pi * holeRadius ** 2) - (2 * LengthPiece + 2 * WidthPiece)) * boxHeight
        vleft = area - actual
        return vleft


