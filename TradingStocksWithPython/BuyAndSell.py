import alpaca_trade_api as tradeapi

SEC_KEY = '' # Enter your secret code here
PUB_KEY = '' # Enter your public key here
BASE_URL = 'https://paper-api.alpaca.markets'# This is the base URL for paper trading
api = tradeapi.REST(key_id = PUB_KEY, secret_key = SEC_KEY, base_url = BASE_URL)


# Buy a stock
api.submit_order(
    symbol = 'SPY',# Replace with the tinker of the stock you want to buy
    qty = 1,
    side = 'buy',
    type = 'market',
    time_in_force = 'gtc' # Good till cancelled
)

# Sell a stock
api.submit_order(
    symbol = 'SPY',# Replace with the tinker of the stock you want to buy
    qty = 1,
    side = 'sell',
    type = 'market',
    time_in_force = 'gtc' # Good till cancelled
)