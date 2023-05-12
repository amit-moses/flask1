from flask import Blueprint, render_template
news_bp = Blueprint('news', __name__, url_prefix="/news")


@news_bp.route('/')
def news():
    news_list=['eurovision', 'gaza', 'demonstrations', 'rockets']
    return render_template('news.html', news = news_list)