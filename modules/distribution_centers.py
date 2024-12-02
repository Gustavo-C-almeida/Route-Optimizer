class DistributionCenter:
    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity
    
    def __repr__(self):
        return f"Centro de Distribuição: {self.name}, Localização: {self.location}"
