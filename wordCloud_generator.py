import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import PIL
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator

def wordArt(text, template = None, back_color = 'black', width_img = 4000, length_img = 4000, omit = [], max_limit = 1000, mask_img = './WordArt/passion.jpg'):

    print("Text chosen: ")
    print(text[2080:2089])

    notImp = ['the', 'is', 'in', 'a', 'if', 'i', 'you', 'he', 'she', 'it', 'they', 'and', 'his', 'her', 'schemes', 'its','has','about','over', 'located', 'been', 'or', 'himself', 'not', 'although', 'almost', 'them', 'then', 'from', 'called', 'used', 'uses', 'being', 'where', 'became', 'there', 'on', 'of', 'to', 'at', 'an', 'without', 'by', 'also', 'was', 'will','him', 'who', 'up', 'down','were','before','that', 'which', 'with', 'as', 'for', 'had', 'but', 'those', 'these']

    symbols = [',', '"', "'", '.', '&', '@', '/', "\\", '[', ']', '{', '}','*', '+', '-','(', ')','#', '!', '^', '%','<', '>', '?', ':', ';', '|', '~', '`','_', '=']

    # Function for deleting all instances of a value in a list
    def delAll(coll, word):
        while word in coll:
            coll.remove(word)
        return coll

    # Removing punctuations from Text

    for char in text:
        if char in symbols:
            text = text.replace(char, "")

    # Removing less important words that are used frequently
    words = text.lower().split()

    for word in words:
        if word in notImp or omit:
            words = delAll(words, word)

    word_dict = {}

    for word in words:
        if word.isalpha():
            if word in word_dict.keys():
                word_dict[word] += 1
            else:
                word_dict[word] = 1
        else:
            pass

    print(word_dict)

    char_mask = np.array(Image.open(mask_img))
    # image_colors = ImageColorGenerator(char_mask)
    image_colors = ImageColorGenerator(char_mask)

    wc = WordCloud(background_color=back_color, width=width_img, max_words=max_limit, mask = char_mask, random_state = 1, height=length_img, relative_scaling=0.2, normalize_plurals=False).generate_from_frequencies(word_dict)
    wc.recolor(color_func=image_colors)
    plt.axis('off')
    plt.imshow(wc)
    plt.show()

text  = """    Accomplish
    Accomplishments
    Achieve
    Achieve
    Achieve
    Achieve
    Act
    Action
    Active
    Fire
    Crazy
    Fearless
    Hardwork
    Love
    Kind
    Kind
    Kind
    Caring
    Caring
    Compassion
    Admiration
    Lead
    Drive
    Light
    Advice
    Alert
    Admire
    Adventure
    Alive
    Ambition
    Ambitious
    Ambitious
    Ambitious
    Appreciate
    Appreciation
    Attain
    Attitude



    Beauty
    Believe
    Believable
    Bliss
    Breakdown
    Breathtaking
    Build
    Catalyst
    Challenge
    Clarity
    Commit
    Commitment
    Compassion
    Complete
    Concentrate
    Confidence
    Content
    Control
    Conquer
    Courage
    Create



    Dare
    Dedicate
    Dedicate
    Dedicate
    Dedicate
    Dedication
    Desire
    Determination
    Determine
    Dream
    Dream
    Dream
    Dream
    Dream
    Dream



    Eager
    Earnest
    Empower
    Empowering
    Empowerment
    Encourage
    Encouragement
    Encouraging
    Endurance
    Endure
    Energetic
    Energy
    Enjoy
    Enjoyment
    Enthusiasm
    Envision
    Escape
    Excellence
    Experiences



    Faith
    Faithful
    Faithfulness
    Fearless
    Fighter
    Finish
    Finisher
    Fire
    Fix
    Focus
    Forgive
    Freedom
    Fulfilment
    Glory
    Goal
    Goodness
    Gratitude



    Happiness
    Happy
    Harmony
    Honesty
    Honor
    Honor
    Honor
    Hope
    Humble
    Humility
    Hunger
    Imagination
    Imagine
    Impetus
    Improve
    Incentive
    Ineffable
    Initiative
    Inspiration
    Inspire
    Inspiring
    Integrity
    Interest



    Joy
    Joyful
    Joyfulness
    Kind
    Kindness
    Know
    Knowledge
    Laugh
    Lead
    Leading
    Learn
    Life
    Live
    Limitless
    Love
    Loving



    Mindful
    Mindset
    Mission
    Meaning
    Meaningful
    Memories
    Momentum
    Motivate
    Motivated
    Motivation
    Motive
    Move
    Movement
    Moving
    Now
    Nurture



    Obstacles
    Opportunity
    Optimistic
    Outstanding
    Overcome
    Passion
    Passion
    Passion
    Passion
    Passion
    Passion
    Patience
    Peace
    Peaceful
    Peacefulness
    Persevere
    Perseverance
    Persist
    Persistence
    Persuade
    Plan
    Planner
    Positive
    Possibilities
    Power
    Powerful
    Practice
    Practice
    Practice
    Pride
    Prioritize



    Reach
    Rise
    Risk
    Risk
    Risk
    Risk
    Role
    Safe
    Safety
    Satisfaction
    Satisfy
    Secure
    Security
    Self
    Skill
    Skilful
    Skilfulness
    Spirit
    Spirited
    Spur
    Stimulus
    Strength
    Strong
    Succeed
    Success
    Success
    Success
    Success
    Sustain
    Sustenance



    Teach
    Teachable
    Time
    Trust
    Trustworthy
    Truth
    Understand
    Understood
    Value
    Values
    Versatile
    Will
    Willpower
    Winner
    Wisdom
    Wisdom
    Wisdom
    Wise
    Worthy
    Worthy
    Worthy
    Worthy
    Worthy
    Worthy
    Yearn
    Yearning
    Yes
"""

wordArt(text)
