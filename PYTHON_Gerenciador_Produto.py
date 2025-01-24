from datetime import datetime

produtos=[]

def menu():
    print('Gerenciado de Produtos'.center(100,' '))
    print('1 - Cadastrar Produto')
    print('2 - Remover produto')
    print('3 - Procurar Produto')
    print('4 - Ver Produtos')
    print('5 - Sair')

def cadastrar_produto():
    print('Quantos produtos deseja adicionar? ')
    num=int(input('>> '))
    for i in range(1,num+1):
        data=datetime.now().strftime('%d/%m/%Y')
        nome=input('Nome: ')
        estoque=int(input('Quantidade em estoque: '))
        preco=float(input('Preço: '))
        descricao=input('Descrição do Produto: ')
        produtos.append([nome, estoque, preco, data, descricao])

def remover_produto():
    if len(produtos)>0:
        nome=input('Digite o nome do produto que deseja remover: ')
        for produto in produtos:
            if nome==produto[0]:
                produtos.remove(produto)
                print(f'O produto {nome.lower()} foi removido')
                return True

        print('Produto não encontrado')
    else:
        print('Não há produtos cadastrados')

def procurar_produto():
    if len(produtos)>0:
        nome=input('Qual produto deseja pesquisar? ')
        for produto in produtos:
            if nome==produto[0]:
                print(f'Nome: {produto[0]}')
                print(f'Preço: ${produto[2]}')
                print(f'Estoque: {produto[1]}')
                return True
        print('Produto não encontrado')
    else:
        print('Não há produtos cadastrados')

def ver_produtos():
    if len(produtos)>0:
        for produto in produtos:
            print()
            print(f'Nome: {produto[0]}')
            print(f'Estoque: {produto[1]}')
            print(f'Preço: $ {produto[2]}')
            print(f'Descrição do produto: {produto[4]}')
            print(f'Data de registro: {produto[3]}')
            print()
        print(f'Total de produtos cadastrados: {len(produtos)}.')
    else:
        print('Não há produtos cadastrados')

def main():
    escolha=''
    while escolha!=5:
        menu()
        escolha=input('>> ')
        if escolha in list('1234'):
            if escolha=='1':
                cadastrar_produto()
            elif escolha=='2':
                remover_produto()
            elif escolha=='3':
                procurar_produto()
            elif escolha=='4':
                ver_produtos()
        else:
            if escolha!=5:
                print('Opção Inválida')

if __name__== '__main__':
    main()