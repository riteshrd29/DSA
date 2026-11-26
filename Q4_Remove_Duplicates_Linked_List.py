# Q4. Remove Duplicates from a Sorted Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n = int(input("Enter number of nodes: "))
values = list(map(int, input("Enter sorted elements: ").split()))

if n == 0:
    print("Linked List is empty")
else:
    head = Node(values[0])
    temp = head

    for value in values[1:n]:
        temp.next = Node(value)
        temp = temp.next

    temp = head
    while temp and temp.next:
        if temp.data == temp.next.data:
            temp.next = temp.next.next
        else:
            temp = temp.next

    print("Linked List after removing duplicates:")
    while head:
        print(head.data, end=" ")
        head = head.next
    print()
