###################################################
#  XeggeX Exchange Bot Created by Cryptominer8245 #
#       Marker Maker, WashTrade & Info Bot        #
#                Created 2-22-2023                #
###################################################
import requests
import json
import time
import datetime
import random
import os
import termcolor
import hmac
import hashlib
from urllib.parse import urlparse
from prettytable import PrettyTable
from termcolor import colored
from dotenv import load_dotenv
os.system('clear')
while True:
    load_dotenv()

    api_key = os.getenv("api_key")
    secret_key = os.getenv("secret_key")
#############################################################
# Get current date and time
    now = datetime.datetime.now()
    date_string = now.strftime("%B %d %Y")
    time_string = now.strftime("%I:%M:%S %p")
#############################################################

#############################################################
    symbol = os.getenv("symbol")
    base = os.getenv("base")
    pair = f"{symbol}_{base}"
    pairs= f"{symbol}-{base}"
    market = f"{symbol}{base}"
    markets = f"{symbol}/{base}"
    offset = 0
    limit = 10
    interval = 30
    print(colored("   XeggeX Exchange Bot Loading   \n", "light_magenta"))
    print("\n")
#############################################################
    class XeggexApi:
        def __init__(self, api_key, secret_key):
            self.api_key = api_key
            self.secret_key = secret_key
            self.base_url = 'https://xeggex.com/api/v2/'
#############################################################
# To get The rest of the working Code you must contact me  
# for Purchasing it - Thank you
