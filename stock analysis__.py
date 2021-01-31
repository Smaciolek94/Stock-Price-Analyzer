##JUST update the funds, and start date, output is generated in current directory

#for testing
#os.chdir("C:\\Users\\smaci\\Documents\\GitHub\\Stock-Fund-comparison")

startdate = "2017-05-01" 
#end date is today
<<<<<<< HEAD
funds = ["SCHB","QQQ","SCHZ","SCHF","SCHE","SCHH","SCHA","VT","SCHP","SCHC","GLD","FDKVX"]
#funds = ["SCHB","SCHZ","SCHF","SCHE","FXAIX","FTIHX","FXNAX","FDKVX"]
=======
funds = ["SCHB","QQQ","SCHZ","SCHF","SCHE","SCHH","SCHA","SCHP","SCHC","GLD"]
outfolder = "C:\\Users\\smaci\\Documents\\GitHubStock-Fund-comparison\\"
>>>>>>> d8adb0ded8c5b73c8dc3e3a0a94f6ae7dcfac948

###DO NOT NEED TO CHANGE BELOW HERE
import pandas as pd
import yfinance as yf
import datetime
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime
import os

outfolder = os.getcwd()

outpath = outfolder + "\\data.csv"
null = ["",""]
null = pd.DataFrame(null).transpose() #for spaces in output
n = len(funds)
growth = []
dividends = []
for fund in funds:
    name = yf.Ticker(fund)
    grow = name.history(start = startdate).iloc[:,3]
    grow = grow.to_numpy()
    growth.append(grow)
    div = name.history(start = startdate).iloc[:,5]
    div = div.to_numpy()
    dividends.append(div)

growth = pd.DataFrame(growth)
growth = growth.transpose()
growth.columns = funds
dividends = pd.DataFrame(dividends)
dividends = dividends.transpose()
dividends.columns = funds

m = len(growth) - 1

#correlation Matrix of Growth
growth_Correlation = growth.corr()
growth_Correlation = round(growth_Correlation,2)
growth_Correlation.to_csv(outpath)
null.to_csv(outpath,mode="a",header=False,index=False)

#raw STD
rawSTD = []
for i in range(0,n):
    sd = np.std(growth.iloc[:,i])
    rawSTD.append(sd)
rawSTD
rawSTD = pd.DataFrame(rawSTD).transpose()
rawSTD = round(rawSTD,2)
rawSTD.index = ["Raw_SD"]
rawSTD.to_csv(outpath,mode='a',header=False)

#scaling growth by maximum stock price
growthscale = growth.copy()
for i in range(0,n):
    growthscale.iloc[:,i] = growthscale.iloc[:,i] / max(growthscale.iloc[:,i])

#scaled STD
scaledSTD = []
for i in range(0,n):
    sd = np.std(growthscale.iloc[:,i])
    scaledSTD.append(sd)
scaledSTD = pd.DataFrame(scaledSTD).transpose()
scaledSTD.index = ["Scaled_SD"]
scaledSTD = round(scaledSTD,4)
scaledSTD.to_csv(outpath,mode='a',header=False)

null.to_csv(outpath,mode="a",header=False,index=False)

#relative growth
relative_Growth = []
for i in range(0,n):
    rel = (growth.iloc[m,i] - growth.iloc[0,i]) / growth.iloc[0,i]
    relative_Growth.append(rel)
relative_Growth = pd.DataFrame(relative_Growth).transpose()
relative_Growth.index = ["Raw_Growth_%"]
relative_Growth = round(relative_Growth,4)# * 100
relative_Growth.to_csv(outpath,mode='a',header=False)

#absolute, first relative, and last relative dividend
div_Yield_Absolute = []
div_Yield_Relative_to_First = []
div_Yield_Relative_to_Last = []
for i in range(0,n):
    divs = sum(dividends.iloc[:,i])
    div_Yield_Absolute.append(divs)
    divsrel = divs/growth.iloc[0,i]
    div_Yield_Relative_to_First.append(divsrel)
    divsrellast = divs/growth.iloc[m,i]
    div_Yield_Relative_to_Last.append(divsrellast)
dividendsoutput = pd.DataFrame(list(zip(div_Yield_Absolute,
                                  div_Yield_Relative_to_First,
                                  div_Yield_Relative_to_Last))).transpose()
dividendsoutput.index = ["Total_Dividends_$",
                    "Divs_First_Rel_%",
                    "Divs_Last_Rel_%"]
dividendsoutput.iloc[0,] = round(dividendsoutput.iloc[0,],2)
dividendsoutput.iloc[1,] = round(dividendsoutput.iloc[1,],4)#*100
dividendsoutput.iloc[2,] = round(dividendsoutput.iloc[2,],4)#*100

#growth with dividends
div_Added_Growth = []
for i in range(0,n):
    rel = (growth.iloc[m,i] - growth.iloc[0,i] + div_Yield_Absolute[i]) / growth.iloc[0,i]
    div_Added_Growth.append(rel)
div_Added_Growth = pd.DataFrame(div_Added_Growth).transpose()
div_Added_Growth.index = ["Growth_With_Divs_%"]
div_Added_Growth = round(div_Added_Growth,4)#*100
div_Added_Growth.to_csv(outpath,mode='a',header=False)

null.to_csv(outpath,mode="a",header=False,index=False)

#mins and max
lows = []
highs = []
for i in range(0,n):
    low = min(growth.iloc[:,i])
    high = max(growth.iloc[:,i])
    lows.append(low)
    highs.append(high)
extremes = pd.DataFrame(list(zip(lows,highs))).transpose()
extremes.index = ["Low_Price_$","High_Price_$"]
extremes = round(extremes,2)

#outputting dividends last
dividendsoutput.to_csv(outpath,mode='a',header=False)

null.to_csv(outpath,mode="a",header=False,index=False)

extremes.to_csv(outpath,mode="a",header=False)

#going to need the dates for plotting

#Plotting

#Relative peformance
name = yf.Ticker("SCHB")
grow = name.history(start = startdate)
date = grow.index
os.mkdir("relative_plots")
for i in range(0,n):
    plt.plot(date,growthscale.iloc[:,i])
    title = funds[i]
    plt.title(title + " Relative Preformance")
    #plt.show()
    #plt.axis(xlim=(0,1))
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    plt.ylim([0,1])
    plt.grid(True)
    plt.savefig(outfolder+"\\relative_plots\\"+funds[i]+"_rel.png")
    plt.close()
    
os.mkdir("absolute_plots")
for i in range(0,n):
    plt.plot(date,growth.iloc[:,i])
    title = funds[i]
    plt.title(title + " Absolute Performance")
    #plt.show()
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    plt.grid(True)
    plt.savefig(outfolder+"\\absolute_plots\\"+"_"+funds[i]+"_abs.png")
    plt.close()
