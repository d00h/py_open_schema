from typing import Any, Optional

from flask import Flask
from marshmallow_dataclass import dataclass

from open_schema import route
from open_schema.backends.flask import register_endpoints
from open_schema.backends.swagger import generate_swagger


@dataclass
class User:
    email: str


@dataclass
class Answer:
    success: bool
    code: Optional[str] = None
    data: Optional[Any] = None


@route("user_get") \
    .request("/user/<user_id>/", methods=["GET"]) \
    .response(200, Answer(success=True, data=User)) \
    .response(404, Answer(success=True, code="USER_NOT_FOUND"))
def user_get(user_id):
    if user_id == 2:
        return 200, Answer(success=True, data=User(email="user@email.com"))
    return 404, Answer(success=True, code="USER_NOT_FOUND")


@route("user_post") \
    .request("/user/<user_id>/", methods=["POST"], body=User) \
    .response(200, Answer(success=True)) \
    .response(400, Answer(success=False, code="PARAMS_ERROR"))
def user_post(user_id, user: User):
    print(user.email)
    return 200, Answer(success=True)


@route("swagger") \
    .request("/apispec.json", methods=["GET"]) \
    .response(200, model=dict)
def apispec():
    return generate_swagger()


if __name__ == '__main__':
    app = Flask(__name__)
    register_endpoints(app)
    app.run(port=5000, host="127.0.0.1")
