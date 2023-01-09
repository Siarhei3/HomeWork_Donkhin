def cal_():
    try:
        while True:
            a = int(input("Введите первое число:"))
            b = int(input("Введите второе число:"))
            c = a // b

            if b == 0:
                print("Введены не правильные значение")
            else:
                print(c)
    except ZeroDivisionError:
        print("Деление на ноль!!! попробуйте снова")
        return (cal_())
    except ValueError:
        print("Неправильное значение!!! Попробуйте снова")
        return (cal_())
print(cal_())








