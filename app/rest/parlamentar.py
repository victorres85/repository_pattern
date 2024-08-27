""" Parlamentar REST_API Endpoints """

from flask import Blueprint

parlamentar_api_blueprint = Blueprint("parlamentar", __name__)


@parlamentar_api_blueprint.route("/parlamentar", methods=["GET", "POST"])
def add_parlamentar():
    pass
