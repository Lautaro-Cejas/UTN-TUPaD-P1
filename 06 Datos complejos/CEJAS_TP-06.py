# ===============================================
# EJERCICIO 1: Crea una función recursiva que calcule el factorial de un número. 
# Luego, utiliza esa función para calcular y mostrar en pantalla el factorial 
# de todos los números enteros entre 1 y el número que indique el usuario
# ===============================================
def factorial(n):
    """Calcula el factorial de un número de forma recursiva"""
    # Defino el caso base: tanto 0! como 1! son igual a 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: aplico la definición matemática n! = n × (n-1)!
    else:
        return n * factorial(n - 1)

def mostrar_factoriales():
    """Muestra los factoriales desde 1 hasta el número indicado por el usuario"""
    num = int(input("Ingrese un número para calcular factoriales hasta ese valor: "))
    
    print("Factoriales desde 1 hasta " + str(num) + ":")
    # Itero desde 1 hasta el número ingresado y calculo cada factorial
    for i in range(1, num + 1):
        print(str(i) + "! = " + str(factorial(i)))

# ===============================================
# EJERCICIO 2: Crea una función recursiva que calcule el valor de la serie de 
# Fibonacci en la posición indicada. Posteriormente, muestra la serie completa 
# hasta la posición que el usuario especifique.
# ===============================================
def fibonacci(n):
    """Calcula el valor de Fibonacci en la posición n de forma recursiva"""
    # Casos base de la secuencia de Fibonacci
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Caso recursivo: F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_fibonacci():
    """Muestra la serie de Fibonacci hasta la posición indicada"""
    pos = int(input("Ingrese la posición hasta donde mostrar la serie de Fibonacci: "))
    
    print("Serie de Fibonacci hasta la posición " + str(pos) + ":")
    # Muestro cada valor de la serie desde la posición 0 hasta la indicada
    for i in range(pos + 1):
        print("F(" + str(i) + ") = " + str(fibonacci(i)))

# ===============================================
# EJERCICIO 3: Crea una función recursiva que calcule la potencia de un número 
# base elevado a un exponente, utilizando la fórmula n^m = n * n^(m-1). 
# Prueba esta función en un algoritmo general.
# ===============================================
def potencia(base, exponente):
    """Calcula base^exponente de forma recursiva usando la fórmula dada"""
    # Caso base: cualquier número elevado a la 0 es 1
    if exponente == 0:
        return 1
    # Caso recursivo: aplico la fórmula n^m = n * n^(m-1)
    else:
        return base * potencia(base, exponente - 1)

def probar_potencia():
    """Prueba la función de potencia con valores ingresados por el usuario"""
    base = float(input("Ingrese la base: "))
    exp = int(input("Ingrese el exponente (entero no negativo): "))
    
    resultado = potencia(base, exp)
    print(str(base) + "^" + str(exp) + " = " + str(resultado))

# ===============================================
# EJERCICIO 4: Crear una función recursiva en Python que reciba un número entero 
# positivo en base decimal y devuelva su representación en binario como una cadena de texto.
# ===============================================
def decimal_a_binario(n):
    """Convierte un número decimal a binario de forma recursiva"""
    # Casos base: cuando llego a 0 o 1, devuelvo directamente su representación
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    # Caso recursivo: divido por 2 y concateno el resto
    # Sigo el algoritmo: dividir por 2, guardar resto, repetir con cociente
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

def probar_binario():
    """Prueba la conversión a binario con un número ingresado por el usuario"""
    num = int(input("Ingrese un número decimal positivo: "))
    
    binario = decimal_a_binario(num)
    print("El número " + str(num) + " en binario es: " + binario)

