def palindrom(input_str):

    cleaned_str = ''.join(input_str.lower().split())
    return cleaned_str == cleaned_str[::-1]

inp = input("Введите строку для проверки: ")

result = palindrom(inp)
print(f"Эта строка {'является' if result else 'не является'} палиндромом.")

# примеры для ввода:
# "А роза упала на лапу Азора"
# "Аргентина манит негра"
# "Madam, in Eden, I'm Adam"
# "Able , was I ere I saw Elba"
