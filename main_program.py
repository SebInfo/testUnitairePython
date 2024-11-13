# main_program.py
import math

from math_functions import addition, racice_carre, cosinus, sinus


def main():
    a, b = 5, 3
    print(f"Addition de {a} et {b} : {addition(a, b)}")

    x = 16
    print(f"Racine carrée de {x} : {racice_carre(x)}")

    angle = math.pi / 4  # 45 degrés
    print(f"Cosinus de {angle} : {cosinus(angle)}")
    print(f"Sine de {angle} : {sinus(angle)}")


if __name__ == '__main__':
    main()
