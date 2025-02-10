### Fila de prioridade
```
new(header)
header.chave = none
header.prox =  none
fila_prioridade↑= header
```

### Fila comum
```
new(header)
header.chave = none
header.prox =  none
fila↑= header
```

### Variavel global
```
chamada = 0
pt = none
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
function add(nome, prioridade):
    new(aux)
    aux.chave = nome
    aux.prioridade = prioriade
    aux.prox = none
    if(prioridade == 1):
        pt↑ = fila_prioridade↑
        while(pt↑.prox != none):
            pt = pt.prox
        pt.prox = aux
    else:
        if (prioridade == 2)
            pt↑ = fila↑
            while(pt↑.prox != none):
                pt = pt.prox
            pt.prox = aux
        else:
            print("Prioridade inválida")
    return 0
```

```
function call():
    prioridade_vazia = fila_prioridade↑.prox != none
    fila_vazia = fila↑.prox != none
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

### Programa
```
function interface()
    print("Escolha sua opção")
    print("----------------")
    print("1. Adicionar Paciente (Nome e Prioridade)")
    print("2. Chamar Paciente")
    print("3. Encerrar programa")
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
    else:
        end = true
```