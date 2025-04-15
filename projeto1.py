# Função para validar a entrada do usuário
def input_valido(mensagem, tipo_dado=float):
    while True:
        try:
            return tipo_dado(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, insira o tipo de dado correto.")

# Função para calcular a dosagem de herbicidas
def dosagem():
    """
    Calcula a quantidade de herbicida necessária com base nos parâmetros fornecidos.
    """
    while True:
        litros = input_valido('Digite a quantidade de litros a dosar: ', float)
        vazao = input_valido('Digite a vazão por hectare (ha): ', int)
        dose = input_valido('Qual é a dose por hectare (ha) do produto? ', float)
        print('\n')

        jogar = (litros / vazao) * dose

        print('-=' * 35)
        print(f'Você irá jogar no tanque de {litros} lts {jogar:.2f} lts ou kg de produto.')
        print('-=' * 35)
        print('\n')

        resp = input('Deseja dosar novamente? [S/N]: ').strip().lower()
        if resp == 'n':
            print('-=' * 20)
            print('Espero ter ajudado, bom trabalho!')
            print('-=' * 20)
            print('\n')
            break

# Função para calcular a quantidade de insumos
def calculo_insumos():
    """
    Calcula a quantidade de insumos necessários para uma área determinada.
    """
    while True:
        area = input_valido('Digite o tamanho da área em hectares (ha): ', float)
        vazao = input_valido('Digite a vazão por hectare (ha): ', float)
        print('\n')

        calculo = area * vazao
        print('-=' * 26)
        print(f'A quantidade de insumos para fechar a área é: {calculo:.2f} T')
        print('-=' * 26)
        print('\n')

        resp = input('Deseja calcular área novamente? [S/N]: ').strip().lower()
        if resp == 'n':
            print('-=' * 20)
            print('Espero ter ajudado, bom trabalho!')
            print('-=' * 20)
            print('\n')
            break

# Função para voltar ao menu principal
def voltar_ao_menu():
    print("\nVoltando ao menu principal...\n")

# Menu de escolha de função
def menu():
    """
    Exibe um menu principal para o usuário selecionar a ação desejada.
    """
    while True:
        print('MENU:')
        print('-=' * 10)
        print('1. DOSAGEM:')
        print('2. CALCULAR INSUMOS:')
        print('0. SAIR')
        print('-=' * 10)
        print('\n')

        escolha = input_valido('Escolha uma opção: ', int)
        if escolha == 1:
            dosagem()
            voltar_ao_menu()
        elif escolha == 2:
            calculo_insumos()
            voltar_ao_menu()
        elif escolha == 0:
            print('Saindo...')
            break
        else:
            print('Escolha inválida, tente novamente!')

# Executa o menu
menu()