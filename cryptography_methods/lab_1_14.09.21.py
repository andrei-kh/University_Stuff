# функция для разворота строки
def reverse_string(string):
    # разворот строки
    return string[::-1]


print("\tразворот строки")
# тестовая строка
test_string = "abadce"
print("тестовая строка ->", test_string)

# шифрование строки
c_string = reverse_string(test_string)
print("зашифрованная строка ->", c_string)

# расшифрование строки
d_string = reverse_string(c_string)
print("расшифрованная строка ->", d_string)


# функция применяющая шифр атбаш для строки
def atbash(string):
    # цикл от начала строки до ее середины
    string = list(string)
    for i in range(int(len(string) / 2) + 1):
        # смена i-го элемента с len(string) - i + 1-м элементом
        temp = string[i]
        string[i] = string[len(string) - i - 1]
        string[len(string) - i - 1] = temp

    return "".join(string)


print()
print("\tатбаш")
# тестовая строка
test_string = "abcef"
print("тестовая строка ->", test_string)

# шифрование строки
c_string = atbash(test_string)
print("зашифрованная строка ->", c_string)

# расшифрование строки
d_string = atbash(c_string)
print("расшифрованная строка ->", d_string)
