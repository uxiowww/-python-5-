A = int(input("введите А:"))
B = int(input("введите B:"))
K = int(input("введите K:"))

c = 0
min = 0
max = 0 

for n in range(A, B + 1):
    f = 1
    N = n
    while N > 0:
        d = N % 10
        if d != 0:
            f *= d
        N //= 10

    if f == K:
        c += 1
        if c == 1:
            min = n
            max = n
        else:
            if n < min:
                min = n
            if n > max:
                max = n
if c == 0:
    print("нет подходящих")
else:
    print("Кол-во:", c)
    print("Минимум:", min )
    print("Максимум:", max)