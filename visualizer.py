import matplotlib.pyplot as plt
from random import shuffle
import matplotlib

matplotlib.use("TkAgg")

plt.ion()


def create_random_list(length):
    l = [i for i in range(1, length+1)]
    shuffle(l)
    return l


def display(l, curr=-1, next=-1):
    plt.clf()
    bar_l = plt.bar(range(len(l)), l)
    if curr >= 0:
        # change the color of current bar to red
        bar_l[curr].set_color('yellow')

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


def display_match(l, match, *iter):
    #TODO: change the bar color to default blued
    if match:
        for i in range(2):
            bar_l = plt.bar(range(len(l)), l, color="#1E77B4")
            bar_l[iter[0]].set_color("#e74c3c")
            bar_l[iter[1]].set_color("#e74c3c")
            plt.draw()
            plt.pause(0.2)
            bar_l = plt.bar(range(len(l)), l, color="#1E77B4")
            bar_l[iter[0]].set_color("white")
            bar_l[iter[1]].set_color("white")
            plt.draw()
            plt.pause(0.2)
    else:
        for i in range(2):
            bar_l = plt.bar(range(len(l)), l, color='#1E77B4')
            bar_l[iter[0]].set_color("#7f8c8d")
            bar_l[iter[1]].set_color("#7f8c8d")
            plt.draw()
            plt.pause(0.2)
            bar_l = plt.bar(range(len(l)), l, color='#1E77B4')
            bar_l[iter[0]].set_color("white")
            bar_l[iter[1]].set_color("white")
            plt.draw()
            plt.pause(0.2)

