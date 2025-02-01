# Importing required libraries
import pandas as pd
import yfinance as yf
import plotly.io as pio
import plotly.graph_objects as go

# Set default template for Plotly
pio.templates.default = "plotly_white"

# Define tickers for Apple, Google, and Microsoft
apple_ticker = 'AAPL'
google_ticker = 'GOOGL'
microsoft_ticker = 'MSFT'

# Set the date range for data retrieval
start_date = '2023-07-01'
end_date = '2023-09-30'

# Download stock data using yfinance
apple_data = yf.download(apple_ticker, start=start_date, end=end_date)
google_data = yf.download(google_ticker, start=start_date, end=end_date)
microsoft_data = yf.download(microsoft_ticker, start=start_date, end=end_date)

# Check for and drop missing values
apple_data = apple_data.dropna()
google_data = google_data.dropna()
microsoft_data = microsoft_data.dropna()

# Print basic information about the data
print("Apple Data Info:")
apple_data.info()
print("\nGoogle Data Info:")
google_data.info()
print("\nMicrosoft Data Info:")
microsoft_data.info()

# Descriptive statistics of the datasets
print("\nApple Data Description:")
print(apple_data.describe())
print("\nGoogle Data Description:")
print(google_data.describe())
print("\nMicrosoft Data Description:")
print(microsoft_data.describe())

# Calculate daily returns for each stock
apple_data['Daily_Return'] = apple_data['Adj Close'].pct_change()
google_data['Daily_Return'] = google_data['Adj Close'].pct_change()
microsoft_data['Daily_Return'] = microsoft_data['Adj Close'].pct_change()

# Plot daily returns using Plotly
fig = go.Figure()

# Apple daily returns plot
fig.add_trace(go.Scatter(
    x=apple_data.index, y=apple_data['Daily_Return'],
    mode='lines', name='Apple', line=dict(color='blue')
))

# Google daily returns plot
fig.add_trace(go.Scatter(
    x=google_data.index, y=google_data['Daily_Return'],
    mode='lines', name='Google', line=dict(color='green')
))

# Microsoft daily returns plot
fig.add_trace(go.Scatter(
    x=microsoft_data.index, y=microsoft_data['Daily_Return'],
    mode='lines', name='Microsoft', line=dict(color='red')
))

# Update layout with titles and legend
fig.update_layout(
    title='Daily Returns for Apple, Google, and Microsoft (Last Quarter)',
    xaxis_title='Date', yaxis_title='Daily Return',
    legend=dict(x=0.02, y=0.95)
)

fig.show()
