# XeggeX_trading_bot
Python Trading bot

you will need two files
```
.env

Xeggex_bot.py
```
Email: cryptominer8245@yahoo.com to get the files of this bot

Click here to contact me on Discord: <a href="https://discord.com/users/412476381725720576">Cryptominer8245</a>

For Install you will need Python3
check your version by opening a terminial and type
```python3 --version```

Update the package list and upgrade any existing packages:
```
sudo apt-get update
sudo apt-get upgrade
```
Install Python by running the following command:
```
sudo apt-get install python3
```
Verify the installation by checking the Python version:
```
python3 --version
```

The Bot needs a few libraries

to Install the libraries:
```
pip install requests
pip install termcolor
pip install prettytable
pip install python-dotenv
```

You will need to update your ``Private Keys`` and ``Coin Pairs`` in the .env file
Example:
```
# XeggeX  Keys
# Api-Key
api_key=
# Api-Secret-Key
secret_key=
```

In The Bot ``Xeggex_bot.py``

You can update the following lines of code to your stratigies
```
min_sell_price = 0.00000175
sell_price = round(ask_price - 0.00000001, 8)
sell_amount = round(random.uniform(5, 50), 1)
max_buy_price = 0.00000150
buy_price = round(bid_price + 0.00000005, 8)
buy_amount = round(random.uniform(0.05, 0.15), 3)
```

Disclaimer: The trading bot provided herein is designed for informational and educational purposes only. It is not intended to be, and should not be construed as, financial, investment, or trading advice. Users of this trading bot assume full responsibility for any decisions made based on its outputs, and the creators and maintainers of the bot shall not be held liable for any losses, damages, or claims arising from the use of this tool. Trading in financial markets involves substantial risks, including the potential for loss of principal, and may not be suitable for all investors. Before using this trading bot, users should carefully consider their financial objectives, risk tolerance, and level of experience. We strongly recommend consulting with a qualified financial advisor before making any investment or trading decisions.


