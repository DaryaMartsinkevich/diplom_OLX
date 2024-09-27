from services.store_swagger_service import StoreSwaggerService


def test_post_order_pet():
    store = StoreSwaggerService()
    order_id = 5
    pet_id = 10
    response = store.post_order_pet(order_id, pet_id)
    assert response['id'] == order_id
    assert response['petId'] == pet_id


def test_get_store():
    store = StoreSwaggerService()
    order_id = 5
    response = store.get_order_id(order_id)
    assert response['id'] == order_id


def test_delete_store():
    store = StoreSwaggerService()
    response = store.delete_order_id(5)
    assert response['code'] == 200

