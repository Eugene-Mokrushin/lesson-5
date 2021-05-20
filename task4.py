# 4. Представлен список чисел.
# Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
# Подсказка: использовать возможности python, изученные на уроке.
# Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
from time import perf_counter
import sys

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# Решение 1 - плохое
start = perf_counter()
result = []
for i in range(1, len(src)):
    if src[i] > src[i - 1]:
        result.append(src[i])

print(result, perf_counter() - start, sys.getsizeof(result))

# Решение 2 с помощью comprehension
start = perf_counter()
comprehension_result = [src[i] for i in range(1, len(src)) if src[i] > src[i - 1]]
print(comprehension_result, perf_counter() - start, sys.getsizeof(comprehension_result))

# Решение 3 с помощью сета
start = perf_counter()
set_result = set()
for i in range(1, len(src)):
    if src[i] > src[i - 1]:
        set_result.add(src[i])

print(set_result, perf_counter() - start, sys.getsizeof(set_result))
