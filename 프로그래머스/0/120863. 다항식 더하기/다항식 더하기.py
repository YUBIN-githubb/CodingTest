def solution(polynomial):
    polynomial = polynomial.split(" + ")
    x = 0
    n = 0
    for p in polynomial:
        if "x" in p:
            if p == "x":
                x += 1
            else:
                x += int(str(p[:-1]))
        else:
            n += int(p)
    if x > 0 and n > 0:
        if x == 1:
            return f"x + {n}"
        else:
            return f"{x}x + {n}"
    elif x > 0 and n == 0:
        if x == 1:
            return "x"
        else:
            return f"{x}x"
    elif x == 0 and n > 0:
        return f"{n}"