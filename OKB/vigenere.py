CN = {chr(i + ord("А")): i for i in range(0, 32)}
NC = {i: chr(i + ord("А")) for i in range(0, 32)}


def encrypt(m, key):
    if(len(key) < len(m)):
        key = key * (len(m) // len(key) + 1)
    key = key[:len(m)]
    # print(m)
    # print(key)
    # for mi, ki in zip(m, key):
    #     if mi in CN.keys():
    c = "".join([NC[(CN[mi] + CN[ki]) % 32] if mi in CN.keys()
                 else mi for mi, ki in zip(m, key)])
    print(c)


def decrypt(c, key):
    if(len(key) < len(c)):
        key = key * (len(c) // len(key) + 1)
    key = key[:len(c)]
    m = "".join([NC[(CN[ci] - CN[ki] + 32) %
                    32] if ci in CN.keys() else ci for ci, ki in zip(c, key)])
    print(m)


# encrypt('ЛЮДИ НЕ УМЕЮТ ЖИТЬ. ИХ ЭТОМУ НЕ УЧАТ.',
#        'НУНЕМЕНЯТЬСЯЖЕМНЕИЗЗАКАЖДОГОИДИОТА')
decrypt('ЪЫ ЯУ ФПЯНЯДЫС УН ЮЫТ ТЩ-ФИ ЬОУМШХЬ РОЪЬЯИ.', 'НИТОИК')
encrypt('НУ НЕ МЕНЯТЬСЯ ЖЕ МНЕ ИЗ-ЗА КАЖДОГО ИДИОТА.', 'НИТОИК')
# decrypt('НОЦДВНТ ШБЛГК ЯСЛАЯ ТЖТБРЧ, ЫКЩ РЭЧНЯД.', 'КАЖДЫЙДЕНЬИМЕЕТСВОЧУДО')
# encrypt("ЧЕКАЕМ ЭТУ ХРЕНЬ", "ХАЙП")
# decrypt("МЕУПЪМ МЗУ ДЕЕЦЛ", "ХАЙП")
# print(20)
# encrypt("ПРОШЛЫМ НЕЛЬЗЯ ЖИТЬ ТАК ДОЛГО.", "ЖИЗНЬТРЕБУЕТДВИЖЕНИЙ")
# print(21)
# decrypt("ЯГЯ ЯИЗЮН АЦЩСЬЮЮЯ, ЫРФХВ ШВТМДСПФ ХТДШЗЪ", "ВСС")
# print(22)
# decrypt("УДМ УТТ ОЪПЯОУЧЦИ, НМ ТЫЖЬТ РЙУБ М ЪЫАЙО.", "РАЗУЖНАЧАЛПОБЕЖДАЙ")


# print("АЛЕСЯ:")
# print(20)
# encrypt("СЕРДЦЕ МОЖНО ЛЕЧИТЬ ТОЛЬКО СЕРДЦЕМ",
#         "ЛУЧШАЯЧАСТЬНАШЕЙЖИЗНИСОСТОИТИЗДРУЗЕЙ")
# print(21)
# encrypt("МОЖНО ЛЮБИТЬ ВСЮ ЖИЗНЬ, А РАЗЛЮБИТЬ В ЧЕТВЕРГ.", "ГОРА")
# decrypt("ПЬЦНС ЫЮДЦВЬ РБЮ ФШЗРК. Г ААКЩОБЛАМ Е ЗЕХРХРЖ.", "ГОРА")
# print(22)
# decrypt(
#     "ВРПМЩ МЭЦТД - ТХ ЭТЩВЬБЦК И ЯПЬЫС ЧОЧСК СНМО",
#     "ЧТОБЫНИПРОИСХОДИЛОВСХОРОШО")
