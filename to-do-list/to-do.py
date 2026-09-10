azul = "\033[34m"
amarelo = "\033[93m"
vermelho = "\033[31m"
verde = "\033[32m"
reset = "\033[0m"

tarefas = []

status = ["a fazer", "executando", "pronta"]

def mostrar_menu ():
    print(f"{azul}===== LISTA DE TAREFAS ====={reset}")
    print(f"{verde}1. Adicionar Tarefa{reset}")
    print(f"{verde}2. Exibir tarefas{reset}")
    print(f"{verde}3. Mudar status da tarefa{reset}")
    print(f"{verde}4. Apagar Tarefa{reset}")
    print(f"{verde}5. Sair{reset}")
    print(f"{azul}{'=' * 29}{reset}")

def adicionar_tarefa():
    while True:
        tarefa = input("Insira a tarefa: ")
        if len(tarefa) <= 80:
            break
        print(f"{vermelho}A tarefa não pode ter mais de 80 caracteres (você digitou {len(tarefa)}).{reset}")
    tarefas.append({"tarefa": tarefa, "status": "a fazer"})
    print(f"{amarelo}Tarefa '{tarefa}' adicionada!{reset}")

def alterar_status():
    if not tarefas:
        print(f"\n{vermelho}Você não tem tarefas ainda.{reset}")
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
        print(f"{vermelho}Opção inválida.{reset}")
        return

    novo_status = status[escolha]

    if novo_status == "executando":
        quantidade_fazendo = sum(1 for t in tarefas if t["status"] == "executando")
        if quantidade_fazendo >= 10 and tarefa["status"] != "executando":
            print(f"{vermelho}Limite de 10 tarefas em 'executando' atingido. Mude outra tarefa antes.{reset}")
            return

    tarefa["status"] = novo_status
    print(f"Status atualizado para '{novo_status}'!")

    tarefa["status"] = status[escolha]
    print(f"Status atualizado para '{status[escolha]}'!")

def listar_tarefas():
    if not tarefas:
        print(f"{vermelho}Você não tem tarefas ainda.{reset}")
        return False
    print("\nSuas tarefas: ")           
    for index, tarefa in enumerate(tarefas, start=1):
        print(f"{amarelo}{index}. {tarefa['tarefa']}{reset} [{tarefa['status']}]")
    return True

def exibir_tarefa():
    listar_tarefas()
    input("\nPressione Enter para voltar ao menu...")

def apagar_tarefa ():
    if not tarefas:
            print(f"{vermelho}Você não tem tarefas ainda.{reset}")
            return
    listar_tarefas()
    try:
        index = int(input("Digite qual tarefa deseja apagar: ")) - 1
        if 0 <= index < len(tarefas):
            removed = tarefas.pop(index)
            print(f"Tarefa apagada: {removed['tarefa']}")
        else:
            print(f"{vermelho}Número Inválido!{reset}")
    except ValueError:
        print("Coloque um número válido.")

while True:
    mostrar_menu()
    escolha = input("\nEscolha uma opção: ")
    try:
        escolha = int(escolha)
    except ValueError:
        print(f"{vermelho}Opção inválida, tente novamente{reset}")
        continue

    if escolha == 1:
        adicionar_tarefa()
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
        print(f"{vermelho}Opção inválida, tente novamente{reset}")
