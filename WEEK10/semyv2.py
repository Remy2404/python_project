class TreeNode:
    def init(self, key):
        self.val = key
        self.children = []

    def insert(self, key):
        new_node = TreeNode(key)
        self.children.append(new_node)
        return new_node

    def search(self, key, path=None):
        if path is None:
            path = []

        # Add the current node to the path
        path.append(self.val)

        if self.val == key:
            return path

        for child in self.children:
            result = child.search(key, path.copy())
            if result:
                return result

        return None

    def bfs(self):
        queue = [self]
        while queue:
            node = queue.pop(0)
            print(node.val)
            queue.extend(node.children)

    def dfs(self):
        print(self.val)
        for child in self.children:
            child.dfs()

    def print_tree(self, level=0):
        print(' ' * level * 4 + str(self.val))
        for child in self.children:
            child.print_tree(level + 1)

    def remove(self, key):
        # Helper function to find and remove the node
        def _remove_node(parent, key):
            for i, child in enumerate(parent.children):
                if child.val == key:
                    # Attach the children of the node being removed to the parent
                    parent.children.extend(child.children)
                    # Remove the node
                    del parent.children[i]
                    return True
                else:
                    if _remove_node(child, key):
                        return True
            return False

        # Special case for removing the root node
        if self.val == key:
            raise Exception("Cannot remove the root node directly. Please handle root removal separately.")

        return _remove_node(self, key)


# Function to create the Full Stack Developer Tree
def create_tree():
    # Creating the root of the tree
    root = TreeNode("Full Stack Developer")

    # Client Software (Front-end)
    frontend = root.insert("Client Software (Front-end)")
    html = frontend.insert("HTML")
    css = frontend.insert("CSS")
    css.insert("Bootstrap")
    css.insert("W3.CSS")
    frontend.insert("JavaScript")
    frontend.insert("ES5")
    frontend.insert("HTML DOM")
    frontend.insert("JSON")
    frontend.insert("XML")
    frontend.insert("jQuery")
    frontend.insert("Angular")
    frontend.insert("React")
    frontend.insert("Backbone.js")
    frontend.insert("Ember.js")
    frontend.insert("Redux")
    frontend.insert("Storybook")
    frontend.insert("GraphQL")
    frontend.insert("Meteor.js")
    frontend.insert("Grunt")
    frontend.insert("Gulp")

    # Server Software (Back-end)
    backend = root.insert("Server Software (Back-end)")
    backend.insert("PHP")
    backend.insert("ASP")
    backend.insert("C++")
    backend.insert("C#")
    backend.insert("Java")
    backend.insert("Python")
    backend.insert("Node.js")
    backend.insert("Express.js")
    backend.insert("Ruby")
    backend.insert("REST")
    backend.insert("Go")
    backend.insert("SQL")
    backend.insert("MongoDB")
    backend.insert("Sass")
    backend.insert("Less")
    backend.insert("Firebase.com")
    backend.insert("Parse.com")
    backend.insert("PaaS (Azure and Heroku)")

    return root


# Main function to interact with the tree
def main():
    tree = create_tree()
    while True:
        print("\nOptions:")
        print("1. Display Tree")
        print("2. Search Node")
        print("3. Insert Node")
        print("4. Remove Node")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            print("Tree Structure:")
            tree.print_tree()
        elif choice == '2':
            node_name = input("Enter node value to search: ")
            found_path = tree.search(node_name)
            if found_path:
                print(f"Node '{node_name}' found! Path: {' -> '.join(map(str, found_path))}")
            else:
                print(f"Node '{node_name}' not found!")
        elif choice == '3':
            node_value = input("Enter node value to insert: ")
            tree.insert(node_value)
            print(f"Node '{node_value}' inserted.")
        elif choice == '4':
            node_value = input("Enter node value to remove: ")
            try:
                if tree.remove(node_value):
                    print(f"Node '{node_value}' removed.")
                else:
                    print(f"Node '{node_value}' not found!")
            except Exception as e:
                print(e)
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "main":
    main()