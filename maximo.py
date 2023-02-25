print('Iniciado el orden .....')
# 1 Llenar el arreglo
lista1 = [2, 6, 7, 10, 1, 4, 13]
lista2 = [21, 6, 7, 10, 1, 4, 0]
lista3 = [2, 6, 7, 110, 1, 4, -1]
lista4 = [2, 61, 7, 10, 1, 4, 3]
print('El largo de la lista es: ' + str(len(lista1)))

# 2 hacer el ciclo de recorrido del arreglo
# mayor = 0
# for item in mi_lista:
#    print(item) 
#    if mayor <= item:
#       mayor = item
# # 3 imprimr el mayor
# print('El mayo es:' + str(mayor))


def elmayor(mi_lista):
    mayor = 0
    for item in mi_lista:
        if mayor <= item:
            mayor = item
    return mayor

print('El mayor es:')
print(elmayor(lista1))
print(elmayor(lista2))
print(elmayor(lista3))
print(elmayor(lista4))
