from typing import Optional, List


class Category:
    def __init__(self, data: dict):
        self.id: Optional[int] = data.get('id')
        self.name: Optional[str] = data.get('name')


class Tag:
    def __init__(self, data: dict):
        self.id: Optional[int] = data.get('id')
        self.name: Optional[str] = data.get('name')


class Pet:
    def __init__(self, data: dict):
        self.id: Optional[int] = data.get('id')
        self.name: Optional[str] = data.get('name')
        self.status: Optional[str] = data.get('status')
        self.photo_urls: List[str] = data.get('photoUrls', [])

        category_data = data.get('category')
        self.category: Optional[Category] = Category(category_data) if category_data else None

        tags_data = data.get('tags', [])
        self.tags: List[Tag] = [Tag(tag) for tag in tags_data]

    @classmethod
    def from_response(cls, response_data) -> 'list[Pet] | Pet':
        if isinstance(response_data, list):
            return [cls(pet_data) for pet_data in response_data]
        return cls(response_data)

    # ## /create class that will create and init pet_data for create_pet method in pet_api.py
    # @classmethod
    # def create_pet_data(cls, name: str, status: str, category_id: Optional[int] = None, category_name: Optional[str] = None, photo_urls: Optional[List[str]] = None, tags: Optional[List[dict]] = None) -> dict:
    #     pet_data = {
    #         "name": name,
    #         "status": status,
    #         "photoUrls": photo_urls or [],
    #         "tags": tags or [],
    #         "category": {
    #             "id": category_id,
    #             "name": category_name
    #         } if category_id is not None and category_name is not None else None
    #     }
    #     return pet_data

# / new class to represent pet_data in create_pet method in pet_api.py
class PetData:
    def __init__(self, name: str, status: str, category_id: Optional[int] = None, category_name: Optional[str] = None, photo_urls: Optional[List[str]] = None, tags: Optional[List[dict]] = None):
        self.name = name
        self.status = status
        self.photo_urls = photo_urls or []
        self.tags = tags or []
        self.category = {
            "id": category_id,
            "name": category_name
        } if category_id is not None and category_name is not None else None

    def to_dict(self) -> dict:
        # handle case if category is empty and set it to N/A
        if self.category is None:
            self.category = {
                "id": None,
                "name": "N/A"
            }
        return {
            "name": self.name,
            "status": self.status,
            "photoUrls": self.photo_urls,
            "tags": self.tags,
            "category": self.category
        }

