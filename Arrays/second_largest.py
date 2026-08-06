list = [1,3,5,33,24,5,495,23,34,43,504]
largest = list[0]
second_large = list[0]

for i in list:
    if i > largest:
        second_large = largest
        largest = i
    elif i > second_large and i != largest:
        second_large = i

print("lagest: ",largest)
print("secound_lage: ",second_large)
