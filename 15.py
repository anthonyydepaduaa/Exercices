n1 = float(input("Número 1 :"))
n2 = float(input("Número 2 :"))
while n2 == n1:
    print("Números iguais")
    n2 = float(input("Número 2 :"))
if n1 > n2:
    print(n1, n2)
else:
    print(n2, n1)