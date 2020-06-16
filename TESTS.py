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


##################################   SHOW ALL ROWS & COLS   ####################################
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None)

main_path_data = os.path.abspath("./data")
# my_tornado.json


a_file1 = open(main_path_data + "\\my_tornado.json", "r")
rools = json.load(a_file1)
a_file1.close()
# para = "PZM_USD"




# ########################     ALFA    ##########################
# def alfa(val1, val2, price, amount):
#     #####  direction  (buy  / sell)
#
#
#     if val1 == 'USD' or val1 == 'USDT' or val2 == 'USD' or val2 == 'USDT':
#         if val1 == 'USD' or val1 == 'USDT':
#             direction = "buy"
#             pass
#         else:
#             direction = "sell"
#             pass
#     elif val1 != 'USD' and val2 != 'USD' and val1 != 'USDT' and val2 != 'USDT':
#         if val1 == 'BTC':
#             direction = "buy"
#             pass
#         else:
#             direction = "sell"
#             pass
#
#
#
#     tickers_all = ['BTC_USD', 'PZM_USD', 'ETH_USD', 'ETH_USDT', 'PZM_BTC', 'ETH_BTC']
#
#     parametr1 = "{}_{}".format(val1, val2)
#     parametr2 = "{}_{}".format(val2, val1)
#
#     for i in tickers_all:
#         if i == parametr1:
#             para = i
#             pass
#         elif i == parametr2:
#             para = i
#             pass
#
#     urll = 'https://btc-alpha.com/api/v1/pairs/'
#     respo = requests.request("GET", urll)
#     examm = respo.json()
#
#     dec_val = para.split('_')
#
#     for i in examm:
#         if i['currency2'] == dec_val[1] and i['currency1'] == dec_val[0]:
#             # amount = round(float(amount), int(i['price_precision']))
#             amount = Context(prec=(i['price_precision'] + 2), rounding=ROUND_DOWN).create_decimal(amount)
#             amount = float(amount)
#             pass
#         else:
#             pass
#
#     def keys():
#         if os.path.isfile(main_path_data + "\\keys.json"):
#             pass
#         else:
#
#             dictionary = {"1": {"key": "Api key",
#                                 "api": "Api secret"},
#                           "2": {"key": "Api key",
#                                 "api": "Api secret"},
#                           "3": {"key": "Api key",
#                                 "api": "Api secret"},
#                           "4": {"key": "Chat id", "api": "Token"}}
#
#             keys1 = json.dumps(dictionary, indent=4)
#             with open(main_path_data + "\\keys.json", "w") as outfile:
#                 outfile.write(keys1)
#                 outfile.close()
#                 pass
#
#     keys()
#
#     a_file = open(main_path_data + "\\keys.json", "r")
#     json_object = json.load(a_file)
#     a_file.close()
#
#     input1 = json_object["1"]['key']
#     input2 = json_object["1"]['api']
#
#     if input1 != "Api key" and input2 != "Api secret":
#         # Свой класс исключений
#         class ScriptError(Exception):
#             pass
#
#         class ScriptQuitCondition(Exception):
#             pass
#
#
#
#         print('direction  :', direction)
#         print('para  :', para)
#         print('amount  :', amount)
#         print('price  :', price)
#
#         order = {
#             'type': direction,
#             'pair': para,
#             'amount': str(amount),
#             'price': price
#         }
#
#         def get_auth_headers(self, data):
#             msg = input1 + urlencode(sorted(data.items(), key=lambda val: val[0]))
#             sign = hmac.new(input2.encode(), msg.encode(), digestmod='sha256').hexdigest()
#
#             return {
#                 'X-KEY': input1,
#                 'X-SIGN': sign,
#                 'X-NONCE': str(int(time() * 1000)),
#             }
#
#         response = requests.post('https://btc-alpha.com/api/v1/order/', data=order, headers=get_auth_headers({}, order))
#
#         def resm():
#             try:
#                 # Полученный ответ переводим в строку UTF, и пытаемся преобразовать из текста в объект Python
#                 obj = json.loads(response.text)
#                 # Смотрим, есть ли в полученном объекте ключ "error"
#                 if 'error' in obj and obj['error']:
#                     return obj['error']
#                     # Если есть, выдать ошибку, код дальше выполняться не будет
#                     # raise ScriptError(obj['error'])
#                 # Вернуть полученный объект как результат работы ф-ции
#                 return obj['success']
#             except ValueError:
#                 # Если не удалось перевести полученный ответ (вернулся не JSON)
#                 return ScriptError('Ошибка анализа возвращаемых данных, получена строка', response)
#                 # raise ScriptError('Ошибка анализа возвращаемых данных, получена строка', response)
#
#         return resm()
#
#     else:
#         return ["ОШИБКА"]



d ={'0.02024': ('0', 1592053614338),
 '0.02025': ('0', 1592053587720),
 '0.02027': ('0', 1592053572033),
 '0.02056': ('55.72345257', 1592051462224),
 '0.02098': ('4E+2', 1592046463930),
 '0.01946': ('0', 1592053652180),
 '0.01956': ('0', 1592053719849),
 '0.02023': ('0', 1592053691936),
 '0.02022': ('0', 1592053720441),
 '0.02021': ('0', 1592053723886),
 '0.0202': ('0', 1592053825274),
 '0.02019': ('0', 1592054046907),
 '0.02018': ('0', 1592054051851),
 '0.0218': ('0', 1592054048985),
 '0.02017': ('6678.53657432', 1592054171205),
 '0.02112': ('0', 1592054170579),
 '0.02016': ('16830.3139726', 1592054219586),
 '0.02203000': ('373.26628222', 1591954925735),
 '0.02800000': ('3707.80698048', 1592054220162),
 '0.02015': ('0', 1592054291677),
 '0.02014': ('132.0561811', 1592054345555),
 '0.02013': ('0', 1592054428417),
 '0.02012': ('0', 1592054536930),
 '0.02011': ('0', 1592054671428),
 '0.0201': ('2013.77114572', 1592054778570)}