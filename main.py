from modules.distribution_centers import DistributionCenter
from modules.trucks import Truck
from modules.deliveries import Delivery
from modules.routing import RouteOptimizer
from modules.utils import load_data

def main():
    # Carregar dados de exemplo
    data = load_data('data/mock_data.json')
    
    # Criar centros de distribuição
    centers = [DistributionCenter(**center_data) for center_data in data['centers']]
    
    # Criar caminhões
    trucks = [Truck(**truck_data) for truck_data in data['trucks']]
    
    # Criar entregas
    deliveries = [Delivery(**delivery_data) for delivery_data in data['deliveries']]
    
    # Alocação de rotas
    optimizer = RouteOptimizer(centers, trucks, deliveries)
    optimizer.optimize_routes()

if __name__ == "__main__":
    main()
