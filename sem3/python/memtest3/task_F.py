д = int(input())
попытки = int(input())
результат = []
for и in range(попытки):
    if (int(input()) - 1) % (д - 1) == 0:
        результат.append(1)
    else:
        результат.append(0)

for цифра in результат:
    print(цифра)
