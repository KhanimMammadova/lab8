def f(x):
    return x**5 - x - 2

a = 1.0
b = 1.4
epsilon = 10**(-2)

while (b - a) / 2 > epsilon:
    orta = (a + b) / 2
    if f(orta) == 0:
        break
    if f(a) * f(orta) < 0:
        b = orta
    else:
        a = orta

kök = (a + b) / 2
print("Təqribi kök:", kök)
