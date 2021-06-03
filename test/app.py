from flask import Flask
from views.home import home
from views.admin import admin

app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(admin)

if __name__ == '__main__':

    app.run()