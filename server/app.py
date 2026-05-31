from flask import Flask, jsonify, request
from flask_cors import CORS
import json

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
        "preco": 8.50,
        "status": "DISPONIVEL"
    })

# Fileira B: 12 assentos
for i in range(1, 13):
    assentos.append({
        "codigo": f"B{i}",
        "preco": 12.00,
        "status": "DISPONIVEL"
    })

# Fileira C: 12 assentos
for i in range(1, 13):
    assentos.append({
        "codigo": f"C{i}",
        "preco": 12.00,
        "status": "DISPONIVEL"
    })

# Fileira D: 10 assentos
for i in range(1, 11):
    assentos.append({
        "codigo": f"D{i}",
        "preco": 15.00,
        "status": "DISPONIVEL"
    })

# Alguns assentos começam reservados para teste
'''assentos[2]["status"] = "RESERVADO"
assentos[5]["status"] = "RESERVADO"
assentos[14]["status"] = "RESERVADO"
'''

# Endpoint para listar os assentos
@app.route("/api/assentos", methods=["GET"])
def listar_assentos():
    with open('Data/seats.json', 'w') as file:
        json.dump(assentos, file, sort_keys=True, indent=4, ensure_ascii=False)
    return jsonify(assentos)

# Endpoint para reservar assentos
@app.route("/api/reservas", methods=["PUT"])
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

@app.route("/api/get_list", methods=["GET"])
def get_dictionary():
    num = request.args.get('num')
    url = f'Data/AssentosPorSala/seats_{num}.json'
    
    # CORREÇÃO: usar a variável url, não a string "url"
    with open(url, "r") as file:  
        seats = json.load(file)

    html = f"""
    <div class="seat-grid">
        <div class="row" style="padding-right: 20px; font-size: 18px">
    """
    for seat in seats:
        if seat["codigo"].startswith("A"):
            position = f"""
            <div class="seat" data-price="{seat["preco"]}">{seat["codigo"]}</div>
            """
            html += position
    html += f"""
        </div>
        <div class="row" style="padding-right: 20px; font-size: 18px">
    """

    for seat in seats:
        if seat["codigo"].startswith("B"):
            position = f"""
            <div class="seat" data-price="{seat["preco"]}">{seat["codigo"]}</div>
            """
            html += position
    html += f"""
        </div>
        <div class="row" style="padding-right: 20px; font-size: 18px">
    """

    for seat in seats:
        if seat["codigo"].startswith("C"):
            position = f"""
            <div class="seat" data-price="{seat["preco"]}">{seat["codigo"]}</div>
            """
            html += position
    html += f"""
        </div>
        <div class="row" style="padding-right: 20px; font-size: 18px">
    """

    for seat in seats:
        if seat["codigo"].startswith("D"):
            position = f"""
            <div class="seat" data-price="{seat["preco"]}">{seat["codigo"]}</div>
            """
            html += position



    html += f"""
        </div>
    </div>"""
    return html



# Inicia o servidor
if __name__ == "__main__":
    app.run(debug=True, port=5000)