from sqlalchemy.orm.exc import NoResultFound
from ..entities.people import PeopleTable
from ..entities.pets import PetsTable
from ..interfaces.people_repository import PeopleRepositoryInterface


class PeopleRepository(PeopleRepositoryInterface):

    def __init__(self, db_connection):
        self.__db_connection = db_connection
    
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int):

        try:
            with self.__db_connection as database:

                person = PeopleTable(
                    first_name = first_name,
                    last_name = last_name,
                    age = age,
                    pet_id = pet_id
                )

                database.session.add(person)
                database.session.commit()
        except Exception as exception:
            database.session.rollback()
            raise exception

    def get_person(self, person_id: int) -> PeopleTable:

        with self.__db_connection as database:
            try:

                person_data = (
                    database.session
                        .query(PeopleTable) #Onde vou realizar a query
                        .outerjoin(PetsTable, PetsTable.id == PeopleTable.pet_id) #Join com PetsTable
                        .filter(PeopleTable.id == person_id)
                        .with_entities(
                            PeopleTable.first_name,
                            PeopleTable.last_name,
                            PetsTable.name.label("pet_name"),
                            PetsTable.type.label("pet_type"),
                        ).one()
                )
                return person_data
            
            except NoResultFound:
                return None 
