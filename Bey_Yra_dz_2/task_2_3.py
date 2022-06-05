list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
answer = {}

for elem in range(len(list)):
    normal_view = list[elem].split(' ')[len(list[elem].split(' ')) -1]
    print(f"Привет, {normal_view.lower().title()}!")