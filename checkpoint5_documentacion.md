# Checkpoint 5 - Documentación básica de Python

## Introducción

En este documento se explican algunos conceptos fundamentales de Python de manera clara y detallada. El objetivo no es solo responder brevemente a unas preguntas, sino crear un material que pueda servir de apoyo a personas que están comenzando en programación.

Cuando una persona empieza a aprender Python, necesita algo más que definiciones cortas. Necesita entender qué es cada concepto, para qué sirve, cómo funciona, por qué se utiliza y en qué situaciones aparece. Por eso, en esta documentación se incluye teoría, sintaxis, utilidad y ejemplos sencillos.

Python es un lenguaje muy usado porque su sintaxis es bastante legible y permite aprender programación de una forma más intuitiva. Sin embargo, para avanzar correctamente, es importante dominar bien sus bases.

---

## 1. ¿Qué es un condicional?

Un condicional es una estructura de control que permite al programa tomar decisiones. Gracias a los condicionales, un programa no ejecuta siempre lo mismo, sino que puede actuar de una manera u otra dependiendo de si se cumple una condición.

Dicho de una forma simple, un condicional le permite al programa “preguntar” algo y actuar según la respuesta.

Por ejemplo, un programa puede comprobar si una persona es mayor de edad, si un usuario ha escrito bien una contraseña, si un número es positivo o negativo, o si un producto está disponible en stock.

### ¿Para qué sirve un condicional?

Los condicionales sirven para controlar el flujo del programa. Son muy importantes porque permiten que el programa no sea rígido, sino dinámico. Es decir, permiten adaptar la respuesta del programa a distintas situaciones.

Se utilizan para:

- validar datos introducidos por el usuario  
- comparar valores  
- decidir entre varias opciones  
- controlar acciones diferentes según una condición  
- evitar errores en algunos procesos  

### ¿Por qué son útiles?

Sin condicionales, todos los programas ejecutarían siempre las mismas instrucciones, sin importar lo que ocurra. Gracias a ellos, los programas pueden responder a distintas circunstancias y comportarse de forma más inteligente.

Por ejemplo:

- una app puede dejar entrar o no a un usuario dependiendo de su contraseña  
- un sistema puede mostrar un mensaje diferente según la edad  
- un programa puede comprobar si un número es par o impar  

### Palabras que se usan en Python

En Python los condicionales se construyen principalmente con:

- `if`  
- `elif`  
- `else`  

### ¿Cómo funciona?

El programa evalúa una condición.  
Si la condición es verdadera, ejecuta un bloque de código.  
Si no lo es, puede ejecutar otro bloque diferente.

### Sintaxis básica

```python
if condicion:
    # código que se ejecuta si la condición es verdadera
elif otra_condicion:
    # código que se ejecuta si esta otra condición es verdadera
else:
    # código que se ejecuta si ninguna se cumple
```

### Ejemplo sencillo

```python
edad = 20

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

### Explicación del ejemplo

En este caso, el programa comprueba si la variable `edad` es mayor o igual que 18.

- Si lo es, imprime `Eres mayor de edad`  
- Si no lo es, imprime `Eres menor de edad`  

### Otro ejemplo

```python
nota = 7

if nota >= 9:
    print("Sobresaliente")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")
```

En este ejemplo hay varias posibilidades. El programa no solo toma una decisión entre dos caminos, sino entre varias opciones.

### Conclusión sobre los condicionales

Los condicionales son una de las bases de la programación porque permiten que el programa tome decisiones. Son imprescindibles en casi cualquier aplicación real, ya que ayudan a validar, comparar y responder de forma diferente según la situación.

---

## 2. ¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?

Los bucles son estructuras que permiten repetir un bloque de código varias veces sin tener que escribirlo una y otra vez.

En programación, repetir tareas es algo muy común. Por ejemplo, imprimir varios números, recorrer una lista de nombres, mostrar productos en una tienda online o repetir una acción hasta que el usuario escriba un dato correcto. Para todo eso sirven los bucles.

En Python existen principalmente dos tipos de bucles:

- `for`  
- `while`  

---

### Bucle `for`

El bucle `for` se utiliza para recorrer una secuencia, como por ejemplo una lista, una tupla, una cadena de texto o un rango de números.

Es muy útil cuando sabemos qué elementos queremos recorrer o cuántas veces queremos repetir una acción.

### Sintaxis del bucle `for`

```python
for variable in secuencia:
    # código que se repite
