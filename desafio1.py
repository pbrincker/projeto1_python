'''
- A aplicação deve iniciar mostrando uma lista de opções do que é possível fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
- Deve ser possível adicionar um contato
    - O contato pode ter os dados:
    - Nome
    - Telefone
    - Email
    - Favorito (está opção é para poder marcar um contato como favorito)
- Deve ser possível visualizar a lista de contatos cadastrados
- Deve ser possível editar um contato
- Deve ser possível marcar/desmarcar um contato como favorito
- Deve ser possível ver uma lista de contatos favoritos
- Deve ser possível apagar um contato
'''


def get_infos():
    name = input("Informe o nome do contato: ")
    phone_number = input("Informe o número do contato: ")
    mail = input("Informe o e-mail do contato [opcional]: ")
    favorite = input("Informe se este é um contato favorito [opcional] [sim/não]: ")
    favorite = favorite.lower()
    while True:
        if name == "":
            print("Não consegui localizar o nome do seu contato, favor informar um nome")
            name = input("Informe o nome do contato: ")
        
        if phone_number == "":
            print("Não consegui localizar o número do seu contato, favor informar um número")
            phone_number = input("Informe o número do contato: ")
        if favorite == "sim" or favorite == True:
            favorite = True
        elif favorite == "não" or favorite == False:
            favorite = False
        elif favorite == "":
            favorite = False
        else:
            print("Houve um erro ao tentar ler sua resposta, responda apenas como 'sim' ou 'não'")
            favorite = input("Informe se este é um contato favorito [opcional] [sim/não]: ")

        if name and phone_number and favorite == True or favorite == False:
            __dados = {
                'name': name,
                'phone_number': phone_number,
                'mail': mail,
                'favorite': favorite
            }
            return __dados


def add_contact(contact_book, dados_contato):
    contact_book.append(dados_contato)
    print(f"O contato {dados_contato['name']} foi cadastrado com sucesso")
    return


def get_contacts(contact_book):
    for contact_index, contact in enumerate(contact_book, start=1):
        print(f"{contact_index} - {"♥" if contact["favorite"] else " "} Nome: {contact['name']} | Nº telefone: {contact['phone_number']} | E-mail: {contact['mail']}")
    return


def edit_contact(contact_book, contact_index):
    contact_index_correct = contact_index - 1
    if contact_index_correct >= 0 and contact_index_correct <= len(contact_book):
        dados_contact = get_infos()
        contact_book[contact_index_correct] = dados_contact
        print(f"O contato {contact_book[contact_index_correct]['name']} foi atualizado com sucesso")
    else:
        print("Houve um erro ao tentar localizar o contato, tente novamente")
    return


def set_contact_favorite(contact_book, contact_index):
    contact_index_correct = contact_index - 1
    if contact_index_correct >= 0 and contact_index_correct <= len(contact_book):
        if contact_book[contact_index_correct]['favorite']:
            contact_book[contact_index_correct]['favorite'] = False
            print(f"O Contato {contact_book[contact_index_correct]['name']} foi removido dos seus favoritos.")
        else:
            contact_book[contact_index_correct]['favorite'] = True
            print(f"O Contato {contact_book[contact_index_correct]['name']} foi adicionado dos seus favoritos.")
    return


def get_favorites(contact_book):
    for contact_index, contact in enumerate(contact_book, start=1):
        if contact['favorite']:
            print(f"{contact_index} - {"♥" if contact["favorite"] else " "} Nome: {contact['name']} | Nº telefone: {contact['phone_number']} | E-mail: {contact['mail']}")
    return


def delete_contact(contact_book, contact_index):
    contact_index_correct = contact_index - 1
    if contact_index_correct >= 0 and contact_index_correct <= len(contact_book):
        name = contact_book[contact_index_correct]['name']
        contact_book.remove(contact_book[contact_index_correct])
        print(f"O Contato {name} foi deletado.")
    return


contact_book = []


def menu():
    while True:
        print("1. Adicionar Contato")
        print("2. Visualizar Contatos")
        print("3. Editar Contato")
        print("4. Marcar/desmarcar um contato como favorito")
        print("5. Visualizar Favoritos")
        print("6. Apagar Contato")
        print("7. Sair")

        choice = input("Escolha um opção: ")

        if choice == "1":
            dados_contact = get_infos()
            add_contact(contact_book, dados_contact)
        elif choice == "2":
            get_contacts(contact_book)
        elif choice == "3":
            get_contacts(contact_book)
            index_contact = int(input("Informe o número do contato que quer editar: "))
            edit_contact(contact_book, index_contact)
        elif choice == "4":
            get_contacts(contact_book)
            index_contact = int(input("Informe o número do contato que quer favoritar: "))
            set_contact_favorite(contact_book, index_contact)
        elif choice == "5":
            get_favorites(contact_book)
        elif choice == "6":
            get_contacts(contact_book)
            index_contact = int(input("Informe o número do contato que quer deletar: "))
            delete_contact(contact_book, index_contact)
        elif choice == "7":
            break


menu()
