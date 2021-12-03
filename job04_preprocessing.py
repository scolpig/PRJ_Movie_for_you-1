import pandas as pd
from konlpy.tag import Okt
import re

df = pd.read_csv('./crawling_data/naver_movie_reviews_onesentence_2015_2021.csv')
# print(df.head())
df.info()

# df2 = pd.read_csv('./crawling_data/cleaned_review_2015_2021.csv')
#
# print(df2.head())
# df2.info()
# exit()
okt = Okt()

stopwords = pd.read_csv('./crawling_data/stopwords.csv', index_col=0)
# print(df.loc[0, 'reviews'])
# setence = re.sub('[^가-힣 ]', ' ', df.loc[0, 'reviews'])
# print(setence)
# token = okt.pos(setence, stem=True)
# print(token)
count = 0
cleaned_sentences = []
for sentence in df.reviews:
    count += 1
    if count % 10 == 0:
        print('.', end='')
    if count % 100 == 0:
        print()
    sentence = re.sub('[^가-힣 ]', '', sentence)
    token = okt.pos(sentence, stem=True)
    df_token = pd.DataFrame(token, columns=['word', 'class'])
    df_cleaned_token = df_token[(df_token['class'] == 'Noun') |
                                (df_token['class'] == 'Verb') |
                                (df_token['class'] == 'Adjective')]
    words = []
    for word in df_cleaned_token['word']:
        if len(word) > 1:
            if word not in stopwords:
                words.append(word)
    cleaned_sentence = ' '.join(words)
    cleaned_sentences.append(cleaned_sentence)
df['cleaned_sentences'] = cleaned_sentences
print(df.head())
df.info()
df = df[['titles', 'cleaned_sentences']]
df.to_csv('./crawling_data/cleaned_review_2015_2021.csv', index=False)














