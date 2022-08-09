sentence1 = input("Type a sentence: ")
sentence2 = sentence1.lower()
list = ["a", "e", "i", "o", "u"]
count = 0
for char in sentence2:
    if char in list:
        count = count+1 
print("There are", count, "vowels in this sentence.")