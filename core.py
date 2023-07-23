from analysis import pandas_test
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def corr():
    df = pandas_test()
    df.loc[df['game_3'] == 'Победа', 'game_3'] = 1
    df.loc[df['game_3'] == 'Поражение', 'game_3'] = 0
    df = df.drop(columns=["game_1", "game_2", "game_13"])
    df[['game_4','game_5', 'game_6']] = df[['game_4','game_5', 'game_6']].apply(LabelEncoder().fit_transform)
    onehot_first = OneHotEncoder(sparse_output=False)

    encoded_df = pd.DataFrame(onehot_first.fit_transform(df[['game_7','game_8','game_9','game_10','game_11','game_12']]))
    encoded_df.columns = onehot_first.get_feature_names_out()

    df = df.join(encoded_df)
    df.drop(['game_4','game_5','game_6','game_7','game_8','game_9','game_10','game_11','game_12'], axis=1, inplace=True)

    # df = df.astype({'game_4': np.float64,
    #                 'game_5': np.float64,
    #                 'game_6': np.float64,
    #                 'game_7': np.float64,
    #                 'game_8': np.float64,
    #                 'game_9': np.float64,
    #                 'game_10': np.float64,
    #                 'game_11': np.float64,
    #                 'game_12': np.float64,
    #                 })

    y_labels = df['game_3']

    y_labels = y_labels.astype({'game_3': np.float64
                    })

    df = df.drop(columns=["game_3"])

    correlations = df.corrwith(y_labels).sort_values(ascending=False)

    plot = sns.barplot(y=correlations.index, x=correlations)
    plot.figure.set_size_inches(15, 10)
    plt.title('Зависимость от всего(+к победе, -к поражению)')
    plt.show()
