from collections import defaultdict

import networkx as nx

with open("input.txt") as f:
    lines = f.read().split("\n")


connections = [line.split("-") for line in lines]

graph = defaultdict(set)
for connection in connections:
    graph[connection[0]].add(connection[1])
    graph[connection[1]].add(connection[0])

triangles = set()
for node1 in graph:
    for node2 in graph[node1]:
        for node3 in graph[node2]:
            if node1 in graph[node2] and node1 in graph[node3]:
                triangles.add(tuple(sorted([node1, node2, node3])))

sum_t_start = 0
for triangle in triangles:
    for node in triangle:
        if node[0] == "t":
            sum_t_start += 1
            break

print("Part 1:", sum_t_start)


G = nx.Graph()
G.add_edges_from(connections)
maximal_cliques = list(nx.enumerate_all_cliques(G))
largest_maximal_clique = sorted(maximal_cliques[-1])
largest_maximal_clique_str = ",".join(largest_maximal_clique)

print("Part 2:", largest_maximal_clique_str)
