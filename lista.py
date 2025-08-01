afazeres = []

print("""\nBem vindo! Esta é a sua lista de afazeres,
      escolha a opção abaixo que deseja executar!\n""")

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
    
    try:
        acao = int(input("O que você deseja fazer agora? "))

    except ValueError:
        print("\nOpção inválida! Tente Novamente.")
        continue
    
    if acao == 1:
        item = input("\nO que você deseja adicionar na sua lista? ").upper()
        afazeres.append(item)
        print("Adicionado!")

    elif acao == 2:
        if not afazeres:
            print("\nA sua lista está vazia!")
        else:
            print("\nDê uma olhada na lista:")
            i = 0
            for tarefa in afazeres:
                print(f"{i} {tarefa}")
                i += 1
            item = int(input("\nQual item você deseja retirar? "))
            afazeres.pop(item)
            print("Retirado!")

    elif acao == 3:
        if not afazeres:
            print("\nA sua lista está vazia!")
        else:
            print("\nDê uma olhada na lista:")
            i = 0
            for tarefa in afazeres:
                print(f"{i} {tarefa}")
                i += 1
            concluir = int(input("\nQual o índice do item que você deseja marcar como conlcluído? "))
            afazeres[concluir] = afazeres[concluir] + " ✓"
            print("Concluído!")

    elif acao == 4:
        if not afazeres:
            print("\nA sua lista está vazia!")
        else:
            print("\nDê uma olhada na lista:")
        i = 0
        for tarefa in afazeres:
            print(f"{i} {tarefa}")
            i += 1

    elif acao == 0:
        print("Até mais!")
        break

    else:
        print("\nOpção inválida! Tente Novamente.")