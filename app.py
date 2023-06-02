from flask import Flask, render_template, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "fatec"
app.config["MYSQL_DB"] = "Unes"

mysql = MySQL(app)

@app.route("/")
def renderIndex():
    return render_template("index.html")

@app.route("/quemsomos")
def renderQuemSomos():
    return render_template("quemsomos.html")

@app.route("/contato", methods=["GET", "POST"])
def renderContato():
    if request.method == "POST":
        email = request.form["email"]
        assunto = request.form["assunto"]
        descricao = request.form["descricao"]

        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute(f"insert into Contato(email, assunto, descricao) values('{email}', '{assunto}', '{descricao}');")
        conn.commit()
        cursor.close()
    
    return render_template("contato.html")

@app.route("/users")
def renderUsers():
    conn = mysql.connection
    cursor = conn.cursor()

    select = cursor.execute("select * from Contato")
    conn.commit()
    if select > 0:
        users = cursor.fetchall()
        cursor.close()
        return render_template("users.html", users=users)
    return render_template("users.html")
