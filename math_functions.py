# math_functions.py
import math

def addition(a, b):
    return a + b

def square_root(x):
    if x < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(x)

def cosine(x):
    return math.cos(x)

def sine(x):
    return math.sin(x)
