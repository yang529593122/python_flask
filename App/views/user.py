from flask import Blueprint, render_template, request, redirect, make_response
from models.mysql import db
user = Blueprint("user", __name__, template_folder='templates')


@user.route('/login', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username']  # 获取表单提交的数据
        password = request.form['password']
        sql = "SELECT name, password FROM user_list WHERE name='%s' and password='%s'" % (username, password)
        data = db.select_db(sql)
        if data:
            resp = make_response(redirect('/home'))
            resp.set_cookie('username', data[0]['name'])
            return resp
        else:
            return '账号或密码错误'


@user.route('/loginOut')
def del_cookie():
    resp = make_response(redirect('/home'))
    resp.delete_cookie('username')
    return resp

