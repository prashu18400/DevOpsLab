from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h3>Hi Guys, hope you learnt alot from the session</h3> <br/> <p>For more such sessions, please notify a week prior and I expect the efforts from your side as well</p>"

