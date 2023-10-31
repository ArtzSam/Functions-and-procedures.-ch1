def format(first_name, last_name, middle_name, age):
    return f"{last_name} {first_name} {middle_name} {age} г.р. зарегистрирован"

first_name = input("Введите имя: ")
last_name = input("Введите фамилию: ")
middle_name = input("Введите отчество: ")
age = input("Введите год рождения: ")

result = format(first_name, last_name, middle_name, age)
print(result)
