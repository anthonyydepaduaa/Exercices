b = int(input("Votos brancos :"))
n = int(input("Votos nulos :"))
v = int(input("Votos válidos :"))
t = b + n + v
print("Total de votos :", t)
print("Brancos", (b / t) * 100, "%")
print("Nulos", (n / t) * 100, "%")
print("Válidos", (v / t) * 100, "%")