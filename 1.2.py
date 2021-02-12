import math

x = 100

if x < 97:
    result = 53 * ((math.log(x) + 77 * x ** 3) ** 2) - 13 * x ** 6
elif 97 <= x < 144:
    result = 53 * x ** 2 + math.fabs(x) + 50
elif x >= 144:
    result = math.exp(91 * x + x ** 4) - x ** 2

print(f"{result:.2e}")