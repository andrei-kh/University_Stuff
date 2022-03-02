from itertools import permutations
from math import ceil
from random import randint, shuffle


def vertical_permutation_encrypt(s, k=None, use_perm=False, perm=None):
    if k is None:
        k = randint(2, ceil(len(s) / 2))

    table = []
    list_s = list(s)
    for i in range(ceil(len(s) / k)):
        table.append(list_s[i * k:i * k + k])
    table[-1] += [' ' for _ in range(k - len(table[-1]))]

    res = ""
    if use_perm and perm:
        j_iterable = perm
    else:
        j_iterable = list(range(len(table[0])))
        if use_perm:
            shuffle(j_iterable)

    for j in j_iterable:
        for i in range(len(table)):
            res += str(table[i][j])

    return res, k, j_iterable


def vertical_permutation_decrypt(s, k, p):
    table = [['' for _ in range(k)] for _ in range(ceil(len(s) / k))]
    for j in range(k):
        for i in range(ceil(len(s) / k)):
            try:
                table[i][p[j]] = s[j * ceil(len(s) / k) + i]
            except IndexError:
                table[i][p[j]] = ' '

    res = ""
    for i in range(len(table)):
        for j in range(len(table[0])):
            res += str(table[i][j])

    return res

# this does not work
def vertical_permutation_decrypt_full(s):
    possible_k = [i for i in range(2, ceil(len(s) / 2)) if len(s) % i == 0]

    for k in possible_k:
        row_permutations = permutations([i for i in range(k)])
        for perm in row_permutations:
            d = vertical_permutation_decrypt(s, k, perm)
            yield k, perm, d


s = 'Common sense is not so common.'
k = 8
e_s, k, p = vertical_permutation_encrypt(s, k, True, [1, 7, 6, 5, 3, 2, 0, 4])
# print(e_s, k, p)
# print(vertical_permutation_decrypt(e_s, k, p))

for k, p, d in vertical_permutation_decrypt_full(e_s):
    print(f"k: {k}, перестановка: {p} -> {d}")
