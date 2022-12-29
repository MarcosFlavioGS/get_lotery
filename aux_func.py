import random

def generator(list, input):
    nums = [random.choice(list) for i in range(1, input+1)]
    for n in nums:
        if nums.count(n) > 1:
            result = generator(list, input)
            result.sort()
            return result
        else:
            continue
    nums.sort()
    return nums

def fast_generator(list, input):
    nums = []
    while len(nums) < input:
        num = random.choice(list)
        if num not in nums:
            nums.append(num)
    nums.sort()
    return nums

def read_integers(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        numbers = []
        for line in lines:
            for number in line.split():
                numbers.append(int(number))
        return numbers

# def read_integers(filename):
#     with open(filename) as f:
#         return [int(x) for x in f]

def number_ocurrence(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        numbers = {}
        for line in lines:
            for number in line.split():
                if number in numbers:
                    numbers[number] += 1
                else:
                    numbers[number] = 1
        return numbers

def line_ocurrence(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        numbers = {}
        for line in lines:
            if line in numbers:
                numbers[line] += 1
            else:
                numbers[line] = 1
        return numbers