# Идея

* Прослойка для генерации swagger на основе схем
* Валидации оного через тестирования
* Тестирования контроллера как отдельной сущности 

# Определение endpoint 


```python
from marshmallow_dataclass import dataclass

from open_schema import route


@route("user_get") \
    .doc("какая то фигня") \
    .path("/user/<user_id>/", methods=["GET"]) \
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

```

# Регистрация во flask 


```python
from flask import current_app 
from open_schema.backends.flask import register_endpoints

register_endpoints(current_app)
```


# Проверка через pytest 

```python
from open_schema.backends.pytest import HttpClient

def test_success():
    client = HttpClient("user_get", user_id=123)
    resp = client.request(json={})
  
```

# Генерация swagger 

```python
from open_schema.backends.swagger import generate_swagger 
from flask import current_app  as app

@app.route("/apispec.json")
def endpoint():
    spec = generate_swagger()
    retutn jsonify(spec)
```

# Тупо получение контроллера, например для отдельного тестирования


```python
from open_schema.backends.controller import get_controller 


controler = get_controller("user_get")
result = controller(user_id=123)

```

