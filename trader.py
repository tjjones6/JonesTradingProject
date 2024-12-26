################################################
### Automatic Trading Algorithm (Robinhood) ###
################################################
# Authors: Tyler Jones
# Last Edit: 12.25.2024

### Imports ###
import robin_stocks.robinhood as rh
from pyotp import TOTP
import base64
import binascii
import datetime as dt
import time
import yfinance as yf

def get_login_info_from_file():
    """
    This function reads the login information from a file ('login_info.py'). 
    It retrieves the username, password, and TOTP secret key from the file 
    to be used for logging into the Robinhood account.
    
    Returns:
        tuple: A tuple containing username, password, and TOTP secret key.
    """
    with open('login_info.txt', 'r') as file:
        username = file.readline().strip()  
        password = file.readline().strip() 
        totp_secret = file.readline().strip()  
    return username, password, totp_secret

def is_valid_base32(secret):
    """
    This function checks whether the provided TOTP secret key is valid Base32 encoding.
    It attempts to decode the secret key using Base32, and if it fails, it returns False.
    
    Args:
        secret (str): The TOTP secret key to be checked.
    
    Returns:
        bool: True if the secret is valid Base32 encoding, False otherwise.
    """
    try:
        base64.b32decode(secret, casefold=True)
        return True
    except binascii.Error:
        return False

def login(days):
    """
    This function performs the login process to Robinhood using the provided credentials
    and TOTP secret key. It attempts to log in using a one-time password (OTP) generated
    from the TOTP secret. If OTP fails, it falls back to a backup code for login.
    """
    # Get login info and TOTP secret from the file
    username, password, totp_secret = get_login_info_from_file()

    # Validate the TOTP secret
    if not is_valid_base32(totp_secret):
        print("Invalid TOTP secret.")
        return

    # Generate OTP using the TOTP secret
    totp = TOTP(totp_secret)
    otp_code = totp.now()  # This will generate a new OTP code

    print(f"Generated OTP: {otp_code}")

    # You can replace this line with the backup code (in case TOTP fails)
    backup_code = "129642"  # Backup code from Robinhood account

    # Try logging in with the generated OTP first
    try:
        rh.authentication.login(username, password, mfa_code=otp_code, store_session=False)
        print("Logged in with OTP.")
    except Exception as e:
        # If OTP login fails, attempt login with the backup code
        print(f"Error logging in with OTP: {e}")
        print("Trying backup code...")
        rh.authentication.login(username, password, mfa_code=backup_code, scope='internal', by_sms=True, store_session=True)
        print("Logged in with backup code.")
        
    time_logged_in = 60*60*24*days # Seconds

def logout():
    """
    This function logs the user out from their Robinhood account.
    """
    rh.authentication.logout()

def open_market():
    """
    This function checks if the market is open based on the current time.
    The market is open between 9:30 AM and 3:59 PM (Eastern Time).
    
    Returns:
        bool: True if the market is open, False otherwise.
    """
    market = True
    time_now = dt.datetime.now().time()
    
    market_open = dt.time(9, 30, 0)  # 9:30 am
    market_close = dt.time(15, 59, 0)  # 3:59 pm
    
    if time_now > market_open and time_now < market_close:
        market = True
    else:
        # print('Market is closed')
        pass
    
    return market

def get_stocks():
    """
    This function returns a list of stocks of interest to be monitored.
    
    Returns:
        list: A list containing the symbols of the stocks of interest.
    """
    stocks = list()
    stocks.append('VTI')
    stocks.append('QQQ')
    stocks.append('DIA')
    return stocks

def pretty_print_dict(dictionary):
    """
    This function prints a dictionary in a human-readable format, with each key-value pair
    displayed on a new line. This helps in visualizing the dictionary contents clearly.
    
    Args:
        dictionary (dict): The dictionary to be printed.
    """
    print('Owned Stocks = {')
    for symbol, details in dictionary.items():
        print(f'\t{symbol} : {details}')
    print('}')

def view_profile():
    """
    This function retrieves and displays the Robinhood account profile, including buying power.
    It also fetches and prints all the stocks owned by the user along with their details 
    (quantity, average buy price, current price, etc.).
    """
    try:
        # Get basic profile information and display buying power
        profile_basics = rh.account.build_user_profile()
        buying_power = rh.account.load_account_profile().get('buying_power', None)
        
        if buying_power is not None:
            print(f'Buying power = {buying_power}')
        else:
            print("Unable to retrieve buying power.")
    except Exception as e:
        print(f"Error retrieving profile: {e}")
    
    try:
        # Get all the holdings (stocks)
        owned_stocks = rh.account.build_holdings()
        pretty_print_dict(owned_stocks)
    except Exception as e:
        print(f"Error retrieving stocks: {e}")

def calculate_moving_averages(stocks):
    """
    This function calculates the 50-day and 200-day moving averages for a list of stocks 
    using yfinance.
    
    Args:
        stocks (list): A list of stock symbols (e.g., ['VTI', 'QQQ', 'DIA']).
        
    Returns:
        dict: A dictionary with stock symbols as keys and their moving averages as values.
    """
    moving_averages = {}
    
    for stock in stocks:
        # Fetch historical stock data
        data = yf.download(stock, period="1y", interval="1d")  # Last 1 year of data
        
        # Calculate the moving averages
        ma_50 = data['Close'].rolling(window=50).mean().iloc[-1]
        ma_200 = data['Close'].rolling(window=200).mean().iloc[-1]
        
        # Store in the dictionary
        moving_averages[stock] = {'50_day_MA': ma_50, '200_day_MA': ma_200}
    
    return moving_averages

if __name__ == "__main__":
    """
    This block is executed when the script is run directly. It logs the user into Robinhood 
    and displays their profile information, including the stocks they own and their buying power.
    """
    # Login and view profile
    login(days=1)
    view_profile()

    # Get list of stocks
    stocks = get_stocks()
    print('Stocks: ', stocks)
    
    # Calculate moving averages
    moving_averages = calculate_moving_averages(stocks)
    print("Moving Averages: ", moving_averages)
    
    while open_market():
        prices = rh.stocks.get_latest_price(stocks)
        print('Prices: ', prices)
        
        time.sleep(30)  # 30 second intermission
