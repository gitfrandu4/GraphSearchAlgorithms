# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print("Breadth-first Search: " + str(search.breadth_first_graph_search(ab).path()))
print("Depth-first Search: " + str(search.depth_first_graph_search(ab).path()))

print("\n--------------------Primera parte--------------------\n")

# Estrategia de Ramificación y Acotación (BBS):
print("Branch-and-Bound Search: " + str(search.branch_and_bound_search(ab).path()))

# Estrategia de Ramificación y Acotación con subestimación:
print("Branch-and-Bound-with-Underestimates Search: " + str(search.branch_and_bound_search_with_und(ab).path()))

# Result:
# Breadth-first Search:     [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
# Depth-first Search:       [<Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>] : 101+138+120+75+70+111+118=733
# Branch-and-Bound Search:  [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418

print("\n--------------------Segunda parte--------------------\n")
print("Ejemplo 1: Desde Oradea hasta Bucharest")

ob = search.GPSProblem('O', 'B'
                       , search.romania)
print("Branch-and-Bound Search: " + str(search.branch_and_bound_search(ob).path())  + "\n")
print("B&Bound-with-Und Search: " + str(search.branch_and_bound_search_with_und(ob).path()))

print("-----------------------------------------------------")

print("Ejemplo 2: Desde Timisoara hasta Neamt")
tn = search.GPSProblem('T', 'N'
                       , search.romania)
print("Branch-and-Bound Search: " + str(search.branch_and_bound_search(tn).path()) + "\n")
print("B&Bound-with-Und Search: " + str(search.branch_and_bound_search_with_und(tn).path()))

print("-----------------------------------------------------")
print("Ejemplo 3: Desde Urziceni hasta Eforie")

ue = search.GPSProblem('U', 'E'
                       , search.romania)
print("Branch-and-Bound Search: " + str(search.branch_and_bound_search(ue).path()) + "\n")
print("B&Bound-with-Und Search: " + str(search.branch_and_bound_search_with_und(ue).path()))