from verificarInput import verificarInput
def adicionar(contatos):

    print("\nAdicionar contato")

    nome = verificarInput("Digite o nome do contato: ")
    telefone = verificarInput("Digite o telefone: ")
    email = verificarInput("Digite o email: ")
    favorito = verificarInput("Favoritar contato:\n1. Sim\n2. Não\nFavoritar: ", numeroInteiro=True)
    
    while favorito <= 0 or favorito >= 3:
        print("\nDigite uma opção válida!")
        favorito = verificarInput("Favoritar contato:\n1. Sim\n2. Não\nFovoritar: ", numeroInteiro=True)
        if favorito == 1 or favorito == 2:
            break
    if favorito == 1:
        favorito = True
    else:
        favorito = False
        
    contato = {
        "nome" : nome,
        "telefone" : telefone,
        "email" : email,
        "favorito" : favorito
    }
    contatos.append(contato)
    return contatos

