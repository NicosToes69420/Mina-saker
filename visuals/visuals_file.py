from collections import *
import matplotlib.pyplot as plt

from Word_Analysis import *

from Statistics import *
from char import *
from sentence_analysis import sentence_analysis, words_in_sentence
from text_selection import *
from word_analysis import *

def bar_top10(txt_path):
    #txt_path = Path("/home/nicolai/PycharmProjects/Mina-saker-Localtree/Books/Dialogues concerning second religion.txt")
    x = top_10_words(word_counter((txt_path)))
    y = list( x.values())

    print(y)
    plt.bar(list(x),y)
    #plt.xticks( )
    plt.show()
def bar_comp(txt_path):
    #txt_path = Path("/home/nicolai/PycharmProjects/Mina-saker-Localtree/Books/Dialogues concerning second religion.txt")
    x = top_10_words(word_counter((txt_path)))
    y = list( x.values())

    print(y)
    plt.bar(list(x),y)
    #plt.xticks( )
    plt.show()


def pichart(txt_path):
    #txt_path = Path("/home/nicolai/PycharmProjects/Mina-saker-Localtree/Books/Dialogues concerning second religion.txt")
    #labels = list(word_counter((txt_path)).keys())
    #values = list(word_counter((txt_path)).values())

    labels = list(statistics_count(txt_path).keys())
    values = list(statistics_count(txt_path).values())
    plt.pie(values, labels=labels)
    plt.title("Pie Chart")
    plt.show()
""" 
def histogram(txt_path):
    #txt_path = Path("/home/nicolai/PycharmProjects/Mina-saker-Localtree/Books/Dialogues concerning second religion.txt")
    bert = sentence_analysis()
    x = list(bert.keys())
    y = list(bert.values())
    #plt.figure(figsize = (10,10))
    data = y
    print(y)
    plt.hist(data, bins=30, range=(-1, 30), color='skyblue', edgecolor='black')
    #plt.xticks( )
    plt.xlabel('Values')
    plt.ylabel('Density')
    plt.grid(axis='y')
    plt.show()

"""
def hist_top10(txt_path):
    bert = top_10_words(word_counter(txt_path))

    x = list(bert.keys())
    y = list(bert.values())
    plt.figure(figsize = (10,10))
    data = y
    print(y)
    plt.hist(data, range=(0, 10), color='skyblue', edgecolor='black')
    #plt.xticks()
    plt.xlabel('Values')
    plt.ylabel('Density')
    plt.grid(axis='y')
    plt.show()


def plot_basic_statistics(txt_path):
    stats = statistics_count(txt_path)
    alla_meningar = sentence_analysis(txt_path)

    counter = word_counter(txt_path)
    unika_ord = unique_word(counter)

    tecken_data = alla_tecken_icke_filt(txt_path)
    char_dist = char_type_distribution(tecken_data)

    plt.subplot(1, 2, 1)
    categories = ["Lines", "Paragraphs", "Sentences", "Words"]
    counts = [stats["total liness"], stats["paragraph"], len(alla_meningar), len(unika_ord)]
    plt.bar(categories, counts)
    plt.title("Text Composition")

    plt.subplot(1, 2, 2)
    labels = ["Letters", "Punctuation", "Spaces"]
    sizes = [char_dist["letters"], char_dist["punctuations"], char_dist["spaces"]]
    plt.pie(sizes, labels=labels)
    plt.title("Character Distribution")

    plt.show()


def plot_word_analysis(txt_path):
    counter = word_counter(txt_path)
    top10_data = top_10_words(counter)
    length_dist_data = word_length_distribution(counter)

    plt.subplot(1, 2, 1)
    words = list(top10_data.keys())
    frequencies = list(top10_data.values())
    plt.bar(words, frequencies)
    plt.title("Top 10 Words")

    plt.subplot(1, 2, 2)
    lengths = list(length_dist_data.keys())
    counts = list(length_dist_data.values())
    plt.bar(lengths, counts)
    plt.title("Word Length")

    plt.show()


def plot_sentence_analysis(txt_path):
    alla_meningar = sentence_analysis(txt_path)
    sentence_lengths = words_in_sentence(alla_meningar)

    length_counts = dict()

    for length in sentence_lengths:
        if length in length_counts:
            length_counts[length] += 1
        else:
            length_counts[length] = 1

    sorted_items = sorted(length_counts.items(), key=lambda item: item[1], reverse=True)[:10]

    plt.subplot(1, 2, 1)
    plt.hist(sentence_lengths)
    plt.title("All Sentence Lengths")

    plt.subplot(1, 2, 2)
    x_labels = []
    y_counts = []

    for length, count in sorted_items:
        x_labels.append(str(length))
        y_counts.append(count)

    plt.bar(x_labels, y_counts)
    plt.title("Most Common Lengths")

    plt.show()


def plot_character_analysis(txt_path):
    dic_all = alla_tecken_icke_filt(txt_path)
    dic_letters = most_common_letters(dic_all)
    top10_data = top10_letters(dic_letters)
    char_dist = char_type_distribution(dic_all)

    plt.subplot(1, 2, 1)
    letters = list(top10_data.keys())
    frequencies = list(top10_data.values())
    plt.bar(letters, frequencies)
    plt.title("Top 10 Letters")

    plt.subplot(1, 2, 2)
    labels = ["Letters", "Punctuation", "Spaces", "Numbers"]
    sizes = [char_dist["letters"], char_dist["punctuations"], char_dist["spaces"], char_dist["numbers"]]
    plt.pie(sizes, labels=labels)
    plt.title("Character Types")

    plt.show()


def run_all_visuals(txt_path):
    plot_basic_statistics(txt_path)
    plot_word_analysis(txt_path)
    plot_sentence_analysis(txt_path)
    plot_character_analysis(txt_path)
