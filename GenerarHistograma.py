"""

1. ¿Que debemos mostrar? El histograma
2. ¿De donde obtenemos los valores del histograma? De un generador de numeros pseudoaleatorios
3. ¿Donde almacenaremos los resultados del generador? En una array
4. ¿Como sabremos la cantidad de veces que toco cada resultado? Usando el count() o un def que compare numeros pendiente preguntar al albert
5. ¿Cuantos valores debera tener el histograma? A eleccion del usuario, creamos variable de tiradas
6. ¿Como sacamos los numeros pseudoaleatorios? Usando la cantidad de tiradas como semillas
7. ¿Como  se mostraran los datos? Podemos usar prints de los posibles resultados que muestres pipes de la cantidad de estos mismos


Pasos a seguir:

1. Crear los def's necesarios: Programa inicial, Aleatorizador, Printeo del histograma

2. Se agrega la variable de tiradas para la semilla

3. Se agrega la array que almacena los resultados

4. Se hace el pseudo aleatorizador con la congruencia lineal

4.1. Se itera sobre la semilla para la cantidad de resultados

4.2. Se va operando a partir de la semilla y del resultado de esta

4.3. Se devuelve la array de resultados

5. Se crean los prints de los posibles numeros aleatorios

6. Se modifican los prints para que se muestre en forma de barritas

Pasos a posterior: .... 
"""
tiradas = 0
resultados = []

def Aleatorizador(semilla):
    resultados = []
    for i in range(semilla):
        a = 4387438
        b = 98980
        resultado = resultado.append( (((a * b) * semilla) % 12) + 1)


def Histograma():



def Programa():
tiradas = int(input("Agrega la cantidad de tiradas"))
