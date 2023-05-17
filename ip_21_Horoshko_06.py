import random
import string
import time
import numpy as np
import matplotlib.pyplot as plt
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
        global n1
        i = 0
        start = time.time()
        b = True
        while b:
            n1 = n1 + 1
            j = self._hash_function(key, i)
            if self.table[j][0] == key:
                t1 = time.time() - start
                return (self.table[j][1], t1)
            else:
                i = i + 1
            if i == self.size or self.table[j] is None:
                b = False
        return None
    
def murmur_hash2(key):
    m = 0x5bd1e995
    r = 24
    length = len(key)
    h = length
    data = bytearray(key, 'utf-8')  # Перетворюємо ключ у бінарний масив
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

def binarySearch(arr, x):
    global n2
    l = 0
    r = len(arr) - 1
    start = time.time()
    while l <= r:
 
        mid = l + (r - l) // 2
        n2 = n2 + 1
        if arr[mid] == x:
            end = time.time()
            return (mid, end - start)
 
        elif arr[mid] < x:
            l = mid + 1
 
        else:
            r = mid - 1
        n2 = n2 + 1
    t2 = time.time() - start
    return (-1, t2)

def genar(size):
    return [i for i in range(1, size + 1)]

class Node:
    def __init__(self, data):
        self.data = data # Додаємо елемент до ноди
        self.next = None
        self.prev = None
    
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def push(self, new_data): # Додаємо елемент в кінець
        new_node = Node(new_data)
        new_node.prev = self.tail
        if self.tail == None: # Перевіряємо чи список пустинй, якшо так, то робимо голову та хвіст новою нодою
            self.head = new_node 
            self.tail = new_node
            new_node.next = None
        else: # Якшо список не пустий, змінюємо хвіст
            self.tail.next = new_node
            new_node.next = None
            self.tail = new_node
            
    def middle(self, start, last):
        global n3
        if (start == None):
            return None
        slow = start
        fast = start.next
        while (fast != last):
            n3 = n3 + 1
            fast = fast.next
            if (fast != last):
                n3 = n3 + 1
                slow = slow.next
                fast = fast.next
        return slow
    
    def bin_search(self, value):
        global n3
        st = time.time()
        start = self.head
        last = None
        while True :
            # Знаходимо середнє значення
            mid = self.middle(start, last)
            if (mid == None):
                return None
            # Якщо значення всередині
            n3 = n3 + 1
            if (mid.data == value):
                t3 = time.time()-st
                return (mid, t3)
            # Якщо значення більше за середину
            elif (mid.data < value):
                start = mid.next
            # Якщо значення менше за середину.
            else:
                last = mid
            n3 = n3 + 1
            if not (last == None or last != start):
                break
        # Значення не має в масиві
        return None
    
def genlist(size):
    l = DoubleLinkedList()
    for i in range(1, size + 1):
        l.push(i)
    return l

choose = input("Do you want to see a graph(Yes or No):")
n1 = 0
n2 = 0
n3 = 0
if choose == 'No' or choose == 'no':
    choice = input('What data structure do you want to choose(h for hashtable, a for array, l for linked list):')
    if choice == 'h' or choice =='H':
        num = int(input('Enter number of elements in hashtable:'))
        h = rand_gen(num)
        v = h.find("ZRpklDExgLFOlsmYAzMR")
        print(n1)
        print(h.size)
        print(v[0])
        print(v[1])
    elif choice =='a' or choice =='A':
        num = int(input('Enter number of elements in array:'))
        x = random.randint(1, num)
        ar = genar(num)
        v = binarySearch(ar, x)
        print(n2)
        print(v[0])
        print(v[1])
    else:
        num = int(input('Enter number of elements in linked list:'))
        x = random.randint(1, num)
        l = genlist(num)
        v = l.bin_search(x)
        print(n3)
        print(v[0].data)
        print(v[1])
else:
    x = [100, 1000, 5000, 10000, 20000]
    y1 = [binarySearch(genar(100), 26)[1], binarySearch(genar(1000), 365)[1], binarySearch(genar(5000), 1268)[1], binarySearch(genar(10000), 2657)[1], binarySearch(genar(20000), 10598)[1]]
    y2 = [genlist(100).bin_search(26)[1], genlist(1000).bin_search(365)[1], genlist(5000).bin_search(1268)[1], genlist(10000).bin_search(2657)[1], genlist(20000).bin_search(10598)[1]]
    plt.plot(x, y1, label=r'$Array$')
    plt.plot(x, y2, label=r'$Linkedlist$')
    plt.xlabel('Size', fontsize='18')
    plt.ylabel('Time(seconds)', fontsize='18')
    plt.legend(loc='best', fontsize=12)
    plt.show()
