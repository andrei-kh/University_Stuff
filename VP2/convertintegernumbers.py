q = int(input())
p = int(input())
num = input()[::-1]

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

num10 = 0
for i in range(len(num)):
    num10 += pow(q, i) * digits.index(num[i])

ans = []
while num10:
    ans.append(digits[num10 % p])
    num10 //= p

print("".join(ans[::-1]))
