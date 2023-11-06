def maximum(a, b, c=None):
    if c is None:
        return a if a > b else b
    else:
        max_ab = a if a > b else b
        return max_ab if max_ab > c else c

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

max_value = maximum(num1, num2)
print("Максимальное значение составляет:", max_value)

num3 = int(input("Введите третье число: "))
max_value = maximum(num1, num2, num3)
print("Максимальное значение составляет:", max_value)