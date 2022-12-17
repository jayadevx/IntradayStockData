import yfinance as yf
import sys
import pandas as pd

ticker_string = sys.argv[1]
print ("symbol: "+ticker_string)
tickers=ticker_string.split(",")
for ticker in tickers:
    data = yf.download (tickers=ticker, period = '5d', interval = '5m')#reset the index and move the old index to a new column 5m', rounding= True)
    data['Symbol'] = ticker
    data.reset_index (inplace=True)

    #rename the new column to the desired name 

    data.rename(columns={'Datetime': 'Datetime'}, inplace=True)
    data['Datetime2'] = pd.to_datetime(data['Datetime'])
    data['Date'] = data['Datetime2'].dt.date
    data['Time'] = data['Datetime2'].dt.time

    #specify the new column order 

    #new_column_order = ['Symbol', 'Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume']

    #reindex the dataframe with the new column order data 

    data.reindex(['Symbol', 'Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume'])
    data = data[['Symbol', 'Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume']]
    data.to_csv(ticker+'.csv')
    print ("Written " + ticker + '.csv')
