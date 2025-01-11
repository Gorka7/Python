# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=10872

### Lists ###

# Definición

print("----------------------------")
print('- Formas de Definir LISTAS -')
print("----------------------------")
print('-     my_list = list()     -')
print('-     my_other_list = []   -')
print("----------------------------")
print("                            ")

my_list = list()
my_other_list = []

print("------------------------")
print('- print(len(my_list))  -')
print("------------------------")
print(len(my_list))
print("Actualmente la lista esta vacia ")
print("                                ")
my_list = [35, 24, 62, 52, 30, 30, 17]


print("---------------------------------")
print("- Imprimir por pantalla my_list -")
print("---------------------------------")
print(my_list)
print("                                      ")
print("--------------------------------------")
print("- Imprimir por pantalla tamaño lista -")
print("--------------------------------------")
print(len(my_list))
print("                                      ")
my_other_list = [35, 1.77, "Brais", "Moure"]

print("--------------------------------------")
print("-          De que tipo es?           -")
print("--------------------------------------")
print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y búsqueda
print("              ")
print("--------------------------------------------------------------------------")
print("-        Acceder a elementos de la lista "+"my_other_list[0]                -")
print("--------------------------------------------------------------------------")
print(my_other_list[0])
print("--------------------------------------------------------------------------")
print("-        Acceder a elementos de la lista "+"my_other_list[1]                -")
print("--------------------------------------------------------------------------")
print(my_other_list[1])
print("--------------------------------------------------------------------------")
print("-        Acceder a elementos de la lista "+"my_other_list[-1]               -")
print("--------------------------------------------------------------------------")
print(my_other_list[-1])
print("--------------------------------------------------------------------------")
print("-        Acceder a elementos de la lista "+"my_other_list[-4]               -")
print("--------------------------------------------------------------------------")
print(my_other_list[-4])
print("--------------------------------------------------------------------------")
print("'my_list.count(30)' "+"Cuantas veces se repite el numero 30 en my_list      -")
print("--------------------------------------------------------------------------")
print(my_list.count(30))
#print(my_other_list[4]) #IndexError: list index out of range
# print(my_other_list[-5]) IndexError: list index out of range
print('-')

print("-----------------------------------------------------------------")
print('-  Posición del elemento introducido  -'+"my_other_list.index(35)  -")
print("-----------------------------------------------------------------")
print(my_other_list.index(35))

#my_other_list = [35, 1.77, "Brais", "Moure"]
print("----------------------------------------------------------------------------------------------------------")
print('-  my_other_list = [35, 1.77, "Brais", "Moure -'+" age, height, name, surname = my_other_list -"+" print(name) -")
print("----------------------------------------------------------------------------------------------------------")
age, height, name, surname = my_other_list
print(name)

#my_other_list = [35, 1.77, "Brais", "Moure"]
print("------------------------------------------------------------------------------------------------------------------")
print("name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3] - "+"print(age) -")     
print("------------------------------------------------------------------------------------------------------------------")
name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)
#Saca por consola 35

# Concatenación
print("---------------------------------------------")
print("-    Contenacion |my_list + my_other_list|  -")
print("---------------------------------------------")
print(my_list + my_other_list)
print("                                             ")
#print(my_list - my_other_list)

# Creación, inserción, actualización y eliminación
print("-------------------------------------------------------------")
print("-  Insertar Elemento a la lista (al final del indice)       -")
print("-------------------------------------------------------------")
my_other_list.append("MoureDev")
print(my_other_list)
print("                                        ")

#my_other_list = [35, 1.77, "Brais", "Moure,MoureDev"]
print("---------------------------------------------------------------")
print("-  Insertar Elemento a la lista - Indice,Elemento - (1, Rojo) -")
print("---------------------------------------------------------------")
my_other_list.insert(1, "Rojo")   
print(my_other_list)

print("                                        ")
print("------------------------------------------------------------------")
print("-  Modificar Elemento a la lista - my_other_list[1] = Azul       -")
print("------------------------------------------------------------------")
my_other_list[1] = "Azul"
print(my_other_list)

print("                                        ")
print("--------------------------------------------------------------------")
print("-  Elimimar Elemento de la lista - my_other_list.remove('Azul')    -")
print("--------------------------------------------------------------------")
my_other_list.remove('Azul')
print(my_other_list)

print('--')
my_list.remove(30)
print(my_list)
print('--')

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

print('---')
del my_list[2]
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

# Sublistas

print(my_new_list[1:3])

# Cambio de tipo

my_list = "Hola Python"
print(my_list)
print(type(my_list))