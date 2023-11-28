from flask import Blueprint, request, jsonify, Response
from models.cats import Cats
from extentions import db

cats = Blueprint('cats', __name__)


"""Get all cats info in the db

Returns:
    JSON: a list of cats
"""


@cats.get('/')
def all_cats() -> Response:
    all_cats: list[Cats] = Cats.query.all()
    return jsonify([cat.to_dict() for cat in all_cats])
