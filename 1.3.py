import math

def dada(n,m):
    a = 0
    b = 0

    for i in range (1, n+1):
        for j in range (1, m+1):
            a = a + ((59 * i ** 5) - (j ** 7))

    for i in range (1, n+1):
        b = b + ((i ** 5 / 30) - math.sin(i))

    result = a + 92 * b
    return result

print(f"{dada(49,52):.2e}")
