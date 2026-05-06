from flask import Flask
app = Flask(_name_)

@app.route("/")
def inicio():
    return """
    <h1>Calculadora del Millonario</h1>
    <p>Bienvenido Miguel!</p>
    <p>Con 1 millon de usuarios ganas: <b>$10,000</b></p>
    <p>Con 10 millones ganas: <b>$100,000</b></p>
    <p>Con 100 millones ganas: <b>$1,000,000</b></p>
    """