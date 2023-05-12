from flask import Flask
from news import news_bp

app = Flask(__name__)
app.register_blueprint(news_bp)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



app.run()