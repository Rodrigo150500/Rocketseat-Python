from src.models.connections.connection_handler import db_connection_handler
from src.models.repository.order_repository import OrderRepository
from src.use_cases.registry_updater import RegistryUpdater


def registry_updater_composer():

    conn = db_connection_handler.get_db_connection()
    model = OrderRepository(conn)
    use_case = RegistryUpdater(model)

    return use_case