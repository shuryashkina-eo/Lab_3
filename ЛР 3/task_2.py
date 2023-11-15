# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants (a, b, separator=','):
    a = a.split(separator)
    b = b.split(separator)
    final = []
    for i in a:
        for j in b:
            if i == j:
                final.append(i)
    final.sort()
    return final
# TODO Провеьте работу функции с разделителем отличным от запятой

common = find_common_participants(participants_first_group, participants_second_group, '|')
print(common)
