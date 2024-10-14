def verContatos(contatos, favoritos = False):

    if len(contatos) == 0:
        print("\nNenhum contato cadastrado!")
        return
    print("")

    if favoritos == False:
        for pos, contato in enumerate(contatos, start=1):
            print(f"{pos}. \nNome:{contato['nome']}\nTelefone: {contato['telefone']}\nE-mail: {contato['email']}\nFavorito: {'Não' if contato['favorito'] == False else 'Sim'}\n")
    else:
        count = 1
        for contato in contatos:
            if contato['favorito'] == True:
                print(f"{count}. \nNome:{contato['nome']}\nTelefone: {contato['telefone']}\nE-mail: {contato['email']}\nFavorito: {'Não' if contato['favorito'] == False else 'Sim'}\n")
                count += 1
            if count == 1:
                print("Nenhum contato favorito cadastrado!")
                return