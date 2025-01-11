# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=8643

### Strings ###

print("-------------------")
print("-     Strings     -")
print("-------------------")

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo

print("-------------------")
print("-     Formateo    -")
print("-------------------")

name, surname, age = "Gorka", "Sanchez", 34
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d"  %(name, surname, age))
#print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaqueado de caracteres


print("------------------------------------")
print("-  Desempaquetado de Caracteres    -")
print("------------------------------------")

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

print("-------------------")
print("-    División     -")
print("-------------------")

language_slice = language[1:3]
print(language_slice) #yt

language_slice = language[1:]
print(language_slice) #ython

language_slice = language[-2]
print(language_slice) #o

language_slice = language[0:6:2]
print(language_slice) #

# Reverse


print("-------------------")
print("-    Reverse      -")
print("-------------------")

reversed_language = language[::-1]
print(reversed_language)


# Funciones del lenguaje


print("-------------------------------")
print("-   Funciones del lenguaje    -")
print("-------------------------------")

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py")  # No es lo mismo
print("-")