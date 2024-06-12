lista_de_compras = []
opcao = 1

while opcao != 0:

    print('1 Inserir')
    print('2 Excluir')
    print('3 Listar')
    print('4 Editar')
    print('0 Sair')
    opcao = int(input('Qual opção? '))
    
    if opcao == 1:
        print('Inserir')    

        item = input('Qual item? ')

        lista_de_compras.append(item)

        print(lista_de_compras)

    elif opcao == 2:
        print('Excluir')

        print(lista_de_compras)
        item_excluir = input('Qual deseja excluir? ')
        
        tamanho = len(lista_de_compras)
        for indice in range(tamanho):
            
            if lista_de_compras[indice] == item_excluir:
                print('Item excluido ', lista_de_compras[indice])
            
                lista_de_compras.pop(indice)
            
                break

    elif opcao == 3:
        print('Listar')

        tamanho = len(lista_de_compras)
        for indice in range(tamanho):
            print(f'{indice} - {lista_de_compras[indice]}')

    elif opcao == 4:
        print('Editar')

        print(lista_de_compras)
        item_editar = input('Qual deseja editar? ')
        
        tamanho = len(lista_de_compras)
        for indice in range(tamanho):
            
            if lista_de_compras[indice] == item_editar:
                novo_item = input('Diga o novo item: ')
                
                lista_de_compras[indice] = novo_item

                print('Item editado ', lista_de_compras[indice])
            
                break

    elif opcao == 0:
        print('Saindo...')

    else:
        print('Opção inválida!')

    print()