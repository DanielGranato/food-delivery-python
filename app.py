import os
from modelos.restaurante import Restaurante

Restaurante('Praça', 'Japonesa', False)
Restaurante('Pizza Superma', 'Pizza', True)
Restaurante('Cantina', 'Italiano', False)

def exibir_nome_do_programa():
    print('Sabor Express\n')

def exibir_subtitulo(texto):
    os.system('cls')
    print(f'{texto}\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app')

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrar novo restaurante')
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria = input('Digite a categoria do restaurante: ')
    Restaurante(nome_restaurante, categoria)
    print(f'Restaurante {nome_restaurante} cadastrado com sucesso\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listar restaurantes')
    Restaurante.listar_restaurantes()
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input('\nPressione enter para voltar ao menu principal\n')
    main()

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')

def alterar_estado_restaurante():
    exibir_subtitulo('Alterar estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in Restaurante.restaurantes:
        if nome_restaurante == restaurante.nome:
            restaurante_encontrado = True
            restaurante.alternar_estado()
            mensagem = 'Restaurante ativado com sucesso' if restaurante.ativo else 'Restaurante desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('Restaurante não encontrado\n')
    voltar_ao_menu_principal()

def opcao_invalida():
    print('Opção inválida\n')
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
    except ValueError:
        opcao_invalida()
        return

    if opcao_escolhida == 1:
        cadastrar_novo_restaurante()
    elif opcao_escolhida == 2:
        listar_restaurantes()
    elif opcao_escolhida == 3:
        alterar_estado_restaurante()
    elif opcao_escolhida == 4:
        finalizar_app()
    else:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()



