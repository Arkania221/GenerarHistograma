"""
Primero vamos a crear un generador de numeros aleatorios
"""

Time = 0  # Inicializamos el contador de tiempo

# Inicializamos el contador de tiempo
Time = 0  

# Guardamos el tiempo inicial del sistema en segundos
start_time = sum(map(int, str(__import__('time').time()).split('.')))

while True:
    # Solicitamos la entrada del usuario
    Tiradas = input("Agregue numero de tiradas: ")

    # Si el usuario ha ingresado algo, salimos del bucle
    if Tiradas:
        break
    else:
        # Si el usuario no ha ingresado nada, actualizamos el tiempo actual del sistema y aumentamos el contador con el tiempo que tardó
        end_time = sum(map(int, str(__import__('time').time()).split('.')))
        Time += end_time - start_time
        start_time = end_time

print("El usuario ingresó:", Tiradas)
print("El tiempo que tardó el usuario en ingresar la variable fue:", Time, "segundos")
