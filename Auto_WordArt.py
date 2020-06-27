## For making word cloud

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import PIL
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator

## For getting info on the internet

from selenium import webdriver
import urllib.request # For python 2 just import urllib, urllib.request is needed for python 3+ because it has been been segmented into many subsets
from selenium.webdriver.common.keys import Keys # Helps to stimulate keyboard key presses
import os
import time


def wordArt(text = "", Auto = False, AutoTopic = "", back_color = 'black', width_img = 4000, length_img = 4000, omit = [], max_limit = 1000, mask_img = None):

    ## When nothing is supplied
    if (text == "" and Auto == False):
        print("SUPPLY TEXT OR CHOOSE AUTO!")
        return

    notImp = ['the', 'is', 'in', 'a', 'if', 'i','archived','be','have','me','my','you','january', 'february','march','april','may', 'june', 'july', 'august','september','october','november','december', 'he', 'she', 'it', 'they', 'and', 'his', 'her', 'schemes', 'its',
    'has','about','over', 'located', 'been', 'or', 'himself', 'not', 'although', 'almost', 'them', 'then', 'from', 'called', 'used', 'uses', 'being', 'where', 'became', 'there', 'on', 'of', 'to', 'at', 'an', 'without', 'by', 'also', 'was', 'will','him', 'who', 'up',
    'down','were','before','that', 'which', 'with', 'as','while','for', 'had', 'but', 'those', 'these', 'would', 'when', 'original', 'retrieved','because', 'this', 'most', 'than', 'after', 'other', 'began', 'every','during','upon',]

    symbols = [',', '"', "'", '.', '&', '@', '/', "\\", '[', ']', '{', '}','*', '+', '-','(', ')','#', '!', '^', '%','<', '>', '?', ':', ';', '|', '~', '`','_', '=']

    if Auto == True:
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.binary_location = "/usr/bin/chromium"
        driver = webdriver.Chrome("D:\Python files\Web Automation\chromedriver.exe")


        bio = AutoTopic ## input('So what topic would you like to make a word cloud on: ')

        driver.get('https://www.wikipedia.org/')
        search = driver.find_element_by_id('searchInput')
        search.send_keys(bio)
        search.send_keys(Keys.ENTER)
        info = driver.find_elements_by_class_name("mw-parser-output")
        text = info[0].text
        print(text[1902:10000])
        driver.close()
    else:
        pass

    # Function for deleting all instances of a value in a list
    def delAll(coll, word):
        while word in coll:
            coll.remove(word)
        return coll

    # Removing punctuations from Text
    for char in text:
        try:
            if char in symbols:
                text = text.replace(char, "")
        except:
            pass

    # Removing less important words that are used frequently and the ones mentioned in "omit" parameter
    words = text.lower().split()

    for word in words:
        try:
            if word in notImp or omit:
                words = delAll(words, word)
        except:
            pass

    word_dict = {}

    # Removing words that are not alphabets
    for word in words:
        try:
            if word.isalpha():
                if word in word_dict.keys():
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
            else:
                pass
        except:
            pass

    # Printing the dictionary to get an # IDEA
    print(word_dict)
    if mask_img != None:
        char_mask = np.array(Image.open(mask_img))
        # image_colors = ImageColorGenerator(char_mask)
        image_colors = ImageColorGenerator(char_mask)

        wc = WordCloud(background_color=back_color, width=width_img, max_words=max_limit, mask = char_mask, random_state = 1, height=length_img, relative_scaling=0.2, normalize_plurals=False).generate_from_frequencies(word_dict)
        wc.recolor(color_func=image_colors)
        plt.axis('off')
        plt.imshow(wc)
        plt.show()
    else:
        wc = WordCloud(background_color=back_color, width=width_img, max_words=max_limit, random_state = 1, height=length_img, relative_scaling=0.2, normalize_plurals=False).generate_from_frequencies(word_dict)
        plt.axis('off')
        plt.imshow(wc)
        plt.show()


# import sys
# print(sys.stdout.encoding)

wordArt(Auto = True, AutoTopic = "Robert Downey Junior", max_limit = 400, back_color = 'white')
