from flask import Flask, request
import requests

app = Flask(__name__)

WHATSAPP_API_URL = "https://graph.facebook.com/v20.0/382357811621980/messages"
ACCESS_TOKEN = "EAALuCkcVXeQBO5sAxZA49TXI10z8oME42ZCZCNYZA2H3ERISmTvArkYEgSAbUp82ODSrQf1j2AZAGOeOgW93TMAysrbVtXloL5w3GcqCYwcOCvTsrogqGlNtJhueNJkuZC58ZBtak4ratfHQz8jZAFsNKEb8z3TGxqppg1tYfPX6SQYfHEPqgUnZCFjhrgIMsZBPdxsAZDZD"

@app.route('/', methods=['GET'])
def send_message():
    text = request.args.get('text')
    # numero = request.args.get('numero')

    # if not numero:

    for numero in ['5592982411933', '5592993356810']:

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

        return {"status": response.status_code, "response": response.json()}

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=80, debug=True)
