
import matplotlib.pyplot as plt

from Statistics import statistics_count
from text_selection import *
from word_analysis import *
from statistics import *
def bar_top10():
    txt_path = Path("/home/nicolai/PycharmProjects/Mina-saker-Localtree/Books/Dialogues concerning second religion.txt")
    x = top_10_words(word_counter((txt_path)))
    y = list( x.values())

    print(y)
    plt.bar(list(x),y)
    #plt.xticks( )
    plt.show()


def pichart():
    txt_path = Path("/home/nicolai/PycharmProjects/Mina-saker-Localtree/Books/Dialogues concerning second religion.txt")
    #labels = list(word_counter((txt_path)).keys())
    #values = list(word_counter((txt_path)).values())

    labels = list(statistics_count(txt_path).keys())
    values = list(statistics_count(txt_path).values())
    plt.pie(values, labels=labels)
    plt.title("Pie Chart")
    plt.show()
pichart()