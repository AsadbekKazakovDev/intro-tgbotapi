import requests
import time
TOKEN = "6565529385:AAEAcOoC3SkHhoK0pYMGdhKYppspW591Nws"
BASE_URL = "https://api.telegram.org/bot"


def send_photo(chat_id: str, photo: str) -> None:
    '''send photo to tg user'''
    url = f"{BASE_URL}{TOKEN}/sendPhoto"
    payload = {
        "chat_id": chat_id,
        "photo": photo,
        "caption": "*this is a dog's photo*",
        "parse_mode": "MarkdownV2"
    }
    requests.get(url, params=payload)
    
def sendMessage(chat_id: str, text: str) ->None:
    '''send message to tg user'''
    url=f"{BASE_URL}{TOKEN}/sendMessage"
    payload={
        'chat_id':chat_id,
        'text': text
    }
    response=requests.get(url,params=payload)
        
    
def last_update() -> list[dict]:
    '''get last updates'''
    url = f"{BASE_URL}{TOKEN}/getUpdates"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['result'][-1]

    return False


def dog_photo() -> str:
    url = 'https://random.dog/woof.json'

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['url']

    return


def main():
    last_update_id = last_update()['update_id']

    while True:
        time.sleep(0.5)


        curr_update = last_update()

        # if last_update_id!=curr_update['update_id']:
        #     chat_id=curr_update['message']['chat']['id']
        #     text=curr_update['message']['text']
        #     sendMessage(chat_id,text)
        # last_update_id=curr_update['update_id']

        if last_update_id == curr_update['update_id']:
            continue

        text = curr_update['message']['text']
        if text == '/dog':
            chat_id = curr_update['message']['chat']['id']
            photo = dog_photo()
            send_photo(chat_id, photo)
        else:
            chat_id=curr_update['message']['chat']['id']
            sendMessage(chat_id,text)
        last_update_id = curr_update['update_id']
main()