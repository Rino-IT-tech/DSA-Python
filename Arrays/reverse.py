list = [1,2,3,4,5]
reverse =[]

for num in range(len(list)):
    a = list.pop()
    reverse.append(a)
print(reverse)
