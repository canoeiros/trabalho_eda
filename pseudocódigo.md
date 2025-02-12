### Fila de prioridade
```
new(header)
header.chave = λ
header.senha = λ
header.prox =  λ
fila_prioridade↑= header
```

### Fila comum
```
new(header)
header.chave = λ
header.senha = λ
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
function add-mod():
    chamada = chamada + 1 
    if(chamada > 2):
        chamada = 0
```

### Procedimentos
```
function add(nome, prioridade):
    new(aux)
    aux.chave = nome
    aux.prioridade = prioriade
    aux.senha = random_number()
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
    prioridade_disponivel = fila_prioridade↑.prox != λ
    fila_disponivel = fila↑.prox != λ
    if (chamada == 2 and fila_disponivel):
        pt↑ = fila↑.prox
        aux1 = pt↑.chave
        aux2 = pt.senha
        print(aux1, aux2)
        fila↑.prox = pt.prox
        free(pt↑)
        add_mod()
    else:
        if (prioridade_disponivel):
            pt↑ = fila_prioridade.prox
            aux1 = pt↑.chave
            aux2 = pt.senha
            print(aux1, aux2)
            fila_prioridade↑.prox = pt.prox
            free(pt↑)
            add_mod()
        else:
            if (fila_disponivel):
                pt↑ = fila↑.prox
                aux1 = pt↑.chave
                aux2 = pt.senha
                print(aux1, aux2)
                fila↑.prox = pt.prox
                free(pt↑)
                add_mod()
            else:
                print("Filas Vazias")
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
