import asyncio
from logic import ApartmentLogic


logic = ApartmentLogic()
a_obj = {"title": "ASDASD"}


async def main():
    await logic.create_apartment(apartment_data=a_obj)


asyncio.run(main())
