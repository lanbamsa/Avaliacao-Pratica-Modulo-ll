from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/somar", methods = ["Get"])
def somar():
    valor1 = float(request.args.get("valor1", 0))
    valor2 = float(request.args.get("valor2", 0))
    soma = valor1 + valor2 
    return jsonify({"somar": soma})

@app.route("/subtrair", methods = ["Get"])
def subtrair():
    valor1 = float(request.args.get("valor1", 0))
    valor2 = float(request.args.get("valor2", 0))
    soma = valor1 - valor2 
    return jsonify({"subtrair": subtrair})

@app.route("/multiplicar", methods = ["Get"])
def multiplicar():
    valor1 = float(request.args.get("valor1", 0))
    valor2 = float(request.args.get("valor2", 0))
    soma = valor1 * valor2 
    return jsonify({"multiplicar": multiplicação})

@app.route("/dividir", methods = ["Get"])
def dividir():
    valor1 = float(request.args.get("valor1", 0))
    valor2 = float(request.args.get("valor2", 0))
    soma = valor1 / valor2 
    return  Ssomify({"dividir": dividir})


if __name__ == "__main__":
    app.run(debug=True)