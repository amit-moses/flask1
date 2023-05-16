from flask import Flask
from news import news_bp
from login import login_bp

app = Flask(__name__)
app.register_blueprint(news_bp)
app.register_blueprint(login_bp)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p> <button>press</button"



app.run()