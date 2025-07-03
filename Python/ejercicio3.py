""""
numero = int(input('Ingrese un numero: '))
valorMinimo = 0
valorMaximo = 5
dentroRango = numero >= valorMinimo and numero <= valorMaximo
if dentroRango:
    print(f'El {numero} esta dentro del rango')
else:
    print(f'El {numero} no esta dentro del rango')
"""    

# Ejercicio operador or y operador not

vacaciones = False
diaDescanso = False

if not (vacaciones or diaDescanso):
    print('Tiene trabajo que hacer')
else: 
    print('Puede asistir al juego')