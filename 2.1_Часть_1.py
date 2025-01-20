# 1.
# Функция hide_card().
def hide_card(card_number):
    card_number = card_number.replace(' ', '')
    result = '*' * len(card_number[:-4]) + card_number[-4:]

    return result

print(hide_card('905 678123 45612 56'))


# 2.
# Функция same_parity().
# def same_parity(numbers):
#     if len(numbers) > 0:
#         first_num = numbers[0]
#
#         if first_num % 2 == 0:
#             is_even = True
#             is_odd = False
#         else:
#             is_even = False
#             is_odd = True
#
#         result = []
#         for i in numbers:
#             if (i % 2 == 0) and is_even:
#                 result.append(i)
#             elif (i % 2 != 0) and is_odd:
#                 result.append(i)
#
#         return result
#
#     else:
#         return numbers

def same_parity(numbers):
    if not numbers:
        return numbers

    parity = numbers[0] % 2  # Определяем четность первого числа.
    return [num for num in numbers if num % 2 == parity]

print(same_parity([-7, 0, 67, -9, 70, -29, 90]))


# 3.
# Функция is_valid().
# def is_valid(pin_code):
#     if (len(pin_code) > 3 and len(pin_code) < 7) and \
#         (pin_code.isdigit()):
#         return True
#     else:
#         return False

def is_valid(pin):
    return pin.isdigit() and len(pin) in (4, 5, 6)

print(is_valid('89abc1'))


# 4.
# Функция print_given().
def print_given(*args, **kwargs):
    for arg in args:
        print(f'{arg} {type(arg)}')

    for key in sorted(kwargs.keys()):
        print(f'{key} {kwargs[key]} {type(kwargs[key])}')

print_given(1, [1, 2, 3], 'three', two=2)


# 5.
# Функция convert().
import string
def convert(text):
    lower_case_symbols = len(list(filter(lambda x: x in string.ascii_lowercase, text)))
    upper_case_symbols = len(list(filter(lambda x: x in string.ascii_uppercase, text)))

    if lower_case_symbols >= upper_case_symbols:
        return text.lower()
    else:
        return text.upper()

print(convert('ABCdef'))
