# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=5665

### Operadores Aritméticos ###

# Operaciones con enteros

print("--------------------------------------")
print("- Operadores Aritmeticos con enteros -")
print("--------------------------------------")


print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3)
print(2 ** 3)
print(2 ** 3 + 3 - 7 / 1 // 4)

# Operaciones con cadenas de texto

print("-------------------------------------")
print("- Operadores con cadenas de textos  -")
print("-------------------------------------")

print("Hola " + "Python " + "¿Qué tal?")
print("Hola " + str(5))

# Operaciones mixtas

print("----------------------")
print("- Operaciones mixtas -")
print("----------------------")

print("Hola " * 5)
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print("Hola " * int(my_float))

### Operadores Comparativos ###

print("----------------------------")
print("- Operaciones Comparativos -")
print("----------------------------")

print("----------------------------")
print("- Operaciones con enteros  -")
print("----------------------------")

# Operaciones con enteros
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

print("------------------------------------")
print("- Operaciones con cadenas de texto -")
print("------------------------------------")

# Operaciones con cadenas de texto
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

### Operadores Lógicos ###

print("----------------------------")
print("-    Operadores Lógicos    -")
print("----------------------------")

print("----------------------------------------------------------")
print("-    Operadores Lógicos Basada en el Álgebra de Boole    -")
print("----------------------------------------------------------")

# Basada en el Álgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))