bob = "tester"
bob_wyear = 0

if bob == "tester":
    if bob_wyear > 4:
        print("高级")
    else:
        print("小白")
    print("软件工程师")
elif bob == "developer":
    print("开发工程师")
else:
    print("无业")

print("测试工程师") if bob == "tester" else print("开发工程师")

i = 1
while i < 6:
    print(i)
    i += 2

j = 1
while j < 8:
    print(j)
    if j == 5:
        break
    j += 2

k = 1
while k < 8:
    print(k)
    if k == 4:
        k += 1.2
        continue
    k += 1

sum = 0
for i in range(0,101,2):
    sum += i
print(sum)