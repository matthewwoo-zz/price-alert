from flask import Blueprint

item_blueprint = Blueprint('items', __name__)
# __name__ is unique to this file so that the flask application can find this file

@item_blueprint.route('/item/<string:name>')
def item_page():
    pass


@item_blueprint.route('/load')
def load_item():
    pass