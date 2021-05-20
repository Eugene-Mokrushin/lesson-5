# 1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...
# 2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.

# Генератор c yield
def sequence_number_generator(max_num):
    """Возвращает генератор - последовательность элементов от 1 до n"""

    for num in range(1, max_num + 1):
        yield num


sequence = sequence_number_generator(15)
for number in sequence:
    print(number)

# Генератор без yield
max_num = 6
nums_gen = (num for num in range(1, max_num + 1))

# Либо:

# for num in nums_gen:
#     print(num)

# Либо:
print('\nДругой вариант решения и их значения\n')
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))


