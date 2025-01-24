from datetime import datetime

produtos=[]

def menu():
    print('Gerenciado de Produtos'.center(100,' '))
    print('1 - Cadastrar Produto')
    print('2 - Remover produto')
    print('3 - Procurar Produto')
    print('4 - Ver Produtos')
    print('5 - Sair')

def adicionar_produto():
    print('Quantos produtos deseja adicionar? ')
    num=int(input('>> '))

def main():
    escolha=''
    while escolha!=5:
        menu()
        escolha=input('>> ')

if __name__== '__main__':
    main()