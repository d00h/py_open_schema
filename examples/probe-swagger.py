from marshmallow_dataclass import dataclass

from open_schema import route


@dataclass
class UserNotFound:
    success: bool = False
    code: str = 'USER_NOT_FOUND'


@dataclass
class SuccessDataAppsflyer:

    appsflyer_id: str
    advertising_id: str


@dataclass
class SuccessData:
    email: str
    phone: str
    apple_email: str
    fb_email: str
    google_email: str
    google_email: str
    appsflyer: SuccessDataAppsflyer


@dataclass
class Success:

    success: bool = True
    data: SuccessData

    @classmethod
    def example(cls) -> 'Success':
        return cls()


@route("user_get") \
    .doc("какая то фигня") \
    .request("/user/<user_id>/", methods=["GET"]) \
    .response(status_code=200, model=Success) \
    .response(status_code=400, model=UserNotFound)
def endpoint(user_id):
    try:
        db_session = app.db_session
        user = get_user(user_id)
        return 200, Success(
            data=SuccessData(
                email=user.email,
            )
        )
    except UserNotFound:
        return 400, UserNotFound()


def get_user(db_session, user_id):
    users = UserRepository(db_session)
    user = users.get_by_id(user_id)
    if user is None:
        raise UserNotFound(user_id=user_id)
    return user
