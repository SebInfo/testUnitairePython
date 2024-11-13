# math_functions.py
import math

def addition(a, b):
    return a + b

def racice_carre(x):
    if x < 0:
        raise ValueError("Le nombre doit être positif ou égal à 0")
    return math.sqrt(x)

def cosinus(x):
    return math.cos(x)

def sinus(x):
    return math.sin(x)
