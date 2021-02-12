import math

x = 63
y = 67

a = 73 * y ** 4
b = y ** 7
c = (86 * y ** 4 + (x ** 7 / 76))
d = ((math.log(y) + math.sin(x) - 73) / (math.sin(y) - math.tan(y)))
result = a - b - c - math.sqrt(d)
print(f"{result:.2e}")