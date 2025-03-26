# Nombre completo: Lautaro Ariel Cejas
# Comision: 11

# Actividades

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

nombreUsuario = str(input("Ingrese su nombre: "))

print(f'Hola {nombreUsuario}!')

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

nombreUsuario = str(input("Ingrese su nombre: "))
apellidoUsuario = str(input("Ingrese su apellido: ")) 
edadUsuario = int(input("Ingrese su edad: "))
lugarResidenciaUsuario = str(input("Ingrese su lugar de residencia: "))

print(f'Soy {nombreUsuario} {apellidoUsuario}, tengo {edadUsuario} años y vivo en {lugarResidenciaUsuario}')

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

radio = float(input('Ingrese el radio de su circulo: '))

area = 3.14 * radio ** 2
perimetro = 2 * 3.14 * radio

print(f'El área de su circulo es {area} y el perimetro del mismo es {perimetro}.')

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

segundos = int(input('Ingrese una cantidad de segundos: '))

horas = segundos / 3600

print(f'{segundos} segundo/s equivale a {horas} hora/s.')

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número

numero = int(input('Ingrese un número: '))

print(f'{numero} x 1 = {numero * 1}')
print(f'{numero} x 2 = {numero * 2}')
print(f'{numero} x 3 = {numero * 3}')
print(f'{numero} x 4 = {numero * 4}')
print(f'{numero} x 5 = {numero * 5}')
print(f'{numero} x 6 = {numero * 6}')
print(f'{numero} x 7 = {numero * 7}')
print(f'{numero} x 8 = {numero * 8}')
print(f'{numero} x 9 = {numero * 9}')
print(f'{numero} x 10 = {numero * 10}')

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

x = int(input("Ingrese su primer número distinto del 0: "))
y = int(input("Ingrese su segundo número distinto del 0: "))

print(f'Suma: {x + y}')
print(f'División: {x / y}')
print(f'Multiplicación: {x * y}')
print(f'Resta: {x - y}')

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo:
# 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚) ^ 2

altura = float(input('Ingrese su altura (metros): '))
peso = float(input('Ingrese su peso (kilos): '))

imc = peso / (altura ** 2)

print(f'Su índice de masa corporal es: {imc}')

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

temperaturaCelsius = float(input('Ingrese la temperatura (grados Celsius): '))

temperaturaFahrenheit = (9/5) * temperaturaCelsius + 32

print(f'Temperatura (grados Fahrenheit): {temperaturaFahrenheit}')

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

x = int(input('Ingrese el primer número: '))
y = int(input('Ingrese el segundo número: '))
z = int(input('Ingrese el tercer número: '))

promedio = (x + y + z) / 3

print(f'Promedio de sus tres números: {promedio}')