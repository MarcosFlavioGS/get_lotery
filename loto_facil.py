from aux_func import generator, line_occurrence

def check_for_occurrence(occurrence, result):
    for i in occurrence:
        if i == result:
            return True
    return False

def loto_facil():
    numbers = []
    for i in range(1, 26):
        numbers.append(i)

    occurrence = line_occurrence('loto.txt')

    for item in occurrence:
        if occurrence[item] > 1:
            print(f"Volante {item} já saiu {occurrence[item]} vezes")

    while (True):
        choice = int(input("\nGostaria de quantos números ? (15 - 20): "))
        result = generator(numbers, choice)
        print(f"\nNúmeros sorteados: {result}")

        if check_for_occurrence(occurrence, result) == True:
            print(f"\nEsse volante já saiu {occurrence[result]} vezes")
        else:
            print(f"\nEsse volante ainda não saiu nos ultimos {len(occurrence)} sorteios")
        
        re = input("\nDeseja gerar mais números ? (1 - Sim / 2 - Não) ")
        if re == "1":
            continue
        else:
            break

    input("\nSaindo da lotofácil, pressione qualquer tecla para continuar...")

if __name__ == "__main__":
    loto_facil()
