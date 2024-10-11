from verContatos import verContatos
from verificarInput import verificarInput

def deletarContato(contatos):
    if len(contatos) == 0:
        print("\nNenhum contato cadastrado!")
        return
    else:
        verContatos(contatos)

        contatoDeletado = verificarInput("Digite a opção para deletar o contado: ", True)

        while contatoDeletado <= 0 or contatoDeletado >= len(contatos):
            print("\nDigite uma opção válida!")
            contatoDeletado = verificarInput("Digite a opção para deletar o contado: ", True)
            if contatoDeletado >= 1 and contatoDeletado <= len(contatos):
                break
        
        contatos.pop(contatoDeletado-1)
        print("\nContato deletado!")
        return contatos