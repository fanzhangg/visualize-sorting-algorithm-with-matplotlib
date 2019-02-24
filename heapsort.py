from heapq import heappush
from heapq import heappop
from visualizer import *

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
    l = []
    display_heap(h)
    for value in iterable:
        # TODO: a[0] is the smallest/biggest?
        # TODO: shift_down() behavior is strange
        display_heap(h)
        heappush(h, value)

    display(l, color="#AF9AB2", x=range(len(iterable)))

    for i in range(len(h)):
        display(l, color="#AF9AB2", x=range(len(iterable)))
        value = heappop(h)
        l.append(value)
    return l


if __name__ == "__main__":
    random_l = create_random_list(10)
    sorted_l = sort(random_l)
    print(sorted_l)
