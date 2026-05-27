import random

# b = "Что такое damage control? Я не знаю("
# c = 0 
# while c<7:
#     print(b)
#     c += 1


# A = int(input("Введите А:"))
# B = int(input("Введите В:"))

# if 0<A<B:
#     num = A
#     while num <= B:
#         print(num)
#         num += 1
#     print()
# else:
#     print("Ошибка")


# while True:
#     slon = input("Купи слона ")
#     print(f"Все говорят {slon}, а ты купи слона!")


# while True:
#     print("Угадай число от 1 до 7!!!")
#     b = int(input("Число:"))
#     a = random.randint(1,7)
#     if b>a:
#         print("меньше")
#     elif b<a:
#         print("больше")
#     else:
#         print("Ура")
#         break

# while True:
#     print("Угадай число от 1 до 15!!!")
#     b = random.randint(1, 15)
    
#     popat = 3
#     right_popat = False
    
#     while popat > 0:
#         user_guess = int(input(f"У вас осталось {popat} поп. Введите число: "))
        
#         if user_guess < b:
#             print("Больше!")
#             popat -= 1
#         elif user_guess > b:
#             print("Меньше!")
#             popat -= 1
#         else:
#             print("Ура")
#             right_popat = True
#             break
            
#     if not right_popat:
#         print(f"Вы проиграли. Было загадано число {b}.")