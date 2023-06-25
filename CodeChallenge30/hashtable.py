class HashTable:
    def __init__(self):
        self.max_size = 12
        self.item_list = [None]*self.max_size
            
    def hashing(self, key):
        """
        Hashes the given key using the ASCII values of its characters.

        Parameters:
            key (str): The key to be hashed.

        Returns:
            int: The index computed based on the hashed value.

        """
        result = 0
        for i in key:
            number = ord(i)
            result += number
        index = result % len(self.item_list)
        return index
    
    def set_new_key_and_value(self, key, value):
        """
        Sets a new key-value pair in the hash table or updates an existing key's value.

        If the hash table is at half of its maximum capacity, it doubles its size before adding the new key-value pair.

        Parameters:
            key (str): The key to be added or updated.
            value: The value associated with the key.

        Returns:
            list: The updated item list representing the hash table.

        """
        x = self.keys()
        if len(x) == self.max_size/2:
            self.max_size *= 2
            self.item_list += [None] * int(self.max_size / 2)
        index = self.hashing(key)
        if self.has(key):
            self.update_item(key, value)
        elif self.item_list[index] is not None and self.item_list[index][0] != key:
            for i in range(index, len(self.item_list)):
                if self.item_list[index] == None:
                    self.item_list[i] = [key, value]
                    return self.item_list
                else:
                    index += 1
        else:
            self.item_list[index] = [key, value]
        return self.item_list
    
    def keys_items(self):
        """
        Returns a list of keys in the hash table.

        Returns:
            list: A list of keys in the hash table.

        """
        return [x[0] for x in self.item_list if x is not None]
    
    def keys(self):
        """
        Returns a list of items in the hash table.

        Returns:
            list: A list of keys in the hash table.

        """
        return [x for x in self.item_list if x is not None]
    
    def get(self, key):
        """
        Retrieves the value associated with the given key from the hash table.

        Parameters:
            key (str): The key to search for.

        Returns:
            Any: The value associated with the key, or None if the key is not found.

        """
        x = self.keys()
        for i in x:
            if i[0] == key:
                return i[1]
            else:
                pass
        return None
    
    def has(self, key):
        """
        Checks if the hash table contains the given key.

        Parameters:
            key (str): The key to check for.

        Returns:
            bool: True if the key is found in the hash table, False otherwise.

        """
        x = self.keys()
        for i in x:
            if i[0] == key:
                return True
            else:
                pass
        return False
    
    def update_item(self, key, value):
        """
        Updates the value associated with the given key in the hash table.

        If the key is found in the hash table, its associated value is updated with the provided value.

        Parameters:
            key (str): The key to update.
            value: The new value to associate with the key.

        Returns:
            None

        """
        index = 0
        for i in self.item_list:
            if i == None:
                pass
            elif i[0] == key:
                index = self.item_list.index(i)
                self.item_list[index] = [key, value]
    
hashtable1 = HashTable()
hashtable1.set_new_key_and_value("Abdullah", 24)
hashtable1.set_new_key_and_value("Abdullha", 24)
hashtable1.set_new_key_and_value("islam", 24)
hashtable1.set_new_key_and_value("isam", 24)
hashtable1.set_new_key_and_value("issa", 24)
hashtable1.set_new_key_and_value("issb", 24)
hashtable1.set_new_key_and_value("ista", 24)
hashtable1.set_new_key_and_value("ist4", 24)
hashtable1.set_new_key_and_value("ist5", 24)
hashtable1.set_new_key_and_value("ist6", 24)
hashtable1.set_new_key_and_value("ist7", 24)
hashtable1.set_new_key_and_value("ist8", 24)
hashtable1.set_new_key_and_value("ist8", 29)

# print(hashtable1.get("ist4"))
# print(hashtable1.has("ist4"))
print(hashtable1.keys())
print(hashtable1.item_list)