import os

restaurantes = ['Restaurante 1', 'Restaurante 2', 'Restaurante 3']

def exibir_nome_do_programa():
    print('Sabor Express\n')

def finalizar_app():
    os.system('cls')
    print('Finalizando o app\n')

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastrar novo restaurante\n')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_do_restaurante)
    print(f'Restaurante {nome_do_restaurante} cadastrado com sucesso\n')
    input('Pressione enter para voltar ao menu principal')
    main()

def listar_restaurantes():
    os.system('cls')
    print('Listar restaurantes\n')
    for restaurante in restaurantes:
        print(f'{restaurante}')
    input('Pressione enter para voltar ao menu principal')
    main()

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def opcao_invalida():
    print('Opção inválida\n')
    input('Pressione enter para continuar')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            print('Ativar restaurante')
        elif opcao_escolhida == 4: 
            finalizar_app()
        else:
            opcao_invalida()
    except: 
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()


