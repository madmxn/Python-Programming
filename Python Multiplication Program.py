num1 = int(input("Enter the number you want to multiply: "))
count = 0
for i in range (0, 12):
  count = count + 1
  answer = num1 * count
  print(num1, "x", count, "=", answer)