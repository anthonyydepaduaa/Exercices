h1 = int(input("Hora de início :"))
h2 = int(input("Hora de termino :"))
if h1 > h2:
    h2 = h2 + 24
d = h2 - h1
print("Duração :", d, "horas")