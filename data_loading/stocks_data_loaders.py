import pandas_datareader.data as pdr

def get_stock_data(tickers, start_date, end_date, quandl_api_key):
	'''
	Inputs:
	tickers: tickers in quandl format: 'WIKI/AAPL' or 'AAPL.US' for Apple stock
	start_date: history start date in datetime format
	end_date: history end date in datetime format
	quandl_api_key: quandl API key you can get to https://data.nasdaq.com/sign-up
	Ouput:
	df: pandas datframe containing attributes: 
	AdjClose, AdjHigh, AdjLow, AdjOpen, ExDividend, Close, High, Low, Open, SplitRatio, Volume
	'''

	df = pdr.DataReader(tickers,'quandl',start_date, end_date,api_key=quandl_api_key)
	
	return df
