# #'''Напишите функцию sport(), при запуске которой происходит заполнение двух списков: sportlased[], tulemused[].  Список sportlased[] - заполняет пользователь, а список результаты[] – заполняется автоматически: оздаеются случайные 3 числа и наибольшее из них заносится в списокПосле заполнения списков появляется меню с выбором действий:
# • Узнать n лучших результатов;
# • Упорядочить список в порядке возрастания баллов. Отобразить спортсменов их баллы и места;
# • Ввести имя одного или нескольких спортсменов и показать его/их результат;
# • Дисквалифицировать(удалить из списка)  спортсменов, у которых результаты хуже чем придуманный вами критерий;
# • Свой вариант.
# Для описания действий создайте необходимые функции.'''
# import random 
# def random(num: int) -> int:
#     '''
#     '''
#     i = randint(3, 10)
#     for b in range(i):
#         while True:
#             sportlane = input(f"Sisesta sportlase nimi ({i} osalejat): ").capitalize()
#             if sportlane.isalpha():
#                 break
#             else:
#                 print("Nimi peab sisaldama ainult tähti!")

#         arv1, arv2, arv3 = randint(1, 100), randint(1, 100), randint(1, 100)
#         tulemus = max(arv1, arv2, arv3)

#         sportlased.append(sportlane)
#         tulemused.append(tulemus)

#     tabel(sportlased, tulemused)
#     return tulemus