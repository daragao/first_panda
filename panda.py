import datetime
from pandas_datareader import data, wb
import math
import matplotlib.pyplot as plt

def growth(df,ticker):
    days = (df.index[-1]-df.index[0]).days
    dfCAGR = ((((df['Adj Close'][-1]) / df['Adj Close'][1])) ** (365.0/days)) - 1
    print ('CAGR ',ticker,'=',str(round(dfCAGR,4)*100)+"%")

    df['Returns'] = df['Adj Close'].pct_change()
    trading_days = 252
    vol = df['Returns'].std()*math.sqrt(trading_days)
    print ("Annual Volatility =",str(round(vol,4)*100)+"%")

    return df,dfCAGR,vol

def plotCompoundedReturns(df,label):
    ((df['Adj Close'].resample('B').mean().pct_change() + 1).cumprod() - 1).plot(label=label)

#days_passed = 30*(12)
#start = datetime.datetime.now() + datetime.timedelta(-days_passed)
start = datetime.date(2010,1,1)
end = datetime.datetime.now()
df = data.DataReader("DPZ", "yahoo", start, end)
df1 = data.DataReader("GOOGL", "yahoo", start, end)
df2 = data.DataReader("AMZN", "yahoo", start, end)
df3 = data.DataReader("AAPL", "yahoo", start, end)

growth(df,'DPZ')
growth(df1,'GOOGL')
growth(df2,'AMZN')
growth(df3,'AAPL')

plotCompoundedReturns(df,'DPZ')
plotCompoundedReturns(df1,'GOOGL')
plotCompoundedReturns(df2,'AMZN')
plotCompoundedReturns(df3,'AAPL')

plt.grid(True)
plt.legend()
plt.show()
