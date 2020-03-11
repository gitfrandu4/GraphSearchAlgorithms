# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print("Breadth-first Search: " + str(search.breadth_first_graph_search(ab).path()))
print("Depth-first Search: " + str(search.depth_first_graph_search(ab).path()))

# Estrategia de Ramificación y Acotación (BBS):
print("Branch-and-Bound Search: " + str(search.branch_and_bound_search(ab).path()))

# Result:
# Breadth-first Search:     [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
# Depth-first Search:       [<Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>] : 101+138+120+75+70+111+118=733
# Branch-and-Bound Search:  [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418