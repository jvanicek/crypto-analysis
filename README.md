# Crypto Analysis and Visualization 

This project takes Crypto market data from 2014 to 2017 to create a price comparison candlestick graph, a Relative Strength Index model, 12-day and 26-day moving averages and Correlation Matric comparing the correlation coeffcients for Bitcoin, Ethereum, Litecoin, Ripple and Dash.

## Notes for Understanding the Models
**Candlestick Graph:** 
    * Plots the daily open, high, low and close market values.
    * Green bodies indicate days where the closing price was greater than the opening price. 
    * Red bodies indicate days where the closing price was less than the opening price. 
    * ![candlestick example](https://github.com/jvanicek/crypto-analysis/blob/development/images/candlestick_components.jpg)<br> 
</a>For more on Candlestick Graphs: https://www.investopedia.com/trading/candlestick-charting-what-is-it/
**Relative Strength Index (RSI):**
    * Used to analyze overbought and oversold conditions by the magnitude of recent price changes. <br>

</a>For more on RSI: https://www.investopedia.com/terms/r/rsi.asp

**Moving Averages:**
    * Smoothes the price flucuations to help identify trends and can be used as a support or resistance indicator.<br>
</a>For more on Moving Averages: https://www.investopedia.com/terms/m/movingaverage.asp

**Pearson Corelation Coefficients:**
    * In this project, this is measuring the correlations between each coin.
    * Measured as a number between -1 and 1. A value of -1 represents a perfectly negative correlation. Meaning as one value increases, the other will decrease. A value of 1 represents a perfectly positive correlation. Meaning as one value increases, the other value also increases. <br>
</a>For more on correlation: https://en.wikipedia.org/wiki/Pearson_correlation_coefficient

##Figures
**90 day price comparison candlestick graph. Corresponding file: candle_prices.py**<br>
![90day candlestick](https://github.com/jvanicek/crypto-analysis/blob/development/images/price_compare_90day.png)<br>
**Bitcoin Relative strength index with the 12-day and 26 day moving averages on top of a candlestick graph for comparison. Corresponding file: rsi.py**<br>
![rsi/simple moving averages](https://github.com/jvanicek/crypto-analysis/blob/development/images/rsi_sma.png)<br>
**3.    Correlation Matrix comparing the correlation coefficients of close prices for Bitcoin, Ethereum, Litecoin, Ripple and Dash. Corresponding File: corr_matrix.py**
![Correlation Matrix](https://github.com/jvanicek/crypto-analysis/blob/development/images/corr_matrix.png)