
import requests
import allure

from api.pet_api import PetAPI
from db.pet_db_connection import DBConnection
from db.pet_queriespy import PetQueries
from models.pet import Pet

@allure.feature('Pet API')
@allure.story('Find pets by status')
class TestPetAPI:

    @allure.title('Find pets with sold status')
    @allure.description('Test GET /pet/findByStatus endpoint with status=sold')
    def test_find_pets_by_sold_status(self, base_url, api_logger):


       # api_logger.info(f'Response Status Code: {response.status_code}')
        pet_api = PetAPI(base_url, api_logger)
        pets, status_code = pet_api.get_pets_by_status('sold')

        assert status_code == 200, f'Expected 200, got {status_code}'
        assert len(pets) > 0, 'Should return at least one pet with sold status'

        api_logger.info(f'Found {len(pets)} pets with sold status')

        for pet in pets:
            assert pet.status == 'sold', f'Pet status should be sold, got {pet.status}'

        # Database validation (ready to use once credentials are available)
        # db = DBConnection(host='your_host', port=3306, user='your_user', password='your_password', database='your_db')
        # db.connect()
        # try:
        #     query = PetQueries.get_pets_count_by_status('sold')
        #     result = db.execute_query(query)
        #     db_count = result[0][0]
        #     assert len(pets) == db_count, f'API returned {len(pets)} pets, but DB has {db_count}'
        # finally:
        #     db.disconnect()
    #teest
    def test_create_pet(self, base_url, api_logger):
        from models.pet import PetData
        name = 'Vmio'
        status = 'sold'

        pet_data = PetData(name, status, category_id=1, category_name='person', photo_urls=None, tags=None).__dict__
        pet_api = PetAPI(base_url, api_logger)
        created_pet, status_code = pet_api.create_pet(pet_data)

        assert status_code == 200, f'Expected 200, got {status_code}'
        assert created_pet['name'] == name, f'Expected name {name}, got {created_pet["name"]}'
        assert created_pet['status'] == status, f'Expected status {status}, got {created_pet["status"]}'

        api_logger.info(f'Created pet with ID: {created_pet["id"]}')