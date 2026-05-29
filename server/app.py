from flask import Flask, jsonify, request
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

# Endpoint para reservar assentos
@app.route("/api/reservas", methods=["POST"])
def reservar():
    dados = request.get_json()
    codigos = dados.get("assentos", [])

    for codigo in codigos:
        for assento in assentos:
            if assento["codigo"] == codigo:
                if assento["status"] == "RESERVADO":
                    return jsonify({
                        "erro": f"Assento {codigo} já reservado"
                    }), 400

                assento["status"] = "RESERVADO"

    return jsonify({
        "mensagem": "Reserva realizada com sucesso"
    })

# Inicia o servidor
if __name__ == "__main__":
    app.run(debug=True, port=5000)