'''
Author: Joseph Vanicek
Date: 11/28/17
Class: ISTA 131

Final Project: Correlation matrix visualizing the correlation coefficients of 
Bitcoin, Ethereum, Litecoin, Ripple and Dash.
'''
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import ticker as mticker
import seaborn as sns

def get_data():
    df = pd.read_csv('crypto-updated.csv', index_col = 'date', usecols = ['date','coin','close'], parse_dates=True)
    
    df = df[(df['coin'] == 'Bitcoin') | (df['coin'] == 'Ethereum') | (df['coin'] == 'Litecoin') | (df['coin'] == 'Ripple') | (df['coin'] == 'Dash')]
    btc = df[df['coin'] == 'Bitcoin']
    eth = df[df['coin'] == 'Ethereum']
    ltc = df[df['coin'] == 'Litecoin']
    rip = df[df['coin'] == 'Ripple']
    das = df[df['coin'] == 'Dash']

    column = ['Bitcoin','Ethereum','Litecoin','Ripple','Dash']
    index = []

    btc = btc['close'].values 
    eth = eth['close'].values
    ltc = ltc['close'].values
    rip = rip['close'].values
    das = das['close'].values

    

    
    data = [btc,eth,ltc,rip,das]

    
    coins = pd.DataFrame(index = index, columns = column)
    coins['Bitcoin']=btc[:90]
    coins['Ethereum']=eth[:90]
    coins['Litecoin']=ltc[:90]
    coins['Ripple']=rip[:90]
    coins['Dash']=das[:90]

        
    return coins

def plot_corr(df,size=10):
    f, ax = plt.subplots(figsize=(10, 8))
    corr = df.corr()
    sns.heatmap(corr,annot=True, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),square=True, ax=ax)    
    plt.title('Coin Correlation Matrix', fontsize = 14)


def main():
    
    df = get_data()
    plot_corr(df)
    plt.show()
    


if __name__ == '__main__':
    main()