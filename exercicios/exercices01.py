
# Exercico 1
# Crie uma função que receba uma lista de strings e um valor (uma palavra). 
# A função deve retornar quantas vezes essa palavra aparece na lista.
palavras = ["python", "java", "python", "c++", "python"]

def contar_palavra(list, palavra):
    c = 0
    for i in list:
        if i == palavra:
            c += 1

    return c


print(contar_palavra(palavras, "python"))
print("=" * 50)

# Exercico 2
# Escreva uma função que receba uma lista de números e retorne uma nova lista contendo apenas os números pares.
def filtrar_pares(list):
    new_list = []
    for n in list:
        if n % 2 == 0:
            new_list.append(n)
    return new_list


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = filtrar_pares(numeros)
print(pares)
print("=" * 50)

# Exercico 3
# Crie uma função que receba uma lista de números e um número limite. 
# A função deve somar apenas os números maiores que o limite.
def soma_acima_limite(list, limite):
    soma = 0
    for n in list:
        if n > limite:
            soma += n
    return soma

numeros = [10, 20, 5, 30]
limite = 15
resultado = soma_acima_limite(numeros, limite)

print(resultado)
print("=" * 50)

# Exercico 4
# Escreva uma função que receba uma lista e retorne um dicionário indicando a frequência de cada elemento.
# A Key seria o elemento, e o Value a sua frequencia.
def frequencia(list):
    dicionario = dict()
    for i in list:
        c = 0
        for j in list:
            if i == j:
                c += 1
        dicionario[i] = c
    return dicionario

lista = [1, 2, 2, 3, 3, 3, 4, 1, 1, 4]

print(frequencia(lista))
print("=" * 50)
