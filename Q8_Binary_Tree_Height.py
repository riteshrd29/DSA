# Q8. Height of a Binary Tree
# Enter nodes in level order. Use N for a missing child.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_tree(values):
    if not values or values[0] == "N":
        return None

    root = Node(int(values[0]))
    queue = [root]
    i = 1

    while queue and i < len(values):
        current = queue.pop(0)

        if i < len(values) and values[i] != "N":
            current.left = Node(int(values[i]))
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] != "N":
            current.right = Node(int(values[i]))
            queue.append(current.right)
        i += 1

    return root

def height(root):
    if root is None:
        return -1
    return 1 + max(height(root.left), height(root.right))

values = input("Enter level-wise elements (use N for NULL): ").split()
root = create_tree(values)
print("Height of Binary Tree:", height(root))
