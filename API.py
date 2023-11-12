import requests
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import cross_origin, CORS

app = Flask(__name__)
CORS(app)

url = "http://localhost:8080"

def enviar_vistoria(vistoria):
    data_hoje = datetime.now()
    resultado = {
	"foto": {
		"dtFoto": data_hoje.strftime("%Y-%m-%d"),
		"dsFoto": "1231231",
		"urlFoto": "http:12341.com.br/1231231.jpg"
	},
	"vistoria": {
		"dtVistoria": data_hoje.strftime("%Y-%m-%d"),
		"dsResultado": "Positivo"
	},
	"bike" : {
		"cdSerie" : vistoria['cdSerie'],
		"nmMarca" : vistoria['nmMarca'],
		"nmModelo" : vistoria['nmModelo']
	}

}
    
    url = url + "/apiporto/webapi/ia"
    response = requests.post(url, json=resultado)
    if(response.status_code == 200):
        return{'success': 'Arquivo enviado com sucesso'}
    else:
       return {'error': 'Erro ao enviar o arquivo (imagem)'}



@app.route('/vistoria', methods=['POST'])
@cross_origin()
def vistoria():
    # No request vira a imagem + os dados da bike(cdSerie, nmMarca e nmModelo)
    
    
    #Verifica se o arquivo foi enviado
    print(request.files.keys())
    if 'image' not in request.files:
        # Caso o arquivo não tenha sido enviado, retorna um erro
        return jsonify({'error': 'Nenhum arquivo foi enviado'})
    file = request.files['image']

    # Verifica se o arquivo foi enviado
    if file.filename == '':
        return jsonify({'error': 'Erro ao enviar o arquivo (imagem)'})
    
    enviar_vistoria(request.files['dados'])


if __name__ == '__main__':
    app.run(debug=True, port=8000)