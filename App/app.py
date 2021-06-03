from flask import Flask
from views.home import home
from views.admin import admin
from views.user import user

app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(admin)
app.register_blueprint(user)

if __name__ == '__main__':
    # 参数 host port debug options
    # host 要监听的主机名 默认 127.0.0.1
    # port 端口  默认 500
    # debug  是否开启调试模式 默认 false  开启 true
    app.run(debug=True)