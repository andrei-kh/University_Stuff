import networkx as nx
import matplotlib.pyplot as plt
from numpy import inf
import heapq


def print_table(table, headers, e='.3f'):
    new_table = [headers]
    max_h_len = [len(_) for _ in headers]
    for i in range(len(table)):
        new_table.append([])
        for j in range(len(table[0])):
            if isinstance(table[i][j], str):
                new_table[-1].append(table[i][j])
            elif isinstance(table[i][j], int):
                new_table[-1].append(str(table[i][j]))
            else:
                new_table[-1].append(str(format(table[i][j], e)))

            max_h_len[j] = max(max_h_len[j], len(new_table[-1][j]))

    headers_str = "| "
    for i in range(len(new_table[0])):
        half1 = (max_h_len[i] - len(new_table[0][i])) // 2
        half2 = max_h_len[i] - half1 - len(new_table[0][i])
        headers_str += ' ' * half2 + new_table[0][i] + ' ' * half1 + ' | '
    print(headers_str)
    print('-' * (len(headers_str) - 1))

    for r in new_table[1:]:
        print('| ', end='')
        for i in range(len(r)):
            half1 = (max_h_len[i] - len(r[i])) // 2
            half2 = max_h_len[i] - half1 - len(r[i])
            print(' ' * half2 + r[i] + ' ' * half1, end=' | ')
        print()


def ex1():
    def dijkstra_algorithm(G, s, f):
        weights = {}
        for u in G.nodes():
            weights[u] = inf

        pred = {s: None}
        weights[s] = 0
        pQueue = [(0, s)]
        while len(pQueue) > 0:
            uWeight, u = heapq.heappop(pQueue)

            if uWeight <= weights[u]:
                for v in G[u]:
                    tempWeight = uWeight + G[u][v]['weight']
                    if tempWeight < weights[v]:
                        weights[v] = tempWeight
                        heapq.heappush(pQueue, (tempWeight, v))
                        pred[v] = u

        path = [f]
        while pred[f] is not None:
            f = pred[f]
            path.append(f)

        return weights, path[::-1]

    G = nx.DiGraph()
    G.add_edge('s', 'a', weight=6, color='b')
    G.add_edge('s', 'c', weight=5, color='b')
    G.add_edge('s', 'd', weight=2, color='b')
    G.add_edge('a', 'b', weight=2, color='b')
    G.add_edge('a', 'f', weight=5, color='b')
    G.add_edge('a', 'g', weight=4, color='b')
    G.add_edge('b', 'c', weight=4, color='b')
    G.add_edge('b', 'g', weight=6, color='b')
    G.add_edge('c', 't', weight=4, color='b')
    G.add_edge('d', 'f', weight=1, color='b')
    G.add_edge('f', 'g', weight=2, color='b')
    G.add_edge('g', 't', weight=1, color='b')

    weights, path = dijkstra_algorithm(G, 's', 't')
    print(f"Path weight is: {weights['t']}")
    print("Path is:", path)

    for i in range(len(path) - 1):
        G[path[i]][path[i + 1]]['color'] = 'r'

    pos = {
        's': (1, 1),
        'a': (2, 1.5),
        'd': (2, 0.5),
        'f': (3, 0.5),
        'g': (4, 0.5),
        't': (5, 1),
        'c': (4, 1.5),
        'b': (3, 1.5),
    }
    wlabels = nx.get_edge_attributes(G, 'weight')
    colors = nx.get_edge_attributes(G, 'color').values()
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=wlabels)
    nx.draw(G, pos=pos, with_labels=True, width=2, edge_color=colors)
    plt.show()


