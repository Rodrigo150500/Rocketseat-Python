'''
SINGLE RESPONSABILITY PRINCIPLE

Note que nessa classe, temos várias ações e responsabilidades. O que torna a manutenção, usabilidade e até a performance ruins.

Seguindo o conceito do Princípio da Responsabilidade única, organize essa classe e, se necessário, crie outras 
classes com suas devidas responsabilidades.

'''
from .crud.interface.crud_interface import CRUD_Interface

class TaskHandler:    
    def __init__(self, crud_handle: CRUD_Interface) -> None:
        self.__crud_handle = crud_handle
    
    