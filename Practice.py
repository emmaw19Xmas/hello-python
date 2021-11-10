#不使用分支结构实现1~100之间的奇数求和
sum = 0
for i in range(1, 100, 2):
    sum += i
print(sum)
#使用while语句实现1~100之间奇数求和
j = 0
sum2 = 0
while j < 100:
    if j%2 != 0:
        sum2 += j
    j+=1
print(sum2)
