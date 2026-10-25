import os

restaurantes = ['Restaurante 1', 'Restaurante 2', 'Restaurante 3']

def exibir_nome_do_programa():
    print('Sabor Express\n')

def exibir_subtitulo(texto):
    os.system('cls')
    print(f'{texto}\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app')

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrar novo restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_do_restaurante)
    print(f'Restaurante {nome_do_restaurante} cadastrado com sucesso\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listar restaurantes')
    for restaurante in restaurantes:
        print(f'{restaurante}')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input('\nPressione enter para voltar ao menu principal\n')
    main()

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def opcao_invalida():
    print('Opção inválida\n')
    voltar_ao_menu_principal()

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


