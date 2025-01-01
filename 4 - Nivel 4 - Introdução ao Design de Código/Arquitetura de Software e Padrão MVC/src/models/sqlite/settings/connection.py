from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHanlder:
    def __init__(self) -> None:
        self.__conection_string = "sqlite:///C:/Users/Rodrigo/Desktop/Rocketseat-Python/4 - Nivel 4 - Introdução ao Design de Código/Arquitetura de Software e Padrão MVC/storage.db"

        self.__engine = None
        self.session = None

    def conect_to_db(self):
        self.__engine = create_engine(self.__conection_string)

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker()

        self.session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


db_connect_handler = DBConnectionHanlder()