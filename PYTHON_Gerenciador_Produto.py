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

def main():
    escolha=''
    while escolha!=5:
        menu()
        escolha=input('>> ')
        if escolha in list('1234'):
            if escolha=='1':
                cadastrar_produto()

if __name__== '__main__':
    main()