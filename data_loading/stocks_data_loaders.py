import quandl 
import logging

def get_stock_data(tickers,start_date,end_date,quandl_api_key):
	'''
	Inputs:
	tickers: tickers in quandl format: 'WIKI/AAPL' or 'AAPL.US' for Apple stock
	start_date: history start date in datetime format
	end_date: history end date in datetime format
	quandl_api_key: quandl API key you can get to https://data.nasdaq.com/sign-up
	Outputs:
	stocks_df: pandas dataframe containing attributes: 
	Adj. Close, Adj. High, Adj. Low, Adj. Open, Adj. Volume, ExDividend, Close, High, Low, Open, SplitRatio, Volume
	'''
	quandl.ApiConfig.api_key=quandl_api_key
	stocks_df=quandl.get(tickers,start_date=start_date,end_date=end_date)
	return stocks_df
	
def get_stock_attribute_data(stocks_df,attribute):
	'''
	Get stocks attribute data from stocks dataframe
	inputs:
	stocks_df: pandas dataframe containing attributes
	attribute: one of stocks attributes 
	Adj. Close, Adj. High, Adj. Low, Adj. Open, Adj. Volume, ExDividend, Close, High, Low, Open, SplitRatio, Volume
	Outputs:
	df: dataframe containing specified stocks attribute
	'''
	
	tickers_attributes=stocks_df.keys().tolist()
	keys = [key.split(' - ')[1] for key in tickers_attributes]
	relevant = [tickers_attributes[n] for n in range(len(keys)) if keys[n]=='Adj. Open']
	
	if len(relevant)>0:
		return stocks_df[relevant]
	else:
		logging.debug(f"{attribute} is not a valid attribute")
		
def compute_stock_returns(prices_df):
	'''
	Compute stock price returns from prices data frame
	Inputs:
	prices_df: stock prices data frame
	Ouputs:
	return_df: stock returns dataframe (in percentage)
	'''
	returns_df = 100.0*prices_df.pct_change()
	returns_df = returns_df.iloc[1:]
	return returns_df

def compute_dataframe_mean_std(df):
	'''
	Compute mean standard deviation for an input dataframe.
	If df is a stock return dataframe, stock mean returns and volatilities are computed
	Inputs:
	df: input dataframe
	Outputs:
	mean_df: mean dataframe
	std_df: standard deviation dataframe
	'''
	mean_df = df.mean()
	std_df = df.std()
	return mean_df, std_df
	
