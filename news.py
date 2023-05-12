from flask import Blueprint, render_template
news_bp = Blueprint('news', __name__, url_prefix="/news")


@news_bp.route('/')
def news():
    return "<p>Hello, this is the news</p> <button>btn</button>"