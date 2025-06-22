import time 
import os

def limpar_tela():
    """Limpa o terminal de forma compatível com Windows, Linux e macOS."""
    os.system('cls' if os.name == 'nt' else 'clear')

#Simulador de empréstimos 
limpar_tela()

print('='*30)
print('   Simulador de empréstimos')
print('='*30)

while True:
    try:
        valor_emp = float(input('Qual o valor do empréstimo desejado? ').strip())
        if valor_emp > 0:
            break
        else:
           print('O valor precisa ser maior que zero.')
    except ValueError:
        print('Digite um número válido.')

while True:
    try:
        prazo = int(input('Insira o prazo de pagamento (em meses): ').strip())
        if prazo > 0:
            break
        else:
            print('O prazo precisa ser de no mínimo 1 mês.')
    except ValueError:
        print('Digite um número válido.')

while True:
    try:
        taxa_juros = int(input('Informe a taxa de juros mensal (%): ').strip())
        if taxa_juros >= 0:
            break
        else:
            print('A taxa de juros não pode ser nagativa.')
    except ValueError:
        print('Digite um número válido.')

time.sleep(1)
limpar_tela()

def sac(valor_emp, prazo, taxa_juros):
    amortizacao = valor_emp / prazo
    saldo = valor_emp
    parcelas = []
    for mes in range(1, prazo + 1):
        juros = saldo * taxa_juros
        parcela = amortizacao + juros
        parcelas.append(parcela)
        saldo -= amortizacao
    total_pago = sum(parcelas)
    total_juros = total_pago - valor_emp
    return parcelas, total_pago, total_juros
    
def price(valor_emp, prazo, taxa_juros):
    parcela_fixa = (valor_emp * taxa_juros) / (1 - (1 + taxa_juros) ** -prazo)
    total_pago = parcela_fixa * prazo
    total_juros = total_pago - valor_emp
    parcelas = [parcela_fixa] * prazo
    return parcelas, total_pago, total_juros

while True:
    time.sleep(1)
    limpar_tela()
    print('='*30)
    print('Tipo de amortização')
    print('='*30)
    print('[1] SAC')
    print('[2] PRICE')

    opcao = int(input('Escolha uma opção: ').strip())
    if opcao == 1:
        parcelas, total_pago, total_juros = sac(valor_emp, prazo, taxa_juros / 100)  # Corrige taxa: % para decimal

        # Exibir resultados
        print('\n--- Resultado da Simulação (SAC) ---')
        for i, valor in enumerate(parcelas, start=1):
            print(f'Mês {i}: R$ {valor:.2f}')
        print(f'\nTotal pago ao final do empréstimo: R$ {total_pago:.2f}')
        print(f'Total de juros pagos: R$ {total_juros:.2f}')
        break

    elif opcao == 2:
        parcelas, total_pago, total_juros = price(valor_emp, prazo, taxa_juros / 100)

        for i, valor in enumerate(parcelas, start=1):
            print(f'Mês {i}: R$ {valor:.2f}')
        print(f'\nTotal pago ao final do empréstimo: R$ {total_pago:.2f}')
        print(f'Total de juros pagos: R$ {total_juros:.2f}')
        break
       
    else:
        print('Insira um digito válido (1 ou 2).')
