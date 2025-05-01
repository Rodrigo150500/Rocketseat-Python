from src.models.connections.connection_handler import db_connection_handler
from src.models.repository.order_repository import OrderRepository
from src.use_cases.registry_finder import RegistryFinder


def registry_finder_composer():

    conn = db_connection_handler.get_db_connection()
    model = OrderRepository(conn)
    use_case = RegistryFinder(model)

    return use_case