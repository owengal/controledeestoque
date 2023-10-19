#variável global
lista_peca = [] #lista criada pra receber peças
codigo_peca = 0 #inicio dos códigos que serão cadastrados

#função para cadastrar peça
def cadastrar_peca(codigo):
    print('Bem-vindo ao menu de cadastrar peça')
    print('Código da peça: {}'.format(codigo))
    #variaveis criadas pra receber nome, fabricante e valor
    nome = input('Por favor entre com o NOME  da peça:')
    fabricante = input('Por favor entre com o FABRICANTE  da peça:')
    valor = int(input('Por favor entre com o VALOR(R$) da peça:'))
    #dicionário criado pra receber as informações que vão ser salvas na lista
    dicionario_peca = {'codigo': codigo, 'nome': nome, 'fabricante': fabricante, 'valor': valor}
    lista_peca.append(dicionario_peca.copy()) #salvando o dicionario na lista

#função para consultar peças
def consultar_peca():
    print('Bem-vindo ao menu de consultar peça')
    while True:
        #variavel criada para receber a opção desejada
        opcao_consultar = input('Escolha a opção desejada: \n' +
                                '1 - Consultar todas as peças \n' +
                                '2 - Consultar peças por código \n' +
                                '3 - Consultar Peças por fabricante\n' +
                                '4 - Retornar \n' +
                                '>>')
        #condição para retornar a opção desejada, de consultar todas as peças, por códigos, por fabricante e retornar
        if opcao_consultar == '1':
            print('Você escolheu a opção consultar TODAS as peças')
            for peca in lista_peca:
                print('-------------------------')
                for key, value in peca.items(): #varrer todos os conjuntos de chave e valor do dicionário  de peças
                    print('{}: {}'.format(key, value))
                print('-------------------------')
        elif opcao_consultar == '2':
            print('Você escolheu a opção consultar peças por CÓDIGO')
            valor_desejado = int(input('Entre com o CÓDIGO desejado:'))
            for peca in lista_peca:
                if peca['codigo'] == valor_desejado: #vai buscar dentro de codigo o valor que a pessoa colocou
                    print('-------------------------')
                    for key, value in peca.items():  # varrer todos os conjuntos de chave e valor do dicionário  de peças
                        print('{}: {}'.format(key, value))
                    print('-------------------------')
        elif opcao_consultar == '3':
            print('Você escolheu a opção consultar peças por FABRICANTE')
            valor_desejado = input('Entre com o FABRICANTE desejado:')
            for peca in lista_peca:
                if peca['fabricante'] == valor_desejado: #vai buscar dentro de fabricante o valor que a pessoa colocou
                    print('-------------------------')
                    for key, value in peca.items():  # varrer todos os conjuntos de chave e valor do dicionário  de peças
                        print('{}: {}'.format(key, value))
                    print('-------------------------')
        elif opcao_consultar == '4':
            return #saí do laço e retorna para o inicio do programa
        else:
            print('Opção inválida. Tente novamente')
            continue

 # função para remover peça
def remover_peca():
    print('Bem-vindo ao menu de remover peça')
    valor_desejado = int(input('Entre com  o CÓDIGO do produto que deseja remover'))
    for peca in lista_peca:
        if peca['codigo'] == valor_desejado: #vai buscar dentro de codigo a opção que deseja remover, a peça só vai ser removida através do código
            lista_peca.remove(peca) #remoção da peça da lista
            print('Produto removido')
#inicio do programa
print('Bem-vindo ao controle de estoque da bicicletaria da Galdina Silva de Souza, RU:4370444')
while True:
    #variavel criada para mostrar as opções de escolha
    opcao_principal = input('Escolha a opção desejada: \n'+
                            '1 - Cadastrar peças \n'+
                            '2 - Consultar peças \n'+
                            '3 - Remover Peças \n'+
                            '4 - Sair \n'+
                            '>>')
    #condições criadas para retornar de acordo com a opção inserida
    if opcao_principal == '1':
        codigo_peca = codigo_peca + 1
        cadastrar_peca(codigo_peca)
        #de acordo com essa opção irá trazer essa função
    elif opcao_principal == '2':
        consultar_peca()
        # de acordo com essa opção irá trazer essa função
    elif opcao_principal == '3':
        remover_peca()
        # de acordo com essa opção irá trazer essa função
    elif opcao_principal == '4':
        break #irá encerrar o programa
    else:
        print('Opção inválida. Tente novamente')
        continue