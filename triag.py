import math
import re


#CHANGE INPUTS!!!!

def checkSides (a, b, c):
    isTri = a < b + c
    isTri *= b < a + c
    isTri *= c < a + b
    return isTri

def trigInput (inpt):
    if re.match(r'[1-9][,.]?\d?', inpt):
        return inpt.replace(',', '.')
    return "a"

lengthArr = [0.0, 0.0, 0.0]
coordArr = [(-1, -1), (-1, -1), (-1, -1)]
triType = 0
lengthArr[0] = float(input("A length: "))
lengthArr[1] = float(input("B length: "))
lengthArr[2] = float(input("C length: "))
print(lengthArr)
if checkSides(lengthArr[0], lengthArr[1], lengthArr[2]):
    triType += 1
    triType += lengthArr[0] == lengthArr[1]
    triType += lengthArr[2] == lengthArr[1]
    triType += lengthArr[2] == lengthArr[0]
match triType:
    case 0:
        print("не треугольник")
    case 1:
        print("разносторонний")
    case 2:
        print("равнобедренный")
    case 4:
        print("равносторонний")
if triType:
    coordArr[0] = (0, 0)
    coordArr[1] = (int(lengthArr[2]), 0)
    cx = int(((lengthArr[1] ** 2) + (lengthArr[2] ** 2) - (lengthArr[0] ** 2))/(2 * lengthArr[2]))
    cy = int(math.sqrt((lengthArr[1] ** 2) - (cx ** 2)))
    coordArr[2] = (cx, cy)
print(coordArr)