class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def display(self, level=0, prefix="Root: "):
        print(" " * (level * 4) + prefix + str(self.data))
        if self.left:
            self.left.display(level + 1, "L--- ")
        if self.right:
            self.right.display(level + 1, "R--- ")

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end=' ')
        if self.right:
            self.right.inorder()

    def preorder(self):
        print(self.data, end=' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data, end=' ')

    # Other methods (delete, height, count_nodes, etc.) go here

def main():
    tree1 = Node(1)
    tree1.insert(2)
    tree1.insert(3)
    tree1.insert(4)
    tree1.insert(5)
    tree1.insert(6)
    tree1.insert(7)

    print("Binary Tree 1:")
    tree1.display()

    # Visualization of Binary Tree 1
    graph1 = draw_binary_tree(tree1)
    graph1.render('binary_tree1', format='png', cleanup=True)

    print("\nInorder Traversal:", end=' ')
    tree1.inorder()

    print("\nPreorder Traversal:", end=' ')
    tree1.preorder()

    print("\nPostorder Traversal:", end=' ')
    tree1.postorder()

    # Other operations...

if __name__ == "__main__":
    main()
