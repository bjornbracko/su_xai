import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

actual_path = 'data/actual.csv'
train_path = 'data/data_set_ALL_AML_train.csv'
test_path = 'data/data_set_ALL_AML_independent.csv'



class Data:
    def __init__(self, actual, train, test):
        self.actual = pd.read_csv(actual)
        self.train_full = pd.read_csv(train)
        self.test_full = pd.read_csv(test)
        self.train = self.clean_data(self.train_full)

    def clean_data(self, data):
        df1 = [col for col in data.columns if "call" not in col]
        df = data[df1]
        df = df.T
        df2 = df.drop(['Gene Description', 'Gene Accession Number'], axis=0)
        df2.index = pd.to_numeric(df2.index)
        df2.sort_index(inplace=True)
        df2['cat'] = list(self.actual[:38]['cancer'])
        dic = {'ALL': 0, 'AML': 1}
        df2.replace(dic, inplace=True)
        return df2

if __name__ == '__main__':
    df = Data(actual_path, train_path, test_path)
    print(df.train.head())
