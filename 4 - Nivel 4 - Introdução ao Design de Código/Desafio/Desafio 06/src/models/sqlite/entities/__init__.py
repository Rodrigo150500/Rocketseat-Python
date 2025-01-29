from src.models.sqlite.settings.base import Base
from sqlalchemy import Column, String, Integer


class PeopleTable(Base):

    __tablename__ = "People_table"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    pet_id = Column(Integer, nullable=False)
