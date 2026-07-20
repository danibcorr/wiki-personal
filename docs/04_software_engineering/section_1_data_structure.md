---
authors: Daniel Bazo Correa
description: Notación Big O, algoritmos de ordenación, búsqueda y estructuras de datos.
title: Estructuras de datos y algoritmos
---

Este capítulo aborda la notación Big O para el análisis de complejidad algorítmica, los
métodos clásicos de ordenación y búsqueda, y las estructuras de datos fundamentales.

## Notación Big O

La notación Big O se utiliza para evaluar la eficiencia de los algoritmos en términos de
complejidad temporal y espacial. La **complejidad temporal** describe cómo varía el
tiempo requerido por un algoritmo en función del número de elementos de entrada,
mientras que la **complejidad espacial** describe el uso de memoria en función del
número de variables utilizadas por el algoritmo.

### Órdenes de complejidad

- $O(1)$: El tiempo de ejecución es constante, independientemente del tamaño de la
  entrada. Es típico en algoritmos que acceden a un número fijo de elementos, como
  devolver el primer elemento de una lista.

- $O(\log N)$: El tiempo de ejecución crece logarítmicamente con el tamaño de la
  entrada. Común en algoritmos que dividen el problema a la mitad en cada paso, como la
  búsqueda binaria.

- $O(N)$: El tiempo de ejecución crece linealmente con el tamaño de la entrada. Típico
  de algoritmos que realizan una operación en cada elemento de la entrada, como sumar
  todos los elementos de una lista.

- $O(N \log N)$: Representa una combinación de comportamiento lineal y logarítmico. Es
  común en algoritmos de ordenación eficientes, como _quicksort_.

- $O(N^2)$: El tiempo de ejecución crece cuadráticamente con el tamaño de la entrada. Se
  presenta en algoritmos que realizan operaciones sobre cada par de elementos, como la
  ordenación por burbuja.

- $O(2^N)$: El tiempo de ejecución crece exponencialmente con el tamaño de la entrada.
  Es típico de algoritmos que generan todas las combinaciones posibles de elementos,
  como el problema del viajante.

En casos donde se realizan múltiples operaciones con diferentes costes temporales, la
notación Big O representa el peor caso.

### Complejidad en algoritmos multipartes

En algoritmos que involucran múltiples estructuras de datos, la complejidad puede
depender de más de un parámetro.

???+ example "Bucles secuenciales"

    ```python linenums="1"
    def funcion(array_a: list[int], array_b: list[int]) -> None:
        for i in array_a:
            ...

        for i in array_b:
            ...
    ```

    Cada bucle tiene una complejidad de $O(N)$, pero como operan en *arrays* diferentes,
    la complejidad total es $O(A + B)$, donde $A$ y $B$ son los tamaños de `array_a` y
    `array_b` respectivamente.

???+ example "Bucles anidados"

    ```python linenums="1"
    def funcion(array_a: list[int], array_b: list[int]) -> None:
        for i in array_a:
            for j in array_b:
                ...
    ```

    En este caso, la complejidad es $O(A \times B)$, ya que los bucles anidados operan
    sobre *arrays* diferentes. Es un error asumir $O(N^2)$ sin considerar los tamaños de
    los *arrays* involucrados.

Es importante señalar que la notación Big O no está limitada a la letra $N$. Cualquier
letra puede representar el tamaño de la entrada en función del contexto del problema.

## Métodos de ordenación

### Ordenación por burbuja (_Bubble Sort_)

La ordenación por burbuja compara pares adyacentes de elementos en una lista e
intercambia sus posiciones si están en orden incorrecto. Este proceso se repite hasta
que no se requieren más intercambios, lo que indica que la lista está ordenada.

- **Complejidad temporal**: $O(N^2)$ en el peor caso.
- **Complejidad espacial**: $O(1)$.

???+ tip "Implementación"

    ```python linenums="1"
    def ordenacion_burbuja(lista: list[int]) -> list[int]:
        n: int = len(lista)

        for i in range(n):
            for j in range(n - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

        return lista
    ```

### Ordenación por selección (_Selection Sort_)

La ordenación por selección selecciona el elemento más pequeño de la parte no ordenada
de la lista y lo coloca en la siguiente posición de la parte ordenada. Este proceso se
repite hasta que la lista está completamente ordenada.

- **Complejidad temporal**: $O(N^2)$ en el peor caso.
- **Complejidad espacial**: $O(1)$.

???+ tip "Implementación"

    ```python linenums="1"
    def ordenacion_seleccion(lista: list[int]) -> list[int]:
        n: int = len(lista)

        for i in range(n):
            idx_min: int = i

            for j in range(i + 1, n):
                if lista[j] < lista[idx_min]:
                    idx_min = j

            lista[i], lista[idx_min] = lista[idx_min], lista[i]

        return lista
    ```

### Ordenación por inserción (_Insertion Sort_)

La ordenación por inserción divide la lista en una parte ordenada y otra desordenada. Se
toma un elemento de la parte desordenada y se inserta en la posición correcta dentro de
la parte ordenada. En el mejor caso (lista ya ordenada) alcanza $O(N)$.

- **Complejidad temporal**: $O(N^2)$ en el peor caso, $O(N)$ en el mejor caso.
- **Complejidad espacial**: $O(1)$.

???+ tip "Implementación"

    ```python linenums="1"
    def ordenacion_insercion(lista: list[int]) -> list[int]:
        for i in range(1, len(lista)):
            j: int = i

            while j > 0 and lista[j - 1] > lista[j]:
                lista[j - 1], lista[j] = lista[j], lista[j - 1]
                j -= 1

        return lista
    ```

## Métodos de búsqueda

### Búsqueda lineal (_Linear Search_)

La búsqueda lineal recorre cada elemento de la lista uno por uno hasta encontrar el
elemento buscado o hasta recorrer todos los elementos.

- **Complejidad temporal**: $O(N)$ en el peor caso.
- **Complejidad espacial**: $O(1)$.

???+ tip "Implementación"

    ```python linenums="1"
    def busqueda_lineal(lista: list[int], valor_buscar: int) -> int | None:
        for idx, valor in enumerate(lista):
            if valor_buscar == valor:
                return idx

        return None
    ```

### Búsqueda binaria (_Binary Search_)

La búsqueda binaria divide repetidamente a la mitad la parte de la lista que podría
contener el elemento buscado, hasta reducir las posibles ubicaciones a una sola. Este
método requiere que la lista esté previamente ordenada.

- **Complejidad temporal**: $O(\log N)$ en el peor caso.
- **Complejidad espacial**: $O(1)$.

???+ tip "Implementación"

    ```python linenums="1"
    def busqueda_binaria(lista: list[int], valor_buscar: int) -> int | None:
        izquierda: int = 0
        derecha: int = len(lista) - 1

        while izquierda <= derecha:
            punto_medio: int = (izquierda + derecha) // 2

            if valor_buscar == lista[punto_medio]:
                return punto_medio
            elif valor_buscar > lista[punto_medio]:
                izquierda = punto_medio + 1
            else:
                derecha = punto_medio - 1

        return None
    ```

## Estructuras de datos

### Pilas

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

### Colas

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

### Listas enlazadas

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

### Listas doblemente enlazadas

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

### Árboles binarios de búsqueda

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
