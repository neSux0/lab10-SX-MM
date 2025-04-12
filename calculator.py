#https://github.com/neSux0/lab10-SX-MM/tree/main
#Partner 1: Marina Ma (moonmara)
#Partner 2: Sen Xu (neSux0)

import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take square root of negative number")
        return math.sqrt(a)
    except ValueError as error:
        print("Value Error:", str(error)) #revised
        raise ValueError #needs to be raised again if we are using the try/execpt
def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a+b

def sub(a, b):
    return  a-b

def mul(a, b):
    return a*b

def div(a,b):
    if b == 0:
        raise ValueError("ZeroDivisionError")
    else:
        return a/b

def log(a, b):
    if a <= 0 or b <= 1:
        raise ValueError("Domain Error")
    else:
        return math.log(b,a)

def exp(a, b):
    return math.pow(a,b)


