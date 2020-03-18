import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Flask</h1><p>This is a sample api call!!</p>"

app.run(host="0.0.0.0",port=80)
