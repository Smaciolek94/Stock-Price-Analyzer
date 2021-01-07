# Stock-Fund-comparison
The program outputs some decriptive statitsics and performance data as well as pricing charts for selected funds

on the excel sheet

    the first table is a correlation matrix of the different funds
    raw SD is the standard deviation of the stock prices in the time window
    I scaled the stock prices by dividing all of them by their all time high, and scaled sd is the standard deviation of that
    raw growth is how much the stock grew in price over the time window selected
    growth with dividends is how much the stock grew if you include dividends
    total dividends is all the dividends in that window
    div_First_rel is the dividend amount divided by the starting price of the stock. It's basically your return on investment
    div_Last_rel is the dividend amount divided by the current price of the stock. It the percentage of a share you could buy now with the dividends you got
    low price is the lowest the stock got during the window
    high price is the highest the stock got during the window

Relative plots show the daily price of the stock divided by it's maximum price. It gives you a good idea of it's volatility and overall growth

Absolute plots show the daily actual price of the stock
