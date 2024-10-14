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
        validarQuantidade = verificarQuantidadeTarefa(tarefas, atualizarItem)

        while validarQuantidade == False:
            print("\nTarefa não existente!")
            atualizarItem = verificarInput("Qual tarefa deseja atualizar: ", True)
            validarQuantidade = verificarQuantidadeTarefa(tarefas, atualizarItem)
            
            if validarQuantidade == True:
                break

        for posicao, valor in enumerate(tarefas):
            if posicao == atualizarItem-1:
                nomeAtualizado = verificarInput("Digite o novo nome da tarefa: ")
                valor['nome'] = nomeAtualizado
                print(f"\nA tarefa {valor['nome']} atualizada com sucesso!")
        return

def completarTarefa(tarefas):

    if len(tarefas) == 0:
        print("\nNenhuma tarefa cadastrada!")
        return []
    verTarefas(tarefas)
    
    numeroTarefa = verificarInput("Digite o numero da tarefa: ", True)
    validarQuantidade = verificarQuantidadeTarefa(tarefas, numeroTarefa)

    while validarQuantidade == False:
        print("\nTarefa não existente!")
        
        numeroTarefa = verificarInput("Digite o numero da tarefa: ", True)
        validarQuantidade = verificarQuantidadeTarefa(tarefas, numeroTarefa)
        if validarQuantidade == True:
            break

    for posicao, tarefa in enumerate(tarefas):
        if posicao == numeroTarefa-1:
            if tarefa["completa"] == True:
                print("\nTarefa já completada!")
                return
            else:
                tarefa["completa"] = True
    verTarefas(tarefas)
    return

def deletarTarefa(tarefas):

    if len(tarefas) == 0:
        print("\nNenhuma tarefa cadastrada!")
        return
    verTarefas(tarefas)

    numeroTarefa = verificarInput("Digite o número da tarefa: ", True)
    validarQuantidade = verificarQuantidadeTarefa(tarefas, numeroTarefa)

    while validarQuantidade == False:
        print("\nTarefa Inexistente!")

        numeroTarefa = verificarInput("Digite o número da tarefa: ", True)
        validarQuantidade = verificarQuantidadeTarefa(tarefas, numeroTarefa)
        if validarQuantidade == True:
            break
    
    for posicao, tarefa in enumerate(tarefas):
        if tarefa['completa'] == True and posicao == numeroTarefa-1:
            tarefas.pop(posicao-1)
            print("Tarefa excluída!")
            return tarefas
    print("\nComplete a tarefa!")
    return tarefas


def verificarInput(msgInput, inteiro=False):
    if inteiro == False:
        valor = input(msgInput)
        while valor == "":
            print("\nDigite um valor válidado!")
            valor = input(msgInput)
            if valor != "":
                break
    else:
        while True:
            try:
                valor = int(input(msgInput))
                if valor >= 1 and valor <=6:
                    return valor
                else:
                    print("Digite um item válido")
            except Exception as e:
                print("Digite um número válido!")   

    return valor

def verificarQuantidadeTarefa(tarefas, input):
    if input > len(tarefas) or input <= 0:
        print("Digite um número da tarefa")
        return False
    return True


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
    elif escolha == 4:
        completarTarefa(tarefas)
    elif escolha == 5:
        tarefas = deletarTarefa(tarefas)
    elif escolha == 6:
        break
    else:
        print("Digite um número válido!")

print("Programa Finalizado")
