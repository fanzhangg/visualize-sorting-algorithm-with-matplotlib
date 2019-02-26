from heapq import heappush
from heapq import heappop
from visualizer import *
import matplotlib.pyplot as plt

"""
Heapsort algorithm using the module `heapq`

Divide its input into a sorted and an unsorted region, and it iteratively shrinks the unsorted region by extracting the 
largest element and moving that to the sorted region

Reference: 
https://docs.python.org/3.7/library/heapq.html
https://en.wikipedia.org/wiki/Heapsort
"""


def sort(iterable):
    h = []
    l = iterable

    plt.figure(1)
    display(l, color="#AF9AB2", x=range(len(iterable)))

    plt.figure(2)
    display_heap(h)


    for value in iterable:
        # TODO: a[0] is the smallest/biggest?
        # TODO: shift_down() behavior is strange
        l = l[1:]
        plt.figure(1)
        display(l, color="#AF9AB2", x=range(len(iterable)))

        heappush(h, value)
        plt.figure(2)
        display_heap(h)


    display(l, color="#AF9AB2", x=range(len(iterable)))

    for i in range(len(h)):
        plt.figure(1)
        display(l, color="#AF9AB2", x=range(len(iterable)))

        plt.figure(2)
        display_heap(h)
        value = heappop(h)
        l.append(value)
    return l


if __name__ == "__main__":
    random_l = create_random_list(10)
    sorted_l = sort(random_l)
    print(sorted_l)
