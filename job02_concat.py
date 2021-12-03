import pandas as pd

df = pd.read_csv('./crawling_data/reviews_2020_1.csv')
df.info()

for i in range(2, 38):
    df_temp = pd.read_csv(
        './crawling_data/reviews_2020_{}.csv'.format(i),
        index_col=0)




