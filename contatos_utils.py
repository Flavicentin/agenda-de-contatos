def adicionar_contato(contatos, nome, telefone, email):
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    }
    contatos.append(contato)
    print("\nContato Adicionado!")


def visualizar_contatos(contatos):
    print("\nLista Contatos:")
    for index, contato in enumerate(contatos, start=1):
        status = "★" if contato["favorito"] else ""
        print(f"{index}. [{status}] {contato['nome']} - {contato['telefone']} - {contato['email']}")


def editar_contato(contatos, index, nome, telefone, email):
    index -= 1
    if 0 <= index < len(contatos):
        if nome:
            contatos[index]["nome"] = nome
        if telefone:
            contatos[index]["telefone"] = telefone
        if email:
            contatos[index]["email"] = email
        print("\nContato Editado!")
    else:
        print("Contato Inexistente")


def editar_favorito(contatos, index):
    index -= 1
    if 0 <= index < len(contatos):
        contatos[index]["favorito"] = not contatos[index]["favorito"]
        print("\nFavorito Alterado!")
    else:
        print("Contato Inexistente")


def visualizar_favoritos(contatos):
    print("\nContatos Favoritos:")
    for index, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            print(f"{index}. {contato['nome']}")


def deletar_contato(contatos, index):
    index -= 1
    if 0 <= index < len(contatos):
        contatos.pop(index)
        print("\nContato Deletado!")
    else:
        print("Contato Inexistente")
