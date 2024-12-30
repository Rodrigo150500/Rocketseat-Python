from sqlalchemy import BIGINT, String, Column, ForeignKey

class PeopleTable:

    __tablename__ = "people"

    id = Column(BIGINT, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(BIGINT, nullable=False)
    pet_id = Column(BIGINT, ForeignKey("pets.id"))

    def __repr__(self):
        return f"People [name={self.first_name}, last_name={self.last_name}, pet_id={self.pet_id}]"
