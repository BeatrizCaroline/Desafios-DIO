import sys

saldo = 3500
limite_dia = 500
extrato = ""
LIMITE_SAQUES = 3

Opcoes = int(input("Informe uma opção: \n [1] Sacar \n [2] Depositar \n [3] Investir \n [4] Extrato "))

if Opcoes == 1:
    valor_saque = float(input("Valor do saque: "))
if valor_saque > saldo:
    if valor_saque > limite_dia:
        print("Saldo insuficiente! ")
    else:
        print("Quantia retirada com sucesso! ")

elif Opcoes == 2:
    valor_deposito = float(input("Valor do deposito: "))
    if valor_deposito < 2:
        print("Valor não aceito. ")
    else:
        print("Quantia depositada com sucesso! ")

elif Opcoes == 3:
    valor_investido = float(input("Valor do investimento: "))
    if valor_investido < 10:
        print("Inestimento insuficiente. ")
    else:
        print("Quantia investida com sucesso! ")

#saldo_atual = saldo - valor_saque - valor_investido + valor_deposito

elif Opcoes == 4:  
    print("Exibindo extrato...")
    print("Saldo: ", saldo)

else:
    sys.exit("Opção inválida")