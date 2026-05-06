from flask import Flask
app = Flask(__name__)

@app.route("/")
def inicio():
	return """
	<h1>Calculadora del Millonario</h1>
	<p>Bienvenido Miguel!<p>
	<p>Con 1 millon de usuarios ganas: <b>$10,000</b></p>
	<p>Con 10 millones de usuarios ganas: <b>$100,000</b></p>
	<p>Con 100 millones de usuarios ganas. <b>$1,000,000</b></p>
	"""

app.run(host="0-0.0.0", port=10000)