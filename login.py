#!/usr/bin/env python3

import cgi

# Obtener los datos del formulario
form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")

# Comprobar las credenciales (aquí puedes usar tu propia lógica de autenticación)
if username == "admin" and password == "password":
    print("Content-type: text/html")
    print()
    print("<h1>Bienvenido, {}</h1>".format(username))
else:
    print("Content-type: text/html")
    print()
    print("<h1>Error de inicio de sesión</h1>")
