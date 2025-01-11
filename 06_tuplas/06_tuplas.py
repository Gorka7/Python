# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=14711

### Tuples ###

# Definición

print("----------------------------")
print('- Formas de Definir TUPLAS -')
print("----------------------------")
print('-    my_tuple = tuple()    -')
print('-    my_other_tuple = ()   -')
print("----------------------------")
print("                            ")
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_other_tuple = (35, 60, 30)

print("---------------------")
print("- Datos de my_tuple -")
print("---------------------")

print(my_tuple)

print("                     ")
print("---------------------")
print("-   Tipo de Dato    -")
print("---------------------")
print(type(my_tuple))

# Acceso a elementos y búsqueda
print("                                                 ")
print("-------------------------------------------------")
print("-   Acceso a elemento 0 | print(my_tuple[0])    -")
print("-------------------------------------------------")

print(my_tuple[0])

print("                                                 ")
print("-------------------------------------------------")
print("-   Acceso a elemento -1 | print(my_tuple[-1])  -")
print("-------------------------------------------------")
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print("                                                                           ")
print("---------------------------------------------------------------------------")
print("-   Contabilizar un elemento dela TUPLA | print(my_tuple.count('Brais'))  -")
print("---------------------------------------------------------------------------")
print(my_tuple.count("Brais"))

print("                                                                                ")
print("--------------------------------------------------------------------------------")
print("-      Acceso a un elemento del Indice | print(my_tuple.index('Moure'))        -")
print("--------------------------------------------------------------------------------")
print(my_tuple.index("Moure"))

print("                                                 ")
print("-------------------------------------------------")
print("-   Acceso a elemento -1 | print(my_tuple[-1])  -")
print("-------------------------------------------------")
print(my_tuple.index("Brais"))

# my_tuple[1] = 1.80 'tuple' object does not support item assignment

# Concatenación
print("                                                 ")
print("-------------------------------------------------")
print("-          Concatenación de TUPLAS              -")
print("-------------------------------------------------")
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# Subtuplas
print("                                                 ")
print("-------------------------------------------------")
print("-    Subtuplas | print(my_sum_tuple[3:6])       -")
print("-------------------------------------------------")
print(my_sum_tuple[3:6])

# Tupla mutable con conversión a lista

print("                                                                           ")
print("---------------------------------------------------------------------------")
print("-        Convertir TIPO TUPLA a LISTA | my_tuple = list(my_tuple)         -")
print("---------------------------------------------------------------------------")
my_tuple = list(my_tuple)
print(type(my_tuple))

print("                                                          ")
print("----------------------------------------------------------")
print("-    Una vez convertido ya podemos añadir elemento       -")
print("----------------------------------------------------------")
my_tuple[4] = "MoureDev"
my_tuple.insert(1, "Azul")
#La volvemos a convertir en TUPLA
print("                                                                         ")
print("-------------------------------------------------------------------------")
print("-    La volvemos a convertir en TUPLA | my_tuple = tuple(my_tuple)      -")
print("-------------------------------------------------------------------------")
my_tuple = tuple(my_tuple)
print(my_tuple)
print("                                        ")
print("----------------------------------------")
print("-    Comprobamos de que tipo es        -")
print("----------------------------------------")
print(type(my_tuple))

# Eliminación

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined