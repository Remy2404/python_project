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
            print(f"{node.data[0]}: {node.data[1]}", end=' ')
            self._inorder(node.right)

    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self, node):
        if node:
            print(f"{node.data[0]}: {node.data[1]}", end=' ')
            self._preorder(node.left)
            self._preorder(node.right)

    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(f"{node.data[0]}: {node.data[1]}", end=' ')

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, root, data):
        if root is None or root.data[0] == data:
            return root
        if data < root.data[0]:
            return self._search(root.left, data)
        return self._search(root.right, data)

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, root, data):
        if root is None:
            return root
        if data < root.data[0]:
            root.left = self._delete(root.left, data)
        elif data > root.data[0]:
            root.right = self._delete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._min_value_node(root.right)
            root.data = temp.data
            root.right = self._delete(root.right, temp.data[0])
        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def display(self):
        fig, ax = plt.subplots(figsize=(20, 12))
        ax.axis('off')
        self._display(self.root, ax)
        plt.show()

    def _display(self, node, ax, x=0, y=0, spacing=80):
        if node is None:
            return
        
        # Display the current node
        ax.text(x, y, f"{node.data[0]}\n{node.data[1]}", ha='center', va='center', 
                bbox=dict(facecolor='skyblue', edgecolor='black', boxstyle='round,pad=0.5'))
        
        # Display the left child
        if node.left:
            ax.plot([x, x - spacing], [y, y - 100], color='red')
            self._display(node.left, ax, x - spacing, y - 100, spacing / 2)
        
        # Display the right child
        if node.right:
            ax.plot([x, x + spacing], [y, y - 100], color='green')
            self._display(node.right, ax, x + spacing, y - 100, spacing / 2)

# Example usage
bt = BinaryTree()
provinces = [
    ("Phnom Penh", 2237400),
    ("Banteay Meanchey", 859549),
    ("Battambang", 1036288),
    ("Kampong Cham", 928694),
    ("Kampong Chhnang", 523202),
    ("Kampong Speu", 872219),
    ("Kampong Thom", 690414),
    ("Kampot", 585850),
    ("Kandal", 1195547),
    ("Kep", 41798),
    ("Koh Kong", 117481),
    ("Kratie", 366666),
    ("Mondulkiri", 92995),
    ("Oddar Meanchey", 231390),
    ("Pailin", 70482),
    ("Preah Vihear", 251645),
    ("Prey Veng", 947357),
    ("Pursat", 397161),
    ("Ratanakiri", 204000),
    ("Siem Reap", 1006512),
    ("Stung Treng", 122791),
    ("Svay Rieng", 482788),
    ("Takeo", 843931),
    ("Tbong Khmum", 754000)
]

# Sort the provinces based on population in descending order
provinces.sort(key=lambda x: x[1], reverse=True)

# Print the sorted provinces
print("\nSorted Provinces by Population:")
for province in provinces:
    print(f"{province[0]}: {province[1]}")

print("\n")

# Insert the provinces into the binary tree
for province in provinces:
    bt.insert(province)

# Print the inorder traversal of the tree
print("Inorder Traversal:")
bt.inorder()
print("\n")

print("Preorder Traversal:")
bt.preorder()
print("\n")

# postorder traversal of the tree
print("Postorder Traversal:")
bt.postorder()
print("\n")

# Search for a province (e.g., 'Banteay Meanchey')
search_result = bt.search("Banteay Meanchey")
print("Search for 'Banteay Meanchey':", "Found" if search_result else "Not Found")

# Delete a province (e.g., 'Kampong Cham')
bt.delete("Kampong Cham")
print("\nAfter deleting 'Kampong Cham':")
print("Inorder Traversal:")
bt.inorder()

# Display the binary tree
print("\nDisplaying the binary tree:")
bt.display()