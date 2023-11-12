# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants_first_group = participants_first_group.split('|')

participants_second_group = participants_second_group.split('|')


first = set()
for i in participants_first_group:
    first.append(i)
find_common_participants = participants_first_group.intersection(participants_second_group)
print(find_common_participants) ff


# TODO Провеьте работу функции с разделителем отличным от запятой
