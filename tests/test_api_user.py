from services.user_swagger_service import UserSwaggerService


def test_post_user():
    user = UserSwaggerService()
    response = user.post_user('Ola', 'ola@gmail.com')
    assert response['code'] == 200


def test_get_user():
    user = UserSwaggerService()
    user_name = 'Ola'
    response = user.get_user(user_name)
    assert response['username'] == user_name


def test_put_user():
    user = UserSwaggerService()
    response = user.put_user('Ola', 'Ivanova', 'ola@gmail.com', '291234567')
    assert response['code'] == 200


def test_delete_user():
    user = UserSwaggerService()
    response = user.delete_user('Ola')
    assert response['code'] == 200


