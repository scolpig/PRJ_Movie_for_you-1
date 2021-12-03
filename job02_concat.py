import pandas as pd

df = pd.read_csv('./crawling_data/reviews_2020_1.csv')
df.info()

for i in range(2, 38):
    df_temp = pd.read_csv(
        './crawling_data/reviews_2020_{}.csv'.format(i))
    df_temp.dropna(inplace=True)
    df_temp.drop_duplicates()
    df_temp.columns = ['title','reviews']
    df_temp.to_csv('./crawling_data/reviews_2020_{}.csv'.format(i),
                   index=False)
    df = pd.concat([df, df_temp], ignore_index=True)
df.info()
df.to_csv('./crawling_data/reviews_2020.csv', index=False)



