from abc import ABC, abstractclassmethod, abstractproperty
import textwrap


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, usuario):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._usuario = usuario
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, usuario, numero):
        return cls(numero, usuario)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def usuario(self):
        return self._usuario
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\nXXX Operação falhou! Você não tem saldo suficiente. XXX")

        elif valor > 0:
            self._saldo -= valor
            print("\n>>> Saque realizado com sucesso! <<<")
            return True
        
        else:
            print("\nXXX Operação falhou! O valor informado é inválido. XXX")
            return False
        
    def investir(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\nXXX Operação falhou! Você não tem saldo suficiente. XXX")

        elif valor > 0:
            self._saldo -= valor
            print("\n>>> Investimento realizado com sucesso! <<<")
            return True
        
        else:
            print("\nXXX Operação falhou! O valor informado é inválido. XXX")
            return False
    
        
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n>>> Depósito realizado com sucesso! <<<")
        else:
            print("\nXXX Operação falhou! O valor informado é inválido. XXX")
            return False

        return True
        
class ContaCorrente(Conta):
    def __init__(self, numero, usuario, limite=500, limite_saques=3):
        super().__init__(numero, usuario)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes
             if transacao["tipo"] == Saque.__name__])

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\nXXX Operação falhou! O valor do saque excedeu o limite XXX")

        elif excedeu_saques:
            print("\nXXX Operação falhou! Número máximo de saques excedido. XXX")

        else:
            return super().sacar(valor)
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.usuario.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
            }
        )        

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass 

    @abstractclassmethod
    def registrar(self, conta):
        pass   

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Investir(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.investir(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
        
class Deposito(Transacao):

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

def menu():
    return int(input("___Escolha uma das opções:___ \n [1] Sacar \n [2] Depositar \n [3] Investir \n [4] Extrato \n [5] Novo usuário \n [6] Nova conta \n [7] Listar contas \n [8] Sair \nDigite... "))

def sacar(usuarios):
    cpf = input("Informe o CPF do cliente: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\n XXX Cliente não encontrado! XXX")
        return

    valor = float(input("Informe o valor do saque: "))
    
    transacao = Saque(valor)

    conta = recuperar_conta_usuario(usuario)
    if not conta:
        return

    usuario.realizar_transacao(conta, transacao)

def depositar(usuarios):
    cpf = input("Informe o CPF do cliente: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\nXXX Cliente não encontrado! XXX")
        return
    
    valor = float(input("informe o valor do depósito: "))
    transacao = Deposito(valor)
    conta = recuperar_conta_usuario(usuario)
    if not conta:
        return
    
    usuario.realizar_transacao(conta, transacao)

def investir(usuarios):
    cpf = input("Informe o CPF do cliente: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\n XXX Cliente não encontrado! XXX")
        return

    valor = float(input("Informe o valor do ivestimento: "))
    
    transacao = Investir(valor)

    conta = recuperar_conta_usuario(usuario)
    if not conta:
        return

    usuario.realizar_transacao(conta, transacao)

def exibir_extrato(usuarios):
    cpf = input("Informe o CPF do cliente: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\nXXX Cliente não encontrado! XXX")
        return

    conta = recuperar_conta_usuario(usuario)
    if not conta:
        return
    
    print("\n________Exibindo extrato________")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações"
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("________________________________")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nXXX Já existe usuário com esse CPF! XXX")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a sua data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, Nº - bairro - cidade/sigla estado): ")

    usuario = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    usuarios.append(usuario)

    print("<<<< Usuário criado com sucesso >>>>")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario.cpf == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\nXXXX Usuário não encontrado, fluxo de criação de conta encerrado! XXXX")
        return

    conta = ContaCorrente.nova_conta(usuario=usuario, numero=numero_conta)
    contas.append(conta)
    usuario.contas.append(conta)

    print("\n<<<< Conta criada com sucesso! >>>>")

def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta))) 

def recuperar_conta_usuario(usuario):
    if not usuario.contas:
        print("\nXXX Cliente não possui conta! XXX")
        return
    
    # FIXME: não permite cliente escolher a conta
    return usuario.contas[0]

def main():

    usuarios = []
    contas = []

    while True:
        Opcoes = menu()

        if Opcoes == 1:
            sacar(usuarios)
        elif Opcoes == 2:
            depositar(usuarios)
        elif Opcoes == 3:
            investir(usuarios)
        elif Opcoes == 4:
            exibir_extrato(usuarios)
        elif Opcoes == 5:
            criar_usuario(usuarios)
        elif Opcoes == 6:
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, usuarios, contas)
        elif Opcoes == 7:
            listar_contas(contas)

        elif Opcoes == 8:
            print("Saindo...")
            break

        else:
            print("XXXX Opção inválida, tente novamente. XXXX")

main()
