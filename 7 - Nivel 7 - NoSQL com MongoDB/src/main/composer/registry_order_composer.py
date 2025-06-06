from src.models.connections.connection_handler import db_connection_handler
from src.models.repository.order_repository import OrderRepository
from src.use_cases.registry_order import RegistryOrder

def registry_order_composer():

    conn = db_connection_handler.get_db_connection()
    models = OrderRepository(conn)
    use_case = RegistryOrder(models)

    return use_case
