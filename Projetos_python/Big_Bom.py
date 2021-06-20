# Um mercadinho de bairro expandiu seus caixas e funcionários, agora eles precisam deum programa que implemente uma caixa registradora simples.  
# O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
#Mercadinho BigBom
#Produto 1: R$ 2.20 
#Produto 2: R$ 5.80
#Produto 3: R$ 0
#Total: R$ 9.00
#Dinheiro: R$ 20.00
#Troco: R$ 11.00

print("_" * 60)
print("Mercadinho BigBom")
precos = []
contador = 1
produto = 1
valores = 1
print("_" * 60)
print("Quando terminar de inserir todos os produtos, digite 0 (ZERO) para parar.")

while (valores > 0):
    valores = float(input(f"Produto {produto}: insira o valor em R$: "))
    precos.append(valores)
    produto += 1
 
i = 0
soma = 0
while i < len(precos):
    soma += precos[i]
    i += 1
print("_" * 60)    
print(f"O valor de suas compras: R${soma:.2f}")

while contador != 0:
    valorPago = float(input(f"Pagamento: "))
    troco =  valorPago - soma 
    if (soma > valorPago):
        print(f"Por favor, inserir um valor valido. Valor total R$: {soma} reais")
    else:
        print("_" * 60)
        print(f"O valor de suas compras: R${soma:.2f}\nValor pago R$ {valorPago}\nTroco de: R$ {troco:.2f} reais")
        print("Obrigado\nVolte sempre! ")
        contador = 0