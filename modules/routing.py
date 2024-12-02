import heapq

class RouteOptimizer:
    def __init__(self, centers, trucks, deliveries):
        self.centers = centers
        self.trucks = trucks
        self.deliveries = deliveries
    
    def optimize_routes(self):
        # Implementação do algoritmo de Dijkstra ou A*
        for delivery in self.deliveries:
            # Achar o centro mais próximo e alocar o caminhão
            print(f"Roteamento para a entrega {delivery.id_delivery}")
        # Aqui será feito o cálculo da rota
