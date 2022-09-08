import asyncio

# from logic import ApartmentLogic
from parser import Parser


# logic = ApartmentLogic()
parser = Parser()
a_obj = {"title": "ASDASD"}


async def main():
    # await logic.create_apartment(apartment_data=a_obj)
    res = await parser.parse_page(33)
    raw_html = res[1]
    parser.extract_data(raw_html)


asyncio.run(main())

while True:
    pass
