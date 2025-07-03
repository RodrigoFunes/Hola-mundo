numero = int(input('Ingresa un numero: '))
print(f"El residuo de la division es: {numero % 2}")

if numero % 2 == 0:
    print(f'El numero es par: {numero} es par')
else:
    print(f'El numero es impar: {numero} es impar')