# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    d = b ** 2 - 4 * a * c

    if d > 0:
        r1 = (-b + d ** 0.5) / (2 * a)
        r2 = (-b - d ** 0.5) / (2 * a)
        return f"({r1}, {r2})"
    elif d == 0:
        r = -b / (2 * a)
        return f"({r})"
    else:
        return "( )"


def value_y(a, b, c, x):

    return a * x ** 2 + b * x + c


def to_string(a, b, c):
    return f"f(x) = {a} * x^2 + {b} * x + {c}"


def derivation(a, b, c):
    return f"f'(x) = {2 * a}x + {b}"
