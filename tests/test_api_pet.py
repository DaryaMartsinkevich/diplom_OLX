from services.pet_swagger_service import PetSwaggerService


def test_post_pet():
    pet = PetSwaggerService()
    pet_id = 10
    pet_name = 'Ola'
    response = pet.post_pet_store(pet_id, pet_name)
    assert response['name'] == pet_name


def test_get_pet():
    pet = PetSwaggerService()
    response = pet.get_pet_id(10)
    assert response['name'] == 'Ola'


def test_put_pet():
    pet = PetSwaggerService()
    response = pet.post_pet_store(10, 'Ola')
    assert response['name'] == 'Ola'


def test_delete_pet():
    pet = PetSwaggerService()
    response = pet.delete_pet_id(10)
    assert response['code'] == 200