def ex2():
    def bellman_ford(G, s):
        shortest = {}
        pred = {}
        for v in G.nodes():
            shortest[v] = inf
            pred[v] = None
        shortest[s] = 0

        table = [[0] + list(shortest.values())]
        for i in range(len(G.edges())):
            for u, v in G.edges():
                w = G[u][v]['weight']
                if shortest[u] + w < shortest[v]:
                    shortest[v] = shortest[u] + w
                    pred[v] = u
            table.append([i + 1] + list(shortest.values()))

        print_table(table, ['i'] + list(G.nodes()))
        return shortest, pred

    G = nx.DiGraph()
    G.add_edge('A', 'C', weight=-2)
    G.add_edge('C', 'D', weight=2)
    G.add_edge('C', 'F', weight=1)
    G.add_edge('F', 'D', weight=3)
    G.add_edge('S', 'A', weight=7)
    G.add_edge('S', 'C', weight=6)
    G.add_edge('S', 'F', weight=5)
    G.add_edge('S', 'E', weight=6)
    G.add_edge('E', 'F', weight=-2)
    G.add_edge('E', 'H', weight=3)
    G.add_edge('H', 'G', weight=1)
    G.add_edge('I', 'H', weight=1)
    G.add_edge('G', 'I', weight=-1)
    G.add_edge('A', 'B', weight=4)
    G.add_edge('B', 'G', weight=-2)
    G.add_edge('B', 'H', weight=-4)

    distances, routs = bellman_ford(G, 'S')
    print("Distances at the end:")
    print(distances)
    T = nx.DiGraph()
    for u, v in routs.items():
        if v is not None:
            T.add_edge(v, u, weight=G[v][u]['weight'])

    pos = {
        'I': (1, 0),
        'G': (0, 1),
        'B': (0, 2),
        'H': (2, 1),
        'E': (3, 0.5),
        'S': (1.5, 1.9),
        'F': (3.2, 1.7),
        'D': (3.4, 2.6),
        'C': (2.2, 2.5),
        'A': (1.2, 3)
    }
    wlabels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=wlabels)
    nx.draw(G, pos=pos, with_labels=True, width=1)
    nx.draw(T, pos=pos, with_labels=True, width=5, edge_color='green')
    plt.show()


def ex3():
    def floyd_warshall(G):
        dist = {v: {u: inf for u in G.nodes()} for v in G.nodes()}
        nxt = {v: {u: None for u in G.nodes()} for v in G.nodes()}

        for u, v in G.edges():
            dist[u][v] = G[u][v]['weight']
            nxt[u][v] = v

        for v in G.nodes():
            dist[v][v] = 0
            nxt[v][v] = v

        for q in G.nodes():
            for i in G.nodes():
                for j in G.nodes():
                    if dist[i][j] > dist[i][q] + dist[q][j]:
                        dist[i][j] = dist[i][q] + dist[q][j]
                        nxt[i][j] = nxt[i][q]

        return dist, nxt

    G = nx.DiGraph()
    G.add_edge(1, 2, weight=3)
    G.add_edge(1, 3, weight=2)
    G.add_edge(1, 4, weight=7)
    G.add_edge(2, 1, weight=3)
    G.add_edge(2, 4, weight=4)
    G.add_edge(3, 1, weight=4)
    G.add_edge(3, 4, weight=3)
    G.add_edge(4, 2, weight=6)
    G.add_edge(4, 3, weight=6)

    distanses, fpaths = floyd_warshall(G)

    paths = {}
    for u in G.nodes():
        for v in G.nodes():
            if u == v:
                continue
            idx = (u, v)
            paths[idx] = [u]
            t = u
            while t != v:
                t = fpaths[t][v]
                paths[idx].append(t)

    for k, v in paths.items():
        print(f'Path from {k[0]} to {k[1]}:')
        print("", ' -> '.join(map(str, v)), "| Distance:", distanses[k[0]][k[1]])
        print()

    pos = {
        1: (0, 1),
        2: (1, 2),
        3: (1, 0),
        4: (2, 1),
        12: (0, 2),
        24: (2, 2),
        43: (2, 0),
        31: (0, 0),
    }
    Ghelp1, Ghelp2 = nx.Graph(), nx.DiGraph()
    edgeList = [(1, 2), (2, 4), (4, 3), (3, 1)]
    for u, v in edgeList:
        w = G[u][v]['weight']
        G.remove_edge(u, v)
        Ghelp1.add_edge(u, u * 10 + v, weight=w)
        Ghelp1.add_edge(u * 10 + v, v)
        Ghelp2.add_edge(u * 10 + v, v)

    wlabelsHelp = nx.get_edge_attributes(Ghelp1, 'weight')
    nx.draw_networkx_edge_labels(Ghelp1, pos=pos, edge_labels=wlabelsHelp)
    nx.draw_networkx_edges(Ghelp1, pos, width=2)
    nx.draw_networkx_edges(Ghelp2, pos)

    wlabels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=wlabels)
    nx.draw(G, pos=pos, with_labels=True, width=2)
    plt.show()


ex1()
ex2()
ex3()
