# XeggeX_trading_bot
Python Trading bot

1. Market Making
2. Wash Trading
3. Info (Balances, Markets, Market Depth{bids & asks})

You will need two files to run the bot

1. Make a directory for the files for the bot 
```
mkdir Xeggex_Trading_Bot
```
than 
```
cd Xeggex_Trading_Bot
```
2. Download files to the new directory you just created
```
.env

Xeggex_Bot.py
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
nano .env
```

```
# XeggeX  Keys
# Api-Key
api_key=ENTER_YOUR_KEY_HERE
# Api-Secret-Key
secret_key=ENTER_YOUR_KEY_HERE
```
In The Bot.py using nano command you can change lines of code 
```
nano Xeggex_Bot.py
```

You can update the following lines of code to your stratigies
```
min_sell_price = 0.00000175
sell_price = round(ask_price - 0.00000001, 8)
sell_amount = round(random.uniform(5, 50), 1)
max_buy_price = 0.00000150
buy_price = round(bid_price + 0.00000005, 8)
buy_amount = round(random.uniform(0.05, 0.15), 3)
```
add # to the ``order_info =`` line of code to stop the bot order from being placed

To start Bot in Terminal:
1. `screen -S Xeggex_Trading_Bot` this is the folder where the bot is located
2. start bot
```
python3 Xeggex_Bot.py
```
3. to exit screen and keep bot running hold the key `Control` and than press keys `a d` at the same time
4. to resume screen type `screen -r`
5. to stop bot press `Control c`

Trading Bot Example:

<img src="https://user-images.githubusercontent.com/40405385/225445192-c7b023e7-2922-4252-bd25-16755e2699b9.png" width="25%" alt="Xeggex_bot">


<div style="color: yellow;">

**Disclaimer:**

The trading bot provided herein is designed for informational and educational purposes only. It is not intended to be, and should not be construed as, financial, investment, or trading advice. Users of this trading bot assume full responsibility for any decisions made based on its outputs, and the creators and maintainers of the bot shall not be held liable for any losses, damages, or claims arising from the use of this tool. Trading in financial markets involves substantial risks, including the potential for loss of principal, and may not be suitable for all investors. Before using this trading bot, users should carefully consider their financial objectives, risk tolerance, and level of experience. We strongly recommend consulting with a qualified financial advisor before making any investment or trading decisions.

</div>


