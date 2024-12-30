from sqlalchemy import create_engine


class DBConnectionHandle:
    def __init__(self) -> None:
        self.__connction_string = "sqlite:///storage.db"
        self.__engine = None
    
    def conect_to_db(self):
        self.__engine = create_engine(self.__connction_string)

    def get_engine(self):
        return self.__engine


db_connect_handler = DBConnectionHandle()
