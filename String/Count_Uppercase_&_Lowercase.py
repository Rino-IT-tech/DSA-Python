text = "PytHOn"
uppercase = 0
lowercase = 0
for i in text:
     if i.isupper():
          uppercase = uppercase + 1
     elif i.islower():
          lowercase = lowercase + 1
print(uppercase)
print(lowercase)