```

### Ejemplo con lista

```python
frutas = ["manzana", "pera", "uva"]

for fruta in frutas:
    print(fruta)
```

### Explicación

Este bucle recorre la lista `frutas` elemento por elemento.  
En cada vuelta, la variable `fruta` toma uno de los valores de la lista y lo imprime.

### Ejemplo con `range()`

```python
for numero in range(1, 6):
    print(numero)
```

### Explicación

Aquí `range(1, 6)` genera una secuencia de números desde 1 hasta 5.  
El 6 no se incluye.  
El bucle va recorriendo esos números y los imprime.

---

### Bucle `while`

El bucle `while` se utiliza para repetir un bloque de código mientras una condición sea verdadera.

A diferencia del `for`, este bucle se usa mucho cuando no sabemos exactamente cuántas veces habrá que repetir algo, pero sí sabemos cuál es la condición que debe cumplirse.

### Sintaxis del bucle `while`

```python
while condicion:
    # código que se repite mientras la condición sea verdadera
```

### Ejemplo

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
```

### Explicación

En este ejemplo, el programa imprime números del 1 al 5.

- Primero `contador` vale 1  
- Mientras sea menor o igual que 5, el bucle sigue ejecutándose  
- En cada vuelta, el contador aumenta en 1  

Si no aumentáramos el contador, el bucle no terminaría nunca. A eso se le llama bucle infinito.

---

### ¿Por qué son útiles los bucles?

Los bucles son muy útiles porque permiten automatizar tareas repetitivas. En vez de escribir varias veces el mismo código, podemos usar un bucle para repetirlo.

Sus beneficios principales son:

- ahorran tiempo  
- hacen el código más limpio  
- evitan repeticiones innecesarias  
- permiten recorrer datos con facilidad  
- ayudan a automatizar procesos  

### Ejemplo práctico de utilidad

Imagina una lista con 100 nombres.  
Sería muy poco práctico escribir 100 instrucciones `print()`.  
Con un bucle, el programa puede recorrer toda la lista automáticamente.

### Diferencia general entre `for` y `while`

- `for` se usa normalmente cuando queremos recorrer una secuencia o cuando sabemos cuántas veces se repetirá algo  
- `while` se usa cuando la repetición depende de una condición y no siempre sabemos cuántas vueltas dará  

### Conclusión sobre los bucles

Los bucles son fundamentales porque permiten repetir acciones de forma automática. Son una herramienta básica para trabajar con listas, cadenas, números y muchos otros elementos en Python.

---

## 3. ¿Qué es una lista por comprensión en Python?

Una lista por comprensión, también llamada *list comprehension*, es una forma breve y elegante de crear listas nuevas a partir de una secuencia o de otra lista.

En lugar de escribir varias líneas con un bucle y luego usar `append()`, Python permite crear listas de forma más compacta.

### ¿Para qué sirve?

Sirve para construir listas de una manera más rápida y clara cuando queremos:

- transformar elementos  
- filtrar valores  
- crear listas nuevas a partir de otras secuencias  

### ¿Por qué es útil?

Es útil porque reduce código y muchas veces hace que una operación sencilla sea más fácil de leer. Sin embargo, debe usarse con sentido. Si una lista por comprensión se vuelve demasiado complicada, puede dejar de ser clara.

### Sintaxis general

```python
[nueva_expresion for elemento in secuencia]
```

### Sintaxis con condición

```python
[nueva_expresion for elemento in secuencia if condicion]
```

### ¿Cómo funciona?

La lista por comprensión recorre los elementos de una secuencia y va construyendo una nueva lista con el resultado.

### Ejemplo básico

```python
numeros = [1, 2, 3, 4, 5]
cuadrados = [n**2 for n in numeros]

print(cuadrados)
```

### Resultado

```python
[1, 4, 9, 16, 25]
```

### Explicación

En este caso, el programa recorre la lista `numeros`.  
Cada número se eleva al cuadrado y se guarda en una nueva lista llamada `cuadrados`.

### Cómo se haría sin lista por comprensión

```python
numeros = [1, 2, 3, 4, 5]
cuadrados = []

for n in numeros:
    cuadrados.append(n**2)

print(cuadrados)
```

