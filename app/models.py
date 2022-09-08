from db import Base
from sqlalchemy import Column, Integer, Float, String, Date


class Apartment(Base):
    __tablename__ = "apartments"
    id = Column(Integer, primary_key=True, index=True)
    img_url = Column(String)
    title = Column(String)
    date_created = Column(Date)
    city = Column(String)
    beds = Column(Integer)
    description = Column(String)
    price = Column(Float)
    currency = Column(String)
