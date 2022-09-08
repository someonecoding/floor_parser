from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config import settings


Base = declarative_base()

engine = create_async_engine(settings.DATABASE_URL, echo=True)

async_session = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
