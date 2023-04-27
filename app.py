from flask import Flask, render_template, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_Host"] = "127.0.0.1"
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
        conn.cursor().execute(f"insert into Contato(email, assunto, descricao) values('{email}', '{assunto}', '{descricao}');")

        conn.commit()

        conn.cursor().close()
    
    return render_template("contato.html")