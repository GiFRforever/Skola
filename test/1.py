import math


def find_roots(a, b, c) -> tuple:
    """Find roots of quadratic equation"""
    if a == 0:
        if b == 0:
            if c == 0:
                return (0, 0)
            else:
                return (0, 0)
        else:
            if c == 0:
                return (0, 0)
            else:
                return -c / b
    d: float = b * b - 4 * a * c
    if d < 0:
        return (0, 0)
    discRoot: float = math.sqrt(d)
    root1: float = (-b + discRoot) / (2 * a)
    if d == 0:
        return (root1, root1)
    root2: float = (-b - discRoot) / (2 * a)
    return (root1, root2)
