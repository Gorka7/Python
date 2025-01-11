# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=16335

### Sets ###

# Definición

print("------------------------")
print("-    Definición        -")
print("-   my_set = set()     -")
print("-   my_other_set = {}  -")
print("------------------------")

my_set = set()
my_other_set = {}

print("-----------------------------------------------")
print("-       Inicialmente es un diccionario        -")
print("-              my_other_set                   -")
print("-----------------------------------------------")
print("-   my_set = set()      -")
print("-------------------------")
print(type(my_set))
print("                         ")
print("-------------------------")
print("-   my_other_set = {}   -")
print("-------------------------")
print(type(my_other_set))  # Inicialmente es un diccionario

print("                         ")
print("--------------------------------------------------")
print("-   Una vez introducidos los datos ya es un SET  -")
print("-     my_other_set = {'Brais', 'Moure', 35}      -")
print("--------------------------------------------------")

my_other_set = {"Brais", "Moure", 35}
print(type(my_other_set))

print("                                                  ")
print("--------------------------------------------------")
print("-        Longitud de Elementos del SET           -")
print("--------------------------------------------------")
print(len(my_other_set))

#Inserción
print("                                                 ")
print("-------------------------------------------------")
print("-   Inserción |my_other_set.add('MoureDev')     -")
print("-------------------------------------------------")
my_other_set.add("MoureDev")
print(my_other_set)  # Un SET no es una estructura ordenada

my_other_set.add("MoureDev")  # Un SET no admite repetidos

print(my_other_set)
print("                                                   ")
print("---------------------------------------------------")
print("-      Un SET NO es una estructura ordenada       -")
print("-          Un SET NO admite repetidos             -")
print("---------------------------------------------------")

#Búsqueda
print("------------------------------------------")
print("-  Busqueda de elementos dentro del SET  -")
print("------------------------------------------")
print("-      print('Moure' in my_other_set)    -")
print("------------------------------------------")
print("Moure" in my_other_set)
print("------------------------------------------")
print("-      print('Mouri' in my_other_set)    -")
print("------------------------------------------")
print("Mouri" in my_other_set)

#Eliminación
print(" ")
print("-----------------------------------------------------------")
print("- Eliminación de Elementos | my_other_set.remove('Moure') -")
print("-----------------------------------------------------------")
my_other_set.remove("Moure")
print(my_other_set)

print(" ")
print("----------------------------------------------------------")
print("-    Vaciar SET de elementos | my_other_set.clear()      -")
print("----------------------------------------------------------")
my_other_set.clear()
print(len(my_other_set))

print("--------------------------------------------------")
print("-    Eliminar my_other_set | del my_other_set    -")
print("--------------------------------------------------")
del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

# Transformación
print("---------------------------------------------------")
print("-         Transformación de SET a LIST            -")
print("-        my_set = {'Brais', 'Moure', 35}          -")
print("-            my_list = list(my_set)               -")
print("---------------------------------------------------")
my_set = {"Brais", "Moure", 35}
my_list = list(my_set)
print(my_list)
print("--------------------------------------------------------------------")
print("-  Una vez que es lista accedemos al elemento 0 | print(my_list[0]) ")
print("--------------------------------------------------------------------")
print(my_list[0])
print("")
my_other_set = {"Kotlin", "Swift", "Python"}

# Otras operaciones
print("---------------------------------------------------------------------------")
print("-     Concatenación de SETS | my_new_set = my_set.union(my_other_set)     -")
print("---------------------------------------------------------------------------")
#Unir dos conjuntos de Sets
my_new_set = my_set.union(my_other_set)
#print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))
#print(my_new_set.difference(my_set))
print(my_new_set)

print("")
print("------------------------------------------------------------------------")
print("-     Comprobar si los elementos que hay en X estan presentes en Y     -")
print("-                      x = {'a', 'b', 'c'}                             -")
print("-                      y = {'f', 'e', 'd', 'c', 'b', 'a'}              -")
print("------------------------------------------------------------------------")
#Comprobar si los elementos que hay en X estan presentes en Y
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)