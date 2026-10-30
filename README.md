PDV Python — Sistema de Ponto de Venda
1. Objetivo do projeto

Este projeto consiste no desenvolvimento de um sistema de PDV (Ponto de Venda) utilizando a linguagem Python. O programa permite registrar várias compras de um cliente, aplicando descontos de acordo com sua idade e o valor de cada compra. Ao finalizar as operações, o sistema apresenta um resumo contendo a quantidade de compras realizadas, o total bruto, o total de descontos concedidos e o valor final a ser pago.

2. Como o código funciona

O programa funciona seguindo as seguintes etapas:

Inicialização: são criadas duas listas, listaCompras e ComprasComDesconto, para armazenar os valores originais e os valores após a aplicação dos descontos.
Identificação do cliente: o sistema solicita o nome e a idade do cliente. Caso a idade seja negativa, solicita novamente uma idade válida.
Registro das compras: o programa utiliza um loop while para permitir o registro de várias compras. Quando o usuário digita 0, o registro é encerrado.
Validação dos valores: caso o usuário informe um valor negativo, o programa exibe uma mensagem de aviso e solicita outro valor.
Desconto por idade: se o cliente tiver 65 anos ou mais, recebe 20% de desconto sobre o valor da compra.
Desconto por valor: depois da aplicação do desconto por idade, o programa verifica se o valor restante é maior que R$ 100,00. Caso seja, aplica mais 10% de desconto.
Armazenamento: os valores originais são armazenados na lista listaCompras, enquanto os valores finais, já com os descontos aplicados, são armazenados na lista ComprasComDesconto.
Resumo final: quando as compras são encerradas, o programa utiliza as funções sum() e len() para calcular e apresentar:
Quantidade de compras realizadas.
Total bruto das compras.
Total de descontos concedidos.
Total final a pagar.
3. Regras de negócio
Condição	Desconto aplicado
Cliente com idade menor que 65 anos	0%
Cliente com idade igual ou superior a 65 anos	20%
Compra com valor, após desconto por idade, maior que R$ 100,00	Mais 10%

Observação: o desconto de 10% é aplicado sobre o valor que já recebeu o desconto por idade, quando houver. Para que ele seja aplicado, o valor precisa ser maior que R$ 100,00.

4. Casos de teste

A tabela abaixo apresenta os resultados esperados para validar o funcionamento do programa.

Nº	Valor (R$)	Idade	Desconto idade	Desconto valor	Valor final esperado
1	50,00	30	0%	0%	R$ 50,00
2	100,00	30	0%	0%	R$ 100,00
3	80,00	65	20%	0%	R$ 64,00
4	100,00	70	20%	0%	R$ 80,00
5	125,00	70	20%	0%	R$ 100,00
6	200,00	30	0%	10%	R$ 180,00
7	101,00	30	0%	10%	R$ 90,90
8	200,00	65	20%	10%	R$ 144,00
9	1.000,00	80	20%	10%	R$ 720,00
10	200,00	64	0%	10%	R$ 180,00
5. Tecnologias e recursos utilizados

O projeto foi desenvolvido utilizando Python e os seguintes recursos:

input(): recebe informações digitadas pelo usuário.
print(): exibe informações no console.
while: permite repetir o registro das compras e realizar validações.
for: estrutura de repetição disponível para percorrer listas, embora não seja necessária na versão final.
if, elif e else: estruturas condicionais utilizadas para verificar as regras de desconto.
append(): adiciona os valores às listas.
sum(): calcula a soma dos valores armazenados.
len(): conta a quantidade de compras registradas.
break: encerra o loop de compras quando o usuário digita zero.
f-string: permite formatar e exibir os valores monetários com duas casas decimais.
6. Como executar o programa

Requisito: ter o Python instalado no computador.

Siga os passos:

Abra a pasta nivel_1 no terminal.
Certifique-se de que o arquivo pdv.py está dentro da pasta.
Execute o seguinte comando:
bash
python pdv.py

Digite o nome e a idade do cliente.
Informe os valores das compras.
Digite 0 quando desejar encerrar as compras.
Confira o resumo final apresentado no console.
7. Estrutura de entrega

A estrutura dos arquivos deve ser:

text
nivel_1/
│
├── pdv.py
│
└── README.md

8. Conclusão

O desenvolvimento deste projeto permitiu praticar conceitos fundamentais da linguagem Python, como listas, estruturas condicionais, laços de repetição, validação de dados e operações matemáticas. Além disso, foi possível compreender como organizar informações e aplicar regras de negócio em um sistema simples de ponto de venda.