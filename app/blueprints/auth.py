from flask import Blueprint, request, jsonify, Response
from extentions import db
from config.config import APP_ID, SECRET
from config.config import BUCKET, ACCESS_KEY, SECRET_KEY
import requests
import qiniu


auth = Blueprint('auth', __name__)

q = qiniu.Auth(ACCESS_KEY, SECRET_KEY)


@auth.get('/jscode2session')
def get_jscode() -> Response:
    js_code = request.args['js_code']
    url = f'https://api.weixin.qq.com/sns/jscode2session?appid={APP_ID}&secret={SECRET}&js_code={js_code}&grant_type=authorization_code'
    response = requests.get(url)
    if (response.status_code == 200):
        return response.json()
    else:
        return Response(status=400, response='Bad Request')


@auth.get('/imageUploadToken')
def get_upload_token() -> Response:
    token = q.upload_token(BUCKET)
    return dict(uptoken=token)
