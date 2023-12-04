from flask import Blueprint, request, jsonify, Response
from models.imageLikes import ImageLikes
from extentions import db


imageLikes = Blueprint('imageLikes', __name__)


@imageLikes.get('/')
def get_all() -> Response:
    all_likes: list[ImageLikes] = ImageLikes.query.all()
    return jsonify([like.toDict() for like in all_likes])


@imageLikes.post('/')
def add() -> Response:
    new_like = ImageLikes(
        openId=request.json['openId'], imageUrl=request.json['imageUrl'], time=None)
    db.session.add(new_like)
    db.session.commit()
    return Response(status=204, response='New Like Added')
