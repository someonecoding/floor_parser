from db import Base
from sqlalchemy import Column, Integer, Float, String, Date

from datetime import date


class Apartment(Base):
    __tablename__ = "apartments"
    id = Column(Integer, primary_key=True, index=True)
    img_url = Column(String)
    title = Column(String)
    date_created = Column(Date, default=date.today())
    city = Column(String)
    beds = Column(String)
    description = Column(String)
    price = Column(Float)
    currency = Column(String)
