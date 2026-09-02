## 📊 Stock Analysis Web App

An interactive web app built with Streamlit to visualize historical stock data (closing prices and trading volume) of leading tech stocks using the yfinance API. Users can dynamically select a stock, time period, and data interval to explore price trends over time. This project demonstrates practical knowledge of interactive data visualization, API-based data retrieval, UI/UX design using Streamlit, and deployment of Python applications to the cloud. It provides a robust foundation for building financial analytics dashboards and showcases effective use of modern Python tools in real-world projects.

### 🔧 Tech Stack

- **Python**
- **Streamlit**
- **yFinance**
- **Plotly Express**

### 🌟 Features

- Sidebar controls to select:
  - Stock ticker
  - Time period (e.g., 1 week, 1 month)
  - Interval (e.g., daily)
- Dynamic chart titles based on selected stock
- Hoverable tooltips showing:
  - Date
  - Price
  - Volume
- Custom validation logic to:
  - Ensure interval is always shorter than the selected period
  - Restrict maximum interval to 1 month
- Exception handling for robust error messaging
- Hosted on **Streamlit Community Cloud**

### 📸 Screenshots

**Closing Prices**

<img width="950" alt="image" src="https://github.com/user-attachments/assets/c5191309-9444-4f33-807d-074e382ab392" />

**Trading Volume**

<img width="950" alt="image" src="https://github.com/user-attachments/assets/bfed006d-cf72-4751-99e4-a8977e865bfa" />

### 🚀 Deployment

The app is deployed on Streamlit and can be accessed here:  
**[Stock Analytics App](https://stock-app-analytics.streamlit.app/)**




