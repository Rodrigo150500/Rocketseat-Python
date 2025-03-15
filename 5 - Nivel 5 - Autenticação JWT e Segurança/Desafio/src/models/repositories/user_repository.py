from sqlite3 import Connection
from .interfaces.user_repository_interface import UserRepositoryInterface
from datetime import datetime

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

    def get_user_by_username(self, username: str) -> list(tuple[int, str, str]):
        cursor = self.__conn.cursor()

        cursor.execute(
            """
                SELECT id, username, password
                FROM users
                WHERE username = ?
            """, (username,)
        )

        user = cursor.fetchone()

        return user
    
    def list_all_tasks_by_user_id(self, user_id: int) -> tuple[int, str, str, str]:

        cursor = self.__conn.cursor()

        cursor.execute(
            """
                SELECT id, date_order, task_name, task_detail
                FROM orders
                WHERE user_id == ?
            """, (user_id,)
        ), 

        orders = cursor.fetchall()

        return orders

    def create_new_task(self, user_id: int, task_name: str, task_detail: str ) -> None:
        cursor = self.__conn.cursor()

        date = datetime.now()

        date_order = date.strftime("%d-%m-%Y %H:%M:%S")

        cursor.execute(
            """
                INSERT INTO orders
                    (user_id, date_order, task_name, task_detail)
                VALUES
                    (?, ?, ?, ?)
            """, (user_id, date_order, task_name, task_detail)
        )

        self.__conn.commit()