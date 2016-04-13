from flask import Blueprint

store_blueprint = Blueprint('stores', __name__)
# __name__ is unique to this file so that the flask application can find this file


@store_blueprint.route('/store/<string:name>')
def store_page():
    pass
