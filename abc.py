import math, sys

def abc(a,b,c):
    """Simple abc formula for quadratic equations
    """
    d = b - 4*a*c
    if d > 0:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        return x1, x2
    elif d == 0:
        x = (-b)/(2*a)
    else:
        raise ValueError("Discriminant is smaller than 0, specifically: ",d)

if __name__ == '__main__':
    a,b,c = map(float, sys.argv[1:])
    print abc(a,b,c)
