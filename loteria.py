import random

def generator(dif, input):
    nums = [random.choice(dif) for i in range(1, input+1)]
    for n in nums:
        if nums.count(n) > 1:
            result = generator(dif, input)
            result.sort()
            return result
        else:
            continue
    nums.sort()
    return nums

def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f]

list = read_integers("numbers.txt")
commons = []
dif = []

print("*******************************************************************************************************")
print("Números com uma determinada quantidade de ocorrência nos ultimos sorteios serão filtrados!")
print("Foi notado que um número que se repete 2 vezes ou mais nos últimos 15 sorteios, raramente é sorteado...")
print("Porém, fica a sua escolha qual a ocorrência desejada para a aplicação do filtro!")
print("*******************************************************************************************************")
ocurrence = int(input("Qual a o número de ocorrências gostaria de filtrar pros ultimos 15 sorteios ? "))
print("*******************************************************************************************************")

for n in list:
    if list.count(n) > ocurrence:
        if n in commons:
            continue
        else:
            commons.append(n)
    else:
        dif.append(n)

commons.sort()
dif.sort()

print(f"Números que saíram {ocurrence} vezes ou mais nos ultimos 15 sorteios: {commons}")
input = int(input("Gostaria de quantos números ? "))

result = generator(dif, input)

print(f"Números sorteados: {result}")
