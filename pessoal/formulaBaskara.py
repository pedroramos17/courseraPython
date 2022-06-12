a = float(input("Digite o valor de a por favor: "))
b = float(input("Digite o valor de b por favor: "))
c = float(input("Digite o valor de c por favor: "))

delta = b ** 2 - 4 * a * c
x1 = ((- b + (delta ** 0.5)) / (2 * a))
x2 = ((- b - (delta ** 0.5)) / (2 * a))

print("O resultado da fórmula de baskara de x1 é:", x1, "e de x2 é:", x2)
