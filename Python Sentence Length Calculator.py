sentence = input("Type a sentence: ")
sentence2 = sentence.lower()
list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
count = 0
for char in sentence2:
    if char in list:
        count = count+1
print("There are", count, "characters in this sentence.")