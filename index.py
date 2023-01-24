from flask import Flask, render_template

app = Flask(__name__)
# Uma página tem uma rota e uma função
# route -> É o endereço, ex.: redss.com.br/contato
# function -> O que será exibido na página

@app.route("/")
def homepage():
  return render_template("index.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
  return render_template("usuarios.html", nome_usuario=nome_usuario)

@app.route("/contato")
def contato():
  return render_template("contato.html")

if __name__ == "__main__":
  app.run(debug=True)