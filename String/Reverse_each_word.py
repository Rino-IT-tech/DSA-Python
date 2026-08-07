text = "I love python"

result = ""

new_text = text.split()

for word in new_text:
    reverse = ""

    for ch in word:
        reverse = ch + reverse
    result = result + reverse + " "

print(result)
