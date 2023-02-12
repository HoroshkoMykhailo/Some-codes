import random
import numpy as np
import matplotlib.pyplot as plt
import functions as fun
number = int(input('Enter the number of elements in the list:'))
listbest = []
listworst = []
listrand = []
for n in range(number):
    listbest.append(n+1)
    listworst.append(n+1)
    listrand.append(n+1)
listworst.reverse()
random.shuffle(listrand)
time = [fun.bubble_sort(listbest), fun.bubble_sort(listworst),
        fun.bubble_sort(listrand), fun.mod_bubble_sort(listbest),
        fun.mod_bubble_sort(listworst), fun.mod_bubble_sort(listrand),
        fun.insertion_sort(listbest), fun.insertion_sort(listworst),
        fun.insertion_sort(listrand)]
bars = ('Best bubble', 'Worst bubble', 'Rand bubble', 'Best mod bubble',
        'Worst mod bubble', 'Rand mod bubble', 'Best insertion',
        'Worst insertion', ' Rand insertion')
y_pos = np.arange(len(bars))
plt.bar(y_pos, time, color=['black', 'red', 'orange', 'gray',
                            'green', 'blue', 'cyan', 'yellow', 'purple'])
plt.title(number, fontsize='18')
plt.xlabel('Methods', fontsize='18')
plt.ylabel('Time(seconds)', fontsize='18')
plt.xticks(y_pos, bars)
plt.show()
