# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cmath
def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root,
    else:
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        return root1, root2
a = float(input("："))
b = float(input("："))
c = float(input("："))
roots = solve_quadratic_equation(a, b, c)
print(":", roots)
