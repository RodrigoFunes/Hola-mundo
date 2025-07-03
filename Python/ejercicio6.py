input('Ingrese los siguientes datos del libro')
nombre = input('Ingrese el nombre del libro: ')
id = input('Ingrese la ID del mismo: ')
precio = input('Ingrese el precio del libro: ')
envio = input('Ingrese si el envio es gratuito (True/false): ')

if envio == 'True':
    envio = True
elif envio == 'False':
    envio = False
else:
    print('Debe indicar si es True o False')

print(f'''
      Nombre: {nombre}
      id: {id}      
      precio: {precio}
      envio gratuito?: {envio}
'''      )    
