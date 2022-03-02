# алфавит
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."


# функция зашифровки
def encrypt(text, rot):
    # длина алфавита используемая в качестве модуля
    m = len(alphabet)

    # строка для зашифрованного текста
    res = ""
    # цикл по всем символам в тексте
    for c in text:
        # если символ есть в алфавите, то мы его шифруем
        # в противном случае оставляем как есть
        try:
            # находим индекс символа в алфавите и
            # сдвигаем 'вперед' на нужное количество
            # если символа нет в алфавите, то будет брошен ValueError
            res += alphabet[(alphabet.index(c) + rot) % m]
        except ValueError:
            # Добавляем символ без изменений если его нет в алфавите
            res += c
    # возвращаем зашифрованную строку
    return res


# функция расшифровки для определенного сдвига
def decrypt(text, rot):
    # длина алфавита используемая в качестве модуля
    m = len(alphabet)

    # строка расшифрованного текста
    res = ""
    # цикл по всем символам в тексте
    for c in text:
        # если символ есть в алфавите, то мы его расшифруем
        # в противном случае оставляем как есть
        try:
            # находим индекс символа в алфавите и
            # сдвигаем 'назад' на нужное количество
            # если символа нет в алфавите, то будет брошен ValueError
            res += alphabet[(alphabet.index(c) - rot) % m]
        except ValueError:
            # Добавляем символ без изменений если его нет в алфавите
            res += c

    # возвращаем расшифрованную строку
    return res


# функция перебора всех возможных сдвигов
def decrypt_full(text):
    # массив результатов
    res = []

    # пробегаем по всем возможным сдвигам
    for rot in range(len(alphabet)):
        # расшифруем текст для конкретного сдвига
        # и записывам в результирующий массив
        res.append(decrypt(text, rot))

    # возвращаем массив результатов
    return res


def task_1():
    a = "\"You can show black is white by argument,\" said Filby, \"but you will never convince me.\""
    a_rot = 8

    b = "1234567890"
    b_rot = 21

    print("Задание 1")

    en_a = encrypt(a, a_rot)
    print("a.")
    print("    plain text ->", a)
    print("encrypted text ->", en_a)
    print("encrypted with rot", a_rot)

    en_b = encrypt(b, b_rot)
    print("b.", )
    print("    plain text ->", b)
    print("encrypted text ->", en_b)
    print("encrypted with rot", b_rot)

    print()


def task_2():
    a = "Kv?uqwpfu?rncwukdng?gpqwijB"
    a_rot = 2

    b = "XCBSw88S18A1S 2SB41SE .8zSEwAS50D5A5x81V"
    b_rot = 22

    print("Задание 2")

    de_a = decrypt(a, a_rot)
    print("a.")
    print("encrypted text ->", a)
    print("decrypted text ->", de_a)
    print("decrypted with rot", a_rot)

    de_b = decrypt(b, b_rot)
    print("b.", )
    print("encrypted text ->", b)
    print("decrypted text ->", de_b)
    print("decrypted with rot", b_rot)

    print()


def task_3(verbose=False):

    print("Задание 3.")

    cipher = "guv6Jv6Jz!J6rp5r7Jzr66ntrM"

    dec = decrypt_full(cipher)
    for i, d in enumerate(dec):
        if verbose:
            if i < 10:
                print(i, " ->", d)
            else:
                print(i, "->", d)

    print("Ответ:", dec[13])
    print()


def task_4():
    print("Задание 4.")

    messages = [
        "qeFIP?eGSeECNNS,",
        "5coOMXXcoPSZIWoOI,",
        "avnl1olyD4l\'ylDohww6DhzDjhuDil,",
        "",
        "z.GM?.cEQc. 70c.7KcKMKHA9AGFK,",
        "?MFYp2pPJJUpZSIJWpRdpMFY,",
        "ZqH8sl5HtqHTH4s3lyvH5zH5spH4t pHzqHlH3l5K",
        "",
        "Zfbi,!tif!xpvme!qspcbcmz!fbu!nfA"
    ]

    good_rot = [34, 44, 7, 0, 32, 45, 11, 0, 1]

    for i, m in enumerate(messages):
        dec = decrypt_full(m)

        print(dec[good_rot[i]])


if __name__ == "__main__":
    from os import system
    system('cls')

    task_1()
    task_2()
    task_3()
    task_4()
