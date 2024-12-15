from abc import ABC, abstractmethod

class Notification_Sender(ABC):
    #Define a regra de criação da classe

    @abstractmethod
    def send_notification(self, message: str) -> None:
        pass

class EmailSendNotification(Notification_Sender):

    def send_notification(self, message: str) -> None:
        print(f'Email Notification - {message}')

class SMSSendNotification(Notification_Sender):

    def send_notification(self, message: str) -> None:
        print(f'SMS Notification - {message}')

class Notificator:
    
    def __init__(self, notification_sender: Notification_Sender) -> None:
        self.__notification_sander = notification_sender

    def send(self, message):
        self.__notification_sander.send_notification(message)

obj = Notificator(EmailSendNotification())
obj.send("Ola mundo")


    
    

