n1 = float(input("Número 1 :"))
n2 = float(input("Número 2 :"))
n3 = float(input("Número 3 :"))
if n1 > n2:
    if n1 > n3:
        print(n1, "é o maior")
    else:
        print(n3, "é o maior")
else:
    if n2 > n3:
        print(n2, "é o maior")
    else:
        print(n3, "é o maior")