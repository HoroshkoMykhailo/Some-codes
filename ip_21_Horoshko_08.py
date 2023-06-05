import random
import sys
# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.adj = {}

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
        if u not in self.adj.keys():
            self.adj[u] = []
        if v not in self.adj.keys():
            self.adj[v] = []
        self.adj[u].append(v)
        self.adj[v].append(u)
        
    def greedy(self):
        vertex_cover = []
        uncovered_edges = [i for i in range(len(self.graph))]
        copy_adj = self.adj
    
        while uncovered_edges:
            # Знаходимо вершину з найбільшим степенем
            max_degree = 0
            for k in copy_adj.keys():
                if k not in vertex_cover and max_degree < len(copy_adj[k]):
                    max_degree = len(copy_adj[k])
                    max_degree_vertex = k
        
            # Додаємо вершину до вершинного покриття
            vertex_cover.append(max_degree_vertex)
        
            # Видаляємо всі ребра, що з'єднуються з вибраною вершиною
            edges_to_remove = []
            
            for e in uncovered_edges:
                if max_degree_vertex in self.graph[e][:2]:
                    edges_to_remove.append(e)

            for edge in edges_to_remove:
                uncovered_edges.remove(edge)

            # Видаляємо вершину
            del copy_adj[max_degree_vertex]

            for k in copy_adj.keys():
                if max_degree_vertex in copy_adj[k]:
                    copy_adj[k].remove(max_degree_vertex)
        
        print("Vertex Cover:")
        for i in range(len(vertex_cover) - 1):
            print(vertex_cover[i], end = ", ")
        print(vertex_cover[len(vertex_cover)- 1])
        print("Number of vertexes: ")
        print(len(vertex_cover))    
        
    def aprox(self):
        uncovered_edges = [i for i in range(len(self.graph))]
        vertex_cover = []

        while uncovered_edges:
            # Обираємо ребро рандомно
            edge = random.choice(uncovered_edges)
            
            u, v, _ = self.graph[edge]

            edges_to_remove = []
            i = 0
            j = 0
            #Видаляємо всі ребра, що з'єднані з вершинами
            for e in uncovered_edges:
                if u in self.graph[e][:2]:
                    edges_to_remove.append(e)
                    i = i + 1
                elif v in self.graph[e][:2]:
                    edges_to_remove.append(e)
                    j = j + 1
            for edge in edges_to_remove:
                uncovered_edges.remove(edge)
            # Додаємо вершини до вершинного покриття
            if i == 1:
                vertex_cover.append(v)
            elif j == 0:
                vertex_cover.append(u)
            else:
                vertex_cover.append(u)
                vertex_cover.append(v)
        print("Vertex Cover:")
        for i in range(len(vertex_cover) - 1):
            print(vertex_cover[i], end = ", ")
        print(vertex_cover[len(vertex_cover)- 1])
        print("Number of vertexes: ")
        print(len(vertex_cover))
            
# Input mannually         
def inpg():
    g = Graph(15)
    g.add_edge("Turin", "Milan", 145)
    g.add_edge("Turin", "Genua", 172)
    g.add_edge("Milan", "Genua", 148)
    g.add_edge("Milan", "Bergamo", 51)
    g.add_edge("Milan", "Bolonya", 215)
    g.add_edge("Genua", "Bolonya", 295)
    g.add_edge("Genua", "Pisa", 160)
    g.add_edge("Bergamo", "Verona", 117)
    g.add_edge("Verona", "Venice", 121)
    g.add_edge("Verona", "Bolonya", 150)
    g.add_edge("Venice", "Triest", 160)
    g.add_edge("Venice", "Bolonya", 158)
    g.add_edge("Bolonya", "Florence", 117)
    g.add_edge("Florence", "Pisa", 88)
    g.add_edge("Florence", "Rome", 273)
    g.add_edge("Pisa", "Rome", 348)
    g.add_edge("Rome", "Napoli", 225)
    g.add_edge("Napoli", "Bari", 261)
    g.add_edge("Palermo", "Catania", 145)
    return g
 
# Main code
if __name__ == '__main__':
    c = sys.argv[1]
    g = inpg();
    if(c == 'g'):
        g.greedy()
    else:
        g.aprox()
