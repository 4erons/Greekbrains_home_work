# 2. Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов

# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное: дополнить числа до двух разрядов нулём!
def get_sign(x):
    if x[0] in '+-':
        return x[0]

list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(list_1):
    sign = get_sign(list_1[i])
    if list_1[i].isdigit() or (sign and list_1[i][1:].isdigit()):
        if sign:
            list_1[i] = sign + list_1[i][1:].zfill(2)
        else:
            list_1[i] = list_1[i].zfill(2)

        list_1.insert(i, '"')
        list_1.insert(i + 2, '"')
        i += 2
    i += 1
print(list_1)
