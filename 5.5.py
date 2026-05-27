#1
prod1 = 150
prod2 = 250
print(prod1 + prod2)

#2
S1 = 10
S2 = 5
print(S1*S2)

#3
a1 = 5
a2 = 4
a3 = 5
itog = (a1+a2+a3)/3
print(itog)

#4
sec = 135
min = sec//60
sec2 = sec%60
print(f"{sec} секунд = {min} мин {sec2} сек")

#5
candy = 20
friends = 3
e = candy//3
i = candy%3
print(f"Каждому {e} конфет, мне {i} конфет")

#6
x1 = 7
x2 = 2
x3 = 3
print(x1**x2)
print(x1**x3)

#1
price = 1200
sale = 0.15
sale2 = 0.20
new_price = price-(price*sale)
newnew_price = new_price+(new_price*sale2)
print(newnew_price)

#2
second = 3665
hour = second//60
hour2 = hour%60
min = second//60
min2 = min%60
secc = second%60
print(f"{hour2}:{min2}:{secc}")

#3
ves = float(input("Введите свой вес:"))
rost = float(input("Введите свой рост (см):"))
m = rost/100
rest = ves/(m**2)
res = round(rest, 1)
print(f"Вес {ves} кг, рост {rost} см: ИМТ {res}")

#4
num = int(input("Введите трехзначное число:"))
num3 = num%10
num2 = (num//10)%10
num1 = num//100
summ = num1+num2+num3
mult = num1*num2*num3
print(mult-summ)

#5
curs = 90.5
comm = 0.025
doll = float(input("Сколько купит:"))
result = (doll*curs)*(1+comm)
print(result)