afazeres = []
i = 0

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
        for tarefa in afazeres:
            print(tarefa)
        item = input("Qual o índice do item que você deseja retirar? ").upper()
        afazeres.remove(item)

    elif acao == 3:
        i = 0
        for tarefa in afazeres:
            print(f"{i} {tarefa}")
        concluir = int(input("Qual o índice do item que você deseja marcar como conlcluído? "))
        afazeres[concluir] = afazeres[concluir] + " ✓"
        print("Concluído!")

    elif acao == 4:
        if not afazeres:
            print("A sua lista está vazia!")
        for tarefa in afazeres:
            print(tarefa)
    
    elif acao == 0:
        print("Até mais!")
        break

    else:
        acao = print("Opção inválida!")