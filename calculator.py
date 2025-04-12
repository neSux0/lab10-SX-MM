"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except ValueError as error:
        print("Cannot take square root of negative number", str(error))

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


