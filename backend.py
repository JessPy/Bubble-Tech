from flask import Flask, render_template

app=Flask(__name__,template_folder='template')
# route -> hashtagtreinamentos.com/
# função -> o que você quer exibir naquela página
# template

@app.route("/")
def homepage():
    return "hahaaaaaaaaaaaaaaaaaaaaaauuuuu"


@app.route("/nivel1")
def primeironivel():
    return render_template("network.html")



# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

    # servidor do heroku