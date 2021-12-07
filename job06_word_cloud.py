# -*- coding: utf-8 -*-
"""job06_word_cloud.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wLmd7qGRX0lWj7kxWcpUKSQdyPjJmOTu
"""


import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import collections
from konlpy.tag import Okt
from matplotlib import font_manager, rc
import matplotlib as mpl
import numpy as np
from PIL import Image



fontpath = './malgun.ttf'
font_name = font_manager.FontProperties(fname=fontpath, size=8).get_name()
plt.rc('font', family='NanumBarunGothic')


df = pd.read_csv('./crawling_data/cleaned_review_2015_2021.csv')
print(df.head())

#words = df[df['titles'] == '100% 울프: 푸들이 될 순 없어 (100% Wolf)']['cleaned_sentences']
words = df.iloc[1, 1]
words = words.split()
print(words)

worddict = collections.Counter(words)
worddict = dict(worddict)
print(worddict)

wordcloud_img =WordCloud(
    background_color='white', max_words=2000,
    font_path=fontpath).generate_from_frequencies(worddict)

plt.figure(figsize=(12, 12))
plt.imshow(wordcloud_img, interpolation='bilinear')
plt.axis('off')
plt.show()

stopwords = ['영화', '감독', '개봉', '개봉일', '촬영', '관객', '관람', '주인공', '출연', '배우', '평점',
             '들이다', '푸다', '리뷰', '네이버', '나오다']



alice_mask = np.array(Image.open('./crawling_data/bin_mask.jpg'))

wordcloud_img = WordCloud(
    background_color='white', max_words=2000,
    font_path=fontpath, collocations=False,
    stopwords=stopwords, mask=alice_mask
).generate(df.cleaned_sentences[3])

plt.figure(figsize=(12, 12))
plt.imshow(wordcloud_img, interpolation='bilinear')
plt.axis('off')
plt.show()