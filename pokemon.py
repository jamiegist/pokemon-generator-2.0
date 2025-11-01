from flask import Flask

app = Flask(__name__)
    
@app.route("/")
def index():
    return "<p>This is a Pokemon generator</p>"

app.run(host="0.0.0.0", port=80)