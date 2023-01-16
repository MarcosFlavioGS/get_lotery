from aux_func import generator, line_occurrence

def check_occurrence(dict, list, str):
    for key in dict:
        count = 0
        key_elements = key.split(' ')
        for element in key_elements:
            if element in list:
                count += 1
            if count == 15:
                str = key
                return True
    return False

def loto_facil():
    numbers = []
    for i in range(1, 26):
        numbers.append(i)

    occurrence = line_occurrence('loto.txt')

    for item in occurrence:
        if occurrence[item] > 1:
            print(f"\nVolante {item} já saiu {occurrence[item]} vezes nos ultimos {len(occurrence)} sorteios")

    while (True):
        choice = int(input("\nGostaria de quantos números ? (15 - 20): "))
        result = generator(numbers, choice)
        print(f"\nNúmeros sorteados: {result}")

        str = ""
        if check_occurrence(occurrence, numbers, str) == True:
            print(f"\nEsses números já saíram {occurrence[str]} vezes nos últimos {len(occurrence)} sorteios")
        else:
            print("\nEsses números ainda não saíram nos ultimos sorteios")

        re = input("\nDeseja gerar mais números ? (1 - Sim / 2 - Não) ")
        if re == "1":
            continue
        else:
            break

    input("\nSaindo da lotofácil, pressione qualquer tecla para continuar...")

if __name__ == "__main__":
    loto_facil()
