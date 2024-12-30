from sqlalchemy import BIGINT, String, Column

class PetsTable:

    __tablename__ = 'pets'

    id = Column(BIGINT, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)

    def __repr__(self):
        return f"Pets [name={self.name}, type={self.type}]"        