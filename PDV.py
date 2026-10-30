listaCompras = []
ComprasComDesconto = []

#menu de apresentação
print(10*"==")
print(4*" ","PDV python")
print(10*"==")


#validação de idade e nome   
nome = str(input('digite seu nome: '))
idade = int(input('digite sua idade: '))
while idade <= 0:
    idade = int(input('digite uma idade valida: '))

#valores das compras    
while True:
    listaCompras.append(float(input('digite o valor da compra (0 = sair): ')))
    if listaCompras[-1] == 0:
        listaCompras.remove(0)
        break

#se idade for igual ou maior que 65 ganha desconto de 20 por cento
if idade >= 65:
    for i in range(len(listaCompras)):
        ComprasComDesconto.append(listaCompras[i] - listaCompras[i]*0.20)
if idade >= 65:
    for j in range(len(ComprasComDesconto)):
        if ComprasComDesconto[j] > 100:
            ComprasComDesconto[j] =  ComprasComDesconto[j] -  ComprasComDesconto[j]*0.10
elif idade < 65:
    for j in range(len(listaCompras)):
        if listaCompras[j] > 100:
            listaCompras[j] =  listaCompras[j] -  listaCompras[j]*0.10

#formatação 
print(f"total bruto: {sum(listaCompras)}")
print(f"total de descontos: {sum(listaCompras) - sum(ComprasComDesconto)}")
print(f"total de compras: {len(listaCompras)}")
if idade >= 65:
    print(f"total final: {sum(ComprasComDesconto)}")
else:
    print(f"total final: {sum(listaCompras)}")



    
