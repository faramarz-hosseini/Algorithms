n = int(input())
m = int(input())
edges = []
q_nums = []
for _ in range(m):
    edges.append(list(map(int, input().split())))
q = int(input())
for _ in range(q):
    q_nums.append(list(map(int, input().split())))


class Graph:
    def __init__(self, nodes_count, edges_count, edges):
        self.nodes_count = nodes_count
        self.edges_count = edges_count
        self.nodes = list(range(nodes_count))
        self.edges = {}
        for i in range(self.nodes_count):
            self.edges[i] = []
        for edge in edges:
            self.edges[edge[0]].append(edge[1])
            self.edges[edge[1]].append(edge[0])

    def check_edge(self, first_node, second_node):
        return second_node in self.edges[first_node]


graph = Graph(n, m, edges)
for query in q_nums:
    print(graph.check_edge(query[0], query[1]))

test = """
3
3
0 1
0 2
1 2
1
0 1
"""
