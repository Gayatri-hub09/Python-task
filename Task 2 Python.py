

import pandas as pd
import time

# Alpha Vantage API key
API_KEY = "YOUR_API_KEY"

# Stock Portfolio Class
class StockPortfolio:
    def __init__(self):
        self.portfolio = pd.DataFrame(columns=["Symbol", "Shares", "Purchase Price", "Current Price", "Total Value", "Historical Performance"])
    
    def add_stock(self, symbol, shares, purchase_price):
        """Adds a stock to the portfolio."""
        if symbol in self.portfolio['Symbol'].values:
            print(f"Stock {symbol} already in the portfolio.")
            return
        self.portfolio = self.portfolio.append({
            "Symbol": symbol,
            "Shares": shares,
            "Purchase Price": purchase_price,
            "Current Price": 0.0,  # Current price will be fetched from API
            "Total Value": 0.0,  # Total value will be calculated
            "Historical Performance": None  # Historical performance will be fetched
        }, ignore_index=True)
        print(f"Added {shares} shares of {symbol} to the portfolio.")

    def remove_stock(self, symbol):
        """Removes a stock from the portfolio."""
        if symbol not in self.portfolio['Symbol'].values:
            print(f"Stock {symbol} not found in the portfolio.")
            return
        self.portfolio = self.portfolio[self.portfolio['Symbol'] != symbol]
        print(f"Removed {symbol} from the portfolio.")
    
    def fetch_current_price(self, symbol):
        """Fetches the current stock price from Alpha Vantage."""
        url = f"https://www.alphavantage.co/query"
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": symbol,
            "interval": "1min",  # Get data for the most recent 1 minute interval
            "apikey": API_KEY
        }
        response = requests.get(url, params=params)
        data = response.json()
        
        try:
            # Extract the most recent closing price
            latest_close = list(data['Time Series (1min)'].values())[0]['4. close']
            return float(latest_close)
        except KeyError:
            print("Error retrieving data for {symbol");
