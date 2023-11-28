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


@cats.post('/')
def create_cat() -> Response:
    new_cat = Cats(**request.json)
    db.session.add(new_cat)
    db.session.commit()
    return Response(status=201, response=f'New Cats {request.json["name"]} Created')


@cats.delete('/')
def remove_all() -> Response:
    db.session.query(Cats).delete()
    db.session.commit()
    return Response(status=204, response="All Cats Removed")
