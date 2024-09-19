from diagram
from collections import deque

class Node:
    def init(self, data=None, full_stack=None):
        self.data = data
        self.full_stack = full_stack
        self.left = None
        self.right = None

    def insert(self, data, full_stack):
        """
        Inserts a new node with the given data and full_stack name into the tree.
        """
        if data < self.data:
            if self.left is None:
                self.left = Node(data, full_stack)
            else:
                self.left.insert(data, full_stack)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data, full_stack)
            else:
                self.right.insert(data, full_stack)

    def print_tree(self):
        """
        Prints the tree in an in-order traversal.
        """
        if self.left:
            self.left.print_tree()
        print(f"{self.data}, {self.full_stack}")
        if self.right:
            self.right.print_tree()

    def search_node(self, data):
        """
        Searches for a node by the data value. If found, prints the ID and full_stack.
        """
        if self.data == data:
            return f"Search found: ID {self.data}, {self.full_stack}."
        elif data < self.data and self.left:
            return self.left.search_node(data)
        elif data > self.data and self.right:
            return self.right.search_node(data)
        return f"Search not found: ID {data} does not exist."

    def remove_node(self, data):
        """
        Removes a node with the specified data from the tree.
        Returns the removed node's data and full_stack, or None if not found.
        """
        if data < self.data:
            self.left, removed_node = (self.left.remove_node(data) if self.left else (None, None))
        elif data > self.data:
            self.right, removed_node = (self.right.remove_node(data) if self.right else (None, None))
        else:
            removed_node = (self.data, self.full_stack)
            # Node with only one child or no child
            if self.left is None:
                return self.right, removed_node
            elif self.right is None:
                return self.left, removed_node

            # Node with two children: Get the inorder successor
            temp = self.right.find_min()
            self.data = temp.data
            self.full_stack = temp.full_stack
            self.right, _ = self.right.remove_node(temp.data)

        return self, removed_node

    def find_min(self):
        """
        Finds the node with the minimum data value in the tree.
        """
        current = self
        while current.left is not None:
            current = current.left
        return current

    def bfs(self):
        """
        Performs a breadth-first search (BFS) traversal of the tree.
        """
        queue = deque([self])
        result = []
        while queue:
            node = queue.popleft()
            result.append((node.data, node.full_stack))
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def dfs(self):
        """
        Performs a depth-first search (DFS) traversal of the tree.
        """
        stack = [self]
        result = []
        while stack:
            node = stack.pop()
            result.append((node.data, node.full_stack))
            # Push right first so left is processed first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

# Create the root node and insert full-stack with IDs
root = Node(100, "full-stack")
root.insert(80, "Bootstrap")
root.insert(75, "CSS")
root.insert(90, "Tailwin")
root.insert(70, "HTML")
root.insert(65, "Frontend")
root.insert(97, "Javascript")
root.insert(95, "React")
root.insert(99, "Vue")
root.insert(120, "MySql")
root.insert(115,"Node.js")
root.insert(125,"MongoDB")
root.insert(110,"Backend")
root.insert(150,"API")
# Print the tree
print("Tree Structure:")
root.print_tree()
print()

# Perform BFS and DFS
bfs_result = root.bfs()
dfs_result = root.dfs()

# Print BFS and DFS traversal results
print("\nBFS Traversal:", bfs_result)
print("\nDFS Traversal:", dfs_result)

# Search for the node with ID 70
search_result = root.search_node(70)
print("\nSearching for the full_stack:")
print("+---------------------------------------------------------------+")
print(f"| {search_result:<61} |")
print("+---------------------------------------------------------------+\n")

# Remove the node with ID 75
print("\nRemoving node with ID 75")
root, removed_node = root.remove_node(75)
if removed_node:
    print("+---------------------------------------------------------------+")
    print(f"| Node with ID {removed_node[0]} ({removed_node[1]}) removed.\t\t\t\t|")
    print("+---------------------------------------------------------------+\n")

# Print the tree after remove
print("Tree Structure After remove:")
root.print_tree()