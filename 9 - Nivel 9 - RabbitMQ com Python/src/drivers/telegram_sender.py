import requests

def send_telegram_message(message: str) -> None:
    
    token = "7756226133:AAGnmiTEKNlfrMk7bNJOQbb6aw3gWm8BBRA"
    chat_id = -1002537185870
    
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    requests.post(url=url, data=payload)

