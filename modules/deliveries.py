class Delivery:
    def __init__(self, id_delivery, destination, deadline, weight):
        self.id_delivery = id_delivery
        self.destination = destination
        self.deadline = deadline
        self.weight = weight
    
    def __repr__(self):
        return f"Entrega {self.id_delivery}, Destino: {self.destination}, Prazo: {self.deadline}, Peso: {self.weight}"
