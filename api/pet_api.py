import requests


class PetAPI:
    def __init__(self, base_url: str, api_logger):
        self.base_url = base_url
        self.api_logger = api_logger

    def get_pets_by_status(self, status: str):
        from models.pet import Pet

        endpoint = f'{self.base_url}/pet/findByStatus'
        params = {'status': status}

        self.api_logger.info(f'Requesting: {endpoint} with params: {params}')
        response = requests.get(endpoint, params=params)
        pets = Pet.from_response(response.json())

        self.api_logger.info(f'Response Status Code: {response.status_code}')

        return pets, response.status_code

    ## / create method to create a new pet
    def create_pet(self, pet_data: dict):
        endpoint = f'{self.base_url}/pet'
        self.api_logger.info(f'Creating pet with data: {pet_data}')
        response = requests.post(endpoint, json=pet_data)
        self.api_logger.info(f'Response Status Code: {response.status_code}')
        return response.json(), response.status_code


