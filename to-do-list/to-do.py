tarefas = []

status = ["a fazer", "fazendo", "concluida"]

def mostrar_menu ():
    print("\n===== LISTA DE TAREFAS =====")
    print("1. Adicionar Tarefa")
    print("2. Exibir tarefas")
    print("3. Mudar status da tarefa")
    print("4. Apagar Tarefa")
    print("5. Sair")

def adiconar_tarefa ():
    tarefa = input("Insira a tarefa: ")
    tarefas.append({"tarefa": tarefa, "status": "a fazer"})
    print(f"Tarefa '{tarefa}' adicionada!")

def exibir_tarefa ():
    if not tarefas:
        listar_tarefas()
        input("\nPressione Enter para voltar ao menu...")
        return
    print("\nSuas tarefas: ")           
    for index, tarefa in enumerate(tarefas, start=1):
        print(f"{index}. {tarefa['tarefa']}")
    input("\nPressione Enter para voltar ao menu...")

def alterar_status():
    if not tarefas:
        print("\nVocê não tem tarefas ainda.")
        return
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa: ")) - 1
        tarefa = tarefas[indice]
    except (ValueError, IndexError):
        print("Tarefa inválida.")
        return
    
    print("\nStatus disponíveis:")
    for i, s in enumerate(status, start=1):
        print(f"{i}. {s}")

    try:
        escolha = int(input("Escolha o número do novo status: ")) - 1
        if escolha < 0 or escolha >= len(status):
            raise ValueError
    except ValueError:
        print("Opção inválida.")
        return

    tarefa["status"] = status[escolha]
    print(f"Status atualizado para '{status[escolha]}'!")

def listar_tarefas():
    if not tarefas:
        print("Você não tem tarefas ainda.")
        return False
    print("\nSuas tarefas: ")           
    for index, tarefa in enumerate(tarefas, start=1):
        print(f"{index}. {tarefa['tarefa']}")
    return True

def exibir_tarefa():
    listar_tarefas()
    input("\nPressione Enter para voltar ao menu...")

def apagar_tarefa ():
    if not tarefas:
            print("Você não tem tarefas ainda.")
            return
    listar_tarefas()
    try:
        index = int(input("Digite qual tarefa deseja apagar: ")) - 1
        if 0 <= index < len(tarefas):
            removed = tarefas.pop(index)
            print(f"Tarefa apagada: {removed['tarefa']}")
        else:
            print("Número Inválido!")
    except ValueError:
        print("Coloque um número válido.")

while True:
    mostrar_menu()
    escolha = input("\nEscolha uma opção: ")
    try:
        escolha = int(escolha)
    except ValueError:
        print("Opção inválida, tente novamente")
        continue

    if escolha == 1:
        adiconar_tarefa()
    elif escolha == 2:
        exibir_tarefa ()
    elif escolha == 3:
        alterar_status()
    elif escolha == 4:
        apagar_tarefa()
    elif escolha == 5:
        print("Adeus!")
        break
    else:
        print("Opção inválida, tente novamente")
