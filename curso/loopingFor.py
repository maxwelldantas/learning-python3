# Looping for
# for x in range(10):
#     print(x)


# Contagem iniciando de 1 a 10, o 11 não entra na contagem pois é exclusivo
# já o número 1 entra na contagem por ser inclusivo
# for x in range(1, 11):
#     print(x)

# Contagem iniciando de 0 a 10, o 10 não entra na contagem pois é exclusivo
# já o número 0 entra na contagem por ser inclusivo
# o terceiro argumento passado que é o 3 quer dizer que serão contados de 3 em 3 o for
# for x in range(0, 10, 3):
#     print(x)
#
# for x in range(0, 10, 2):
#     print(x)


carros = ['Camaro', 'Ranger', 'Pajero', 'Hilux']
# Para cada elemento de carros 'a' assumirá o valor
# isso quer dizer que será percorrida toda a lista de carros e
# a cada looping será atribuído o valor a 'a'
# for a in carros:
#     print(a)


nome = 'Maxwell'
# a função len() tem objetivo com contar objetos ou caracteres contidos dentro de uma variável
print(len(nome))
# dentro de carros temos 4 objetos, por isso será imprimido 4
print(len(carros))

# irá imprimir cada na cada em sua posição
for a in range(len(carros)):
    print(carros[a])
