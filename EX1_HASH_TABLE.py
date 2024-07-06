class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for i in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)

    def delete(self, key):
        index = self.hash_function(key)
        if key in self.table[index]:
            self.table[index].remove(key)

    def display(self):
        for index, keys in enumerate(self.table):
            print(f"{index} -->", " --> ".join(map(str, keys)))
#Main Program
# Initialize hash table with size 10
hash_table = HashTable(10)

# Insert data (a)
keys_to_insert = [20, 11, 12, 23, 5, 17, 9]
for key in keys_to_insert:
    hash_table.insert(key)

print("Hash table after inserting data (a):")
hash_table.display()

# Delete key 12 (b)
hash_table.delete(12)

print("\nHash table after deleting 12 (b):")
hash_table.display()

# Insert data to observe collision handling (c)
additional_keys = [13, 44, 86, 57]
for key in additional_keys:
    hash_table.insert(key)

print("\nHash table after inserting additional data (c):")
hash_table.display()
