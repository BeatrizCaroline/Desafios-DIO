def menu():
    return int(input("___Informe uma opção:___ \n [1] Sacar \n [2] Depositar \n [3] Investir \n [4] Extrato \n [5] Novo usuário \n [6] Nova conta \n [7] Listar contas \n [8] Sair \nDigite... "))

def sacar(*, valor_saque, saldo, limite_dia, nmr_saques, LIMITE_SAQUES, extrato):
    if valor_saque > saldo:
        print("Saldo insuficiente.")
    elif valor_saque > limite_dia:
        print("O limite de valor diário foi excedido.")
    elif nmr_saques >= LIMITE_SAQUES:
        print("O limite de saques foi excedido.")
    else:
        nmr_saques += 1
        saldo -= valor_saque
        extrato += f"Saque: R$ {valor_saque:.2f}\n"
        print("Quantia retirada com sucesso!")

    return saldo, extrato, nmr_saques  # Retornando o número de saques atualizado

def depositar(valor_deposito, saldo, extrato):
    if valor_deposito >= 1:
        print("Quantia depositada com sucesso!")
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
    else:
        print("Valor não aceito.")
    return saldo, extrato

def investir(valor_investido, saldo, extrato):
    if valor_investido < 10:
        print("Investimento insuficiente.")
    else:
        print("Quantia investida com sucesso!")
        saldo -= valor_investido
        extrato += f"Investimento: R$ {valor_investido:.2f}\n"
    return saldo, extrato

def exibir_extrato(saldo, extrato):
    print("\n________Exibindo extrato________")
    print("\nNão foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("________________________________")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a sua data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, Nº - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("___Usuário criado com sucesso___")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n___Conta criada com sucesso!___")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n___Usuário não encontrado, fluxo de criação de conta encerrado!___")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def main():

    saldo = 3500
    limite_dia = 500
    extrato = ""
    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    nmr_saques = 0
    usuarios = []
    contas = []

    while True:
        Opcoes = menu()

        if Opcoes == 1:
            valor_saque = float(input("Valor do saque: "))
            saldo, extrato, nmr_saques = sacar(
                valor_saque=valor_saque,
                saldo=saldo,
                limite_dia=limite_dia,
                nmr_saques=nmr_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,
                extrato=extrato,
            )

        elif Opcoes == 2:
            valor_deposito = float(input("Valor do depósito: "))
            saldo, extrato = depositar(valor_deposito=valor_deposito, saldo=saldo, extrato=extrato)

        elif Opcoes == 3:
            valor_investido = float(input("Valor do investimento: "))
            saldo, extrato = investir(valor_investido=valor_investido, saldo=saldo, extrato=extrato)

        elif Opcoes == 4:
            exibir_extrato(saldo=saldo, extrato=extrato)

        elif Opcoes == 5:
            criar_usuario(usuarios)

        elif Opcoes == 6:
            numero_conta = len(contas) + 1
            contas.append(criar_conta(AGENCIA, numero_conta, usuarios))

        elif Opcoes == 7:
            listar_contas(contas)

        elif Opcoes == 8:
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

main()