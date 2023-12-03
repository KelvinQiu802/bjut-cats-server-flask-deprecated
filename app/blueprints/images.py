from flask import Blueprint, request, jsonify, Response
from models.images import Images
from extentions import db


images = Blueprint('images', __name__)


@images.post('/')
def add_image() -> Response:
    new_image = Images(**request.json)
    db.session.add(new_image)
    db.session.commit()
    return Response(status=204, response='New Image Added')


@images.get('/<string:state>')
def get_by_state(state) -> Response:
    images: list[Images] = Images.query.filter(
        Images.state == state).all()
    return jsonify([image.toDict() for image in images])


@images.put('/')
def update_image() -> Response:
    image: Images = Images.query.get(request.json['imageUrl'])
    image.state = request.json['state']
    image.campus = request.json['campus']
    image.catName = request.json['catName']
    db.session.commit()
    return Response(status=200, response="Update Success")
