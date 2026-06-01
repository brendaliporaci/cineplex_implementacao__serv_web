from flask import Flask, jsonify, request
from flask_cors import CORS
import json

# Cria a aplicação Flask
app = Flask(__name__)

# Permite comunicação entre frontend e backend
CORS(app)

# Lista que armazenará todos os assentos
assentos_base = []
assentos = [[],[],[]]

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

def conta_assentos(num):
    sala = assentos[int(num)-1]
    conta_a = 0
    conta_b = 0
    conta_c = 0
    conta_d = 0

    for seat in sala:
        if seat['codigo'].startswith('A'):
            conta_a += 1
        elif seat['codigo'].startswith('B'):
            conta_b += 1
        elif seat['codigo'].startswith('C'):
            conta_c += 1
        else:
            conta_d += 1
    
    contagem = [conta_a, conta_b, conta_c, conta_d]
    return contagem

def descobre_menor(contagem):
    menor = 0
    if contagem[0] <= contagem[1]:
        if contagem[0] <= contagem[2]:
            if contagem[0] <= contagem[3]:
                menor = 0
            else:
                menor = 3
        elif contagem[2] <= contagem [3]:
            menor = 2
        else:
            menor = 3
    elif contagem[1] <= contagem[2]:
        if contagem[1] <= contagem[3]:
            menor = 1
        else:
            menor = 3
    elif contagem[2] <= contagem[3]:
        menor = 2
    else:
        menor = 3
    
    return menor

# Endpoint para listar os assentos
@app.route("/api/assentos", methods=["GET"])
def listar_assentos():
    with open('Data/seats.json', 'w') as file:
        json.dump(assentos_base, file, sort_keys=True, indent=4, ensure_ascii=False)
    return jsonify(assentos)

# Endpoint para reservar assentos
@app.route("/api/reservas", methods=["POST"])
def reservar():
    dados = request.get_json()
    codigos = dados.get("assentos", [])

    for codigo in codigos:
        for assento in assentos_base:
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
    assentos[int(num)-1] = seats
    resposta = [html, seats]
    return resposta

@app.route("/api/add_seat", methods=["POST"])
def add_seat():
    num = request.args.get('num')
    url = f'Data/AssentosPorSala/seats_{num}.json'
    
    with open(url, "r") as file:  
        assentos[int(num)-1] = json.load(file)
    
    
    contagem = conta_assentos(num)
    menor = descobre_menor(contagem)
    carreira = ''
    
    if menor == 0:
        carreira = 'A'
    elif menor == 1:
        carreira = 'B'
    elif menor == 2:
        carreira = 'C'
    else:
        carreira = 'D'

    posicao = contagem[menor] + 1
    novo = {
        "codigo": carreira+ str(posicao),
        "preco": 12.0,
        "status": "DISPONIVEL"
    }
    #print(f"Novo:\n{novo}")
    assentos[int(num)-1].append(novo)
    print(assentos)
    with open(f'Data/AssentosPorSala/seats_{num}.json', 'w') as file:
        json.dump(assentos[int(num)-1], file, sort_keys=True, indent=4, ensure_ascii=False)
    return assentos[int(num)-1]


# Inicia o servidor
if __name__ == "__main__":
    app.run(debug=True, port=5000)