Este código hace lo mismo, pero ocupa más líneas.

### Ejemplo con condición

```python
pares = [n for n in range(1, 11) if n % 2 == 0]
print(pares)
```

### Explicación

Aquí se crea una lista con los números pares del 1 al 10.  
La condición `n % 2 == 0` sirve para seleccionar solo los números divisibles entre 2.

### Beneficios de una lista por comprensión

- permite escribir menos código  
- hace más rápida la creación de listas sencillas  
- ayuda a trabajar mejor con datos  
- es muy común en Python y conviene saber leerla y escribirla  

### Conclusión sobre las listas por comprensión

Las listas por comprensión son una herramienta muy útil de Python para crear listas de manera más breve y expresiva. Son especialmente útiles cuando se quiere transformar o filtrar información.

---

## 4. ¿Qué es un argumento en Python?

Un argumento es un valor que se le pasa a una función cuando se la llama para que pueda trabajar con ese dato.

Las funciones se crean para realizar tareas concretas. Muchas veces, para que una función pueda hacer su trabajo, necesita recibir información. Esa información se le entrega mediante argumentos.

### ¿Para qué sirve un argumento?

Los argumentos sirven para que una función sea reutilizable. En vez de crear una función distinta para cada caso, podemos usar la misma función con diferentes datos.

Por ejemplo, una función puede saludar a distintas personas, sumar distintos números o calcular distintos resultados dependiendo de los argumentos que reciba.

### Parámetro y argumento: diferencia

Aunque muchas veces se confunden, no son exactamente lo mismo.

- **Parámetro**: es la variable que aparece en la definición de la función  
- **Argumento**: es el valor real que se pasa cuando se llama a la función  

### Ejemplo sencillo

```python
def saludar(nombre):
    print("Hola", nombre)

saludar("Ana")
```

### Explicación

En este ejemplo:

- `nombre` es el parámetro  
- `"Ana"` es el argumento  

La función recibe el argumento `"Ana"` y lo usa para mostrar el saludo.

### Ejemplo con varios argumentos

```python
def suma(a, b):
    return a + b

resultado = suma(3, 5)
print(resultado)
```

### Explicación

En este caso:

- `a` y `b` son parámetros  
- `3` y `5` son argumentos  

La función toma esos dos valores, los suma y devuelve el resultado.

### ¿Por qué son importantes los argumentos?

Son importantes porque hacen que las funciones sean flexibles. Sin argumentos, las funciones serían muy limitadas y solo servirían para casos muy concretos.

Gracias a los argumentos podemos:

- reutilizar funciones  
- evitar repetir código  
- trabajar con distintos datos  
- hacer programas más dinámicos  

### Tipos básicos de argumentos

A nivel básico, lo más importante es entender que una función puede recibir uno o varios argumentos. Más adelante en Python también existen otros tipos, como argumentos por defecto o argumentos nombrados, pero en una primera toma de contacto basta con comprender la idea principal: pasar valores a una función.

### Conclusión sobre los argumentos

Un argumento es el dato que se envía a una función para que pueda realizar una tarea. Entender los argumentos es esencial porque las funciones son una parte central de la programación en Python.

---

## 5. ¿Qué es una función Lambda en Python?

Una función lambda es una función pequeña y anónima. Se llama anónima porque normalmente no se define con `def` ni necesita tener un nombre como una función tradicional.

Se utiliza para operaciones simples y rápidas, especialmente cuando no compensa crear una función completa.

### ¿Para qué sirve?

Sirve para escribir funciones cortas de una manera más rápida. Son útiles cuando la operación es sencilla y se quiere expresar en una sola línea.

Sin embargo, aunque las funciones lambda son útiles, no conviene abusar de ellas. Si la lógica empieza a ser más larga o más difícil de leer, normalmente es mejor usar una función normal definida con `def`.

### Sintaxis

```python
lambda argumentos: expresion
```

### ¿Cómo funciona?

La función lambda recibe uno o varios argumentos y devuelve el resultado de una única expresión.

### Ejemplo

```python
suma = lambda a, b: a + b
print(suma(4, 6))
```

### Explicación

La lambda recibe dos argumentos, `a` y `b`, y devuelve su suma.

### Equivalencia con una función normal

Función normal:

```python
def suma(a, b):
    return a + b
```

