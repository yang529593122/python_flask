from flask import Blueprint, render_template, redirect, url_for
from models.mysql import db
home = Blueprint("home", __name__, template_folder='templates')


@home.route('/')
def index_home():
    return redirect('/home')


@home.route('/home')
def index():
    sql = "SELECT * FROM article"
    data = db.select_db(sql)
    print(data)
    return render_template('index.html', articledata=data)