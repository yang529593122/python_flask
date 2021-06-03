from flask import Flask, request, redirect, url_for, make_response, Blueprint
from flask import render_template
from common.mysql_operate import db

app = Flask(__name__)


@app.route('/')
def hello_world():
    name = request.cookies.get('username')
    sql = "SELECT * FROM article"
    data = db.select_db(sql)

    if data:
        return render_template('index.html', data=data, username=name)
    return render_template('index.html', data='yang')


@app.route('/login', methods=['GET', 'POST'])
def hello_home():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        sql = "SELECT name, password FROM user_list WHERE name='%s' and password='%s'" % (username, password)
        data = db.select_db(sql)
        if data:
            resp = make_response(redirect(url_for('hello_world')))
            resp.set_cookie('username', data[0]['name'])
            return resp


@app.route('/loginout')
def login_out():
    resp = make_response(redirect(url_for('hello_world')))
    resp.delete_cookie('username')
    return resp


@app.route('/wait')
def wait():
    return render_template('index.html')


if __name__ == '__main__':

    # 参数 host port debug options
    # host 要监听的主机名 默认 127.0.0.1
    # port 端口  默认 500
    # debug  是否开启调试模式 默认 false  开启 true
    app.run(debug=True)
