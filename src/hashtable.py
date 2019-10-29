# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity):
        self.count = 0
        self.initial_capacity = capacity
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key) % self.capacity

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    

    def insert(self, key, value):
        # hash key
        hashed_key = self._hash(key)
        # if None set key value pair and return
        if not self.storage[hashed_key]:
            self.storage[hashed_key] = LinkedPair(key, value)
            # increment count 
            self.count += 1

        # if not none check to see if the key already exists in the linked list
        # if it does replace its value with the new value and return
        if self.storage[hashed_key]:
            current_item = self.storage[hashed_key]
            # loop through linked list to see if key exists
            while current_item:
                # if keys match set value of item to new value
                if current_item.key == key:
                    current_item.value = value
                    break
                else:
                    current_item = current_item.next

            # if the key is not already in the linked list add the new pair to the head of the linked list
            if not current_item:
                new_item = LinkedPair(key, value)
                new_item.next = self.storage[hashed_key]
                self.storage[hashed_key] = new_item

   
    def remove(self, key):
        # hash key
        hashed_key = self._hash(key)
        # if none at key print error
        if not self.storage[hashed_key]:
            print("No value at this key")
        # if value at key, loop through linked list and find value to remove
        else:
            current_item = self.storage[hashed_key]
            while current_item:
                # set value to none
                if current_item.key == key:
                    current_item.value = None
                    break
                else:
                    current_item = current_item.next
            
            if not current_item:
                 # if no key found print error      
                print("No value at this key")



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(old_capacity, new_capacity)
    ht.remove("line_1")
    ht.remove("line_2")
    ht.remove("line_3")

    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)
    print(old_capacity, new_capacity)
    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
