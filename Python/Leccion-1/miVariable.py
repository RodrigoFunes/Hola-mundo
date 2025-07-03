'''
miVariable = 3;
print(miVariable);
miVariable = "Hola a todos los que lean esto";
print(miVariable);
x = 10;
y = 2;
z = x + y;
print(z);

a = "asd";
print(a);
print(type(a));
a = 10;
print(a);
print(type(a));
a = 10.53;
print(a);
print(type(a));
a = True;
print(a);
print(type(a));

# Manejo de cadenas (string)

miGrupoFavorito = "La Renga: ";
caracteristicas = "Locura de banda"
print("Mi grupo favorito es: ", miGrupoFavorito, caracteristicas);

numero1= "10";
numero2 = "20";
print(int(numero1) + int(numero2));

# Tipos de Boleanos (bool)

miBoleano = 1 > 2
print(miBoleano)

if miBoleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")    

# Procesar la entrada del usuario
# FUNCION input

#resultado = input("Digite un numero: ")
#print(resultado)

# Conversion de entrada de datos

#numero1 = int(input("Digite el primer numero: "))
#numero2 = int(input("Digite el segundo numero: "))
#resultado = numero1 + numero2

#print("La suma de los dos numeros es: ", resultado)

# ACTIVIDADES

miDia = input("Como estuvo tu dia (1 al 10)?: ")
print("Mi dia estuvo de: ",miDia)

titulo = input("Proporciona un titulo: ")
autor = input("Proporciona el autor: ")
print (titulo,"fue escrito por", autor)

'''
# OPERADORES

operadorA = 8
operadorB= 5

suma = operadorA + operadorB
print(f"La suma de los dos operadores es: {suma}")

resta = operadorA - operadorB
print(f"El resultado de la resta es: {resta}")

multiplicacion = operadorA * operadorB
print(f"El resultado de la multiplicacion es: {multiplicacion}")

division = operadorA / operadorB
print(f"El resultado de la division es: {division}")
division = operadorA / operadorB
print(f"El resultado de la division (int) es: {division}")

modulo = operadorA % operadorB
print(f"El resultado del division o residuo (modulo) es: {modulo}")

exponente = operadorA ** operadorB
print(f"El resultado del exponente es: {exponente}")


