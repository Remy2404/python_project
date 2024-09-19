import sympy

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


import matplotlib.pyplot as plt


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, root, data):
        if data[1] < root.data[1]:
            if root.left is None:
                root.left = Node(data)
            else:
                self._insert(root.left, data)
        else:
            if root.right is None:
                root.right = Node(data)
            else:
                self._insert(root.right, data)

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(f"{node.data[0]} ({node.data[1]} districts)", end=' ')
            self._inorder(node.right)

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, root, data):
        if root is None or root.data == data:
            return root
        if data[1] < root.data[1]:
            return self._search(root.left, data)
        return self._search(root.right, data)

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, root, data):
        if root is None:
            return root
        if data[1] < root.data[1]:
            root.left = self._delete(root.left, data)
        elif data[1] > root.data[1]:
            root.right = self._delete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._min_value_node(root.right)
            root.data = temp.data
            root.right = self._delete(root.right, temp.data)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def bfs(self):
        if not self.root:
            print("Tree is empty")
            return

        queue = [self.root]
        while queue:
            node = queue.pop(0)  # Remove the first element in the list
            print(f"{node.data[0]} ({node.data[1]} districts)", end=', ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()

    def display(self):
        fig, ax = plt.subplots(figsize=(20, 12))
        ax.axis('off')
        self._display(self.root, ax, 0, 0, 160)
        plt.show()

    def _display(self, node, ax, x=0, y=0, spacing=80):
        if node is None:
            return

        # Display the current node
        ax.text(x, y, f"{node.data[0]}\n{node.data[1]} districts", ha='center', va='center',
                bbox=dict(facecolor='skyblue', edgecolor='black', boxstyle='round,pad=0.5'))

        # Display left child
        if node.left:
            ax.plot([x, x - spacing], [y, y - 50], color='red')
            self._display(node.left, ax, x - spacing, y - 50, spacing)

        # Display the right child
        if node.right:
            ax.plot([x, x + spacing], [y, y - 50], color='green')
            self._display(node.right, ax, x + spacing, y - 50, spacing)


bt = BinaryTree()
provinces = [
    ("Phnom Penh", 14),
    ("Siem Reap", 12),
    ("Battambang", 14),
    ("Sihanoukville", 5),
    ("Kampong Cham", 10),
    ("Takeo", 10),
    ("Pursat", 6),
    ("Poipet", 8),
    ("Kampot", 8),
    ("Banteay Meanchey", 7)
]

# Print sorted provinces
print("\nSorted Provinces by Districts:\n")
for province in provinces:
    print(f"Inserted: {province[0]}: {province[1]}")
    # Insert provinces
    bt.insert(province)
    bt.inorder()
    print("\n")

print("Breadth-First Search:")
bt.bfs()

# display before delete
bt.display()

# Search for a province
search_key = ("Kampot", 8)
findNode = bt.search(search_key)
if findNode:
    print(f"\n'{search_key[0]}' found in the tree.")
else:
    print(f"\n'{search_key[0]}' not found in the tree.")

# Delete a province
delete_key = ("Poipet", 8)
bt.delete(delete_key)
print(f"\nDeleted '{delete_key[0]}' From the tree.")
# display after delete
bt.display()
