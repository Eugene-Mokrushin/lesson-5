# 3. Есть два списка:
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors,
# необходимо вывести последние кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)
#
# ### Доказать, что вы создали именно генератор.
# Проверить его работу вплоть до истощения. Подумать, в каких ситуациях генератор даст эффект.
#


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Елена1'
]
classes = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]


def tutors_and_classes():
    """Возвращает учителя и приписаный к нему класс"""

    length_tutor = len(tutors)
    length_classes = len(classes)
    for i in range(length_tutor):
        # Если кол-во классов все еще меньше кол-ву приписанных учителей
        if length_classes > i:
            yield (tutors[i], classes[i])
        # Если учителя на классы закончились
        else:
            yield (tutors[i], 'None')


teacher_and_assigned_group = tutors_and_classes()

# Доказываем по заданию что мы написали именно генератор
print(type(teacher_and_assigned_group))

# Можно также с помощью for
print(next(teacher_and_assigned_group))
print(next(teacher_and_assigned_group))
print(next(teacher_and_assigned_group))
print(next(teacher_and_assigned_group))
print(next(teacher_and_assigned_group))
print(next(teacher_and_assigned_group))
print(next(teacher_and_assigned_group))
print(next(teacher_and_assigned_group))
print(next(teacher_and_assigned_group))
print(next(teacher_and_assigned_group))
print(next(teacher_and_assigned_group))

# Вообще правильнее было бы дополнить генератор, чтобы он также мог выводить когда классов больше чем учителей
# Например (None, 12A)
# Но программирование ведь чтобы сделать жизнь проще - зачем усложнять задание?:)
