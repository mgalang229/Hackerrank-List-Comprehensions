x = int(input())
y = int(input())
z = int(input())
n = int(input())

a = []
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            temp = []
            if i + j + k != n:
                temp.append(i)
                temp.append(j)
                temp.append(k)
                a.append(temp)

print(a)

