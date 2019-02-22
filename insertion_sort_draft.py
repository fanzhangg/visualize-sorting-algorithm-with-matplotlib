from visualizer import *
from time import sleep

matplotlib.use("TkAgg")

plt.ion()


def sort(l: list)->list:
    for i in range(1, len(l)):
        # move the item down the list until the item to its left is smaller than it
        # i > 0 in case of i is out of range
        while i > 0 and l[i-1] > l[i]:
            l[i], l[i-1] = l[i-1], l[i]
            display(l, i)
            i -= 1
    return l


def sort_2(l: list)-> list:
    for j in range(1, len(l)):
        for i in range(j, 1):
            if l[i-1] > l[i]:
                l[i], l[i-1] = l[i-1], l[i]
                display(l, i)
            else:
                break
    return l


def insert(l: list, i: int)->list:
    """
    Move the unordered item from the current place to the correct place where the next item is greater than the item
    :param l: a unordered list
    :param i: an int
    :return: a list
    """
    for j in range(i+1, len(l)):
        if l[j] >= l[i]:
            # move l[i] in front of l[j]
            del(l[i])
            l.insert(j-1, l[i])
            display(l)
            return l
    del(l[i])
    l.append(l[i])
    display(l)
    return l


def sort_3(l: list)->list:
    for i in range(0, len(l)-1):
        if l[i] >= l[i+1]:
            l = insert(l, i)
    return l


if __name__ == "__main__":
    random_l = create_random_list(10)
    sort_2(random_l)



