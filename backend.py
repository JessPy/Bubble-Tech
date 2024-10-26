#from flask import Flask, jsonify #com jsonify dá para converter valores em javascript para uma String JSON


from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "eaee fiotee"
    
@app.route("/:p")
def haha():
    return "eae haha"
    
if __name__ == "__main__":
    #app.run(ssl_context=('cert.pem', 'key.pem'), debug=True) # HTTPS
    app.run(debug=True) #HTTP

