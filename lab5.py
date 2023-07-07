import json
from collections import deque


def _print(seq):
    for i in seq:
        print(i)

    print()


def get_way_index(ways, i):
    for way in ways:
        if way[-1][-1] == i:
            return ways.index(way)

    return None


def get_incidence_matrix():
    global l

    with open("incidence_matrix.json") as file:
        incidence_matrix = json.loads(file.read())
        l = len(incidence_matrix)

    return incidence_matrix


def get_adjacent_vertices(incidence_matrix: list) -> list:
    adjacent_vertices = [[] for i in range(l)]

    for line in list(zip(*incidence_matrix)):
        i1 = line.index(1)
        i2 = line[i1 + 1:].index(1) + i1 + 1

        adjacent_vertices[i1].append(i2 + 1)
        adjacent_vertices[i2].append(i1 + 1)

    return adjacent_vertices


def get_adjacency_matrix(adjacent_vertices: list) -> list:
    adjacency_matrix = [[0] * l for i in range(l)]

    for i in range(len(adjacent_vertices)):
        for j in adjacent_vertices[i]:
            adjacency_matrix[i][j - 1] = 1

    return adjacency_matrix


def get_incident_edges(adjacency_matrix: list) -> list:
    incident_edges = [[] for i in range(l)]

    for i, el in enumerate(adjacency_matrix):
        for j in range(len(el)):
            if el[j]:
                incident_edges[i].append((i + 1, j + 1))

    return incident_edges


def BFS(s, incidence_matrix):
    adjacent_vertices = get_adjacent_vertices(incidence_matrix)
    q = deque()
    reached = []
    ways = [[] for i in range(l)]

    q.append(s)
    while q:
        print("q: ", q)
        v = q.popleft()

        if v not in reached:
            new_v = list(map(lambda x: x - 1, adjacent_vertices[v]))
            reached.append(v)
            # q += new_v

            for nv in new_v:
                if nv not in reached and not ways[nv]:
                    q.append(nv)

            for vn in new_v:
                if not ways[vn] and vn != s:
                    ways[vn] = ways[v] + [(v + 1, vn + 1)]

    return ways


def DFS(v):
    global ways, reached, adjacent_vertices, s

    print("v: ", v + 1)

    new_v = list(map(lambda x: x - 1, adjacent_vertices[v]))
    new_v = filter(lambda x: x not in reached, new_v)

    if not new_v:
        return None

    for vn in new_v:
        reached.append(vn)

        if not ways[vn] and vn != s:
            ways[vn] = ways[v] + [(v + 1, vn + 1)]

        DFS(vn)


incidence_matrix = get_incidence_matrix()
print('incidence matrix:')
_print(incidence_matrix)

data = incidence_matrix
for func in (get_adjacent_vertices, get_adjacency_matrix, get_incident_edges):
    data = func(data)
    print(' '.join(func.__name__.split('_')[1:]) + ':')
    _print(data)

s = int(input(f"Enter number of graph's vertex from 1 to {l}: ")) - 1

print("breadth-first search:")
_print(BFS(s, incidence_matrix))

s = int(input(f"\nEnter number of graph's vertex from 1 to {l}: ")) - 1
ways = [[] for i in range(l)]
reached = []
adjacent_vertices = get_adjacent_vertices(incidence_matrix)
DFS(s)
print("depth-first search:")
_print(ways)
