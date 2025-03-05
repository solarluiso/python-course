###
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí

print("Luiso\nWashington")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

print("a:", type(a))
print("b:", type(b))
print("c:", type(c))
print("d:", type(d))
print("e:", type(e))

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
cadena = "12345"
entero = int(cadena)  # Convertimos la cadena a entero
flotante = float(entero)  # Convertimos el entero a float
print(f"entero: {entero}")
print(f"float: {flotante}")

flotante = 3.99
entero = int(flotante)  # Convertimos el float a entero
print(f"3.99 convertido a entero: {entero}")
print("Al convertir un float a entero, se elimina la parte decimal (no se redondea).")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
name = "Luiso"
age = 33
height = 1.80
print((f"Hola! Me llamo {name} y tengo {age} años, mido {height} metros"))

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

### Completa aquí
print("Resultados:")
#1
import math
pi = math.pi
print("1. pi:", pi)

#2
pi_rounded = round(pi)
print("2. pi_redondeado:", pi_rounded)

#3
division = pi_rounded // 2
print("3. La división entera de", pi_rounded, "entre 2 es:", division)
