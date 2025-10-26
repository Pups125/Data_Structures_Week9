class Contact:

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"Name: {self.name}, Number: {self.number}"

class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)

        current = self.data[index]

        if self.data[index] is None:
            self.data[index] = Node(key, value)
            return
        
        while current:
            if current.key == key:
                current.value = value
                return
        
            if current.next is None:
                break

            current = current.next
        current.next = Node(key, value)

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None
    
    def print_table(self):
        for i, node in enumerate(self.data):
            print(f"Index {i}:", end=" ")
            if node is None:
                print("Empty")
            else:
                current = node
                while current:
                    print(f"[{current.key}: {current.value}]", end=" -> ")
                    current = current.next
                print("None")



if __name__ == "__main__":
    table = HashTable(10)

    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")

    contact = table.search("Martha")
    print("\nSearch result:", contact)

    table.print_table()
   