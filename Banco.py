import sys

saldo = 3500
limite_dia = 500
extrato = ""
LIMITE_SAQUES = 3
nmr_saques = 0

while True:
    Opcoes = int(input("Informe uma opção: \n [1] Sacar \n [2] Depositar \n [3] Investir \n [4] Extrato \n [5] Sair \n Digite... "))

    if Opcoes == 1:
        valor_saque = float(input("Valor do saque: "))
        if valor_saque > saldo:
            print("Saldo insuficiente.")
        elif valor_saque > limite_dia:
            print("O limite de valor foi excedido.")
        elif nmr_saques >= LIMITE_SAQUES:
            print("O limite de saques foi excedido.")
        else:
            print("Quantia retirada com sucesso!")
            nmr_saques += 1
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"

    elif Opcoes == 2:
        valor_deposito = float(input("Valor do depósito: "))
        if valor_deposito >= 1:
            print("Quantia depositada com sucesso!")
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        else:
            print("Valor não aceito.")

    elif Opcoes == 3:
        valor_investido = float(input("Valor do investimento: "))
        if valor_investido < 10:
            print("Investimento insuficiente.")
        else:
            print("Quantia investida com sucesso!")
            saldo -= valor_investido
            extrato += f"Investimento: R$ {valor_investido:.2f}\n"

    elif Opcoes == 4:
        print("\n________Exibindo extrato________")
        print("\nNão foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("__________________________")

    elif Opcoes == 5:
        print("Saindo do programa...")
        break

    else:
        sys.exit("Opção inválida, tente novamente.")