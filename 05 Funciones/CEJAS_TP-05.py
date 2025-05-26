# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”.
# Llamar a esta función desde el programa principal.

# Función que muestra un saludo básico
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Llamo a la función para que se ejecute
imprimir_hola_mundo()


# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre
# y devuelva un saludo personalizado. Llamar a esta función desde el programa principal solicitando el nombre.

# Función que arma un saludo con el nombre que se le pasa
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Pido el nombre al usuario y muestro el saludo
nombre = input("Ingresá tu nombre: ")
print(saludar_usuario(nombre))


# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia)
# que reciba cuatro parámetros e imprima un mensaje con esa info.

# Función que imprime datos personales formateados
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Pido los datos al usuario y llamo a la función con esos datos
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")
informacion_personal(nombre, apellido, edad, residencia)


# 4. Crear dos funciones: una para calcular el área y otra para el perímetro de un círculo.
# Pedir el radio al usuario y mostrar ambos resultados.

import math  # Importo math para usar PI

# Área del círculo: pi * r²
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

# Perímetro del círculo: 2 * pi * r
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Pido el radio y muestro área y perímetro
radio = float(input("Ingresá el radio del círculo: "))
print(f"Área: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")


# 5. Crear una función llamada segundos_a_horas(segundos)
# que convierta segundos a horas.

# Convierte segundos a horas (dividiendo por 3600)
def segundos_a_horas(segundos):
    return segundos / 3600

# Pido los segundos y muestro cuántas horas son
segundos = int(input("Ingresá los segundos: "))
print(f"Equivale a {segundos_a_horas(segundos):.2f} horas")


# 6. Crear una función llamada tabla_multiplicar(numero)
# que imprima la tabla de multiplicar del 1 al 10 del número ingresado.

# Muestra la tabla del número del 1 al 10
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Pido el número al usuario y muestro su tabla
numero = int(input("Ingresá un número para ver su tabla: "))
tabla_multiplicar(numero)


# 7. Crear una función llamada operaciones_basicas(a, b)
# que devuelva suma, resta, multiplicación y división como tupla.

# Hace operaciones básicas entre dos números
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multi = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multi, division)

# Pido dos números al usuario y muestro los resultados
a = float(input("Primer número: "))
b = float(input("Segundo número: "))
resultados = operaciones_basicas(a, b)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")


# 8. Crear una función llamada calcular_imc(peso, altura)
# que devuelva el índice de masa corporal (IMC).

# Calcula el IMC usando la fórmula peso / altura²
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Pido peso y altura al usuario y muestro el IMC con 2 decimales
peso = float(input("Peso en kg: "))
altura = float(input("Altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {imc:.2f}")


# 9. Crear una función llamada celsius_a_fahrenheit(celsius)
# que convierta grados Celsius a Fahrenheit.

# Convierte Celsius a Fahrenheit usando la fórmula estándar
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Pido temperatura en Celsius y muestro en Fahrenheit
celsius = float(input("Temperatura en °C: "))
print(f"Equivale a {celsius_a_fahrenheit(celsius):.2f} °F")


# 10. Crear una función llamada calcular_promedio(a, b, c)
# que devuelva el promedio de tres números.

# Calcula el promedio de 3 números
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Pido tres números y muestro el promedio
a = float(input("Primer número: "))
b = float(input("Segundo número: "))
c = float(input("Tercer número: "))
print(f"El promedio es: {calcular_promedio(a, b, c):.2f}")