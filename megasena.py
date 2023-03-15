from aux_func import read_integers, generator, number_occurrence

def mega_sena():
    list = read_integers("mega.txt")
    commons = []
    dif = []
    numbers = [i for i in range(1, 61)]

    print("******************************************************************************************************************")
    print("Números com uma determinada quantidade de ocorrência nos ultimos sorteios serão filtrados!")
    print("Foi notado que um número que se repete 2 vezes ou mais nos últimos 15 sorteios, raramente é sorteado no próximo...")
    print("Porém, fica a sua escolha qual a ocorrência desejada para a aplicação do filtro!")
    print("******************************************************************************************************************")

    num_occurrence = number_occurrence('mega.txt')

    print(f"Quantidade de vezes que cada número saiu nos ultimos 15 sorteios:\n {num_occurrence}")

    occurrence = int(input("\nQual a o número de ocorrências gostaria de filtrar pros ultimos 15 sorteios ? "))
    print("******************************************************************************************************************")

    for n in numbers:
        if list.count(n) >= occurrence:
            if n in commons:
                continue
            else:
                commons.append(n)
        else:
            dif.append(n)

    commons.sort()
    dif.sort()

    print(f"\nNúmeros que saíram {occurrence} vezes ou mais nos ultimos 15 sorteios: {commons}")
    print(f"\nNúmeros que saíram menos de {occurrence} vezes nos ultimos 15 sorteios: {dif}")

    re = '1'
    while (re == '1'):
        choice = int(input("\nGostaria de quantos números ? "))
        result = generator(dif, choice)
        print(f"\nNúmeros sorteados: {result}")
        re = input("\nDeseja gerar mais números ? (1 - Sim / 2 - Não) ")

    input("\nSaindo da mega sena, pressione qualquer tecla para continuar...")

if __name__ == "__main__":
    mega_sena()
