from flask import Flask, request
from app.app import run

#Region Metodo para a Google Cloud Plataform
def main(request):
    run(request.get_json())
    return 'success', 200
#End Region

#Region Metodo para Testar Local via Postman/Rest Client
#url:http://127.0.0.1:8090/main
#app = Flask(__name__)
#@app.route('/main', methods = ['POST'])
def main_flask():
    run(request.get_json())
    return 'success', 200
#app.run(host='0.0.0.0', port=8090)
#End Region