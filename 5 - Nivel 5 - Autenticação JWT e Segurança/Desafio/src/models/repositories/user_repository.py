from sqlite3 import Connection
from .interfaces.user_repository_interface import UserRepositoryInterface

class UserRepository(UserRepositoryInterface):
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
    

    def registry_user(self, name: str, password: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                INSERT INTO users
                    (username, password)
                VALUES
                    (?, ?);
            """, (name, password)
        )

        self.__conn.commit()

    #get_order_by_user_id

    #get_user_by_username

    #registry_order_by_id