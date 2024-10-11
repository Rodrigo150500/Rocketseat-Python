from verificarInput import verificarInput
from adicionar import adicionar
from verContatos import verContatos
from editarContato import editarContato
from deletarContato import deletarContato
from favoritarContato import favoritarContato

contatos = []

while True:
    print("\nEscolha uma das seguintes opções: ")

    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Editar contato")
    print("4. Ver lista de favoritos")
    print("5. Deletar contato")
    print("6. Favoritar contato")
    print("7. Sair")

    escolha = verificarInput("Digite uma opção: ", numeroInteiro = True)

    if escolha == 1:
        contatos = adicionar(contatos)
    elif escolha == 2:
        verContatos(contatos, favoritos = False)
    elif escolha == 3:
        editarContato(contatos)
    elif escolha == 4:
        verContatos(contatos, favoritos = True)
    elif escolha == 5:
        contatos = deletarContato(contatos)
    elif escolha == 6:
        contatos = favoritarContato(contatos)
    elif escolha == 7:
        print ("\nPrograma Finalizado!")
        break
    else:
        print("Digite um número válido!")