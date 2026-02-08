class PetQueries:
    @staticmethod
    def get_pets_count_by_status(status: str) -> str:
        return f"SELECT COUNT(*) FROM pets WHERE status = '{status}'"