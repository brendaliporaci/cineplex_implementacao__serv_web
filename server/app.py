from flask import Flask, jsonify
from flask_cors import CORS

# Cria a aplicação Flask
app = Flask(__name__)

# Permite comunicação entre frontend e backend
CORS(app)

# Lista inicial de assentos
assentos = [
    {"codigo": "A1", "preco": 20.0, "status": "DISPONIVEL"},
    {"codigo": "A2", "preco": 20.0, "status": "DISPONIVEL"},
    {"codigo": "A3", "preco": 20.0, "status": "RESERVADO"},
    {"codigo": "A4", "preco": 20.0, "status": "DISPONIVEL"},
    {"codigo": "B1", "preco": 25.0, "status": "DISPONIVEL"},
    {"codigo": "B2", "preco": 25.0, "status": "RESERVADO"},
    {"codigo": "B3", "preco": 25.0, "status": "DISPONIVEL"},
    {"codigo": "B4", "preco": 25.0, "status": "DISPONIVEL"}
]

# Endpoint para listar os assentos
@app.route("/api/assentos", methods=["GET"])
def listar_assentos():
    return jsonify(assentos)

# Inicia o servidor
if __name__ == "__main__":
    app.run(debug=True, port=5000)