# ===============================================
# EJERCICIO 5: Implementá una función recursiva llamada es_palindromo(palabra) 
# que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es 
# un palíndromo o False si no lo es. La solución debe ser recursiva. 
# No se debe usar [::-1] ni la función reversed().
# ===============================================
def es_palindromo(palabra):
    """Verifica si una palabra es palíndromo de forma recursiva"""
    # Caso base: una cadena vacía o de un solo carácter siempre es palíndromo
    if len(palabra) <= 1:
        return True
    
    # Comparo el primer carácter con el último (ignoro mayúsculas/minúsculas)
    if palabra[0].lower() != palabra[-1].lower():
        return False
    
    # Caso recursivo: verifico la subcadena sin el primer y último carácter
    # Si los extremos coinciden, el resultado depende del interior
    return es_palindromo(palabra[1:-1])

def probar_palindromo():
    """Prueba la función de palíndromo con una palabra ingresada por el usuario"""
    palabra = input("Ingrese una palabra (sin espacios ni tildes): ")
    if es_palindromo(palabra):
        print("'" + palabra + "' es un palíndromo.")
    else:
        print("'" + palabra + "' no es un palíndromo.")

# ===============================================
# EJERCICIO 6: Escribí una función recursiva en Python llamada suma_digitos(n) 
# que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
# No se puede convertir el número a string. Usá operaciones matemáticas (%, //) y recursión.
# ===============================================
def suma_digitos(n):
    """Suma todos los dígitos de un número de forma recursiva usando operaciones matemáticas"""
    # Caso base: si el número tiene un solo dígito, lo devuelvo directamente
    if n < 10:
        return n
    # Caso recursivo: sumo el último dígito (n % 10) con la suma del resto (n // 10)
    else:
        return n % 10 + suma_digitos(n // 10)

def probar_suma_digitos():
    """Prueba la función suma de dígitos con un número ingresado por el usuario"""
    num = int(input("Ingrese un número entero positivo: "))
    
    suma = suma_digitos(num)
    print("La suma de los dígitos de " + str(num) + " es: " + str(suma))

# ===============================================
# EJERCICIO 7: Un niño está construyendo una pirámide con bloques. En el nivel más 
# bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente 
# hasta llegar al último nivel con un solo bloque. Escribí una función recursiva 
# contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva 
# el total de bloques que necesita para construir toda la pirámide.
# ===============================================
def contar_bloques(n):
    """Cuenta el total de bloques necesarios para construir una pirámide"""
    # Caso base: si solo hay un nivel, necesito exactamente 1 bloque
    if n == 1:
        return 1
    # Caso recursivo: sumo los bloques del nivel actual (n) más los de niveles superiores
    # Esto equivale a la suma 1 + 2 + 3 + ... + n
    else:
        return n + contar_bloques(n - 1)

def probar_piramide():
    """Prueba la función de contar bloques con un valor ingresado por el usuario"""
    niveles = int(input("Ingrese el número de bloques en el nivel más bajo: "))
    
    total = contar_bloques(niveles)
    print("Total de bloques necesarios para una pirámide de " + str(niveles) + " niveles: " + str(total))

# ===============================================
# EJERCICIO 8: Escribí una función recursiva llamada contar_digito(numero, digito) 
# que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y 
# devuelva cuántas veces aparece ese dígito dentro del número.
# ===============================================
def contar_digito(numero, digito):
    """Cuenta cuántas veces aparece un dígito en un número de forma recursiva"""
    # Caso base especial: si el número es 0, verifico si coincide con el dígito buscado
    if numero == 0:
        if digito == 0:
            return 1
        else:
            return 0
    
    # Extraigo el último dígito del número usando operaciones matemáticas
    ultimo_digito = numero % 10
    resto_numero = numero // 10
    
    # Cuento 1 si el último dígito coincide con el buscado, 0 en caso contrario
    if ultimo_digito == digito:
        contador = 1
    else:
        contador = 0
    
    # Caso recursivo: sumo el contador actual con el resultado del resto del número
    if resto_numero == 0:
        return contador
    else:
        return contador + contar_digito(resto_numero, digito)

def probar_contar_digito():
    """Prueba la función de contar dígito con valores ingresados por el usuario"""
    numero = int(input("Ingrese un número entero positivo: "))
    digito = int(input("Ingrese un dígito (0-9) a buscar: "))
    
    cantidad = contar_digito(numero, digito)
    print("El dígito " + str(digito) + " aparece " + str(cantidad) + " veces en el número " + str(numero))

# ===============================================
# MENÚ PRINCIPAL
# ===============================================
def menu_principal():
    """Menú principal para ejecutar los ejercicios"""
    while True:
        print("\n" + "="*60)
        print("TP7 - EJERCICIOS DE RECURSIVIDAD")
        print("="*60)
        print("1. Factorial de números")
        print("2. Serie de Fibonacci")
        print("3. Potencia recursiva")
        print("4. Decimal a Binario")
        print("5. Verificar Palíndromo")
        print("6. Suma de Dígitos")
        print("7. Contar Bloques de Pirámide")
        print("8. Contar Dígito en Número")
        print("0. Salir")
        print("="*60)
        
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 0:
            print("¡Hasta luego!")
            break
        elif opcion == 1:
            mostrar_factoriales()
        elif opcion == 2:
            mostrar_fibonacci()
        elif opcion == 3:
            probar_potencia()
        elif opcion == 4:
            probar_binario()
        elif opcion == 5:
            probar_palindromo()
        elif opcion == 6:
            probar_suma_digitos()
        elif opcion == 7:
            probar_piramide()
        elif opcion == 8:
            probar_contar_digito()
        else:
            print("Opción no válida. Por favor seleccione una opción del 0 al 8.")

# ===============================================
# EJEMPLOS DE PRUEBA
# ===============================================
def ejemplos_prueba():
    """Ejecuta ejemplos de prueba para verificar las funciones"""
    print("EJEMPLOS DE PRUEBA AUTOMÁTICOS:")
    print("-" * 40)
    
    # Pruebo el factorial con 5
    print("factorial(5) = " + str(factorial(5)) + " (esperado: 120)")
    
    # Pruebo Fibonacci en posición 7
    print("fibonacci(7) = " + str(fibonacci(7)) + " (esperado: 13)")
    
    # Pruebo potencia de 2^3
    print("potencia(2, 3) = " + str(potencia(2, 3)) + " (esperado: 8)")
    
    # Pruebo conversión del 10 a binario
    print("decimal_a_binario(10) = " + decimal_a_binario(10) + " (esperado: 1010)")
    
    # Pruebo palíndromos
    print("es_palindromo('radar') = " + str(es_palindromo('radar')) + " (esperado: True)")
    print("es_palindromo('python') = " + str(es_palindromo('python')) + " (esperado: False)")
    
    # Pruebo suma de dígitos con los ejemplos del enunciado
    print("suma_digitos(1234) = " + str(suma_digitos(1234)) + " (esperado: 10)")
    print("suma_digitos(305) = " + str(suma_digitos(305)) + " (esperado: 8)")
    
    # Pruebo contar bloques con el ejemplo del enunciado
    print("contar_bloques(4) = " + str(contar_bloques(4)) + " (esperado: 10)")
    
    # Pruebo contar dígito con los ejemplos del enunciado
    print("contar_digito(12233421, 2) = " + str(contar_digito(12233421, 2)) + " (esperado: 3)")
    print("contar_digito(5555, 5) = " + str(contar_digito(5555, 5)) + " (esperado: 4)")
    print("contar_digito(123456, 7) = " + str(contar_digito(123456, 7)) + " (esperado: 0)")

# ===============================================
# EJECUTAR PROGRAMA
# ===============================================
if __name__ == "__main__":
    # Ejecuto primero los ejemplos de prueba para verificar que todo funciona
    ejemplos_prueba()
    
    # Luego ejecuto el menú principal para interactuar con el usuario
    menu_principal()