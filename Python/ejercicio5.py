numero1 = int(input('Ingrese el primer numero: '))
numero2 = int(input('Ingrese el segundo numero: '))

numeroMayor = numero1 >= numero2 and numero2 <= numero1
if numeroMayor:
    print(f'{numero1} es el numero mayor')
else:
    print(f'{numero2} es el numero mayor')