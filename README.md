# IntradayStockData
Program to download multiple days intraday stock data using yahoo finance.

Requirements:
Python3

Download getdt.py

Then install the following requirements 
```
pip install pandas
pip install yfinance
```

To run

```
python getdt.py 'ACC.NS,TCS.NS' 
```

Here ACC.NS and TCS.NS are ticker names in yahoo finance for two stocks in National Stock Exchange of India. Two CSV files will be generated after
succesful run which will contain intraday data of these stocks.

Then you can import the CSV files in applications such as amibroker
