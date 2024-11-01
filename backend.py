from flask import Flask, render_template  #com jsonify dá para converter valores em javascript para uma String JSON

app=Flask(__name__,template_folder='template')

@app.route("/")  #primeira pagina (homepage)
def homepage():
    return "hahaaaaaaaaaaaaaaaaaaaaaauuuuu"


@app.route("/nivel1")
def primeironivel():
    return render_template("network.html") # render_template busca a pasta template onde deve estar os html

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
