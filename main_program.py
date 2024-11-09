# main_program.py
import math

from math_functions import addition, square_root, cosine, sine


def main():
    a, b = 5, 3
    print(f"Addition de {a} et {b} : {addition(a, b)}")

    x = 16
    print(f"Racine carrée de {x} : {square_root(x)}")

    angle = math.pi / 4  # 45 degrés
    print(f"Cosinus de {angle} : {cosine(angle)}")
    print(f"Sine de {angle} : {sine(angle)}")


if __name__ == '__main__':
    main()
