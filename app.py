from flask import Flask, send_file, render_template, request
from bot import obtener_lenguajes_top
from database import inicializar_db, obtener_historico

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        datos = obtener_lenguajes_top()  # Forzar actualización
    else:
        datos = obtener_lenguajes_top()
    return render_template("index.html", datos=datos)

@app.route("/historico")
def historico():
    registros = obtener_historico()
    return render_template("historicos.html", registros=registros)

if __name__ == "__main__":
    inicializar_db()
    app.run(debug=True)

