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
choose = input("Do you want to see a graph(Yes or No):")
if choose == 'No':
    method = int(input('''Methods:\n1.Bubble sort\n2.Modified bubble sort
3.Insertion sort\nChoose method:'''))
    case = int(input('''Cases:\n1.Best\n2.Worst\n3.Random\nChoose case:'''))
    array = input("Do you want to see arrays(Yes or No):")
    if array != 'No':
        if case == 1:
            print("Best array is:")
            print(listbest)
        elif case == 2:
            print("Worst array is:")
            print(listworst)
        else:
            print("Random array is:")        
            print(listrand)
    if method == 1:
        if case == 1:
            fun.bubble_sort(listbest, 1)
        elif case == 2:
            fun.bubble_sort(listworst, 1)
        else:
            fun.bubble_sort(listrand, 1)
    elif method == 2:
        if case == 1:
            fun.mod_bubble_sort(listbest, 1)
        elif case == 2:
            fun.mod_bubble_sort(listworst, 1)
        else:
            fun.mod_bubble_sort(listrand, 1)
    else:
        if case == 1:
            fun.insertion_sort(listbest, 1)
        elif case == 2:
            fun.insertion_sort(listworst, 1)
        else:
            fun.insertion_sort(listrand, 1)
    if array != 'No':
        print("Sorted array:")
        if case == 1:
            print(listbest)
        elif case == 2:
            print(listworst)
        else:     
            print(listrand)
else:
    time = [fun.bubble_sort(listbest, 0), fun.bubble_sort(listworst, 0),
            fun.bubble_sort(listrand, 0), fun.mod_bubble_sort(listbest, 0),
            fun.mod_bubble_sort(listworst, 0), fun.mod_bubble_sort(listrand, 0),
            fun.insertion_sort(listbest, 0), fun.insertion_sort(listworst, 0),
            fun.insertion_sort(listrand, 0)]
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
