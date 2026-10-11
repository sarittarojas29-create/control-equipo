import sqlite3
from datetime import date
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def conectar():
    conexion = sqlite3.connect("equipo.db")
    conexion.row_factory = sqlite3.Row
    return conexion

def crear_tabla():
    conexion = conectar()
    conexion.execute(
        "CREATE TABLE IF NOT EXISTS equipo ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "nombre TEXT NOT NULL, "
        "responsable TEXT NOT NULL, "
        "fecha_entrega TEXT NOT NULL, "
        "devuelto INTEGER NOT NULL DEFAULT 0)"
    )
    conexion.commit()
    conexion.close()

@app.route("/")
def inicio():
    conexion = conectar()
    equipo = conexion.execute(
        "SELECT *, "
        "CASTE(julianday('now') - julianday(fecha_entrega) AS INTEGER) AS dias "
        "FROM equipo"
    ). fetchall()
    conexion.close()
    return render_template("index.html", equipo=equipo)

@app.route("/agregar", methods=["POST"])
def agregar():
    nombre = request.form["nombre"]
    responsable = request.form["responsable"]
    fecha = date.today().isoformat()
    conexion = conectar()
    conexion.execute(
        "INSERT INTO equipo (nombre, responsable, fecha_entrega) VALUES (?, ?, ?)",
        (nombre, responsable, fecha),
    )
    conexion.commit()
    conexion.close()
    return redirect("/")

@app.route("/borrar/<int:id>", methods=["POST"])
def borrar(id):
    conexion = conectar()
    conexion.execute("DELETE FROM equipo WHERE id = ?", (id,))
    conexion.commit()
    conexion.close()
    return redirect("/")

@app.route("/devolver/<int:id>", methods=["POST"])
def devolver(id):
    conexion = conectar()
    conexion.execute("UPDATE equipo SET devuelto = 1 WHERE id = ?", (id,))
    conexion.commit()
    conexion.close()
    return redirect("/")

if __name__=="__main__":
    crear_tabla()
    app.run(debug=True)