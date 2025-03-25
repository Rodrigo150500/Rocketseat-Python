from src.models.repositories.user_repository import UserRepository
from .interfaces.list_all_tasks_by_user_id_interface import ListAllTasksByUserIdInterface


class ListAllTasksByUserIdController(ListAllTasksByUserIdInterface):

    def __init__(self, repository: UserRepository) -> None:
        self.__repository = repository
    
    def list(self, user_id: int) -> dict:

        tasks = self.__repository.list_all_tasks_by_user_id(user_id)

        formatted_response = self.__formated_response(user_id, tasks)

        return formatted_response

    def __formated_response(self, user_id: int, tasks: list) -> dict:
        
        task_list = []

        for task in tasks:
            task_list.append(task[2])
        
        return {
            "data":{
                "operation": "list tasks",                
                "user_id": user_id,
                "tasks": task_list,
                "tasks_count": len(task_list)                
            }
        }

