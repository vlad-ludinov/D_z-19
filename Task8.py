rowChocolate =  int(input("Введите количество долек шоколада в строчке: "))
columnChocolate = int(input("Введите количество долек шоколада в столбике: "))
breakChocolate = int(input("Введите столько долек шоколада вы хотите отломить: "))
if (rowChocolate*columnChocolate == breakChocolate):
    print("Ешьте всю шоколадку")
elif (breakChocolate%rowChocolate == 0 or breakChocolate%columnChocolate == 0):
    print("да")
else:
    print("нет")
