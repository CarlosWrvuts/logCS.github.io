from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    usuario = request.form.get("usuario")
    contrasena = request.form.get("contrasena")

    # Verificar usuario y contraseña
    if usuario == "admin" and contrasena == "12345":
        return "<h2>Inicio de sesión exitoso!</h2><img src='imagen.jpg'>"
    else:
        return "<script>alert('Usuario o contraseña incorrectos');</script>"

if __name__ == "__main__":
    app.run()
