# math_functions.py
import math

def addition(a, b):
    return a + b

def racine_carre(x):
    return math.sqrt(x)

def log(value):
    if value <= 0:
        return None
    return math.log(value)

def cosinus(x):
    return math.cos(x)

def sinus(x):
    return math.sin(x)

def est_paire(n):
    return n % 2 == 0
