import random
import string
class Hashtable:
    def __init__(self, size=100):
        self.size = size  # Розмір хеш-таблиці
        self.table = [None] * self.size  # Створюємо масив розміру size, ініціалізований значеннями None

    def _hash_function(self, key , i):
        """Хеш-функція для обчислення індексу"""
        return (murmur_hash2(key) + i) % self.size

    def insert(self, key, value):
        """Вставка ключа та значення у хеш-таблицю"""
        i = 0
        b = True
        while b:
            j = self._hash_function(key, i)
            if self.table[j] is None:
                self.table[j] = (key, value)
                return j
            elif self.table[j][0] == key:
                # Ключ вже існує, оновлюємо значення
                self.table[j] = (key, value)
                return j
            else:
                i = i + 1
            if i == self.size:
                b = False
        self.resize(2*self.size)
        self.insert(key, value)

    def resize(self, new_size):
        """Зміна розмірності хеш-таблиці"""
        
        new_table = Hashtable(new_size)

        # Переносимо елементи зі старої хеш-таблиці в нову
        for item in self.table:
            if item is not None:
                key, value = item
                new_table.insert(key, value)

        self.size = new_size
        self.table = new_table.table

    def find(self, key):
        """Отримання значення за ключем з хеш-таблиці"""
        global n
        i = 0
        b = True
        while b:
            n = n + 1
            j = self._hash_function(key, i)
            if self.table[j][0] == key:
                return self.table[j][1]
            else:
                i = i + 1
            if i == self.size or self.table[j] is None:
                b = False
        return None
    
def murmur_hash2(key):
    seed = 0
    m = 0x5bd1e995
    r = 24

    length = len(key)
    h = seed ^ length

    data = bytearray(key, 'utf-8')  # Convert key to bytearray

    index = 0
    while length >= 4:
        k = (data[index] & 0xFF) | ((data[index + 1] & 0xFF) << 8) | ((data[index + 2] & 0xFF) << 16) | (
                    (data[index + 3] & 0xFF) << 24)
        k *= m
        k ^= k >> r
        k *= m

        h *= m
        h ^= k

        index += 4
        length -= 4

    if length == 3:
        h ^= (data[index + 2] & 0xFF) << 16
    if length >= 2:
        h ^= (data[index + 1] & 0xFF) << 8
    if length >= 1:
        h ^= (data[index] & 0xFF)
        h *= m

    h ^= h >> 13
    h *= m
    h ^= h >> 15

    return h

def rand_gen(size):
    h = Hashtable()
    letters = string.ascii_letters
    j = random.randint(1, size)
    for i in range(size):
        if i != j:
            lengthkey = random.randint(1, 20)
            lengthvalue = random.randint(1, 200)
            key = ''.join(random.choice(letters) for i in range(lengthkey))
            value = ''.join(random.choice(letters) for i in range(lengthvalue))
        else:
            key = "ZRpklDExgLFOlsmYAzMR"
            value = "QgJEahYsGtzVcPMbTiwNJLyHnFDvrlSeZBXmOqkxIudfpWRKACj"
        h.insert(key, value)
    return h
if __name__ == '__main__':
    num = int(input('Enter number of elemnts in hashtable:'))
    h = rand_gen(num)
    n = 0
    v = h.find("ZRpklDExgLFOlsmYAzMR")
    print(n)
    print(v)
