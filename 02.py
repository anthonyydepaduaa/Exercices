n = int(input("Número :"))
while n == 0:
    print("Inválido")
    n = int(input("Número :"))
if n > 0:
    print(n, "é positivo")
else:
    print(n, "é negativo")