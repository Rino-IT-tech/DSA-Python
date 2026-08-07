text = "aabbcdde"

found = False

for ch in text:
    if text.count(ch) == 1:
        print("First Non-Repeating Character:", ch)
        found = True
        break

if not found:
    print("No non-repeating character")
