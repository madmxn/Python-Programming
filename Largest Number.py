data = []
while True:
    num = int(input("Enter a number: "))
    data.append(num)

    ans = input("Would you like to enter another number? ( y/n ) : ").lower()
    if ans == 'n':
        breaks
print(data)
largest_number = data[0]
for num in data:
    if num > largest_number:
        largest_number = num
print("the largest number in this list is", largest_number)