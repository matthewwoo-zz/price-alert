from flask import Flask, render_template

from src.common.database import Database

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = "123"
# app.secret key is used to keep the cookies are servers are using to track users safe

@app.before_first_request
def init_db():
    Database.initialize()

from src.models.users.views import user_blueprint
app.register_blueprint(user_blueprint, url_prefix="/users")
# http://flask.pocoo.org/docs/0.10/blueprints/ shows you how to register a blueprint