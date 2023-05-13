import os
lista_de_compras = []

while True:

    menu = input("""Digite uma opção:
[1] Inserir
[2] Apagar
[3] Ver Lista
""")

# Inserindo itens
    if menu == str(1):
        os.system('clear')
        item_acrescentado = input("Informe o item a ser adicionado: ")
        if item_acrescentado == (""):
            print("== Você não digitou um item válido ==")
        else:
            lista_de_compras.append(f'{item_acrescentado}')
            print("==== Item adicionado! ====")

# Apagando itens
    elif menu == str(2):
        try:
            os.system('clear')
            item_apagado = input("Informe o item a ser apagado: ")
            lista_de_compras.remove(item_apagado)
            print("==== Item removido! ====")
        except:
            print("== O item digitado não está na lista ==")

# Exibindo a lista de compra
    elif menu == str(3):
        os.system('clear')
        if len(lista_de_compras) == 0:
            print("=== A lista está vazia! ===")
        else:
            print("====== Lista de Compras ======")
            for nome in set(lista_de_compras):
                print(nome)
            print("==============================")
    
    else:
        print("Operação inválida. Tente novamente.")