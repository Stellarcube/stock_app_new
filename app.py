# The main application
import streamlit as st
import plotly.express as px
from validation import valid_interval
from stock_data import get_stock_data
from config import duration_dict, stock_dict, time_period_duration, time_period_interval


# Get user's selections
duration = st.sidebar.selectbox(
    " Select Time Period: ",
    options = list(duration_dict.keys()), 
    index = 2 # default is 1 month
)
# Compute which intervals are valid for the chosen duration BEFORE building
# the interval selectbox, and feed the result straight into its options.
# (If duration = '1 Day', this list comes back empty - same behavior as
# the single-file version.)
interval_options = valid_interval(duration, time_period_duration, time_period_interval)

interval = st.sidebar.selectbox(
    """
    Select Time Interval:
    """,
    options = interval_options,
    index = 0
)

select_stock = st.sidebar.selectbox(
    """
    Select Stock: 
    """,
    options = list(stock_dict.keys()), 
    index = 4
)

# Fetch stock data: 
tickersymbol = stock_dict[select_stock]
tickerDf = get_stock_data(tickersymbol, duration, interval)

# Display charts (only if the fetch succeeded:)
if tickerDf is not None and not tickerDf.empty:
    st.write(f"""
    ## Stock Price App
    Shown are the chosen stock's **closing price** and **volume** of {select_stock}!
    """)

    fig_close = px.line(
        tickerDf, 
        x = tickerDf.index, 
        y = 'Close', 
        title = f"Closing prices for {tickersymbol}")
    st.plotly_chart(fig_close)

    fig_volume = px.line(
        tickerDf, 
        x = tickerDf.index, 
        y = 'Volume', 
        title = f"Trading volume for {tickersymbol}")
    st.plotly_chart(fig_volume)




