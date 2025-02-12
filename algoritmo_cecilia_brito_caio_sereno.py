# Alunos: Caio Sereno e Cecilia Brito
import random
import string

class Node:
    def __init__(self, chave=None, prioridade=None, senha=None):
        self.chave = chave
        self.prioridade = prioridade
        self.senha = senha
        self.prox = None

fila_prioridade = Node()   
fila_normal = Node() 

chamada = 0
end_program = False 

def add_mod():
    global chamada
    chamada += 1
    if chamada > 2:
        chamada = 0

def add(nome, prioridade): 
    senha = ''.join(random.choices(string.digits, k=3))
    new_node = Node(nome, prioridade, senha)
    if prioridade == 1:
        pt = fila_prioridade
        while pt.prox is not None:
            pt = pt.prox
        pt.prox = new_node
    elif prioridade == 2:
        pt = fila_normal
        while pt.prox is not None:
            pt = pt.prox
        pt.prox = new_node
    else:
        print("Prioridade inválida. Use 1 para PRIORITÁRIO ou 2 para NORMAL.")

def call():
    global chamada
    prioridade_disponivel = (fila_prioridade.prox is not None)
    normal_disponivel = (fila_normal.prox is not None)
    if chamada == 2 and normal_disponivel:
        pt = fila_normal.prox
        fila_normal.prox = pt.prox
        print(f"Chamando paciente : {pt.chave} \nSenha: {pt.senha}")
        add_mod()
    elif prioridade_disponivel:
        pt = fila_prioridade.prox
        fila_prioridade.prox = pt.prox
        print(f"Chamando paciente PRIORITARIO: {pt.chave} \nSenha: {pt.senha}")
        add_mod()
    elif normal_disponivel:
        pt = fila_normal.prox
        fila_normal.prox = pt.prox
        print(f"Chamando paciente : {pt.chave} \nSenha: {pt.senha}")
        add_mod()
    else:
        print("Filas Vazias")

def show_list():
    print("Fila Prioridade:")
    numero = 1
    pt = fila_prioridade.prox
    while pt != None:
        print(f'{numero}. {pt.chave} - Senha:{pt.senha}') 
        pt = pt.prox
        numero += 1
    print('\n')
    print("Fila Normal")
    numero = 1
    pt = fila_normal.prox
    while pt != None:
        print(f'{numero}. {pt.chave} - Senha:{pt.senha}') 
        pt = pt.prox
        numero += 1

def interface():
    print("\nEscolha sua opção")
    print("----------------")
    print("1. Adicionar Paciente (Nome e Prioridade)")
    print("2. Chamar Paciente")
    print("3. Encerrar programa")
    print("4. Mostrar Lista")
    print("")
    valor = input("Opção: ")
    return valor

# Programa principal
while not end_program:
    opcao = interface()
    
    if opcao == "1":
        nome = input("Nome do Paciente: ")
        prioridade_input = input("Prioridade do Paciente (1 = PRIORITÁRIO, 2 = NORMAL): ")
        try:
            prioridade = int(prioridade_input)
        except ValueError:
            print("Prioridade inválida. Digite 1 ou 2.")
            continue
        add(nome, prioridade)
    elif opcao == "2":
        call()
    elif opcao == "3":
        print("Encerrando programa...")
        end_program = True
    elif opcao == "4":
        show_list()
       
    else:
        print("Opção inválida. Tente novamente.")
