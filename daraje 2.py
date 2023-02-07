import math
print("//The function of solving a quadratic equation//")
def raw ():
    a = float(input("Enter the amount of a:"))
    b = float(input("Enter the amount of b:"))
    c = float(input("Enter the amount of c:"))

    d = b ** 2 - 4 * a * c

    if d < 0:
        print("//There is no solution//")
    elif d == 0:
        x = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        print("There is a solution : ", x)
    else:
        x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        print("There are two solutions: " , x1, "and ", x2)
        
raw()