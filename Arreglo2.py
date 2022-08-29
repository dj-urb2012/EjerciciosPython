lista_est = []

res = "Si"

while res.upper() != "NO":
    size = len(lista_est)
    print("Elementos guardados:", size)
    nombres = input("Escriba el nombre del estudiante: ")
    lista_est.append(nombres)
    res =input("Desea agregar otro? ")

for estudiante in lista_est:
    print(estudiante)