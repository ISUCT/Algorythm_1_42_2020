#Задача ЕГЭ  из 8 модуля проба не удалась :)
from collections import defaultdict
 
 
class Graph:
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
 
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
 
    def printArr(self, dist,cities,res):
        for city in cities:
            if dist[city] == float("Inf"):
                continue
            res.append([city,dist[city]])
        for i in range(len(res) - 1):
            for j in range(len(res) - i - 1):
                item = res[j]
                next_it = res[j + 1]
                if (item[1] > next_it[1]):
                    res[j], res[j + 1] = next_it, item
        for i in range(len(res)):
            print(" ".join(map(str, res[i])))    
 
    def BellmanFord(self, src,cities,res):
 
        dist = [float("Inf")] * (self.V+1)
        dist[src] = 0
 
        for i in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        self.printArr(dist,cities,res)
 
 

first_line = list(map(int, input().split()))
capital = first_line[-1]
g = Graph(first_line[0])
cities = list(map(int, input().split()))
ways = []

for i in range(first_line[1]):
    way = list(map(int, input().split()))
    for j in range(len(way)):
        ways.append(way[j])
    g.addEdge(ways[0], ways[1], ways[2])
    ways.clear()

res = []
g.BellmanFord(capital,cities,res)