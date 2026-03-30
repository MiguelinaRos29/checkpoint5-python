# Checkpoint 5 - Documentación básica de Python

## Introducción

En este documento explico varios conceptos básicos de Python de forma sencilla. La idea es que una persona que está empezando en programación pueda entender qué significa cada concepto, para qué sirve y ver algún ejemplo práctico.

---

## 1. ¿Qué es un condicional?

Un condicional es una estructura que permite tomar decisiones dentro de un programa.  
Sirve para ejecutar una acción si se cumple una condición y otra distinta si no se cumple.

En Python se usan principalmente estas palabras:

- `if`
- `elif`
- `else`

### Sintaxis básica

```python
if condicion:
    # código si se cumple
elif otra_condicion:
    # otra opción
else:
    # si no se cumple nada
```

### ¿Para qué sirve?

Los condicionales se usan para:

- comparar valores  
- validar datos  
- controlar el flujo del programa  
- responder de forma distinta según una situación  

### Ejemplo

```python
edad = 20

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

### Explicación

Si la variable `edad` es mayor o igual que 18, muestra un mensaje.  
Si no, muestra el otro.

---

## 2. Bucles en Python

Los bucles sirven para repetir un bloque de código varias veces.

### Tipos de bucles

- `for`
- `while`

---

### Bucle for

Se usa para recorrer elementos.

```python
frutas = ["manzana", "pera", "uva"]

for fruta in frutas:
    print(fruta)
```

 Recorre la lista e imprime cada elemento.

---

### Bucle while

Se usa mientras se cumpla una condición.

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
```

 Se repite hasta que deja de cumplirse la condición.

---

### ¿Por qué son útiles?

- ahorran tiempo  
- evitan repetir código  
- permiten recorrer datos  
- automatizan tareas  

---

## 3. Lista por comprensión

Es una forma rápida de crear listas.

### Sintaxis

```python
[nueva_expresion for elemento in secuencia]
```

### Ejemplo

```python
numeros = [1, 2, 3, 4, 5]
cuadrados = [n**2 for n in numeros]

print(cuadrados)
```

Resultado:

```
[1, 4, 9, 16, 25]
```

---

## 4. Argumentos en Python

Un argumento es un valor que se pasa a una función.

### Ejemplo

```python
def saludar(nombre):
    print("Hola", nombre)

saludar("Ana")
```

 `"Ana"` es el argumento.

---

## 5. Función lambda

Es una función corta y sin nombre.

```python
suma = lambda a, b: a + b
print(suma(4, 6))
```

---

## 6. Paquete pip

`pip` es el gestor de paquetes de Python.

Sirve para instalar librerías.

### Ejemplo

```bash
pip install requests
```

---

## Conclusión

- Condicionales → decisiones  
- Bucles → repetición  
- Listas → creación rápida  
- Argumentos → datos en funciones  
- Lambda → funciones simples  
- pip → instalar paquetes  

Estos conceptos son la base de Python.