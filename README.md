# Stock Price Analyzer
<<<<<<< HEAD
*The program outputs some decriptive statistics and performance data as well as pricing charts for selected stocks, with the time window consisting of a user-selected start date to the current date*

This program utilizes the yfinance library for stock price quotes. To install it and the other libraries needed, use Install_Libraries.bat **Python must be added to your path.* The program will output the data csv to your current directory, and make sub-directories for the plots.

**The output data csv contains:**<ul>
<li>The first table is a correlation matrix of the stocks' prices for the given time window
<li>Raw SD is the standard deviation of the stock prices in the time window
<li>Scaled SD is the standard deviation of stock prices that have been scaled by their all-time-high in the given time window
<li>Raw growth is how much the stock grew in price over the time window 
<li>Growth with dividends is how much the stock grew including dividends over the time window
<li>Total dividends is all the dividends in the time window
<li>Div_First_rel is the dividend amount divided by the starting price of the stock in the time window, representing a return on investment
<li>Div_Last_rel is the dividend amount divided by the current price of the stock, showing how much of a share you could buy today with dividends
<li>Low price is the lowest price of the stock during the time window
<li>High price is the highest price of the stock during the time window
 </ul>

Relative plots show the time window maximum scaled price of the stock over the time window

Absolute plots show the daily price of the stock over the time window
=======
The program outputs some decriptive statistics and performance data as well as pricing charts for selected stocks, with the time window consisting of a user-selected start date to the current date

**The output csv contains:**<ul>
<li>The first table is a correlation matrix of the stocks' prices for the given time window
<li>Raw SD is the standard deviation of the stock prices in the time window
<li>Scaled SD is the standard deviation of stock prices that have been scaled by their all-time-high in the given time window
<li>Raw growth is how much the stock grew in price over the time window 
<li>Growth with dividends is how much the stock grew including dividends over the time window
<li>Total dividends is all the dividends in the time window
<li>Div_First_rel is the dividend amount divided by the starting price of the stock in the time window, representing a return on investment
<li>Div_Last_rel is the dividend amount divided by the current price of the stock, showing how much of a share you could buy today with dividends
<li>Low price is the lowest price of the stock during the time window
<li>High price is the highest price of the stock during the time window
 </ul>

Relative plots show the time window maximum scaled price of the stock over the time window

Absolute plots show the daily price of the stock over the time window
>>>>>>> d8adb0ded8c5b73c8dc3e3a0a94f6ae7dcfac948
