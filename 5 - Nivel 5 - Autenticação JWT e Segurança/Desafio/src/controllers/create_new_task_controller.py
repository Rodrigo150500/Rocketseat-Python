from src.models.repositories.interfaces.user_repository_interface import UserRepositoryInterface
from .interfaces.create_new_task_interface import CreateNewTaskInterface

class CreateNewTaskController(CreateNewTaskInterface):
    
    def __init__(self, repository: UserRepositoryInterface) -> None:
        self.__repository = repository

    def create(self, user_id: int, task_name: str, task_detail: str) -> dict:

        self.__repository.create_new_task(user_id, task_name, task_detail)

        formatted_reponse = self.__format_response(user_id, task_name)

        return formatted_reponse

    def __format_response(self,user_id: int, task_name: str) -> dict:
        return {
            "data":{
                "operation":"create task",
                "task_name": task_name,
                "user_id": user_id

            }
        }
        
