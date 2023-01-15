# task 2

# class Calcul:
#     def __init__(self):
#         self.total()
#
#     def plust(self):
#         print("Результат:")
#         return self.a + self.b
#
#     def minus(self):
#         return self.a - self.b
#
#     def multiply(self):
#         return self.a * self.b
#
#     def divide(self):
#         if self.b == 0:
#             return "Ошибка"
#         else:
#             return self.a / self.b
#
#     def total(self):
#         self.a = int(input("x = "))
#         self.b = int(input("y = "))
#
#
# while True:
#     print("Выберите знак равенства : +,-,/,*")
#     x = input()
#     ex = Calcul()
#     if x == "b":
#         break
#     if x == "+":
#         print(ex.plust())
#     if x == "-":
#         print(ex.minus())
#     if x == "*":
#         print(ex.multiply())
#     if x == "/":
#         print(ex.divide())

# Home Task 18
class Example:
    def __init__(self):
        self.h = 0
        self.d = 0
        self.g = 0
        self.gl = []
        self.sgl = []

    def func(self, a):
        if type(a) is str:
            for i in a:
                if i in "aeoiu":
                    self.h += 1
                    self.gl.append(i)
                else:
                    self.d += 1
                    self.sgl.append(i)
            print('Количество глысных', self.h)
            print('Количество согдасных', self.d)
            print('Длина слова', self.func1(a))
            if (self.h * self.d) <= self.func1(a):
                print('Гласные: ', self.gl)
            else:
                print('Согласные: ', self.sgl)
        elif type(a) is int:
            for i in str(a):
                i = int(i)
                if (i % 2) == 0:
                    self.g += i
            print('Произведение: ', self.g * self.func1(a))

    def func1(self, a):
        return len(str(a))

example = Example()
c = input("Напишите что нибудь на английском: ")
if c.isalpha():
    example.func(c)
elif c.isdigit():
    example.func(int(c))








