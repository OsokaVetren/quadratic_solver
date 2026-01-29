import math

def solve_quadratic(a : float,b : float, c: float):
    if a==0:
        if not b == 0: return [-c/b]
    
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []
    if discriminant == 0:
        return [-b/(2*a)]
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return sorted([root1, root2])