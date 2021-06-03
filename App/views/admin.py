from flask import Blueprint, render_template, request, redirect
admin = Blueprint("admin", __name__, template_folder='templates')


# 模块拦截器  判断用户是否 登录成功
@admin.before_request
def before_user():
    name = request.cookies.get('username')
    if name:
        pass
    else:
        return redirect('/login')


@admin.route('/admin')
def index():
    return render_template('admin.html')