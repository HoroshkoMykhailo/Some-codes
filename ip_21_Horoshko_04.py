import random
# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.adj = [[] for i in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
        self.adj[u].append(v)
        self.adj[v].append(u)

    # Input check function     
    def check_if_connected(self):
        visited =[]
        for i in range(self.V):
            visited.append(False)
        self.DFS(0, visited)
        for i in range(self.V):
            if(not visited[i]):
                return False
        return True
    
    def DFS(self, v, visited):
        visited[v] = True
        for i in self.adj[v]:
            if visited[i] == False:
                self.DFS(i, visited)

    # Search cycle function
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    #  Kruskal algorithm function
    def KruskalMST(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        print("Edges in the constructed MST:")
        for u, v, weight in result:
            print("%d - %d: %d" % (u + 1, v + 1, weight))

    # Matrix output            
    def printg(self):
        matrix = [[0 for j in range(self.V)] for i in range(self.V)]
        for edge in self.graph:
            u = edge[0]
            v = edge[1]
            w = edge[2]
            matrix[u][v] = w
            matrix[v][u] = w
        for row in matrix:
            print(*row, sep = '\t')
            
# Input mannually         
def inpg():
    n =  int(input('Enter the number of nodes in the graph:'))
    g = Graph(n)
    for i in range(n):
        for j in range(i + 1, n):
            w = int(input("W(%d -- %d)(0 if edge is not in the graph):" %(i + 1, j + 1)))
            if w != 0:
                g.add_edge(i, j, w)
    return g

# Input random
def inpg_rand():
    n = random.randint(2, 10)
    g = Graph(n)
    for i in range(n):
        for j in range(i + 1, n):
            edge = random.randint(0, 3)
            if(edge != 0):
                g.add_edge(i, j, random.randint(1, 30))
    return g
 
# Main code
if __name__ == '__main__':
    s = input('Select a input mode(r, rand or random for random):')
    if(s != 'rand' and s!='random' and s!= 'r'):
        g = inpg();
        while(not g.check_if_connected()):
            print('The graph is not connected.\nPlease input graph again.\n')
            g = inpg()
    else:
        g = inpg_rand()
        while(not g.check_if_connected()):
            g = inpg_rand()
        print("The matrix of weighted graph:")
        g.printg()
    g.KruskalMST()
