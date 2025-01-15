from typing import List
from sqlalchemy.orm.exc import NoResultFound
from ..entities.pets import PetsTable
from ..interfaces.pets_repository import PetsRepositoryInterface

class PetsRepository(PetsRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def list_pets(self) -> List[PetsTable]:
        with self.__db_connection as database:
            try:
                pets = database.session.query(PetsTable).all()
                return pets
            except NoResultFound:
                return []
    
    def delete_pet(self, name: str) -> None:
        with self.__db_connection as database:
            try:
                (
                database.session.query(PetsTable)
                    .filter(PetsTable.name == name)
                    .delete()

                )
                database.session.commit()
            
            except Exception as exception:
                database.session.rollback()
                raise exception
