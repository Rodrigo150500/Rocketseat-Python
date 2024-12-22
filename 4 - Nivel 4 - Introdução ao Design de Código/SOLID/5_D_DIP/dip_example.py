from .notificator_interface import NotificatorInterface

class ClienteService:

    def __init__(self, notificator: NotificatorInterface) -> None:
        self.__notificator = notificator

    def send_notification(self, message: str) -> None:
        self.__notificator.send_notification(message)