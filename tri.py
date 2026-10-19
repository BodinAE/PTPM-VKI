import re


def triForDraw(astr, bstr, cstr):
    inputs = [astr, bstr, cstr]
    pattern = re.compile(r'^[1-9](?:\.\d)?$')
    validInput = True
    for str in inputs:
        validInput *= bool(re.match(pattern, str))
    if validInput:
        a = float(astr)
        b = float(bstr)
        c = float(cstr)
        isTri = a < b + c
        isTri *= b < a + c
        isTri *= c < a + b
    else:
        return "не треугольник", [(-2, -2), (-2, -2), (-2, -2)]
    return "aaa"

print(triForDraw("1","1","3"))