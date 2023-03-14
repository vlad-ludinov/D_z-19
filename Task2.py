number = int(input("Введите трехзначное число: "))

if (number > 99 and number <1000):
    sum = number//100 + number//10%10 + number%10
    print(sum)
else:
    print("Это не трехзначное число")