Función lambda equivalente:

```python
lambda a, b: a + b
```

### Diferencias principales con una función normal

Una función lambda:

- suele escribirse en una sola línea  
- se usa para operaciones simples  
- normalmente se emplea en casos concretos y rápidos  

Una función definida con `def`:

- puede tener varias líneas  
- permite una estructura más completa  
- suele ser mejor para lógica más extensa  

### ¿Cuándo se usan?

Se suelen usar mucho con funciones como:

- `map()`  
- `filter()`  
- `sorted()`  

También se usan cuando se necesita una función pequeña de forma puntual.

### Ejemplo sencillo con `sorted()`

```python
personas = [("Ana", 25), ("Luis", 20), ("Marta", 30)]

ordenadas = sorted(personas, key=lambda persona: persona[1])
print(ordenadas)
```

### Explicación

Aquí la lambda se usa para ordenar la lista según la edad, que está en la posición 1 de cada tupla.

### Ventajas de lambda

- permiten escribir menos código  
- son útiles para operaciones breves  
- funcionan bien en contextos concretos  

### Conclusión sobre lambda

Las funciones lambda son una forma compacta de crear funciones simples. No sustituyen a las funciones normales en todos los casos, pero son muy útiles cuando se necesita una operación pequeña y rápida.

---

## 6. ¿Qué es pip en Python?

`pip` es el gestor de paquetes de Python. Su función principal es instalar, actualizar y eliminar paquetes o librerías externas.

En programación, no siempre se escribe todo desde cero. Muchas veces otros desarrolladores ya han creado herramientas que resuelven problemas comunes. Gracias a `pip`, se pueden instalar esas herramientas y utilizarlas en nuestros proyectos.

### ¿Qué es un paquete?

Un paquete es un conjunto de módulos o archivos de Python que ofrecen una funcionalidad concreta.

Por ejemplo, existen paquetes para:

- trabajar con peticiones de internet  
- analizar datos  
- crear aplicaciones web  
- hacer gráficos  
- automatizar tareas  

### ¿Para qué sirve pip?

`pip` sirve para gestionar esos paquetes. Es decir, permite:

- instalar paquetes nuevos  
- actualizar paquetes ya instalados  
- eliminar paquetes  
- ver qué paquetes tenemos en el sistema  

### ¿Por qué es importante?

Es importante porque amplía muchísimo las posibilidades de Python. Gracias a `pip`, un programador puede añadir herramientas listas para usar sin tener que programarlo todo desde cero.

### Ejemplo de instalación

```bash
pip install requests
```

### Explicación

Ese comando instala el paquete `requests`, que se utiliza para hacer peticiones HTTP.

### Otros comandos útiles

Ver paquetes instalados:

```bash
pip list
```

Actualizar un paquete:

```bash
pip install --upgrade requests
```

Desinstalar un paquete:

```bash
pip uninstall requests
```

### Beneficios de usar pip

- ahorra tiempo  
- facilita el trabajo con librerías externas  
- permite ampliar proyectos  
- ayuda a mantener los paquetes actualizados  
- es una herramienta básica en el ecosistema de Python  

### Ejemplo práctico

Si una persona quiere hacer una petición a una página web, podría instalar `requests` con `pip` y luego usarlo en su programa, en lugar de programar toda esa funcionalidad desde cero.

### Conclusión sobre pip

`pip` es una herramienta esencial en Python porque permite instalar y gestionar paquetes externos. Gracias a él, los proyectos pueden crecer y aprovechar librerías muy útiles creadas por otros desarrolladores.

---

## Conclusión general

Todos los conceptos explicados en este documento forman parte de la base de Python y aparecen constantemente al programar.

- Los **condicionales** permiten tomar decisiones.  
- Los **bucles** permiten repetir acciones.  
- Las **listas por comprensión** ayudan a crear listas de forma más breve y eficiente.  
- Los **argumentos** permiten pasar información a las funciones.  
- Las **funciones lambda** sirven para operaciones pequeñas y rápidas.  
- **pip** permite instalar librerías externas para ampliar las capacidades de Python.  

Aprender estos conceptos no solo sirve para aprobar una actividad, sino para construir una base sólida en programación. Cuando estos fundamentos se entienden bien, resulta mucho más fácil avanzar hacia temas más complejos.