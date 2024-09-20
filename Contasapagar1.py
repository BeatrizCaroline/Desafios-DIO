salário = 1500
aluguel = 500
alimento = 300
sobra = aluguel - alimento

if sobra > 0:
    teve_sobra = True
    print('A sobra foi de', sobra)

if sobra < 1:
    Sem_sobra = False
    print('A divida foi de', sobra)

nome_pessoa = "Aurora Reis"
nome_pessoa = nome_pessoa.upper()
print(nome_pessoa)
nome_pessoa = nome_pessoa.lower()
print(nome_pessoa)

print(nome_pessoa.find("R"))

print(nome_pessoa[:6])

novo_sobrenome = nome_pessoa.replace("reis", "brito")
print(novo_sobrenome)

print(novo_sobrenome.title())

reforma_casa = float(input("Escreva quanto paga para um pedreiro: "))
dois_pedreiros = reforma_casa * 2
print(dois_pedreiros)
