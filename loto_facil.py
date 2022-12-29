from aux_func import fast_generator, line_ocurrence

def loto_facil():
    numbers = []
    for i in range(1, 26):
        numbers.append(i)

    print(f"Número de vezes que cada volante saiu nos ultimos 15 sorteios:\n {line_ocurrence('loto.txt')}")

    print("******************************************************************************************************************")
    ocurrence = int(input("Qual a o número de ocorrências gostaria de filtrar pros ultimos 15 sorteios ? "))
    print("******************************************************************************************************************")

    # for n in numbers:
    #     if list.count(n) >= ocurrence:
    #         if n in commons:
    #             continue
    #         else:
    #             commons.append(n)
    #     else:
    #         dif.append(n)

    re = '1'
    while (re == '1'):
        choice = int(input("Gostaria de quantos números ? (15 - 20)"))
        result = fast_generator(numbers, choice)
        print(f"Números sorteados: {result}")
        re = input("Deseja gerar mais números ? (1 - Sim / 2 - Não) ")

    input("Saindo da lotofácil, pressione qualquer tecla para continuar...")

    if __name__ == "__main__":
        loto_facil()
