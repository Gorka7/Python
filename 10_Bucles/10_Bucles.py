#Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=23822

### Loops ###


#While
print("----------------------------------------------------------")
print("-                         While                          -")
print("-                                                        -")
print("-    my_condition = 0                                    -")
print("-                                                        -")
print("-    while my_condition < 10:                            -")
print("-        print(my_condition)                             -")
print("-        my_condition += 2                               -")
print("-    else:                                               -")
print("-        print('Mi condición es mayor o igual que 10')   -")
print("-                                                        -")
print("-    print('La ejecución continúa')                      -")
print("----------------------------------------------------------")


my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:  # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

#While2
print("----------------------------------------------------------")
print("-                        While 2                         -")
print("-                                                        -")
print("-    while my_condition < 20:                            -")
print("-        my_condition += 1                               -")
print("-        if my_condition == 15:                          -")
print("-        print('Se detiene la ejecución')                -")
print("-           break                                        -")
print("-        print(my_condition)                             -")
print("-                                                        -")
print("-    print('La ejecución continúa')                      -")
print("----------------------------------------------------------")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

print("La ejecución continúa")

#ForConListas
print("----------------------------------------------------------")
print("-                  For  (Con Listas)                     -")
print("-                                                        -")
print("-    my_list = [35, 24, 62, 52, 30, 30, 17]              -")
print("-                                                        -")
print("-    for elemento in my_list:                            -")
print("-        print(elemento)                                 -")
print("-                                                        -")
print("----------------------------------------------------------")

my_list = [35, 24, 62, 52, 30, 30, 17]

for elemento in my_list:
    print(elemento)

#ForConTuplas
print("----------------------------------------------------------")
print("-                  For 2 (Con Tuplas)                    -")
print("-                                                        -")
print("-    my_tuple = (35, 1.77, 'Brais', 'Moure', 'Brais')    -")
print("-                                                        -")
print("-    for elemento in my_tuple:                           -")
print("-        print(elemento)                                 -")
print("-                                                        -")
print("----------------------------------------------------------")


my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

for element in my_tuple:
    print(element)

#ForConSets
print("----------------------------------------------------------")
print("-                  For 3 (Con Sets)                      -")
print("-                                                        -")
print("-    my_set = {'Brais', 'Moure', 35}                     -")
print("-                                                        -")
print("-    for elemento in my_set:                             -")
print("-        print(elemento)                                 -")
print("-                                                        -")
print("----------------------------------------------------------")

my_set = {"Brais", "Moure", 35}

for element in my_set:
    print(element)


print("------------------------------------------------------------------------------------------------------")
print("-                  For 4 (Con Diccionarios)                                                          -")
print("-                                                                                                    -")
print("-    my_dict = {'Nombre': 'Brais', 'Apellido': 'Moure', 'Edad': 35, 1: 'Python'}                     -")
print("-                                                                                                    -")
print("-    for elemento in my_dict:                                                                        -")
print("-        print(elemento)                                                                             -")
print("-        if element == 'Edad':                                                                       -")
print("-        break                                                                                       -")
print("-     else:                                                                                          -")
print("-        print('El bucle for para el diccionario ha finalizado')                                     -")
print("-                                                                                                    -")
print("-     print('La ejecución continúa')                                                                 -")
print("-                                                                                                    -")
print("------------------------------------------------------------------------------------------------------")

my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bucle for para el diccionario ha finalizado")

print("La ejecución continúa")

#
"""for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado")
"""