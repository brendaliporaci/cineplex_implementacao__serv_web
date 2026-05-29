from flask import Flask, jsonify, request
from flask_cors import CORS

# Cria a aplicação Flask
app = Flask(__name__)

# Permite comunicação entre frontend e backend
CORS(app)

# Lista que armazenará todos os assentos
assentos = []

# Fileira A: 10 assentos
for i in range(1, 11):
    assentos.append({
        "codigo": f"A{i}",
        "preco": 800,
        "status": "DISPONIVEL"
    })

# Fileira B: 12 assentos
for i in range(1, 13):
    assentos.append({
        "codigo": f"B{i}",
        "preco": 1200,
        "status": "DISPONIVEL"
    })

# Fileira C: 12 assentos
for i in range(1, 13):
    assentos.append({
        "codigo": f"C{i}",
        "preco": 1200,
        "status": "DISPONIVEL"
    })

# Fileira D: 10 assentos
for i in range(1, 11):
    assentos.append({
        "codigo": f"D{i}",
        "preco": 1500,
        "status": "DISPONIVEL"
    })

# Alguns assentos começam reservados para teste
assentos[2]["status"] = "RESERVADO"
assentos[5]["status"] = "RESERVADO"
assentos[14]["status"] = "RESERVADO"

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