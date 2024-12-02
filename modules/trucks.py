class Truck:
    def __init__(self, id_truck, capacity, available_hours):
        self.id_truck = id_truck
        self.capacity = capacity
        self.available_hours = available_hours
        self.status = 'ativo'
    
    def __repr__(self):
        return f"Caminhão {self.id_truck}, Capacidade: {self.capacity}, Horas disponíveis: {self.available_hours}"
