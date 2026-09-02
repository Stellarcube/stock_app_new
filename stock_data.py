#  Handles getting stock data from yFinance.
import yfinance as yf
import streamlit as st
from config import duration_dict, interval_dict, stock_dict

def get_stock_data(tickersymbol, duration, interval):
    """
    Fetch historical price data for a ticker. Returns a DataFrame,
    or None if the fetch fails (e.g. no interval was available for
    the chosen duration, so 'interval' is empty/invalid).
    """
    tickerData = yf.Ticker(tickersymbol)
    try:
        return tickerData.history(
            period = duration_dict[duration], 
            interval = interval_dict[interval]
    ) 
    except Exception:
        st.error(f"Failed to fetch data for {tickersymbol}. "
                 f"Try a different Time Period / Interval combination.")
        return None

