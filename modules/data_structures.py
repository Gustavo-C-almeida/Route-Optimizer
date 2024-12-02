class Graph:
    def __init__(self):
        self.vertices = {}

    def add_edge(self, from_vertex, to_vertex, distance):
        if from_vertex not in self.vertices:
            self.vertices[from_vertex] = {}
        self.vertices[from_vertex][to_vertex] = distance

class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def push(self, item, priority):
        heapq.heappush(self.queue, (priority, item))
    
    def pop(self):
        return heapq.heappop(self.queue)
