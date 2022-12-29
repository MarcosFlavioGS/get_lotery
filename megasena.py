from aux_func import read_integers, generator, number_ocurrence

def mega_sena():
    list = read_integers("mega.txt")
    commons = []
    dif = []
    numbers = []
    for i in range(1, 61):
        numbers.append(i)

    print("******************************************************************************************************************")
    print("Números com uma determinada quantidade de ocorrência nos ultimos sorteios serão filtrados!")
    print("Foi notado que um número que se repete 2 vezes ou mais nos últimos 15 sorteios, raramente é sorteado no próximo...")
    print("Porém, fica a sua escolha qual a ocorrência desejada para a aplicação do filtro!")
    print("******************************************************************************************************************")

    print(f"Quantidade de vezes que cada número saiu nos ultimos 15 sorteios:\n {number_ocurrence('mega.txt')}")

    ocurrence = int(input("Qual a o número de ocorrências gostaria de filtrar pros ultimos 15 sorteios ? "))
    print("******************************************************************************************************************")

    for n in numbers:
        if list.count(n) >= ocurrence:
            if n in commons:
                continue
            else:
                commons.append(n)
        else:
            dif.append(n)

    commons.sort()
    dif.sort()

    print(f"\nNúmeros que saíram {ocurrence} vezes ou mais nos ultimos 15 sorteios: {commons}")
    print(f"\nNúmeros que saíram menos de {ocurrence} vezes nos ultimos 15 sorteios: {dif}")

    re = '1'
    while (re == '1'):
        choice = int(input("Gostaria de quantos números ? "))
        result = generator(dif, choice)
        print(f"Números sorteados: {result}")
        re = input("Deseja gerar mais números ? (1 - Sim / 2 - Não) ")

    input("Saindo da mega sena, pressione qualquer tecla para continuar...")

    if __name__ == "__main__":
        mega_sena()