import asyncio

from logic import ApartmentLogic
from parser import Parser


logic = ApartmentLogic()
parser = Parser()


async def main():
    parsed = []
    last_page = await parser.get_last_page()

    await asyncio.gather(*(parser.parse_page(i, parsed) for i in range(1, last_page + 1)))
    await asyncio.gather(*(logic.create_apartment(i) for i in parsed))


asyncio.run(main())
