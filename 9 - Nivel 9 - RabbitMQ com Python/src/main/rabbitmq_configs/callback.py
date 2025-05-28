import json
from src.drivers.telegram_sender import send_telegram_message

def message_callback(ch, method, properties, body):
    msg = body.decode("utf-8")
    formatted_msg = json.loads(msg) 

    message = formatted_msg["msg"]
    send_telegram_message(message)
    print(formatted_msg["msg"])
