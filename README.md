# BJUT Cats Mini Program Server

## Getting Started

### Using Shell Script

```shell
$ chmod +x start.sh
$ ./start.sh
```

### Manually

```shell
$ python3 -m venv .venv
> .venv\Scripts\activate (for Windows)
$ source .venv/bin/activate (for macOS)
```

```shell
% pip install -r requirements.txt
$ python3 app/app.py
```

### API Endpoints

```text
Endpoint               Methods  Rule
---------------------  -------  --------------------------
articles.get_all       GET      /api/articles/
auth.get_jscode        GET      /api/jscode2session
auth.get_upload_token  GET      /api/imageUploadToken
cats.all_cats          GET      /api/cats/
cats.create_cat        POST     /api/cats/
cats.remove_all        DELETE   /api/cats/
images.add_image       POST     /api/images/
images.get_by_state    GET      /api/images/<string:state>
images.update_image    PUT      /api/images/
static                 GET      /static/<path:filename>
users.create_user      POST     /api/users/
users.get_user         GET      /api/users/<openId>
```
