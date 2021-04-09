from sys import stdin
import networkx as nx
import matplotlib.pyplot as plt
from sys import argv


def graphInput(graph):
    print("Input graph vertecies: ")
    for line in stdin:
        if line == '\n':
            break
        a, b = line.split()
        graph[a] = graph.get(a, []) + [b]
        graph[b] = graph.get(b, []) + [a]


# Exercise 1
# The double degree of a vertex of an undirected graph is the sum
# of the degrees of its neighbors. Construct and implement an
# algorithm that finds the double degrees of all vertices of the graph.
def ex1():
    graph = {}
    usd = {}
    result = {}

    def dfs(v):
        usd[v] = True
        for u in graph[v]:
            result[v] = result.get(v, 0) + len(graph[u])
            if usd.get(u) is None:
                dfs(u)

    graphInput(graph)

    for v in graph.keys():
        if usd.get(v) is None:
            dfs(v)

    print("Double degrees of the vertices:")
    for key, val in result.items():
        print(f"\tFor vertex {key}: {val}")

    nx.draw(nx.Graph(graph), with_labels=True, width=3)
    plt.show()


# Exercise 2
# Construct and implement an algorithm that checks if there exists
# a cycle in this undirected graph containing this edge.
def ex2():
    graph = {}
    usd = {}
    cycle = []

    def dfs(v, v2, parent):
        usd[v] = True
        cycle.append(v)
        for u in graph[v]:
            if usd.get(u) is None:
                if dfs(u, v2, v):
                    return True
            elif parent != u:
                if u == v2:
                    return True
        cycle.remove(v)
        return False
    graphInput(graph)
    print("Input an edge:")
    v1, v2 = input().split()
    usd[v2] = True

    if dfs(v1, v2, v2) is True:
        print(f"There is a cycle containing an edge {v1} - {v2}")
        cycle.append(v2)
        cycle.append(v1)

        print(cycle)
        ng = nx.Graph(graph)
        colors = []
        for node in ng.edges():
            if (node[0] == v1 and node[1] == v2) or (node[1] == v1 and node[0] == v2):
                colors.append('green')
            elif node[0] in cycle and node[1] in cycle:
                colors.append('red')
            else:
                colors.append('black')

        nx.draw(nx.Graph(graph), edge_color=colors, with_labels=True, width=3)
        plt.show()
    else:
        print(f"There is no cycle containing an edge {v1} - {v2}")

    # print(cycle)


# Exercise 3
# Construct and implement an algorithm that checks
# whether the input graph is bipartite.
def ex3():
    graph = {}
    usd = {}

    def dfs(v, c):
        if usd.get(v) is not None and usd.get(v) != c:
            return False

        usd[v] = c
        for u in graph[v]:
            if usd.get(u) is None:
                if not dfs(u, not c):
                    return False

            if usd.get(u) is not None and usd.get(u) != (not c):
                return False

        return True

    graphInput(graph)
    if dfs(list(graph.keys())[0], True) is True:
        print("Graph is bipartite")
        ng = nx.Graph(graph)
        top = nx.bipartite.sets(ng)[0]
        pos = nx.bipartite_layout(ng, top)
        nx.draw(ng, pos=pos, with_labels=True)
        plt.show()

    else:
        print("Graph is not bipartite")


if __name__ == "__main__":
    if len(argv) == 1:
        ex1()
        ex2()
        ex3()
    else:
        if argv.count('1') >= 1:
            ex1()
        if argv.count('2') >= 1:
            ex2()
        if argv.count('3') >= 1:
            ex3()
