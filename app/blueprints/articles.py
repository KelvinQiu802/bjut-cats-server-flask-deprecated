from flask import Blueprint, request, jsonify, Response
from models.articles import Articles
from extentions import db


articles = Blueprint('articles', __name__)


@articles.get('/')
def get_all() -> Response:
    all_articles: list[Articles] = Articles.query.all()
    return jsonify([ar.toDict() for ar in all_articles])
