#Aplicando o princípio da responsabilidade única
class Process:
    def handle(self, username: str, password: str) -> None:
        if isinstance(username, str) and isinstance(password, str):
            print('Acessando o banco de dados ...')
            print('Verificando a existência do usuário ...')
            print('Cadastro de usuarios realizado com sucesso ...')
        else:
            raise Exception('Dados Inválidos')
#-----------------------------------------------------------------------

class SProcess:
    def handle(self, username: str, password: str) -> None:
        if self.__verify_data_input(username, password):
            self.__verify_username_in_database(username)
            self.__insert_username_in_database(username, password)
        else:
            self.__raise_error('Dados Inválidos')

    def __verify_data_input(self, username: str, password: str):
        return isinstance(username, str) and isinstance(password, str)
    
    def __verify_username_in_database(self, username: str):
            print('Acessando o banco de dados ...')
            print('Verificando a existência do usuário ...')
    
    def __insert_username_in_database(self, username: str, password: str):
        print('Cadastro de usuarios realizado com sucesso ...')

    def __raise_error(self, message: str):
        raise Exception(message)