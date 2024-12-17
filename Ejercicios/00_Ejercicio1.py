import random

# Generar un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)

print("¡Bienvenido al juego de adivinar el número!")
print("He pensado en un número entre 1 y 10. ¿Puedes adivinar cuál es?")

while True:
    # Pedir al usuario que ingrese su intento
    intento = int(input("Ingresa tu número: "))
    
    if intento < numero_secreto:
        print("El número es más alto. ¡Intenta de nuevo!")
    elif intento > numero_secreto:
        print("El número es más bajo. ¡Intenta de nuevo!")
    else:
        print("¡Felicidades! Adivinaste el número.")
        break
