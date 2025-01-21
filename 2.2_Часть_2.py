# 1.
# Тимур, Артур и новый курс.
def minimal_distance(d1, d2, d3):
    # Четыре возможных маршрута.
    route1 = d1 + d3 + d2  # Через оба магазина и соединяющую дорожку.
    route2 = 2 * (d1 + d3)  # Через первый магазин и возвращение через второй.
    route3 = 2 * (d2 + d3)  # Через второй магазин и возвращение через первый.
    route4 = 2 * d1 + 2 * d2  # Посещение обоих магазинов с возвращением домой каждый раз.

    # Минимальное расстояние.
    return min(route1, route2, route3, route4)

# Ввод данных.
d1 = int(input())
d2 = int(input())
d3 = int(input())

# Вывод минимального расстояния.
print(minimal_distance(d1, d2, d3))


# 2.
# Схожие буквы.
def same_letters(letters):
    d = {
        'en': 'abcehkmoptxy',
        'ru': 'авекмнорстух'
    }

    en = 0
    ru = 0

    for letter in letters:
        if letter.lower() in d['en']:
            en += 1
        elif letter.lower() in d['ru']:
            ru +=1

    if en == 3:
        return 'en'
    elif ru == 3:
        return 'ru'
    elif (0 < en < 3) and (0 < ru < 3):
        return 'mix'

letter1 = input()
letter2 = input()
letter3 = input()

print(same_letters([letter1, letter2, letter3]))


# 3.
# Переворатор.
def reverse(sequence):
    n, x, y, a, b = sequence

    numbers = list(range(1, n + 1))

    # Переворачиваем часть от X до Y.
    numbers[x - 1:y] = reversed(numbers[x - 1:y])

    # Переворачиваем часть от A до B.
    numbers[a - 1:b] = reversed(numbers[a - 1:b])

    numbers = [str(i) for i in numbers]
    return ' '.join(numbers)

sequence = [int(i) for i in input().split()]

print(reverse(sequence))


# 4.
# Более одного.
def more_than_one(sequence):
    result = []

    for i in sequence:
        if sequence.count(i) > 1 and i not in result:
            result.append(i)

    result = sorted([int(i) for i in result])

    return ' '.join([str(i) for i in result])

sequence = input().split()

print(more_than_one(sequence))
