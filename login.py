from flask import Blueprint, render_template, request
login_bp = Blueprint('login', __name__, url_prefix="/login")


@login_bp.route('/', methods=['GET','POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    # if username == 'amit' and password == '123': return 'amit'
    if username and password: return str(int(username) + int(password))
    return render_template('login.html')