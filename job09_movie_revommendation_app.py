import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from gensim.models import Word2Vec
from scipy.io import mmread
import pickle

form_window = uic.loadUiType('./movie_recommendation.ui')[0]

class Exam(QWidget, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.df_reviews = pd.read_csv('./crawling_data/cleaned_review_2015_2021.csv')
        self.Tfidf_matrix = mmread('./models/Tfidf_movie_review.mtx')
        self.embedding_model = Word2Vec.load('./models/word2VecModel_2015_2021.model')
        with open('./models/tfidf.pickle', 'rb') as f:
            self.Tfidf = pickle.load(f)
        self.btn_recommend.clicked.connect(self.btn_recommend_slot)

    def getRecommendation(self, cosine_sim):
        simScore = list(enumerate(cosine_sim[-1]))
        simScore = sorted(simScore, key=lambda x: x[1],
                          reverse=True)
        simScore = simScore[1:11]
        movieidx = [i[0] for i in simScore]
        recMovieList = self.df_reviews.iloc[movieidx]
        return recMovieList['titles']

    def btn_recommend_slot(self):
        key_word = self.le_keyword.text()
        sentence = [key_word] * 11
        sim_word = self.embedding_model.wv.most_similar(key_word, topn=10)
        words = []
        for word, _ in sim_word:
            words.append(word)
        for i, word in enumerate(words):
            sentence += [word] * (10-i)
        sentence = ' '.join(sentence)
        sentence_vec = self.Tfidf.transform([sentence])
        cosine_sim = linear_kernel(sentence_vec,
                                   self.Tfidf_matrix)
        recommendation_title = self.getRecommendation(cosine_sim)
        recommendation_title = '\n'.join(list(recommendation_title))
        self.lbl_recommend.setText(recommendation_title)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Exam()
    mainWindow.show()
    sys.exit(app.exec_())