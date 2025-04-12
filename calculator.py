"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math


def add(a, b):
    return a+b  #modification. added paranthesis.

def sub(a, b):
    return  a-b

def mul(a, b):
    return a*b

def div(a, b):
    # raise ZeroDivisionError if a == 0
    if a == 0:
        raise ValueError("Zero-Division Error")
    else:
        return b/a

def log(a, b):
    if a <= 0 or b <= 1:
        raise ValueError("Domain Error")
    else:
        math.log(b,a)

def exp(a, b):
    return math.pow(a,b)


