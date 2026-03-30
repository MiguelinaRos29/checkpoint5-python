# Ejercicio 1: bucle for que imprime números del 1 al 5
for numero in range(1, 6):
    print(numero)


# Ejercicio 2: función que suma tres números
def suma(a, b, c):
    return a + b + c

print(suma(2, 4, 6))


# Ejercicio 3: misma función usando lambda
suma_lambda = lambda a, b, c: a + b + c

print(suma_lambda(2, 4, 6))


# Ejercicio 4: comprobar si un nombre está en la lista
nombre = "Enrique"
lista_nombre = ["Jessica", "Paul", "George", "Henry", "Adán"]

if nombre in lista_nombre:
    print("El nombre está en la lista")
else:
    print("El nombre no está en la lista")