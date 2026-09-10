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
        print("Você não tem tarefas ainda.")
        return
    print("\nSuas tarefas: ")           
    for index, tarefa in enumerate(tarefas, start=1):
        print(f"{index}. {tarefa['tarefa']}")

def alterar_status():
    if not tarefas:
        print("Você não tem tarefas ainda.")
        return
    exibir_tarefa()
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

def apagar_tarefa ():
    if not tarefas:
            print("Você não tem tarefas ainda.")
            return
    exibir_tarefa()
    try:
        index = int(input("Digite qual tarefa deseja apagar: ")) - 1
        if 0 <= index < len(tarefas):
            removed = tarefas.pop(index)
            print(f"Tarefa apagada: {removed['tarefa']}")
        else:
            print("Número Inválido!")
    except ValueError:
        print("Coloque um número válido.")
        