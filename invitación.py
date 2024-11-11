from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

# Zona horaria de Perú
zona_horaria = pytz.timezone("America/Lima")

@app.route("/")
def invitacion():
    hora_actual = datetime.now(zona_horaria).strftime("%H:%M:%S")
    return render_template("invitacion.html", hora_actual=hora_actual)

@app.route("/ubicacion")
def abrir_ubicacion():
    url_ubicacion = "https://maps.app.goo.gl/mPNiEeQMSp4KLjSL6"  # Enlace a Google Maps
    return f"<script>window.location.href='{url_ubicacion}';</script>"

@app.route("/regalos")
def abrir_regalos():
    url_regalos = "/mnt/data/ListaRegalos.xlsx"  # Ruta al archivo Excel
    return f"<script>window.location.href='{url_regalos}';</script>"

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
