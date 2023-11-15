# TODO Напишите функцию для поиска индекса товара


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
for find_item in ['банан', 'груша', 'персик']:
    condition = 0
    for i in items_list:
        if i == find_item:
            index_item = items_list.index(i)
            print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
            break
        else:
            condition += 1
            if items_list.index(i) == items_list.index(items_list[-1]):
             if condition == len(items_list):
              print(f"Товар '{find_item}' не найден в списке.")
    # TODO Вызовите функцию, что получить индекс товара



