"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math


def add(a, b):
    return a + b #modification. removed paranthesis.

def subtract(a, b):
    return  a -b
def multiply(a, b):
    return a * b

def divide(a, b):
    # raise ZeroDivisionError if a == 0
    if a == 0:
        raise ValueError("Zero-Division Error")
    else:
        return b / a

def logarithm(a, b):
    if a <= 0 or b <= 1:
        raise ValueError("Domain Error")
    else:
        math.log(b,a)

def exponent(a, b):
    return math.pow(a,b)


