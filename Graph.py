
import heapq

class Graph:

    adjacency_list = {} 
    # Contructor
    #
    # Takes the number of nodes in the graph and builds an
    # adjacency list data structure to store this graph.

    def __init__(self, num_cities, capacities, loads):
        self.num_cities = num_cities
        self.adj_list = {i: [] for i in range(num_cities)}
        self.capacities = {}
        self.loads = {}

        for capacity in capacities:
            start, end, cap = map(int, capacity.split(','))
            self.capacities[(start, end)] = cap

        for load in loads:
            start, end, l = map(int, load.split(','))
            self.loads[(start, end)] = l

    def add_edge(self, start, end):
        self.adj_list[start].append(end)

    def dijkstra(self, start, end):
        min_heap = [(0, start, [])]  # (total load percentage, current city, path)
        visited = set()

        while min_heap:
            load_percent, current_city, path = heapq.heappop(min_heap)

            if current_city == end:
                return path + [end]

            if current_city in visited:
                continue

            visited.add(current_city)

            for neighbor in self.adj_list[current_city]:
                new_load_percent = load_percent + self.calculate_percentage(current_city, neighbor)
                heapq.heappush(min_heap, (new_load_percent, neighbor, path + [current_city]))

        return []

    def calculate_percentage(self, start, end):
            capacity = self.capacities.get((start,end), 0)
            if capacity == 0:
                return float("inf") # if no capacity, return infinity
            load = self.loads.get((start,end), 0)
            return load / capacity * 100 if load < capacity else float("inf") 

   
