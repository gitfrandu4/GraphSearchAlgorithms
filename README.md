# GraphSearchAlgorithms


Práctica 1 de Fundamentos de los Sistemas Inteligentes



<img src="https://github.com/gitfrandu4/GraphSearchAlgorithms/tree/master/img/romania.jpeg" alt="Romania" style="zoom: 67%;" />



## Práctica 1 - Primera parte

#### Tareas

* A partir del código base se implementa el método de búsqueda **Ramificación y Acotación** (_Branch-and-Bound Search_). Utilizando como problema el grafo de las ciudades de Rumanía presente en el código. 

* Comparación de nodos expandidos por este método en comparación a los métodos de búsqueda **Primero en Anchura** (_Breadth-first Search_) y **Primero en profundidad** (_Depth-first Search_):

  ```
  --------------------Primera parte--------------------
  
  Nodos expandidos: 21
  Breadth-first Search: [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
  
  Nodos expandidos: 18
  Depth-first Search: [<Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>] : 101+138+120+75+70+111+118=733
  
  Nodos expandidos: 31
  Branch-and-Bound Search: [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
  ```



## Práctica 1 - Segunda parte

### Ramificación y Acotación con Subestimación

La estrategia de búsqueda **Ramificación y Acotación con Subestimación** pertenece a las estrategias de **búsqueda informada**. En este caso, además de utilizar el coste acumulado de un camino desde el estado inicial hasta un cierto estado del grafo, se utiliza una **estimación heurística** hasta el estado final para ordenar la lista abierta. De esta forma, dado un determinado nodo _n_ del árbol del búsqueda, la expresión de coste estimado _f(n)_ será:

![Eqn1](https://github.com/gitfrandu4/GraphSearchAlgorithms/tree/master/img/Eqn2.png)

Donde _g(n)_ representa el coste acumulado y _h(n)_ la heurística utilizada. Para que el camino encontrado sea **óptimo**, la heurística debe ser **consistente**. Es decir, ha de cumplir que para cada nodo _n_ y cada nodo hijo _n’_ alcanzado mediante la acción _a_, el valor heurístico _h(n)_ debe ser siempre menor o igual al valor heurístico _h(n’)_ más el coste del nodo _n_ al _n’_ mediante la acción _a_.

![Eqn1](https://github.com/gitfrandu4/GraphSearchAlgorithms/tree/master/img/Eqn1.png)

#### Tareas

* A partir del código base se implementa el método de búsqueda **Ramificación y Acotación con Subestimación**.

  Como heurística se utilizará la distancia en línea recta entre cada estado y el estado final. 

* Comparación de la cantidad de nodos expandidos por este método con relación al método ramificación y acotación:

Salida:

```
--------------------Segunda parte--------------------

Ejemplo 1: Desde Oradea hasta Bucharest

Nodos expandidos: 27
Branch-and-Bound Search: [<Node B>, <Node P>, <Node R>, <Node S>, <Node O>]

Nodos expandidos: 17
B&Bound-with-Und Search: [<Node B>, <Node P>, <Node R>, <Node S>, <Node O>]

-----------------------------------------------------
Ejemplo 2: Desde Timisoara hasta Neamt

Nodos expandidos: 46
Branch-and-Bound Search: [<Node N>, <Node I>, <Node V>, <Node U>, <Node B>, <Node P>, <Node R>, <Node S>, <Node A>, <Node T>]

Nodos expandidos: 43
B&Bound-with-Und Search: [<Node N>, <Node I>, <Node V>, <Node U>, <Node B>, <Node P>, <Node R>, <Node S>, <Node A>, <Node T>]

-----------------------------------------------------
Ejemplo 3: Desde Urziceni hasta Eforie

Nodos expandidos: 13
Branch-and-Bound Search: [<Node E>, <Node H>, <Node U>]

Nodos expandidos: 6
B&Bound-with-Und Search: [<Node E>, <Node H>, <Node U>]
```

