'''
 Head developer: Joseph Vanicek
 131 final project
 rsi(Relative Strength Index) and simple moving averages figure
'''

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib.finance import candlestick2_ohlc as candle

# style.use('ggplot')


def get_data():
    df = pd.read_csv('crypto-updated.csv', parse_dates=True)    
    btc = df[df['coin']=='Bitcoin']
    eth = df[df['coin']=='Ethereum']
    ltc = df[df['coin']=='Litecoin']
    
    return btc,eth,ltc

#Calculate Simple moving averages
def sma(df, window):
    weights = np.repeat(1.0, window)/window
    smas = np.convolve(df,weights,'valid')
    return smas
'''
RSI: Predicts if a stock/coin is going to be underboaght or oversold.
n=14: the period of gains and loses used for the calculation
code from matpoltlib documentation example(https://matplotlib.org/examples/pylab_examples/finance_work2.html)
Values above 70 indicate overbought, values under 30 indicate undersold.
'''
def relative_strength(prices, n=14):
    deltas = np.diff(prices)
    seed = deltas[:n+1]
    up = seed[seed>=0].sum()/n
    down = -seed[seed<0].sum()/n
    rs = up/down
    rsi = np.zeros_like(prices)
    rsi[:n] = 100. - 100./(1. + rs)

    for i in range(n, len(prices)):
        delta = deltas[i - 1]  # cause the diff is 1 shorter

        if delta > 0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta

        up = (up*(n - 1) + upval)/n
        down = (down*(n - 1) + downval)/n

        rs = up/down
        rsi[i] = 100. - 100./(1. + rs)

    return rsi




#==========================================================
def main():
    '''
    get_data is only used once to get the data for the .pkl file. 
    Once file is created, read from the pkl to increase performance.
    '''
    # bitcoin = get_data()[0]
    # ether = get_data()[1]
    # lite = get_data()[2]
    bitcoin = pd.read_pickle('bc.pkl')[::-1]
    ether = pd.read_pickle('e.pkl')[::-1]
    lite = pd.read_pickle('l.pkl')[::-1]
    
    date = bitcoin['date']
    
    fig = plt.figure()
    ax = plt.gca()
    
    xtl = []
    for d in date:
        xtl.append(str(d))

    rollave = bitcoin['close'].rolling(12).mean()

    
    #Grpahing the simple moving averages for 12day and 26day
    av1 = sma(bitcoin['close'], 12)
    av2 = sma(bitcoin['close'], 26)



    ax0 = plt.subplot2grid((5,4), (0,0), rowspan=1, colspan=4, axisbg='#07000d')
    rsi = relative_strength(bitcoin['close'])
    bitrsi = pd.Series(rsi,xtl)
    bitrsi.plot()
    ax0.axes.get_xaxis().set_visible(True)
    ax0.set_ylim(0,100)
    plt.ylabel('RSI')
    plt.title('Bitcoin Prices', fontsize = 14)
    ax0.axhline(70, color='r')
    ax0.axhline(30,color='g')
    ax0.set_yticks([30,50, 70])
    ax0.grid(True, color='w')
    ax0.invert_xaxis()



    ax1 = plt.subplot2grid((5,4), (1,0), rowspan=4, colspan=4, sharex = ax0)
    bitsma = pd.Series(av1,xtl[:1626])
    bitsma.plot(label = "12 day moving averages" )
    
    bitsma = pd.Series(av2,xtl[:1612])
    bitsma.plot(label = "26 day moving averages")

    #Candlestick high open close graph for prices
    candle(ax1, bitcoin['open'], bitcoin['high'], bitcoin['low'], bitcoin['close'], width=0.5, colorup = 'g', colordown = 'r')
    ax1.spines['bottom'].set_color("#5998ff")
    ax1.spines['top'].set_color("#5998ff")
    ax1.spines['left'].set_color("#5998ff")
    ax1.spines['right'].set_color("#5998ff")
    ax1.grid(True, color='w')
    
    


    
    ax1.invert_xaxis()
    plt.xlabel('Date', fontsize = 14)
    plt.ylabel('Price', fontsize = 14)
    plt.xticks(rotation = 25)
    ax1.legend()
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))

    plt.draw()
    plt.show()






if __name__ == '__main__':
    main()