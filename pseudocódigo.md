### Fila de prioridade
```
new(header)
header.chave = λ
header.prox =  λ
fila_prioridade↑= header
```

### Fila comum
```
new(header)
header.chave = λ
header.prox =  λ
fila↑= header
```

### Variavel global
```
chamada = 0
pt = λ
end = false
```

### Função adicionar mod 3
```
function add-mod(var):
    variavel = variavel + 1 
    if(variavel > 2):
        variavel = 0
    return variavel
```

### Procedimentos
```
function add(nome, prioridade, senha):
    new(aux)
    aux.chave = nome
    aux.prioridade = prioriade
    senha = random_number()
    aux.prox = λ
    if(prioridade == 1):
        pt↑ = fila_prioridade↑
        while(pt↑.prox != λ):
            pt = pt.prox
        pt.prox = aux
    else:
        if (prioridade == 2)
            pt↑ = fila↑
            while(pt↑.prox != λ):
                pt = pt.prox
            pt.prox = aux
        else:
            print("Prioridade inválida")
    return 0
```

```
function call():
    prioridade_vazia = fila_prioridade↑.prox != λ
    fila_vazia = fila↑.prox != λ
    if (chamada == 2 and prioridade_vazia):
        pt↑ = fila_prioridade↑.prox
        aux1 = pt↑.chave
        aux2 = pt↑.prioridade
        print(aux1, aux2)
        free(pt↑)
    else:
        if (fila_vazia):
            pt↑ = fila.prox
            aux1 = pt↑.chave
            aux2 = pt↑.prioridade
            print(aux1, aux2)
            free(pt↑)
        else:
            if (prioridade_vazia):
                pt↑ = fila_prioridade↑.prox
                aux1 = pt↑.chave
                aux2 = pt↑.prioridade
                print(aux1, aux2)
                free(pt↑)
            else:
                print("Filas Vazias")
                end()
    add_mod(chamada)
    return 0
```
```
funcion show_list():
    pt↑ = fila_prioridade↑.prox
    numero = 1
    print("Fila Prioridade")
    while (pt↑ != λ):
        print(f'{numero}. {pt.nome} - {pt.senha}')
        pt = pt.prox

    pt↑ = fila↑.prox
    numero = 1
    print("Fila Normal")
    while (pt↑ != λ):
        print(f'{numero}. {pt.nome} - {pt.senha}')
        pt = pt.prox

```

### Programa
```
function interface()
    print("Escolha sua opção")
    print("----------------")
    print("1. Adicionar Paciente (Nome e Prioridade)")
    print("2. Chamar Paciente")
    print("3. Mostrar Lista")
    print("4. Encerrar programa")
    print("\n")
    valor = input("Opção: ")
    return valor
```
```
while (end == false):
    valor = interface()
    if(valor == 1):
        aux1 = input("Nome do Paciente: ")
        aux2 = input("Prioridade do Paciente (1 = Prioridade, 2 = Normal)") 
        add(aux1, aux2)
    elif (valor == 2):
        call()
    elif (valor == 3):
        show_list()
    else:
        print("Encerrando Programa...")
        end = true
```