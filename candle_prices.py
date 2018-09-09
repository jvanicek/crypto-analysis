'''
Author: Joseph Vanicek
Date: 11/28/17
Class: ISTA 131

Description:
Compares the 90-day prices of Bitcoin, Ethereum and Litecoin using 3 subplots of candle stick graphs.
'''

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.finance import candlestick2_ohlc as candle
from matplotlib import ticker as mticker
from matplotlib import style
import statsmodels.api as sm
import matplotlib.ticker as mticker
import statsmodels.formula.api as smf

style.use('ggplot')


def get_data():
    df = pd.read_csv('crypto-updated.csv', parse_dates=True)    
    btc = df[df['coin']=='Bitcoin']
    eth = df[df['coin']=='Ethereum']
    ltc = df[df['coin']=='Litecoin']
    
    return btc,eth,ltc


    


#==========================================================
def main():
    '''
    get_data is only used once to get the data for the .pkl file. 
    Once file is created, read from the pkl to increase performance.
    '''
    #bitcoin, ether, lite = get_data()

    bitcoin = pd.read_pickle('bc.pkl')
    ether = pd.read_pickle('e.pkl')
    lite = pd.read_pickle('l.pkl')

    bitcoin = bitcoin[:90]
    ether = ether[:90]
    lite = lite[:90]

    xtl_graph = pd.Series(bitcoin['close'],bitcoin['date'])
    
    fig = plt.figure()
    ax = plt.gca()
    

    ax1 = plt.subplot(311)
    candle(ax1, bitcoin['open'], bitcoin['high'], bitcoin['low'], bitcoin['close'], width=0.5, colorup = 'g', colordown = 'r')
    plt.title('Bitcoin Prices', fontsize = 14)
    ax1.invert_xaxis()
    ax1.axes.get_xaxis().set_visible(False)
    ax1.spines['bottom'].set_color("#5998ff")
    ax1.spines['top'].set_color("#5998ff")
    ax1.spines['left'].set_color("#5998ff")
    ax1.spines['right'].set_color("#5998ff")

    
    ax2 = plt.subplot(312, sharex = ax1)
    candle(ax2, ether['open'], ether['high'], ether['low'], ether['close'], width=0.5, colorup = 'g', colordown = 'r')
    plt.title('Ethereum Prices', fontsize = 14)
    ax2.invert_xaxis()
    ax2.axes.get_xaxis().set_visible(False)
    ax2.spines['bottom'].set_color("#5998ff")
    ax2.spines['top'].set_color("#5998ff")
    ax2.spines['left'].set_color("#5998ff")
    ax2.spines['right'].set_color("#5998ff")


    ax3 = plt.subplot(313, sharex = ax1)
    candle(ax3, lite['open'], lite['high'], lite['low'], lite['close'], width=0.5, colorup = 'g', colordown = 'r')
    plt.title('Litecoin Prices', fontsize = 14)
    ax3.spines['bottom'].set_color("#5998ff")
    ax3.spines['top'].set_color("#5998ff")
    ax3.spines['left'].set_color("#5998ff")
    ax3.spines['right'].set_color("#5998ff")
    xtl_graph.plot()
    ax3.invert_xaxis()
    fig.text(0.08, 0.5, 'Prices', ha='center', va='center', rotation='vertical', fontsize = 14)
    fig.text(0.51, .95, 'Past 90-days from 10/20/17', ha='center', va='center', rotation='horizontal', fontsize = 14)

    plt.xlabel('Date', fontsize = 14)
    plt.xticks(rotation = 25)
    plt.show()
    
    

if __name__ == '__main__':
    main()
