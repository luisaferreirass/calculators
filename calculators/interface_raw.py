from abc import ABC, abstractmethod

class NotificationSender(ABC): #Classe de interface
    # Definir a regra de construção das demias classes que ela é implementada
    @abstractmethod # Classes com metodos abtratos só podemos colocar como herança em putras classes
    def send_notification(self, message: str) -> None:
        pass

class EmailNotificationSender(NotificationSender): # É obrigatório ter todos os metodos abstratos
    def send_notification(self, message: str) -> None:
        print(f"Email message - {message}")


class SMSNotificationSender(NotificationSender):
    def send_notification(self, message: str) -> None:
        print(f"SMS message - {message}")
    
class Notificator:
    def __init__(self, notification_sender: NotificationSender) -> None:
        self.__notification_sender = notification_sender #Vai ser uma das duas classes

    def send(self, message: str) -> None:
        self.__notification_sender.send_notification(message)
        

obj = Notificator(SMSNotificationSender())
obj.send("Ola Mundo")