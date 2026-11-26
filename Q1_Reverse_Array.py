# Q1. Reverse the Array
n = int(input("Enter size: "))
a = list(map(int, input("Enter elements: ").split()))

b = []
for i in range(n - 1, -1, -1):
    b.append(a[i])

print("Reversed Array:", b)
