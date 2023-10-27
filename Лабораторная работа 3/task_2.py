# TODO Напишите функцию find_common_participants
def find_common_participants(string1, string2, sep=','):
    string1 = string1.split(sep)
    string2 = string2.split(sep)
    return sorted(set(string1).intersection(string2))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_second_group, participants_first_group, '|'))