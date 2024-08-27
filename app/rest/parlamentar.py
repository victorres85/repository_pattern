""" Parlamentar REST_API Endpoints """

from flask import Blueprint, request, jsonify
from app.infrastructure.repository.parlamentar import ParlamentarRepository
from app.domain.parlamentar import ParlamentarDomain
from app import db

parlamentar_api_blueprint = Blueprint("parlamentar", __name__)


@parlamentar_api_blueprint.route("/parlamentar", methods=["GET", "POST"])  # type: ignore
def add_parlamentar():
    if request.method == "GET":
        parlamentar_id = request.args.get("id")
        response = ParlamentarRepository().get(int(parlamentar_id))  # type: ignore
        return jsonify({"data": response}), 200

    if request.method == "POST":
        parlamentar = ParlamentarDomain.model_validate_json(request.data)
        repo = ParlamentarRepository().add(parlamentar)
        return jsonify({"data": repo}), 201
    return None


@parlamentar_api_blueprint.route("/test_db")
def test_db():
    try:
        db.session.execute("SELECT 1")  # type: ignore
        return "Database connection successful!"
    except Exception as e:
        return str(e)
