def shortest_path_tree(g,s,d):
    tree = {}
    for v in d:
        if v is not s:
            for e in g.incident_edges(v,False):
                u = e.opposite(v)
                wgt = e.element()
                if d[v] == d[u] +wgt:
                    tree[v] = e
    return tree