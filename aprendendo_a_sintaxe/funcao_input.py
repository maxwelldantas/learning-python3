# Função input()
# Entrada de dados através do console


# nome = 'Maxwell'
# print(nome)

# por padrão a função input() irá considerar string todos os dados digitados
# nome = input('Digite seu nome ')
# print(nome)

# Efetuando Cálculos
# A função input sempre retorna uma string
# int()
# float()
# str()

print('Somar dois números')
# temos que converter o input para inteiro para podermos efetuar a soma
a = int(input('Digite o primeiro número '))
b = int(input('Digite o segundo número '))

soma = a + b

print('A soma do número', a, 'com o número', b, 'é igual a', soma)
