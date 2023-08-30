#Crear un programa que le solicite al usuario dos números enteros y luego imprima por pantalla:
#● la suma de ambos números
#● la resta de ambos números
#● la multiplicación de ambos números
#● la división entera de ambos números
#● el resto

def solicitar_entero():
    while True:
        try:
            numero_entero = int(input('Ingresa un número entero: '))
            return numero_entero
        except ValueError:
            print('Eso no es un número entero válido. Por favor, intenta nuevamente.')

# Crear una lista para almacenar los números
numeros = []

# Solicitar al usuario la cantidad deseada de números enteros y agregarlos a la lista
for _ in range(10):
    numeros.append(solicitar_entero())

# Realizar operaciones entre los números ingresados

if numeros:
    suma = sum(numeros)
    resta = numeros[0] - sum(numeros[1:])
    multiplicacion = 1
    for num in numeros:
        multiplicacion *= num
    division = numeros[0]
    for num in numeros[1:]:
        if num != 0:
            division /= num
        else:
            division = None
            break

    print('Suma:', suma)
    print('Resta:', resta)
    print('Multiplicación:', multiplicacion)
    if division is not None:
        print('División:', division)
    else:
        print('División: No se puede dividir por cero.')
else:
    print('No se ingresaron números para calcular.')







