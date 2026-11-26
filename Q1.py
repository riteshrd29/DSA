n = int(input("Enter size: "))
a = list(map(int, input().split()))
b = []
 
for i in range(n-1,-1,-1):
    b.append(a[i])

print("Reversed Array:", b)
