from flask import Flask, request
import requests

app = Flask(__name__)

NUMEROS = ['5592993356810','5592982411933', '5592982671304', '5592999029558', '5592992560618']
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

if __name__ == '__main__':

    app.run()
