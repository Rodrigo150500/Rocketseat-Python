def adicionarTarefa(tarefas, nomeTarefa):

    tarefa = {
        "nome": nomeTarefa,
        "completa": False,
    }
    tarefas.append(tarefa)
    print(f"\nA tarefa {nomeTarefa} com adicioada com sucesso!")
    return


def verTarefas(tarefas):
    if len(tarefas) == 0:
        print("\nNenhuma tarefa cadastrada!")
        return
    print("")
    for posicao, tarefa in enumerate(tarefas):
        print(
            f"{posicao+1}. {'[x]' if tarefa['completa'] else '[ ]'} - {tarefa['nome']}")
    return


def atualizarTarefa(tarefas):
    
    if len(tarefas) == 0:
        print("\nNenhuma tarefa cadastrada!")
        return
    else:
        verTarefas(tarefas)
        atualizarItem = verificarInput("Qual tarefa deseja atualizar: ", True)

        for posicao, valor in enumerate(tarefas):
            if posicao == atualizarItem-1:
                nomeAtualizado = verificarInput("Digite o novo nome da tarefa: ")
                valor['nome'] = nomeAtualizado
                print(f"\nA tarefa {valor['nome']} atualizada com sucesso!")
        return

        

def verificarInput(msgInput, inteiro=False):
    try:
        if not inteiro:
            valor = input(msgInput)
        else:
            valor = int(input(msgInput))

            while valor == "":
                print('Digite um valor válido!')
                if not inteiro:
                    valor = input(msgInput)
                else:
                    valor = int(input(msgInput))
                if valor != "":
                    break
    except Exception as e:
        print('Digite um valor válido!')
        valor = int(input(msgInput))
    return valor


tarefas = []
while True:
    print("\nMenu de Gerenciador de Tarefas")

    print("1. Adicionar tarefa")
    print("2. Ver tarefa")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefa")
    print("6. Sair")

    escolha = verificarInput("\nDigite um item: ", True)

    if escolha == 1:
        nomeTarefa = verificarInput("Digite o nome da tarefa: ")
        adicionarTarefa(tarefas, nomeTarefa)
    elif escolha == 2:
        verTarefas(tarefas)
    elif escolha == 3:
        atualizarTarefa(tarefas)
    elif escolha == 6:
        break
    else:
        print("Digite um número válido!")

print("Programa Finalizado")
