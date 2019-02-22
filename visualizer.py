import matplotlib.pyplot as plt
from random import shuffle
import matplotlib


def create_random_list(length):
    l = [i for i in range(1, length+1)]
    shuffle(l)
    return l


def display(l, curr=-1, next=-1):
    plt.clf()
    bar_l = plt.bar(range(len(l)), l)
    if curr >= 0:
        # change the color of current bar to red
        bar_l[curr].set_color('r')

    if next >= 0:
        # change the color of next bar to green
        bar_l[next].set_color('g')
    plt.draw()
    plt.pause(0.5)


def display_end(l):
    #TODO: use a more elegant method to keep the graph
    plt.clf()
    plt.bar(range(len(l)), l)
    plt.draw()
    plt.pause(10000000)


def display_match(l, *iter):
    #TODO: change the bar color to default blued
    bar_l = plt.bar(range(len(l)), l, color='azure')
    bar_l[iter[0]].set_color("black")
    bar_l[iter[1]].set_color("black")

    plt.draw()
    plt.pause(0.5)

