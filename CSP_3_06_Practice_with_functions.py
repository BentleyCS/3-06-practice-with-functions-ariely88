#Herons Formula
import math

#returns the square root of the number n
def root(n):
    return math.sqrt(n)

#Takes in the 3 side lengths of a triangle as arguments and returns half of
#the perimeter of a triangle.
def semiPerimeter(length1, length2, length3):
    y = length1 + length2 + length3
    return y/2
    pass

#Modify the below function such that it takes in 4 arguments. multiply the first
#argument by the difference between itself and each individual argument.
# Reference herons formula for more context.
def multiplyDifferences(s, a, b, c):
    her = (s * (s - a) * (s - b) * (s - c))
    return her
    pass

#Given the 3 sides of a triangle return the area.
#use herons formula
#Use the functions above.
def herons(a, b, c):
    s = semiPerimeter(a, b, c)
    h = multiplyDifferences(s, a, b, c)
    x = root(h)
    return x
    pass


#quadratic equation

#takes in a number as an argument and returns that number multiplied by 2.
def denominator(x):
    x = x*2
    return x
    pass

#Takes in two arguments. multiply the first argument by negative 1. Then
#return the modified first argument added and subtracted by the second argument.
def plusMinus(x ,y):
    x = x*-1
    d1 = x-y
    d2 = x+y
    return d1, d2
    pass
#takes in three numbers as arguments. The first and third multiplied together then
#multiplied by 4.Then subtract that result from the second argument squared.
#Return the overall result.
def mainCalc(a, b, c):
    b = b*b
    d = a*c*4
    x = b-d
    return x
    pass

#The below function should take the inputs of the quadratic equation and return the result
#Make sure to use all the formulas from this section.
def quadratic(a, b, c):
     d = mainCalc(a,b,c)
     gf, fg = plusMinus(b, d)
     ab = gf/denominator(a)
     ba = fg/denominator(a)
     return ab, ba
     pass
