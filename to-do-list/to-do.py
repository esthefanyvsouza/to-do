tarefas = []

status = ["a fazer", "fazendo", "concluida"]

def mostrar_menu ():
    print("/n===== LISTA DE TAREFAS =====")
    print("1. Adicionar Tarefa")
    print("2. Exibir tarefas")
    print("3. Mudar status da tarefa")
    print("4. Apagar Tarefa")
    print("5. Sair")

def adiconar_tarefa ():
    tarefa = input("Insira a tarefa: ")
    tarefas.append({"tarefa": tarefa, "status": "a fazer"})
    print(f"Tarefa '{tarefa}' adicionada!")