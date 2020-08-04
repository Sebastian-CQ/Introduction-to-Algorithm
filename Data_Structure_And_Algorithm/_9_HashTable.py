class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def rehash(self, oldhash):
        return (oldhash + 1) % self.size

    def put(self, key, data):
        hash_value = self.hash_function(key)

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data

        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                nextslot = self.rehash(hash_value)
                while self.slots[nextslot] is not None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot)

                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

    def get(self, key):
        startslot = self.hash_function(key)

        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position)
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)


H = HashTable()
H[54] = 'cat'
H[26] = 'dog'
H[93] = 'lion'
H[17] = 'tiger'
H[77] = 'bird'
H[31] = 'cow'
H[44] = 'goat'
H[55] = 'pig'
H[20] = 'chicken'

print(H.slots)
print(H.data)
print(H[77])
print(H.get(55))





