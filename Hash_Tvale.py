import matplotlib.pyplot as plt
import numpy as np

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is None:
            return None
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def display(self):
        for i, entries in enumerate(self.table):
            if entries is not None:
                print(f"Index {i}: {entries}")

# List of faculties and institutes at RUPP
faculties_and_institutes = [
    "Faculty of Agriculture",
    "Faculty of Arts",
    "Faculty of Economics and Management",
    "Faculty of Education",
    "Faculty of Engineering",
    "Faculty of Environmental Science",
    "Faculty of Geosciences",
    "Faculty of Law and Public Affairs",
    "Faculty of Science",
    "Institute of Foreign Languages",
    "Institute of International Relations",
    "Institute of Technology",
    "Institute of Graduate Studies"
]

# Initialize the hash table
hash_table = HashTable(size=10)

# Insert the faculties and institutes into the hash table
for idx, faculty in enumerate(faculties_and_institutes):
    hash_table.insert(faculty, idx)

# Prepare data for plotting
index_labels = range(hash_table.size)
values = [len(entries) if entries is not None else 0 for entries in hash_table.table]

# Plot the hash table distribution
plt.figure(figsize=(12, 6))
plt.bar(index_labels, values, color='skyblue')
plt.xlabel('Hash Table Index')
plt.ylabel('Number of Entries')
plt.title('Distribution of Faculties and Institutes in Hash Table')
plt.xticks(np.arange(hash_table.size), [f'Index {i}' for i in index_labels])
plt.ylim(0, max(values) + 1)

# Annotate bars with the number of entries
for i, v in enumerate(values):
    plt.text(i, v + 0.1, str(v), ha='center', fontweight='bold')

plt.show()
