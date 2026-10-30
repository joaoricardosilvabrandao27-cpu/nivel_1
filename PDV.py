
listaCompras = []
ComprasComDesconto = []

# menu de apresentação
print(10 * "==")
print(4 * " ", "PDV python")
print(10 * "==")

# validação de idade e nome
nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))

if idade < 0:
    print('Idade inválida!')

while idade < 0:
    idade = int(input('Digite uma idade válida: '))

# valores das compras
while True:
    valor = float(input('Digite o valor da compra (0 = sair): '))

    # encerra o programa
    if valor == 0:
        break

    # validação do valor
    if valor < 0:
        print('Valor inválido!')
        continue

    # guarda o valor original
    listaCompras.append(valor)

    # desconto por idade
    if idade >= 65:
        valor = valor - (valor * 0.20)

    # desconto por valor
    if valor > 100:
        valor = valor - (valor * 0.10)

    # guarda o valor com desconto
    ComprasComDesconto.append(valor)

    # exibe o valor final
    print(f'Valor final: R$ {valor:.2f}')

# resumo final
total_bruto = sum(listaCompras)
total_final = sum(ComprasComDesconto)
total_descontos = total_bruto - total_final

print('\n========== RESUMO DO DIA ==========')
print(f'Cliente: {nome}')
print(f'Total bruto: R$ {total_bruto:.2f}')
print(f'Total de descontos: R$ {total_descontos:.2f}')
print(f'Quantidade de compras: {len(listaCompras)}')
print(f'Total final: R$ {total_final:.2f}')
print('==================================')
