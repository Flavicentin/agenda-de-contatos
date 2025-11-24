import contatos_utils

contatos = []
while True:
    print("\nAgenda Contatos")
    print("1 - Adicionar um contato")
    print("2 - Contatos Cadastrados")
    print("3 - Editar Contato")
    print("4 - Editar Favoritos")
    print("5 - Contatos Favoritos")
    print("6 - Apagar Contato")
    print("7 - Sair Programa")
    try:
        opcao = int(input("Digite uma opção: "))
    except Exception as e:
        print(f"ERROR", {e})
        print("Digite um número válido!")
        continue

    if opcao == 1:
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        contatos_utils.adicionar_contato(contatos, nome, telefone, email)

    elif opcao == 2:
        contatos_utils.visualizar_contatos(contatos)

    elif opcao == 3:
        contatos_utils.visualizar_contatos(contatos)
        index = int(input("Digite o numero para editar contato: "))
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato:")
        contatos_utils.editar_contato(contatos, index, nome, telefone, email)

    elif opcao == 4:
        contatos_utils.visualizar_contatos(contatos)
        index = int(input("Digite o numero para alterar favorito: "))
        contatos_utils.editar_favorito(contatos, index)

    elif opcao == 5:
        contatos_utils.visualizar_favoritos(contatos)

    elif opcao == 6:
        contatos_utils.visualizar_contatos(contatos)
        index = int(input("Digite o numero para deletar contato: "))
        contatos_utils.deletar_contato(contatos, index)

    elif opcao == 7:
        break

    else:
        print("\nOpção Não Existe")