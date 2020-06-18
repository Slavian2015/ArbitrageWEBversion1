import os
import json
import requests
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
import uuid
import dash_table
import hashlib

d = 8
def custom_round(number, ndigits=d):
 return int(number * 10 ** ndigits) / 10.0 ** ndigits if ndigits else int(number)

price = '0.0000020999999'
price = custom_round(float(price))
print('PRICE  ####', '{:.10f}'.format(price))