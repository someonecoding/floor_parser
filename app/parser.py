import aiohttp
from bs4 import BeautifulSoup
import datetime


class Parser:
    def get_page_url(self, num):
        url = f"https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{num}/c37l1700273"
        return url

    async def parse_page(self, page):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.get_page_url(page)) as response:
                html = await response.text()
                return str(response.url), html

    def extract_data(self, raw_html):
        soup = BeautifulSoup(raw_html, "html.parser")
        apartments = soup.findAll("div", {"data-listing-id": True})
        extracted = []
        for apartment in apartments:
            info = apartment.find("div", {"class": "info-container"})
            rental_info = apartment.find("div", {"class": "rental-info"})
            full_price = " ".join(info.find("div", {"class": "price"}).text.split()).replace(",", "")
            try:
                image_block = apartment.find("div", {"class": "image"})
            except Exception:
                pass

            clean_data = {
                "title": info.find("div", {"class": "title"}).find("a").contents[0].strip(),
                "city": info.find("div", {"class": "location"}).find("span").text.strip(),
                "beds": " ".join(rental_info.find("span", {"class": "bedrooms"}).text.strip().split()),
                "description": " ".join(info.find("div", {"class": "description"}).text.split()),
            }

            try:
                clean_data["price"] = float(full_price[1::])
                clean_data["currency"] = full_price[0]
            except ValueError:
                pass

            try:
                clean_data["img_url"] = image_block.find("picture").find("source")["data-srcset"]
            except Exception:
                pass

            raw_date = info.find("div", {"class": "location"}).find("span", {"class": "date-posted"}).text
            if raw_date[0] == "<":
                pass
            else:
                clean_data["date_created"] = datetime.datetime.strptime(raw_date, "%d/%m/%Y").date()

            extracted.append(clean_data)

        return extracted

    def get_page_from_url(self, url):
        splitted = str(url).split("/")[5].split("-")
        return int(splitted[1])

    async def get_last_page(self):
        # Hardcode :D
        res = await self.parse_page(99999999)
        return int(self.get_page_from_url(res[0]))
