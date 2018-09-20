# test_20_09
number1 = input()
number2 = input()
number3 = input()
if number1 >= number2:
    if number2 >= number3:
        print(number3, number2, number1)
    else:
        if number1 >= number3:
            print(number2, number3, number1)
        else:
            print(number2, number1, number3)
else:
    if number1 >= number3:
        print(number3, number1, number2)
    else:
        if number2 >= number3:
            print(number1, number3, number2)
        else:
            print(number1, number2, number3)
