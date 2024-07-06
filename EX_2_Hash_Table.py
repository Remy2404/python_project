class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        # Check if key already exists and update the value
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def delete(self, key):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return

    def display(self):
        for index, keys in enumerate(self.table):
            print(f"{index} -->", " --> ".join([f"{k}: {v}" for k, v in keys]))

    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

# Initialize hash table with size 10
hash_table = HashTable(10)

# Insert data
keys_to_insert = [
    (252541, "Bret Chism"),
    (295160, "Celsa Oldham"),
    (297061, "Era Harness"),
    (287519, "Taina Dockery"),
    (331347, "Leno Milligan"),
    (334165, "Rolanda Morisey"),
    (327862, "Twana Willcox")
]

for key, value in keys_to_insert:
    hash_table.insert(key, value)

print("Hash table after inserting data:")
hash_table.display()

# Delete a key
hash_table.delete(297061)

print("\nHash table after deleting key 297061:")
hash_table.display()

# Search for a key
search_key = 287519
result = hash_table.search(search_key)
if result:
    print(f"\nKey {search_key} found with value: {result}")
else:
    print(f"\nKey {search_key} not found.")

# Insert a new key to show updating the value
hash_table.insert(287519, "Updated Taina Dockery")

print("\nHash table after updating key 287519:")
hash_table.display()
