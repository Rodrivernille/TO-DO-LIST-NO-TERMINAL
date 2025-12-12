import json
import os

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=4)

def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    tarefas = carregar_tarefas()
    tarefas.append({"tarefa": tarefa, "concluida": False})
    salvar_tarefas(tarefas)
    print("Tarefa adicionada!")

def listar_tarefas():
    tarefas = carregar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    
    print("\n=== Suas Tarefas ===")
    for i, t in enumerate(tarefas, start=1):
        status = "✔️" if t["concluida"] else "❌"
        print(f"{i}. {t['tarefa']} [{status}]")

def concluir_tarefa():
    listar_tarefas()
    num = int(input("Número da tarefa para concluir: "))
    tarefas = carregar_tarefas()
    
    if 0 < num <= len(tarefas):
        tarefas[num-1]["concluida"] = True
        salvar_tarefas(tarefas)
        print("Tarefa marcada como concluída!")
    else:
        print("Número inválido.")

def remover_tarefa():
    listar_tarefas()
    num = int(input("Número da tarefa para remover: "))
    tarefas = carregar_tarefas()

    if 0 < num <= len(tarefas):
        removida = tarefas.pop(num-1)
        salvar_tarefas(tarefas)
        print(f"Tarefa removida: {removida['tarefa']}")
    else:
        print("Número inválido.")

def menu():
    while True:
        print("\n=== TO-DO LIST ===")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("5 - Sair")
        
        opc = input("Escolha: ")

        if opc == "1":
            adicionar_tarefa()
        elif opc == "2":
            listar_tarefas()
        elif opc == "3":
            concluir_tarefa()
        elif opc == "4":
            remover_tarefa()
        elif opc == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

menu()
