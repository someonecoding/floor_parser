from db import async_session
from models import Apartment


class ApartmentLogic:
    def __init__(self):
        self.session = async_session

    async def create_apartment(self, apartment_data):
        async with self.session() as session:
            apartment_obj = Apartment(**apartment_data)
            session.add(apartment_obj)
            await session.commit()

        return True
