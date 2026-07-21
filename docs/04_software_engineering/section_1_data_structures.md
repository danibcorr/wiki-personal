---
authors: Daniel Bazo Correa
description: Pilas, colas, listas enlazadas y árboles binarios de búsqueda.
title: Estructuras de datos
---

Este capítulo presenta las estructuras de datos fundamentales, describiendo su
organización interna, sus operaciones principales y una implementación de referencia en
Python. El análisis de la complejidad de estas operaciones se apoya en la notación Big
O, que se aborda en el capítulo de [algoritmos](section_2_algorithms.md).

## Pilas

Una pila es una estructura de datos que organiza elementos de manera secuencial
siguiendo el principio LIFO (_Last In, First Out_). El último elemento añadido es el
primero en ser retirado. Las operaciones principales son apilar (_push_) y desapilar
(_pop_).

???+ tip "Implementación"

    ```python linenums="1"
    class Pila:
        def __init__(self, capacidad: int | None = None) -> None:
            self.elementos: list[int] = []
            self.capacidad: int | None = capacidad

        def esta_vacia(self) -> bool:
            return len(self.elementos) == 0

        def push(self, elem: int) -> None:
            if self.capacidad is not None and len(self.elementos) >= self.capacidad:
                raise OverflowError("Pila llena.")
            self.elementos.append(elem)

        def pop(self) -> int:
            if self.esta_vacia():
                raise IndexError("Pila vacía.")
            return self.elementos.pop()

        def top(self) -> int:
            if self.esta_vacia():
                raise IndexError("Pila vacía.")
            return self.elementos[-1]

        def size(self) -> int:
            return len(self.elementos)
    ```

## Colas

Una cola es una estructura de datos que organiza elementos de manera secuencial bajo el
principio FIFO (_First In, First Out_). Las operaciones de inserción se realizan en un
extremo y las de extracción en el otro.

???+ tip "Implementación"

    ```python linenums="1"
    from collections import deque

    class Cola:
        def __init__(self, capacidad: int | None = None) -> None:
            self.elementos: deque[int] = deque()
            self.capacidad: int | None = capacidad

        def esta_vacia(self) -> bool:
            return len(self.elementos) == 0

        def insertar(self, elem: int) -> None:
            if self.capacidad is not None and len(self.elementos) >= self.capacidad:
                raise OverflowError("Cola llena.")
            self.elementos.append(elem)

        def eliminar(self) -> int:
            if self.esta_vacia():
                raise IndexError("Cola vacía.")
            return self.elementos.popleft()

        def frente(self) -> int:
            if self.esta_vacia():
                raise IndexError("Cola vacía.")
            return self.elementos[0]

        def size(self) -> int:
            return len(self.elementos)
    ```

## Listas enlazadas

Las listas enlazadas son estructuras de datos donde cada elemento (nodo) contiene un
valor y un puntero al siguiente nodo. A diferencia de los _arrays_, el acceso a
elementos se realiza recorriendo los enlaces secuencialmente.

???+ tip "Implementación"

    ```python linenums="1"
    from typing import Self

    class Nodo:
        def __init__(self, dato: int) -> None:
            self.dato: int = dato
            self.siguiente: Self | None = None

    class ListaEnlazada:
        def __init__(self) -> None:
            self.cabeza: Nodo | None = None
            self.cola: Nodo | None = None

        def esta_vacia(self) -> bool:
            return self.cabeza is None

        def insertar_final(self, dato: int) -> None:
            nuevo_nodo = Nodo(dato)
            if self.esta_vacia():
                self.cabeza = self.cola = nuevo_nodo
            else:
                self.cola.siguiente = nuevo_nodo
                self.cola = nuevo_nodo

        def insertar_principio(self, dato: int) -> None:
            nuevo_nodo = Nodo(dato)
            if self.esta_vacia():
                self.cabeza = self.cola = nuevo_nodo
            else:
                nuevo_nodo.siguiente = self.cabeza
                self.cabeza = nuevo_nodo

        def eliminar_primero(self) -> int:
            if self.esta_vacia():
                raise IndexError("Lista vacía.")
            dato: int = self.cabeza.dato
            if self.cabeza is self.cola:
                self.cabeza = self.cola = None
            else:
                self.cabeza = self.cabeza.siguiente
            return dato

        def recorrido(self) -> None:
            nodo: Nodo | None = self.cabeza
            while nodo is not None:
                print(nodo.dato)
                nodo = nodo.siguiente
    ```

## Listas doblemente enlazadas

Una lista doblemente enlazada consta de nodos donde cada uno tiene dos enlaces: uno al
siguiente nodo y otro al anterior. Esta estructura permite recorrer la lista en ambos
sentidos.

