# TODO  Напишите функцию count_letters


# TODO Напишите функцию calculate_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
def count_letters(string):
    string = string.lower()
    symbols = list (string)
    letters = []
    for symbol in symbols:
        if symbol.isalpha() == True:
            letters.append(symbol)
    dict = {}
    for letter in letters:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict

def calculate_frequency(dict):
    dictionary = {}
    letter_ammount = 0
    for a in dict:
        c = dict.get(a)
        letter_ammount += c
    for position in dict:
        frequency = dict[position]/letter_ammount
        frequency = round(frequency, 2)
        if position in dictionary:
         dictionary[position] += frequency
        else:
            dictionary[position] = frequency
    return dictionary
main_dict = count_letters(main_str)
main_dictionary = calculate_frequency(main_dict)
for i, j in main_dictionary.items():
    print(i, ': ', j)
