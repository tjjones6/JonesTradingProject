# **Automatic Trading Algorithm in Robinhood**

**Authors**: Tyler Jones, Cody Jones
**Last Edit**: 12.31.2024  

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

## **Example Output**
```bash
Generated OTP: 123456
Logged in with OTP.
Buying power = 15000.00
Owned Stocks = {
    'VTI' : {'quantity': 50, 'average_price': 205.00, 'current_price': 220.00},
    'QQQ' : {'quantity': 20, 'average_price': 330.00, 'current_price': 340.00}
}
Stocks: ['VTI', 'QQQ', 'DIA']
Moving Averages and Hull Moving Averages: 
VTI: {'50_day_MA': 220.25, '200_day_MA': 210.50, 'HMA': 215.75}
QQQ: {'50_day_MA': 335.50, '200_day_MA': 330.00, 'HMA': 332.85}
DIA: {'50_day_MA': 350.00, '200_day_MA': 340.00, 'HMA': 345.60}
Prices: [220.30, 340.50, 350.25]
