import math

def a(n):
    if n == 0:
        return 8
    else:
        return (math.cos(a(n-1)) + math.sin(a(n-1)))
print(f"{a(10):.2e}")