"""
My implementation of heap

Heaps are arrays for which a[k] <= a[2*k+1] and a[k] <= a[2*k+2] for
all k, counting elements from 0. The interesting property of a heap is
that a[0] is always its smallest element

Usage:

heap = []               # creates an empty heap
heappush(heap, item)    # pushes a new item on the heap
item = heappop(heap)    # pops the smallest item from the heap
"""


def heappush(heap, item):
    """
    Push item onto heap, maintaining the heap invariant.
    :return:
    """
    heap.append(item)


def _shift_down(heap,startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place newitems fit
    while pos > startpos:
        pass
