# 1.
num = int(input("Введите число:"))

for i in range(1, num + 1):
    print(i)

# 2.
num = int(input("Введите число:"))

while num>=1:
    print(num)
    num -=1

# 3.
for i in range(2, 21, 2):
    print(i)

# 4.
count = 0 
while True:
    num = int(input("Введите число:"))
    if num == 0:
        break
    count += num
print(f"Итог:{count}")

# 5.
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i}*{j}={i*j}")

# 6.
a = 67
score = 0

print("попробуй угадать число")

while True:
    b = int(input("Число:"))
    score += 1
    if b>a:
        print("меньше")
    elif b<a:
        print("больше")
    else:
        print("Ура")
        break

print(f"Попытки:{score}")

# 7.
st = input("Введите строку:")
bookva = set("aeiouyаеёиоуыэюяAEIOUYАЕЁИОУЫЭЮЯ")

c = 0
for char in st:
    if char in bookva:
        c += 1
print("Кол-во гласных:", c)

# 8.
Num = int(input("Введите n: "))

f = 1
for i in range(2, Num + 1):
    f *= i

print(f"{Num}! =", f)

# 9.
numbers = [12, -5, 0, 44, 23]

maxLOL = numbers[0]

for num in numbers:
    if num > maxLOL:
        maxLOL = num

print("Максимум:", maxLOL)

# 10.
num = int(input("Введите N: "))
a = 0
b = 1
c = 0
while c < num:
    print(a)
    next_val = a + b
    a = b
    b = next_val
    c = c + 1