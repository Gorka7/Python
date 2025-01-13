#Clase en vídeo: https://youtu.be/Kp4Mvapo5kc

### Dictionaries ###

#Definición

print("------------------------")
print("-      Definición      -")
print("-   my_dict = dict()   -")
print("-   my_other_dict = {} -")
print("------------------------")

my_dict = dict()
my_other_dict = {}
print("----------------------------------")
print("-         De que TIPO son :      -")
print("----------------------------------")
print("-      print(type(my_dict))      -")
print("-    print(type(my_other_dict))  -")
print("----------------------------------")
print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Brais",
                 "Apellido": "Moure", "Edad": 35, 1: "Python"}

my_dict = {
    "Nombre": "Brais",
     "Apellido": "Moure",
     "Edad": 35, 
     "Lenguajes": {"Python", "Swift", "Kotlin"},
     1: 1.77
}

print("")
print("------------------------------------------")
print("-    Sacamos por pantalla los Valores    -")
print("------------------------------------------")
print("-         print(my_other_dict)           -")
print("------------------------------------------")
print(my_other_dict)
print("")
print("------------------------------------------")
print("-             print(my_dict)             -")
print("------------------------------------------")
print(my_dict)

print("")
print("---------------------------------------------------------------------------")
print("-         Cantidad de Valores del DIC | print(len(my_other_dict))         -")
print("---------------------------------------------------------------------------")
print(len(my_other_dict))
print("")
print("---------------------------------------------------------------------------")
print("-         Cantidad de Valores del DIC | print(len(my_dict))               -")
print("---------------------------------------------------------------------------")
print(len(my_dict))

#Búsqueda
"""
my_dict = {
    "Nombre": "Brais",
     "Apellido": "Moure",
     "Edad": 35, 
     "Lenguajes": {"Python", "Swift", "Kotlin"},
     1: 1.77
}
"""
print("")
print("---------------------------------------------------------------------")
print("-  Sacar el valor de la clave que le indicamos | print(my_dict[1])  -")
print("---------------------------------------------------------------------")
print(my_dict[1])
print("")
print("----------------------------------------------------------------------------")
print("-  Sacar el valor de la clave que le indicamos | print(my_dict['Nombre'])  -")
print("----------------------------------------------------------------------------")
print(my_dict["Nombre"])

#Busqueda
print("")
print("-------------------------------------------")
print("-       Busqueda de Clave en el DIC       -")
print("--------------------------------------------------------------------------------------------")
print("-          print('Moure' in my_dict) | False , Moure es el valor , lo la clave             -")
print("--------------------------------------------------------------------------------------------")
print("Moure" in my_dict)
print("")
print("-------------------------------------------")
print("-       Busqueda de Clave en el DIC       -")
print("--------------------------------------------------------------------------------------------")
print("-             print('Apellido' in my_dict) | True , Apellido si es en la clave             -")
print("--------------------------------------------------------------------------------------------")
print("Apellido" in my_dict)

#Inserción
print("")
print("----------------------------------------------------------------------------")
print("-     Inserción de un nuevo Dato | my_dict['Calle'] = 'Calle MoureDev'     -")
print("----------------------------------------------------------------------------")
my_dict["Calle"] = "Calle MoureDev"
print(my_dict)

#Actualización
print("")
print("--------------------------------------------------------------")
print("-     Actualización de Datos | my_dict['Nombre'] = 'Pedro'   -")
print("--------------------------------------------------------------")
my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

# Eliminación
print("")
print("-----------------------------------------------------")
print("-        Eliminación | del my_dict['Calle']        - ")
print("-----------------------------------------------------")
del my_dict["Calle"]
print(my_dict)

#Otras operaciones


print("")
print("------------------------------------------------------------------")
print("-     Mostrar items del Diccionario | print(my_dict.items())     -")
print("------------------------------------------------------------------")
print(my_dict.items())
print("")
print("------------------------------------------------------------------")
print("-      Mostrar Keys del Diccionario | print(my_dict.keys())      -")
print("------------------------------------------------------------------")
print(my_dict.keys())
print("")
print("---------------------------------------------------------------------")
print("-     Mostrar Valores del Diccionario | print(my_dict.values())     -")
print("---------------------------------------------------------------------")
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

print("")
print("-------------------------------------------------------------------")
print("-     Crear un SET vacio , unicamente con las claves de Valor     -")
print("-                my_list = ['Nombre', 1, 'Piso']                  -")
print("-             my_new_dict = dict.fromkeys((my_list))              -")
print("-------------------------------------------------------------------")
my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
#print((my_new_dict))
print("")
print("-------------------------------------------------------------------")
print("-     Crear un SET vacio , unicamente con las claves de Valor     -")
print("-               my_new_dict = dict.fromkeys(my_dict)              -")
print("-              En este caso crea uno vacio con my_dict            -")
print("-------------------------------------------------------------------")
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
print("")
print("----------------------------------------------------------------")
print("-        Darle el valor de 'Mourev' a todos los Keys           -")
print("-      my_new_dict = dict.fromkeys(my_dict, 'MoureDev')        -")
print("----------------------------------------------------------------")
my_new_dict = dict.fromkeys(my_dict, "MoureDev")
print((my_new_dict))

print("")
print("------------------------------")
print("-       Clase values()       -")
print("------------------------------")
my_values = my_new_dict.values()
print(type(my_values))

print("")
print("-------------------------------------------------------")
print("-    Mostrar los valores de nuestro Dicccionario      -")
print("-            print(my_new_dict.values())              -")
print("-------------------------------------------------------")
print(my_new_dict.values())
#print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
#print(tuple(my_new_dict))
#print(set(my_new_dict))