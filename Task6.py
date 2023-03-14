ticket = int(input("Введите номер билета: "))
firstHalf = ticket//100000 + ticket//10000%10 + ticket//1000%10
secondHalf = ticket//100%10 + ticket//10%10 + ticket%10
if (firstHalf == secondHalf):
    print("yes")
else:
    print("no")