from flask import Flask, request
import requests
import time
import datetime
from threading import Thread

filename = (__file__.split('\\')[-1]).split('.')[0]
app = Flask(__name__)

NUMEROS = ['5592993356810']#,'5592982411933', '5592982671304', '5592999029558', '5592992560618']
WHATSAPP_API_URL = "https://graph.facebook.com/v20.0/382357811621980/messages"
ACCESS_TOKEN = "EAALuCkcVXeQBO5sAxZA49TXI10z8oME42ZCZCNYZA2H3ERISmTvArkYEgSAbUp82ODSrQf1j2AZAGOeOgW93TMAysrbVtXloL5w3GcqCYwcOCvTsrogqGlNtJhueNJkuZC58ZBtak4ratfHQz8jZAFsNKEb8z3TGxqppg1tYfPX6SQYfHEPqgUnZCFjhrgIMsZBPdxsAZDZD"

@app.route('/', methods=['GET'])
def send_message():
    text = request.args.get('text')

    respostas = []
    for numero in NUMEROS:

        # Configuração da requisição para a API do WhatsApp
        headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }

        data = {
            "messaging_product": "whatsapp",
            "to": numero,
            "type": "text",
            "text": {
                "body": text
            }
        }

        response = requests.post(WHATSAPP_API_URL, headers=headers, json=data)
        respostas.append({'numero': numero, 'status': response.status_code, 'response': response.json()})

    return {'respostas': respostas}

def start_app():
    app.run()

def print_terminal():
    while True:
        print(f"+ + + + + + + + + Executando em {datetime.datetime.now()} + + + + + + + + +")
        time.sleep(60*2)

def deadpool():
    while True:
        try:
            # Faz uma requisição para a própria aplicação
            requests.get(f"https://{filename}.onrender.com/")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao tentar manter vivo: {e}")
        time.sleep(60*2)  # Espera 2 minutos


if __name__ == '__main__':

    # Configuração do tempo de execução da aplicação
    # app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(hours=24)

    thread = Thread(target=deadpool)
    thread.daemon = True
    thread.start()

    start_app()
