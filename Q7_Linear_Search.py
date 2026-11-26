# Q7. Linear Search in Array
n = int(input("Enter size: "))
a = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter key to search: "))

for x in a:
    if x == key:
        print("Found")
        break
else:
    print("Not Found")
