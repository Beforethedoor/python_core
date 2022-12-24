"""Перегрузка метода внутри класса в Python"""
from functools import singledispatchmethod


class SingleDispatchExample:

    @singledispatchmethod  # декорируем функцию make_square
    def make_square(self, num):
        pass # в данном случае, код этой функции можно опустить

    @make_square.register(int)  # регистрируем обработчик при передаче в него целого числа
    def _(self, num):  # здесь, название функции-обработчика не играет никакой роли
        return num ** 2

    @make_square.register(str) # поведение функции make_square при передаче строки
    def _(self, num) :
        number = int(num)
        return number ** 2

    @make_square.register(tuple)
    @make_square.register(list) # можно задавать поведение сразу для нескольких типов данных
    def _(self, sequence):
        result = []
        for i in sequence:
            result.append(int(i) ** 2) # переводим значения в int, т.к. список может содержать строки
        return result

obj = SingleDispatchExample()

print(obj.make_square(3)) # >>> 9
print(obj.make_square("4")) # >>> 16
print(obj.make_square( (1, "2") )) # передаем кортеж: >>> [1, 4]
print(obj.make_square( ["5", 6] )) # передаем список: >>> [25, 36]
