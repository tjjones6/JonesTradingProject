# **Automatic Trading Algorithm (Robinhood)**

**Authors**: Tyler Jones  
**Last Edit**: 12.25.2024  

---

## **Overview**

This project is a Python-based trading bot designed to interact with Robinhood's API for automatic trading. It is currently focused on analyzing stock market data using moving averages (SMA, HMA), logging into the Robinhood account using multi-factor authentication (MFA), and tracking real-time stock prices. The bot can also view and manage the user’s portfolio, including buying power and stocks owned.

In the future, we aim to extend this project to automatically execute trades based on moving average crossovers and other technical indicators, providing an automated trading solution for users.

---

## **Key Features**

1. **Robinhood Authentication**: Logs into the Robinhood account using username, password, and TOTP (Time-based One-Time Password) for two-factor authentication.
2. **Portfolio Management**: Displays the user’s Robinhood portfolio, including current holdings and buying power.
3. **Moving Averages Calculation**: Calculates and visualizes different types of moving averages (Simple Moving Average (SMA), Hull Moving Average (HMA), and Weighted Moving Average (WMA)) for stocks.
4. **Stock Market Analysis**: Retrieves real-time stock data and tracks predefined stocks.
5. **Market Status Check**: Determines if the stock market is currently open based on current time.
6. **Automated Data Plotting**: Plots historical stock data along with calculated moving averages.

---

## **Installation**

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/automatic-trading-robinhood.git
   cd automatic-trading-robinhood
