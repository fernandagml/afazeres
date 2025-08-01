afazeres = []

while True:

    print("""
            ___________________________________
            *            AFAZERES             *
            -----------------------------------
            *                                 *
            *   1 - Inserir tarefa            *
            *   2 - Excluir tarefa            *
            *   3 - Concluir tarefa           *
            *   4 - Listar tarefas            *
            *   0 - SAIR                      *
            ___________________________________
    """)

    acao = int(input("O que você deseja fazer? "))

    if acao == 1:
        item = input("O que você deseja adicionar? ").upper()
        afazeres.append(item)

    elif acao == 2:
        item = input("O que você deseja retirar? ").upper()
        afazeres.remove(item)

    elif acao == 3:
        concluir = input("Qual item você deseja marcar como conlcluído? ").upper()
        for item in afazeres:
            if item == concluir:
                print(*f"{item} ✓")

    elif acao == 4: 
        for item in afazeres:
            print(*item)
    
    elif acao == 0:
        break

    else:
        acao = input("O que você deseja fazer? ")