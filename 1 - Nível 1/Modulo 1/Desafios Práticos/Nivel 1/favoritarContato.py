from verContatos import verContatos
from verificarInput import verificarInput

def favoritarContato(contatos):
    if len(contatos) == 0:
        print("\nNenhum contato cadastrado!")
        return
    else:
        verContatos(contatos)

        escolhaFavorito = verificarInput("Digite o contato para ser favoritado: ", True)

        if escolhaFavorito <= 0 or escolhaFavorito > len(contatos):
            print("\nContato inexistente!\nRetornando ao menu!")
            return
        else:
            contatos[escolhaFavorito - 1]["favorito"] = not contatos[escolhaFavorito - 1]["favorito"]
            print("\nFavorito alterado com sucesso!")
        
        verContatos(contatos)
        return contatos