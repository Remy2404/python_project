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
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                self._insert(root.left, data)
        else:
            if root.right is None:
                root.right = Node(data)
            else:
                self._insert(root.right, data)

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, root, data):
        if root is None or root.data == data:
            return root
        if data < root.data:
            return self._search(root.left, data)
        return self._search(root.right, data)

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, root, data):
        if root is None:
            return root
        if data < root.data:
            root.left = self._delete(root.left, data)
        elif data > root.data:
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

    def display(self):
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.axis('off')
        self._display(self.root, ax)
        plt.show()

    def _display(self, node, ax, x=0, y=0, spacing=20):
        if node is None:
            return
        ax.text(x, y, str(node.data), ha='center', va='center', bbox=dict(facecolor='skyblue', edgecolor='black', boxstyle='round,pad=0.3'))
        if node.left:
            ax.plot([x, x - spacing], [y, y - 10], color='red')
            self._display(node.left, ax, x - spacing, y - 10, spacing / 2)
        if node.right:
            ax.plot([x, x + spacing], [y, y - 10], color='green')
            self._display(node.right, ax, x + spacing, y - 10, spacing / 2)

bt = BinaryTree()
nodes = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
for node in nodes:
    bt.insert(node)

# Search for a node
search_node = 25
found_node = bt.search(search_node)
if found_node:
    print(f"Node {search_node} found in the tree.")
else:
    print(f"Node {search_node} not found in the tree.")

# Delete a node
delete_node = 70
bt.delete(delete_node)
print(f"Node {delete_node} deleted from the tree.")

# Display the tree
bt.display()