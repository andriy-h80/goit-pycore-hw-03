
'''
Напишіть функцію get_numbers_ticket(min, max, quantity),
яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей.
Вона буде повертати випадковий набір чисел у межах заданих параметрів,
причому всі випадкові числа в наборі повинні бути унікальні.
'''
import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000:
        return []
    elif quantity < 1 or quantity > (max - min + 1):
        return []
    else:
        numbers = random.sample(range(min, max + 1), quantity)
        return sorted(numbers)

# 6 з 49
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
# 5 з 36
lottery_numbers = get_numbers_ticket(1, 36, 5)
print("Ваші лотерейні числа:", lottery_numbers)
# 6 з 49 (параметри не відповідають обмеженням)
lottery_numbers = get_numbers_ticket(1, 1001, 6)
print("Ваші лотерейні числа:", lottery_numbers)
# 5 з 36 (параметри не відповідають обмеженням)
lottery_numbers = get_numbers_ticket(0, 36, 5)
print("Ваші лотерейні числа:", lottery_numbers)
