# Q5. Sum of All Elements in Array
n = int(input("Enter size: "))
a = list(map(int, input("Enter elements: ").split()))

total = 0
for x in a:
    total += x

print("Sum of Array Elements:", total)
