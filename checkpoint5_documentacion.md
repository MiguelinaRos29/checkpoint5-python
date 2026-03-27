# 📘 CheckPoint 5 — Documentación Python para Desarrolladores
### Open Consultech | Formación Técnica Interna
**Autora:** Miguelina Rosario  
**Proyecto:** Full Stack Developer Bootcamp — Módulo Python  
**Fecha:** Marzo 2026

---

> **📌 Nota para el lector:** Este documento ha sido preparado como material de referencia para nuevos miembros del equipo de desarrollo. Contiene explicaciones detalladas, sintaxis, ejemplos prácticos y casos de uso reales. Se recomienda leerlo en orden y probar cada ejemplo en tu propio entorno.

---

## 📋 Tabla de Contenidos

1. [¿Qué es un Condicional?](#1--qué-es-un-condicional)
2. [Tipos de Bucles en Python](#2--tipos-de-bucles-en-python)
3. [Listas por Comprensión](#3--listas-por-comprensión-en-python)
4. [Argumentos en Python](#4--qué-es-un-argumento-en-python)
5. [Funciones Lambda](#5--qué-es-una-función-lambda-en-python)
6. [Paquetes pip](#6--qué-es-un-paquete-pip)
7. [Ejercicios Prácticos](#7--ejercicios-prácticos)

---

## 1. 🔀 ¿Qué es un Condicional?

### Definición

Un **condicional** es una estructura de control que permite que un programa **tome decisiones** en función de si una condición es verdadera (`True`) o falsa (`False`). Es la base de la lógica en cualquier programa: "Si esto ocurre → haz esto. De lo contrario → haz esto otro."

En Python, los condicionales se construyen con las palabras reservadas `if`, `elif` y `else`.

---

### 🧠 ¿Para qué sirven?

- Validar datos antes de procesarlos
- Controlar el flujo del programa según las entradas del usuario
- Comparar valores y ejecutar diferentes bloques de código
- Implementar lógica de negocio (ej.: si el usuario es mayor de edad, mostrar contenido restringido)

---

### 🔤 Sintaxis básica

```python
if condicion:
    # Bloque que se ejecuta si la condición es True
elif otra_condicion:
    # Bloque que se ejecuta si la segunda condición es True
else:
    # Bloque que se ejecuta si ninguna condición fue True
```

> ⚠️ **Importante:** Python usa **indentación** (espacios o tabulaciones) para definir los bloques de código. No usa llaves `{}` como otros lenguajes.

---

### 📌 Ejemplo 1 — Condicional simple (`if`)

```python
edad = 20

if edad >= 18:
    print("Eres mayor de edad.")
```

**Salida:**
```
Eres mayor de edad.
```

---

### 📌 Ejemplo 2 — Condicional con alternativa (`if / else`)

```python
temperatura = 15

if temperatura >= 25:
    print("Hace calor, usa ropa ligera.")
else:
    print("Hace frío, lleva un abrigo.")
```

**Salida:**
```
Hace frío, lleva un abrigo.
```

---

### 📌 Ejemplo 3 — Múltiples condiciones (`if / elif / else`)

```python
nota = 75

if nota >= 90:
    print("Calificación: Sobresaliente")
elif nota >= 75:
    print("Calificación: Notable")
elif nota >= 60:
    print("Calificación: Aprobado")
else:
    print("Calificación: Reprobado")
```

**Salida:**
```
Calificación: Notable
```

---

### 📌 Ejemplo 4 — Condicionales anidados

```python
usuario = "admin"
contrasena = "1234"

if usuario == "admin":
    if contrasena == "1234":
        print("Acceso concedido.")
    else:
        print("Contraseña incorrecta.")
else:
    print("Usuario no encontrado.")
```

---

### 📌 Ejemplo 5 — Operadores lógicos en condicionales

Podemos combinar condiciones con `and`, `or` y `not`:

```python
edad = 25
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puede conducir.")
else:
    print("No puede conducir.")
```

| Operador | Significado                            | Ejemplo                  |
|----------|----------------------------------------|--------------------------|
| `and`    | Ambas condiciones deben ser verdaderas | `x > 0 and x < 10`       |
| `or`     | Al menos una condición debe ser True   | `x < 0 or x > 100`       |
| `not`    | Niega la condición                     | `not x > 5`              |

---

### 📌 Ejemplo 6 — Condicional en una línea (Ternario)

Python permite escribir condicionales simples en una sola línea:

```python
# Sintaxis: valor_si_true if condicion else valor_si_false
x = 10
resultado = "positivo" if x > 0 else "negativo"
print(resultado)  # positivo
```

---

### 🔁 Operadores de Comparación

| Operador | Significado        | Ejemplo    |
|----------|--------------------|------------|
| `==`     | Igual a            | `x == 5`   |
| `!=`     | Distinto de        | `x != 5`   |
| `>`      | Mayor que          | `x > 5`    |
| `<`      | Menor que          | `x < 5`    |
| `>=`     | Mayor o igual que  | `x >= 5`   |
| `<=`     | Menor o igual que  | `x <= 5`   |

---

## 2. 🔄 Tipos de Bucles en Python

### Definición

Un **bucle** (o *loop*) es una estructura de control que permite **repetir un bloque de código** múltiples veces. Se usa cuando queremos ejecutar la misma acción sobre una colección de datos, o mientras se cumpla una determinada condición.

Python tiene **dos tipos principales de bucles:**

1. **`for`** — itera sobre una secuencia de elementos
2. **`while`** — se repite mientras una condición sea verdadera

---

### 🧠 ¿Por qué son útiles?

- Evitan la repetición manual de código
- Permiten recorrer listas, cadenas, diccionarios, etc.
- Son esenciales para procesar grandes volúmenes de datos
- Automatizan tareas repetitivas (enviar correos, generar reportes, etc.)

---

### 🔁 Bucle `for`

El bucle `for` itera sobre cualquier **secuencia iterable**: listas, tuplas, cadenas, rangos, diccionarios, etc.

#### Sintaxis:
```python
for variable in secuencia:
    # Código a ejecutar en cada iteración
```

#### Ejemplo 1 — Iterar sobre una lista:
```python
frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(fruta)
```
**Salida:**
```
manzana
banana
naranja
```

#### Ejemplo 2 — Iterar con `range()`:

La función `range()` genera una secuencia de números. Es muy usada con `for`.

```python
# range(inicio, fin, paso)
for i in range(1, 6):
    print(f"Número: {i}")
```
**Salida:**
```
Número: 1
Número: 2
Número: 3
Número: 4
Número: 5
```

> 📝 **Nota:** `range(1, 6)` genera números del 1 al 5. El valor final (`6`) **no se incluye**.

#### Ejemplo 3 — Iterar sobre una cadena de texto:
```python
for letra in "Python":
    print(letra)
```
**Salida:**
```
P
y
t
h
o
n
```

#### Ejemplo 4 — `for` con `enumerate()` (índice y valor):
```python
colores = ["rojo", "verde", "azul"]

for indice, color in enumerate(colores):
    print(f"Índice {indice}: {color}")
```
**Salida:**
```
Índice 0: rojo
Índice 1: verde
Índice 2: azul
```

---

### 🔁 Bucle `while`

El bucle `while` se ejecuta **mientras** una condición sea verdadera. Se usa cuando **no sabemos de antemano cuántas veces** necesitamos repetir el bloque.

#### Sintaxis:
```python
while condicion:
    # Código a ejecutar mientras la condición sea True
```

#### Ejemplo 1 — Contador básico:
```python
contador = 1

while contador <= 5:
    print(f"Iteración número: {contador}")
    contador += 1
```
**Salida:**
```
Iteración número: 1
Iteración número: 2
Iteración número: 3
Iteración número: 4
Iteración número: 5
```

#### Ejemplo 2 — Validación de entrada del usuario:
```python
contrasena = ""

while contrasena != "secreto":
    contrasena = input("Escribe la contraseña: ")

print("Contraseña correcta. ¡Bienvenido!")
```

> ⚠️ **Cuidado con los bucles infinitos:** Si la condición del `while` nunca se vuelve `False`, el programa se ejecutará para siempre. Asegúrate siempre de tener una condición de salida.

---

### 🛑 Palabras clave de control en bucles

| Palabra clave | Función                                           |
|---------------|---------------------------------------------------|
| `break`       | Termina el bucle inmediatamente                   |
| `continue`    | Salta a la siguiente iteración del bucle          |
| `else`        | Se ejecuta cuando el bucle termina sin `break`    |

#### Ejemplo — `break`:
```python
for numero in range(1, 10):
    if numero == 5:
        print("Encontrado el 5, deteniendo.")
        break
    print(numero)
```

#### Ejemplo — `continue`:
```python
for numero in range(1, 8):
    if numero % 2 == 0:
        continue  # Salta los números pares
    print(numero)
```
**Salida:**
```
1
3
5
7
```

---

### 📊 Comparativa: `for` vs `while`

| Característica        | `for`                              | `while`                                |
|-----------------------|------------------------------------|----------------------------------------|
| Uso principal         | Recorrer una secuencia conocida    | Repetir mientras una condición se cumpla |
| Número de iteraciones | Determinado por la secuencia       | Puede ser indefinido                   |
| Riesgo de loop infinito | No                              | Sí, si no se actualiza la condición    |
| Más común en          | Listas, rangos, archivos           | Validaciones, esperas, juegos          |

---

## 3. 📝 Listas por Comprensión en Python

### Definición

Una **lista por comprensión** (*list comprehension*) es una forma **concisa y elegante** de crear listas en Python. Permite construir una lista nueva a partir de otra secuencia, aplicando una expresión y opcionalmente un filtro, **todo en una sola línea**.

---

### 🧠 ¿Para qué sirven?

- Crear listas de manera rápida y legible
- Filtrar elementos de una lista
- Transformar los elementos de una lista
- Reemplazar bucles `for` simples con una sintaxis más limpia

---

### 🔤 Sintaxis

```python
nueva_lista = [expresion for elemento in iterable if condicion]
```

| Parte           | Descripción                                              | Obligatorio |
|-----------------|----------------------------------------------------------|-------------|
| `expresion`     | Qué hacer con cada elemento (puede transformarlo)        | ✅ Sí       |
| `for ... in ...`| Itera sobre el iterable                                  | ✅ Sí       |
| `if condicion`  | Filtra los elementos (solo incluye los que cumplen)      | ❌ Opcional |

---

### 📌 Ejemplo 1 — Sin comprensión vs. Con comprensión

**Versión tradicional (con bucle `for`):**
```python
cuadrados = []
for n in range(1, 6):
    cuadrados.append(n ** 2)
print(cuadrados)
# [1, 4, 9, 16, 25]
```

**Versión con lista por comprensión:**
```python
cuadrados = [n ** 2 for n in range(1, 6)]
print(cuadrados)
# [1, 4, 9, 16, 25]
```

> ✅ ¡Ambas hacen lo mismo, pero la segunda es mucho más compacta!

---

### 📌 Ejemplo 2 — Filtrar elementos (con condición `if`)

```python
# Obtener solo los números pares del 1 al 20
pares = [n for n in range(1, 21) if n % 2 == 0]
print(pares)
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

---

### 📌 Ejemplo 3 — Transformar texto

```python
nombres = ["ana", "carlos", "maria", "pedro"]
nombres_mayusculas = [nombre.upper() for nombre in nombres]
print(nombres_mayusculas)
# ['ANA', 'CARLOS', 'MARIA', 'PEDRO']
```

---

### 📌 Ejemplo 4 — Con condición `if/else`

Cuando usamos `if/else` en la **expresión** (no al final), ambas ramas se aplican a cada elemento:

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
resultado = ["par" if n % 2 == 0 else "impar" for n in numeros]
print(resultado)
# ['impar', 'par', 'impar', 'par', 'impar', 'par', 'impar', 'par']
```

---

### 📌 Ejemplo 5 — Lista de comprensión anidada (matrices)

```python
# Crear una matriz 3x3
matriz = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matriz)
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

---

### 📌 Ejemplo 6 — Aplicación práctica: filtrar correos válidos

```python
emails = ["ana@gmail.com", "sinformato", "pedro@hotmail.com", "invalido"]
emails_validos = [e for e in emails if "@" in e]
print(emails_validos)
# ['ana@gmail.com', 'pedro@hotmail.com']
```

---

### 💡 ¿Cuándo NO usar lista por comprensión?

- Cuando la lógica es muy compleja (mejor usar un `for` normal para mayor legibilidad)
- Cuando hay múltiples niveles de anidamiento que dificultan la lectura
- Cuando necesitas efectos secundarios (como imprimir durante la iteración)

---

## 4. 📦 ¿Qué es un Argumento en Python?

### Definición

Un **argumento** es un valor que se **pasa a una función** cuando esta es llamada. Los argumentos permiten que las funciones sean flexibles y reutilizables, ya que pueden operar sobre distintos datos cada vez que se invocan.

---

### 🧠 Terminología: Parámetro vs. Argumento

| Término       | Definición                                                  | Ejemplo                    |
|---------------|-------------------------------------------------------------|----------------------------|
| **Parámetro** | Variable definida en la declaración de la función           | `def saludar(nombre):`     |
| **Argumento** | Valor real que se pasa cuando se llama la función           | `saludar("Migue")`         |

En la práctica, ambos términos se usan indistintamente.

---

### 🔤 Sintaxis básica

```python
def nombre_funcion(parametro1, parametro2):
    # cuerpo de la función
    return resultado

# Llamada con argumentos:
nombre_funcion(argumento1, argumento2)
```

---

### 📌 Tipos de Argumentos

Python ofrece varios tipos de argumentos para darle mayor flexibilidad a las funciones:

---

#### 🔹 1. Argumentos Posicionales

Se pasan en el **mismo orden** en que están definidos los parámetros.

```python
def presentar(nombre, ciudad):
    print(f"Hola, soy {nombre} y soy de {ciudad}.")

presentar("Migue", "Santo Domingo")
# Hola, soy Migue y soy de Santo Domingo.
```

---

#### 🔹 2. Argumentos con Nombre (Keyword Arguments)

Se pasan indicando explícitamente el nombre del parámetro. El **orden no importa**.

```python
def presentar(nombre, ciudad):
    print(f"Hola, soy {nombre} y soy de {ciudad}.")

presentar(ciudad="Madrid", nombre="Carlos")
# Hola, soy Carlos y soy de Madrid.
```

---

#### 🔹 3. Argumentos con Valor por Defecto (Default Arguments)

Se define un valor predeterminado para el parámetro. Si no se pasa ningún argumento, se usa el valor por defecto.

```python
def saludar(nombre, saludo="¡Hola"):
    print(f"{saludo}, {nombre}!")

saludar("Ana")            # ¡Hola, Ana!
saludar("Pedro", "Buenos días")  # Buenos días, Pedro!
```

> ⚠️ Los parámetros con valor por defecto **siempre deben ir al final** de la lista de parámetros.

---

#### 🔹 4. Argumentos Variables — `*args`

Permite pasar un **número indefinido de argumentos posicionales**. Se reciben como una **tupla**.

```python
def sumar_todos(*numeros):
    total = sum(numeros)
    print(f"La suma es: {total}")

sumar_todos(1, 2, 3)        # La suma es: 6
sumar_todos(5, 10, 15, 20)  # La suma es: 50
```

---

#### 🔹 5. Argumentos de Palabras Clave Variables — `**kwargs`

Permite pasar un **número indefinido de argumentos con nombre**. Se reciben como un **diccionario**.

```python
def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Migue", ciudad="Madrid", profesion="Desarrolladora")
```
**Salida:**
```
nombre: Migue
ciudad: Madrid
profesion: Desarrolladora
```

---

### 📌 Resumen Visual de Tipos de Argumentos

```python
def funcion(a, b=10, *args, **kwargs):
    pass

# a       → posicional (obligatorio)
# b=10    → con valor por defecto
# *args   → múltiples argumentos posicionales (tupla)
# **kwargs → múltiples argumentos con nombre (diccionario)
```

---

## 5. λ ¿Qué es una Función Lambda en Python?

### Definición

Una **función lambda** es una función **anónima** (sin nombre) que se define en una sola línea. Se usa para crear funciones pequeñas y simples de manera rápida, especialmente cuando la función se va a usar una sola vez o como argumento de otra función.

El nombre "lambda" proviene del **cálculo lambda**, una rama de la matemática/lógica computacional.

---

### 🧠 ¿Para qué sirven?

- Crear funciones cortas y temporales sin necesidad de `def`
- Usarlas como argumentos en funciones como `sorted()`, `map()`, `filter()`
- Escribir código más conciso cuando la lógica es simple

---

### 🔤 Sintaxis

```python
lambda argumentos: expresion
```

| Parte          | Descripción                                        |
|----------------|----------------------------------------------------|
| `lambda`       | Palabra clave que define la función anónima        |
| `argumentos`   | Parámetros de entrada (puede haber varios)         |
| `expresion`    | Lo que calcula y retorna (solo **una expresión**)  |

> ⚠️ Una función lambda **solo puede contener una expresión**. No admite múltiples líneas, `if/else` complejo, ni declaraciones como `print()` dentro.

---

### 📌 Ejemplo 1 — Lambda básica

**Función normal:**
```python
def cuadrado(x):
    return x ** 2

print(cuadrado(5))  # 25
```

**Equivalente con lambda:**
```python
cuadrado = lambda x: x ** 2
print(cuadrado(5))  # 25
```

---

### 📌 Ejemplo 2 — Lambda con múltiples argumentos

```python
multiplicar = lambda a, b: a * b
print(multiplicar(4, 7))  # 28
```

---

### 📌 Ejemplo 3 — Lambda con `sorted()` (ordenar)

```python
personas = [
    {"nombre": "Carlos", "edad": 30},
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Pedro", "edad": 35}
]

# Ordenar por edad usando una lambda
ordenados = sorted(personas, key=lambda p: p["edad"])
for p in ordenados:
    print(p["nombre"], "-", p["edad"])
```
**Salida:**
```
Ana - 25
Carlos - 30
Pedro - 35
```

---

### 📌 Ejemplo 4 — Lambda con `map()` (transformar)

`map()` aplica una función a cada elemento de una lista.

```python
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)  # [1, 4, 9, 16, 25]
```

---

### 📌 Ejemplo 5 — Lambda con `filter()` (filtrar)

`filter()` filtra los elementos de una lista según una condición.

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6, 8, 10]
```

---

### 📊 Lambda vs. Función `def`

| Característica           | `def`                          | `lambda`                       |
|--------------------------|--------------------------------|--------------------------------|
| Nombre                   | Tiene nombre                   | Anónima                        |
| Líneas de código         | Múltiples                      | Solo una línea                 |
| Declaraciones permitidas | Todas (`if`, `for`, `print`…)  | Solo una expresión             |
| Retorno                  | Requiere `return`              | Implícito (retorna la expr.)   |
| Reutilización            | Alta (puede llamarse por nombre) | Baja (generalmente desechable)|
| Legibilidad              | Alta para lógica compleja      | Alta para lógica muy simple    |

---

### 💡 Cuándo usar lambda

✅ **Úsala cuando:**
- La función es muy corta (una expresión)
- Solo la vas a usar una vez (ej.: como argumento de `sorted`, `map`, `filter`)
- Quieres escribir código más compacto

❌ **Evítala cuando:**
- La lógica es compleja
- Necesitas reutilizar la función en varios lugares
- La legibilidad del código se ve afectada

---

## 6. 📦 ¿Qué es un Paquete pip?

### Definición

**pip** (*Pip Installs Packages*) es el **gestor de paquetes oficial de Python**. Permite instalar, actualizar y eliminar **bibliotecas externas** (paquetes) que otros desarrolladores han creado y publicado en el repositorio oficial de Python: **PyPI** (*Python Package Index*).

> 🌐 PyPI se encuentra en: [https://pypi.org](https://pypi.org) — cuenta con más de **500,000 paquetes disponibles**.

---

### 🧠 ¿Para qué sirve pip?

- Instalar librerías de terceros (ej.: `requests`, `pandas`, `flask`, `numpy`)
- Gestionar versiones de paquetes en un proyecto
- Compartir dependencias con otros desarrolladores a través de `requirements.txt`
- Desinstalar o actualizar paquetes instalados

---

### 🔤 Comandos esenciales de pip

#### ✅ Verificar que pip está instalado:
```bash
pip --version
# Salida: pip 23.x.x from /usr/local/lib/python3.x/...
```

#### ✅ Instalar un paquete:
```bash
pip install nombre_paquete
```
**Ejemplo:**
```bash
pip install requests
```

#### ✅ Instalar una versión específica:
```bash
pip install requests==2.28.0
```

#### ✅ Actualizar un paquete:
```bash
pip install --upgrade nombre_paquete
```

#### ✅ Desinstalar un paquete:
```bash
pip uninstall nombre_paquete
```

#### ✅ Ver todos los paquetes instalados:
```bash
pip list
```

#### ✅ Buscar información sobre un paquete:
```bash
pip show nombre_paquete
```

---

### 📄 Archivo `requirements.txt`

El archivo `requirements.txt` es un estándar en proyectos Python. Lista todas las dependencias del proyecto para que cualquier desarrollador pueda instalarlas de una vez.

**Ejemplo de `requirements.txt`:**
```
requests==2.28.0
flask==2.2.3
pandas==1.5.3
numpy==1.24.0
```

**Instalar todas las dependencias del archivo:**
```bash
pip install -r requirements.txt
```

**Generar el archivo automáticamente:**
```bash
pip freeze > requirements.txt
```

---

### 🌟 Paquetes populares y sus usos

| Paquete       | Categoría              | ¿Para qué sirve?                                  |
|---------------|------------------------|---------------------------------------------------|
| `requests`    | Web / HTTP             | Hacer peticiones HTTP a APIs y sitios web         |
| `flask`       | Web Framework          | Crear aplicaciones web y APIs REST                |
| `django`      | Web Framework          | Framework web completo para apps robustas         |
| `pandas`      | Análisis de datos      | Manipulación de datos y DataFrames                |
| `numpy`       | Computación científica | Operaciones matemáticas y arrays multidimensionales|
| `matplotlib`  | Visualización          | Crear gráficos y visualizaciones                  |
| `pillow`      | Imágenes               | Procesar y manipular imágenes                     |
| `sqlalchemy`  | Base de datos          | ORM para interactuar con bases de datos           |
| `pytest`      | Testing                | Escribir y ejecutar pruebas unitarias             |
| `openai`      | Inteligencia Artificial| Interactuar con la API de OpenAI (ChatGPT, etc.)  |

---

### 📌 Ejemplo completo — Instalar y usar `requests`

```bash
# 1. Instalar el paquete
pip install requests
```

```python
# 2. Importar y usar en Python
import requests

respuesta = requests.get("https://api.github.com")
print(respuesta.status_code)   # 200
print(respuesta.json())        # Datos del API de GitHub
```

---

### 🔒 Entornos Virtuales (recomendación)

Para evitar conflictos entre proyectos, se recomienda usar **entornos virtuales**. Esto permite que cada proyecto tenga sus propias versiones de paquetes.

```bash
# Crear entorno virtual
python -m venv mi_entorno

# Activar (Windows)
mi_entorno\Scripts\activate

# Activar (Mac/Linux)
source mi_entorno/bin/activate

# Instalar paquetes dentro del entorno
pip install flask

# Desactivar el entorno
deactivate
```

---

## 7. 💻 Ejercicios Prácticos

> Los siguientes ejercicios están disponibles en el archivo `ejercicios_checkpoint5.py`.

---

### Ejercicio 1 — Bucle `for` en Python

```python
# Ejercicio 1: Bucle for
# Recorre una lista de lenguajes de programación e imprime cada uno

lenguajes = ["Python", "JavaScript", "Java", "C++", "TypeScript"]

print("=== Lenguajes de Programación ===")
for lenguaje in lenguajes:
    print(f"→ {lenguaje}")
```

**Salida:**
```
=== Lenguajes de Programación ===
→ Python
→ JavaScript
→ Java
→ C++
→ TypeScript
```

---

### Ejercicio 2 — Función `suma` con 3 argumentos

```python
# Ejercicio 2: Función que suma 3 argumentos

def suma(a, b, c):
    """
    Toma tres números como argumentos y devuelve su suma.
    
    Parámetros:
    a (int/float): Primer número
    b (int/float): Segundo número
    c (int/float): Tercer número
    
    Retorna:
    int/float: La suma de los tres números
    """
    return a + b + c

# Pruebas
print(suma(5, 10, 15))    # 30
print(suma(1.5, 2.5, 3))  # 7.0
print(suma(100, 200, 300)) # 600
```

---

### Ejercicio 3 — Función Lambda equivalente a `suma`

```python
# Ejercicio 3: Lambda equivalente a la función suma

suma_lambda = lambda a, b, c: a + b + c

# Pruebas
print(suma_lambda(5, 10, 15))     # 30
print(suma_lambda(1.5, 2.5, 3))   # 7.0
print(suma_lambda(100, 200, 300))  # 600
```

---

### Ejercicio 4 — Verificar si un nombre está en la lista

```python
# Ejercicio 4: Verificar si el nombre está en la lista

nombre = 'Enrique'
lista_nombres = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

encontrado = False

for n in lista_nombres:
    if nombre == n:
        encontrado = True
        break

if encontrado:
    print(f"✅ El nombre '{nombre}' SÍ se encuentra en la lista.")
else:
    print(f"❌ El nombre '{nombre}' NO se encuentra en la lista.")

# Versión simplificada usando el operador 'in':
if nombre in lista_nombres:
    print(f"✅ (Versión simplificada) '{nombre}' está en la lista.")
else:
    print(f"❌ (Versión simplificada) '{nombre}' no está en la lista.")
```

**Salida:**
```
❌ El nombre 'Enrique' NO se encuentra en la lista.
❌ (Versión simplificada) 'Enrique' no está en la lista.
```

> 💡 **Nota:** El nombre `'Enrique'` **no** está en la lista, pero `'Henry'` sí. Son nombres distintos. La búsqueda es sensible a mayúsculas/minúsculas.

---

## 📚 Referencias y Recursos Adicionales

| Recurso                               | URL                                       |
|---------------------------------------|-------------------------------------------|
| Documentación oficial de Python       | https://docs.python.org/3/               |
| PyPI - Repositorio de paquetes        | https://pypi.org                          |
| Tutorial Python en español (W3Schools)| https://www.w3schools.com/python/        |
| Real Python (tutoriales avanzados)    | https://realpython.com                   |
| Python Tutor (visualizador de código) | https://pythontutor.com                  |

---

## ✍️ Sobre esta documentación

**Autora:** Miguelina Rosario  
**Empresa:** Open Consultech  
**Repositorio:** [github.com/migueross/checkpoint5-python](https://github.com/migueross)  
**Versión:** 1.0 — Marzo 2026  
**Licencia:** Documentación interna para uso educativo

---

*"El mejor código es el que se puede leer como prosa." — Robert C. Martin*
