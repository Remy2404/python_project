# Binary Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Overriding the __str__ method to print the node data
    def __str__(self):
        return str(self.data)

    # Inserting a node in the binary tree
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

    # Searching a node in the binary tree
    def search(self, data):
        if self.data:
            if self.data == data:
                return True
            elif data < self.data and self.left:
                return self.left.search(data)
            elif data > self.data and self.right:
                return self.right.search(data)
        return False

    # Deleting a node from the binary tree
    def delete(self, data):
        if self.data:
            if data < self.data and self.left:
                self.left = self.left.delete(data)
            elif data > self.data and self.right:
                self.right = self.right.delete(data)
            else:
                if not self.left and not self.right:
                    return None
                elif not self.left:
                    return self.right
                elif not self.right:
                    return self.left
                else:
                    min_value = self.right.getMinValue()
                    self.data = min_value
                    self.right = self.right.delete(min_value)
        return self

    # Finding the minimum value in the binary tree
    def getMinValue(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.data

    # Finding the maximum value in the binary tree
    def getMaxValue(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.data

    # Inorder traversal of the binary tree
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end=' ')
        if self.right:
            self.right.inorder()

    # Preorder traversal of the binary tree
    def preorder(self):
        print(self.data, end=' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    # Postorder traversal of the binary tree
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data, end=' ')

    # Calculating the height of the binary tree
    def height(self):
        if not self:
            return 0
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return 1 + max(left_height, right_height)

    # Calculating the number of nodes in the binary tree
    def count_nodes(self):
        if not self:
            return 0
        left_count = self.left.count_nodes() if self.left else 0
        right_count = self.right.count_nodes() if self.right else 0
        return 1 + left_count + right_count

    # Calculating the number of leaf nodes in the binary tree
    def count_leaf_nodes(self):
        if not self:
            return 0
        if not self.left and not self.right:
            return 1
        left_leaf = self.left.count_leaf_nodes() if self.left else 0
        right_leaf = self.right.count_leaf_nodes() if self.right else 0
        return left_leaf + right_leaf

    # Adding two binary trees (assumes they have the same structure)
    def add_binary_trees(self, tree2):
        if not self or not tree2:
            return None
        root = Node(self.data + tree2.data)
        root.left = self.left.add_binary_trees(tree2.left) if self.left and tree2.left else None
        root.right = self.right.add_binary_trees(tree2.right) if self.right and tree2.right else None
        return root

    # Checking if two binary trees are equal
    def equal(self, tree2):
        if not self and not tree2:
            return True
        if not self or not tree2:
            return False
        return (
                self.data == tree2.data and
                (self.left.equal(tree2.left) if self.left and tree2.left else self.left == tree2.left) and
                (self.right.equal(tree2.right) if self.right and tree2.right else self.right == tree2.right)
        )

    # Displaying the binary tree (inorder traversal)
    def display(self):
        if self.left:
            self.left.display()
        print(self.data, end=' ')
        if self.right:
            self.right.display()


# Main function to test the above methods
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

    print("\nInorder Traversal:", end=' ')
    tree1.inorder()

    print("\nPreorder Traversal:", end=' ')
    tree1.preorder()

    print("\nPostorder Traversal:", end=' ')
    tree1.postorder()

    print("\nHeight:", tree1.height())
    print("Number of Nodes:", tree1.count_nodes())
    print("Number of Leaf Nodes:", tree1.count_leaf_nodes())
    

    print("\nBinary Tree 2:")
    tree2 = Node(8)
    tree2.insert(10)
    tree2.insert(11)
    tree2.insert(12)
    tree2.insert(13)
    tree2.insert(14)
    tree2.insert(15)

    print("\nInorder Traversal:", end=' ')
    tree2.inorder()

    print("\nPreorder Traversal:", end=' ')
    tree2.preorder()

    print("\nPostorder Traversal:", end=' ')
    tree2.postorder()

    print("\nHeight:", tree2.height())
    print("Number of Nodes:", tree2.count_nodes())
    print("Number of Leaf Nodes:", tree2.count_leaf_nodes())

    print("\nAdding two binary trees:")
    tree3 = tree1.add_binary_trees(tree2)
    tree3.display()

    print("\nChecking if two binary trees are equal:", tree1.equal(tree2))

    print("\nBinary Tree 3:")
    tree3.display()

    print("\nInorder Traversal:", end=' ')
    tree3.inorder()

    print("\nPreorder Traversal:", end=' ')
    tree3.preorder()

    print("\nPostorder Traversal:", end=' ')
    tree3.postorder()

    print("\nHeight:", tree3.height())
    print("Number of Nodes:", tree3.count_nodes())
    print("Number of Leaf Nodes:", tree3.count_leaf_nodes())

    print("\nDeleting node 3 from Binary Tree 1:")
    tree1.delete(3)
    tree1.display()

    print("\nInorder Traversal:", end=' ')
    tree1.inorder()
#Binary Tree 4 :
    tree4 = Node(16)
    tree4.insert(20)
    tree4.insert(15)
    tree4.insert(10)
    tree4.insert(5)
# Binary Tree 5 :
    tree5 = Node(25)
    tree5.insert(30)
    tree5.insert(28)
    tree5.insert(22)
    tree5.insert(17)
    tree4.add_binary_trees(tree5)
    print("\nBinary Tree 4:")
    tree4.display()
    print("\nInorder Traversal:", end=' ')
    tree4.inorder()
    print("\nPreorder Traversal:", end=' ')
    tree4.preorder()
    print("\nPostorder Traversal:", end=' ')
    tree4.postorder()
    print("\nHeight:", tree4.height())
    print("Number of Nodes:", tree4.count_nodes())
    print("Number of Leaf Nodes:", tree4.count_leaf_nodes())
    print("\nBinary Tree 5:")
    tree5.display()
    print("\nInorder Traversal:", end=' ')
    tree5.inorder()
    print("\nPreorder Traversal:", end=' ')
    tree5.preorder()
    print("\nPostorder Traversal:", end=' ')
    tree5.postorder()
    print("\nHeight:", tree5.height())
    print("Number of Nodes:", tree5.count_nodes())
    print("Number of Leaf Nodes:", tree5.count_leaf_nodes())
    print("\nDeleting node 15 from Binary Tree 4:")
    tree4.delete(15)
    tree4.display()


if __name__ == "__main__":
    main()
