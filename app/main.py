import asyncio

from logic import ApartmentLogic
from parser import Parser


logic = ApartmentLogic()
parser = Parser()


async def main():
    res = await parser.parse_page(33)
    raw_html = res[1]
    clean_data = parser.extract_data(raw_html)


asyncio.run(main())
