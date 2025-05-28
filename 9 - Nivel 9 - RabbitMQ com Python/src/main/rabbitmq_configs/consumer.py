import pika
from .callback import message_callback

class RabbitMQConsumer:
    def __init__(self):
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__queue = "minha_queue"
        self.__channel = self.create_channel()
    
    def create_channel(self):
        connection_paramester = pika.ConnectionParameters(
            host=self.__host,
            port= self.__port,
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password
            )
        )

        channel = pika.BlockingConnection(connection_paramester).channel()


        channel.queue_declare(
            queue=self.__queue,
            durable=True
        )

        channel.basic_consume(
            queue=self.__queue,
            on_message_callback=message_callback,
            auto_ack=True
        )

        return channel

    def start(self):
        print("Iniciando servidor RabbitMQ")
        self.__channel.start_consuming()