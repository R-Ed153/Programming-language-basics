from copy import deepcopy

def floyd_warshall(g):
    closure = deepcopy(g)
    verts = list(closure.vertices())
    n = len(verts)
    for k in range (n):
        for i in range(n):
            if i != k and closure.get_edge(verts[k],verts[i]) is not None:
               for j in range(n):
                if closure.get_edge(verts[i],verts[j]) is None:
                    closure.insert_edge(verts[i],verts[j])
