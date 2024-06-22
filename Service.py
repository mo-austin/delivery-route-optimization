
from Graph import Graph 
class Service:

    def __init__(self):
        return


    def compute(self,numCities, capacities, loads, start, end):
        graph = Graph(numCities, capacities, loads)


        for string in capacities:
            start_city, end_city, _ = map(int, string.split(','))
            graph.add_edge(start_city, end_city)
        
        smallest_path = graph.dijkstra(start,end)
        return smallest_path
        

    def calculate_percentage(self, start, end):
        capacity = self.capacities.get((start,end), 0)
        if capacity == 0:
            return float("inf") # if no capacity, return infinity
        load = self.loads.get((start,end), 0)
        return load / capacity * 100 if load < capacity else float("inf") 
    


