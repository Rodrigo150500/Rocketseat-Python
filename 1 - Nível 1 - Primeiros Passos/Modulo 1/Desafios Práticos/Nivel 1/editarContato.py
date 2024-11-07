from verContatos import verContatos
from verificarInput import verificarInput

def editarContato(contatos):
    
    if len(contatos) == 0:
        print("\nNenhum contato cadastrado!")
        return        
    
    verContatos(contatos, False)
    escolha = verificarInput("Digite o contato para ser atualizado: ", True)

    if escolha <= 0 or escolha > len(contatos):
        print("\nContato não existente!\nRetornando ao menu inicial!")
        return
    else:
        print("\nO que deseja atualizar: ")
        print("1. Nome")
        print("2. Telefone")
        print("3. Email")
        print("4. Favorito")
        print("5. Todos")
        print("6. Sair")

        escolhaAtualizar = verificarInput("Digite o campo que deseja atualizar: ", True)

        if escolhaAtualizar == 1:
            nome = verificarInput("Digite o nome: ")
            contatos[escolha-1]["nome"] = nome 

        elif escolhaAtualizar == 2:
            telefone = verificarInput("Digite o novo número de telefone: ")
            contatos[escolha-1]["telefone"] = telefone

        elif escolhaAtualizar == 3:
            email = verificarInput("Digite o novo email: ")
            contatos[escolha-1]["email"] = email

        elif escolhaAtualizar == 4:
            favorito = verificarInput("Deseja marcar como favorito:\n1.Sim\n2.Não\nFavorito: ", True)
            while favorito <= 0 or favorito >= 3:
                print("\nDigite uma opção válida!")
                favorito = verificarInput("Favoritar contato:\n1. Sim\n2. Não\nFavoritar: ", numeroInteiro=True)

                if favorito == 1 or favorito == 2:
                    break

            if favorito == 1:
                favorito = True
            else:
                favorito = False
            contatos[escolha-1]["favorito"] = favorito

        elif escolhaAtualizar == 5:
            nome = verificarInput("Digite o novo nome: ")
            telefone = verificarInput("Digite o novo número de telefone: ")
            email = verificarInput("Digite o novo email: ")
            favorito = verificarInput("Deseja marcar como favorito:\n1. Sim\n2. Não\nFavoritar: ", True)
            while favorito <= 0 or favorito >= 3:
                print("\nDigite uma opção válida!")
                favorito = verificarInput("Favoritar contato:\n1. Sim\n2. Não\nFavoritar: ", True)

                if favorito == 1 or favorito == 2:
                    break

            if favorito == 1:
                favorito = True
            else:
                favorito = False

            contatos[escolha-1]["nome"] = nome
            contatos[escolha-1]["telefone"] = telefone
            contatos[escolha-1]["email"] = email
            contatos[escolha-1]["favorito"] = favorito

        elif escolhaAtualizar == 6:
            print("\nContato sem atualização!")

        else:
            print("\nOpção inválida! Retornando ao menu inicial")
       
        print("\nContato atualizado")
        return contatos