???+ tip "Implementación"

    ```python linenums="1"
    from typing import Self

    class Nodo:
        def __init__(self, dato: int) -> None:
            self.dato: int = dato
            self.siguiente: Self | None = None
            self.anterior: Self | None = None

    class ListaDobleEnlazada:
        def __init__(self) -> None:
            self.cabeza: Nodo | None = None
            self.cola: Nodo | None = None

        def esta_vacia(self) -> bool:
            return self.cabeza is None

        def insertar_final(self, dato: int) -> None:
            nuevo_nodo = Nodo(dato)
            if self.esta_vacia():
                self.cabeza = self.cola = nuevo_nodo
            else:
                self.cola.siguiente = nuevo_nodo
                nuevo_nodo.anterior = self.cola
                self.cola = nuevo_nodo

        def insertar_principio(self, dato: int) -> None:
            nuevo_nodo = Nodo(dato)
            if self.esta_vacia():
                self.cabeza = self.cola = nuevo_nodo
            else:
                nuevo_nodo.siguiente = self.cabeza
                self.cabeza.anterior = nuevo_nodo
                self.cabeza = nuevo_nodo

        def eliminar_ultimo(self) -> int:
            if self.esta_vacia():
                raise IndexError("Lista vacía.")
            dato: int = self.cola.dato
            if self.cabeza is self.cola:
                self.cabeza = self.cola = None
            else:
                self.cola = self.cola.anterior
                self.cola.siguiente = None
            return dato

        def eliminar_primero(self) -> int:
            if self.esta_vacia():
                raise IndexError("Lista vacía.")
            dato: int = self.cabeza.dato
            if self.cabeza is self.cola:
                self.cabeza = self.cola = None
            else:
                self.cabeza = self.cabeza.siguiente
                self.cabeza.anterior = None
            return dato
    ```

## Árboles binarios de búsqueda

Un árbol binario de búsqueda es una estructura de datos en la que cada nodo puede tener
como máximo dos descendientes (hijo izquierdo e hijo derecho). El valor del hijo
izquierdo es siempre menor que el del nodo padre, y el del hijo derecho es siempre
mayor. Esta propiedad permite búsquedas eficientes con complejidad $O(\log N)$ en el
caso promedio.

Los tres tipos de recorrido principales son:

- **En orden (_inorder_)**: Hijo izquierdo, raíz, hijo derecho. Produce los elementos
  ordenados.
- **En preorden (_preorder_)**: Raíz, hijo izquierdo, hijo derecho.
- **En postorden (_postorder_)**: Hijo izquierdo, hijo derecho, raíz.

???+ tip "Implementación"

    ```python linenums="1"
    from typing import Self

    class Nodo:
        def __init__(self, valor: int) -> None:
            self.valor: int = valor
            self.izquierdo: Self | None = None
            self.derecho: Self | None = None

    class ArbolBinario:
        def __init__(self) -> None:
            self.raiz: Nodo | None = None

        def insertar(self, valor: int) -> None:
            if self.raiz is None:
                self.raiz = Nodo(valor)
            else:
                self._insertar_recursivo(self.raiz, valor)

        def _insertar_recursivo(self, nodo: Nodo, valor: int) -> None:
            if valor <= nodo.valor:
                if nodo.izquierdo is None:
                    nodo.izquierdo = Nodo(valor)
                else:
                    self._insertar_recursivo(nodo.izquierdo, valor)
            else:
                if nodo.derecho is None:
                    nodo.derecho = Nodo(valor)
                else:
                    self._insertar_recursivo(nodo.derecho, valor)

        def buscar(self, valor: int) -> Nodo | None:
            return self._buscar_recursivo(self.raiz, valor)

        def _buscar_recursivo(self, nodo: Nodo | None, valor: int) -> Nodo | None:
            if nodo is None or nodo.valor == valor:
                return nodo
            if valor < nodo.valor:
                return self._buscar_recursivo(nodo.izquierdo, valor)
            return self._buscar_recursivo(nodo.derecho, valor)

        def inorden(self, nodo: Nodo | None) -> None:
            if nodo is not None:
                self.inorden(nodo.izquierdo)
                print(nodo.valor)
                self.inorden(nodo.derecho)

        def preorden(self, nodo: Nodo | None) -> None:
            if nodo is not None:
                print(nodo.valor)
                self.preorden(nodo.izquierdo)
                self.preorden(nodo.derecho)

        def postorden(self, nodo: Nodo | None) -> None:
            if nodo is not None:
                self.postorden(nodo.izquierdo)
                self.postorden(nodo.derecho)
                print(nodo.valor)
    ```
