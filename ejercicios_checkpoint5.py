# ============================================================
#  CHECKPOINT 5 — Ejercicios Prácticos Python
#  Open Consultech | Full Stack Developer Bootcamp
#  Autora: Miguelina Rosario | Marzo 2026
# ============================================================


# ============================================================
# EJERCICIO 1: Bucle FOR en Python
# Descripción: Recorre una lista de lenguajes de programación
#              e imprime cada uno con su número de posición.
# ============================================================

print("=" * 50)
print("  EJERCICIO 1 — Bucle FOR")
print("=" * 50)

lenguajes = ["Python", "JavaScript", "Java", "C++", "TypeScript", "SQL"]

for indice, lenguaje in enumerate(lenguajes, start=1):
    print(f"  {indice}. {lenguaje}")

# También se puede iterar con range directamente:
print("\n  Con range():")
for i in range(len(lenguajes)):
    print(f"  Posición [{i}] → {lenguajes[i]}")


# ============================================================
# EJERCICIO 2: Función SUMA con 3 argumentos
# Descripción: Recibe 3 números y devuelve su suma total.
# ============================================================

print("\n" + "=" * 50)
print("  EJERCICIO 2 — Función suma(a, b, c)")
print("=" * 50)

def suma(a, b, c):
    """
    Suma tres números y devuelve el resultado.

    Parámetros:
        a (int | float): Primer número.
        b (int | float): Segundo número.
        c (int | float): Tercer número.

    Retorna:
        int | float: La suma de los tres argumentos.

    Ejemplo:
        >>> suma(2, 3, 5)
        10
    """
    return a + b + c


# Pruebas de la función
print(f"\n  suma(5, 10, 15)       = {suma(5, 10, 15)}")
print(f"  suma(1.5, 2.5, 3)     = {suma(1.5, 2.5, 3)}")
print(f"  suma(100, 200, 300)   = {suma(100, 200, 300)}")
print(f"  suma(-5, 10, -3)      = {suma(-5, 10, -3)}")


# ============================================================
# EJERCICIO 3: Función LAMBDA equivalente a suma
# Descripción: Misma funcionalidad que la función suma,
#              pero escrita como función anónima (lambda).
# ============================================================

print("\n" + "=" * 50)
print("  EJERCICIO 3 — Lambda equivalente a suma")
print("=" * 50)

# Lambda: recibe 3 argumentos y devuelve su suma
suma_lambda = lambda a, b, c: a + b + c

# Pruebas — mismos valores que en el Ejercicio 2
print(f"\n  suma_lambda(5, 10, 15)       = {suma_lambda(5, 10, 15)}")
print(f"  suma_lambda(1.5, 2.5, 3)     = {suma_lambda(1.5, 2.5, 3)}")
print(f"  suma_lambda(100, 200, 300)   = {suma_lambda(100, 200, 300)}")
print(f"  suma_lambda(-5, 10, -3)      = {suma_lambda(-5, 10, -3)}")

# Verificación: ambas funciones deben producir el mismo resultado
print(f"\n  ¿Resultados iguales (5, 10, 15)?  {suma(5,10,15) == suma_lambda(5,10,15)}")


# ============================================================
# EJERCICIO 4: Verificar si un nombre está en la lista
# Descripción: Comprobar si la variable 'nombre' coincide
#              con algún valor de 'lista_nombres'.
#              Método 1: bucle for + comparación manual
#              Método 2: operador 'in' (forma simplificada)
# ============================================================

print("\n" + "=" * 50)
print("  EJERCICIO 4 — ¿Está el nombre en la lista?")
print("=" * 50)

nombre = 'Enrique'
lista_nombres = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

print(f"\n  Nombre a buscar : '{nombre}'")
print(f"  Lista de nombres: {lista_nombres}")
print()

# --- MÉTODO 1: Bucle for con comparación explícita ---
print("  [Método 1 — Bucle for in]")
encontrado = False

for n in lista_nombres:
    if nombre == n:
        encontrado = True
        break  # Dejamos de buscar si ya encontramos una coincidencia

if encontrado:
    print(f"  ✅ El nombre '{nombre}' SÍ se encuentra en la lista.")
else:
    print(f"  ❌ El nombre '{nombre}' NO se encuentra en la lista.")


# --- MÉTODO 2: Operador 'in' (más pythónico) ---
print("\n  [Método 2 — Operador 'in']")
if nombre in lista_nombres:
    print(f"  ✅ '{nombre}' SÍ está en la lista.")
else:
    print(f"  ❌ '{nombre}' NO está en la lista.")


# --- BONUS: Búsqueda sin distinguir mayúsculas/minúsculas ---
print("\n  [Bonus — Búsqueda sin distinguir mayúsculas]")
nombre_lower = nombre.lower()
lista_lower = [n.lower() for n in lista_nombres]

if nombre_lower in lista_lower:
    print(f"  ✅ '{nombre}' SÍ se encuentra (búsqueda sin distinción de caso).")
else:
    print(f"  ❌ '{nombre}' NO se encuentra (búsqueda sin distinción de caso).")


# ============================================================
# RESUMEN FINAL
# ============================================================

print("\n" + "=" * 50)
print("  RESUMEN DE RESULTADOS")
print("=" * 50)
print(f"  Ej.1 — Bucle for: {len(lenguajes)} lenguajes impresos correctamente.")
print(f"  Ej.2 — Función suma(10, 20, 30)        = {suma(10, 20, 30)}")
print(f"  Ej.3 — Lambda suma(10, 20, 30)          = {suma_lambda(10, 20, 30)}")
print(f"  Ej.4 — '{nombre}' en lista              = {nombre in lista_nombres}")
print("=" * 50)
print("  ✅ Todos los ejercicios completados.")
print("=" * 50)
