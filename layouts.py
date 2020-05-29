import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
import uuid
import pandas as pd
import dash_table
from app import dash_app
import os
import json
import test_order
import New_chains


main_path_data = os.path.abspath("./data")

my_col=['TIME', 'birga_x', 'birga_y', 'rates_x', 'rates_y', 'valin_x', 'valin_y', 'valout_y', 'volume_x',
                 'volume_y', 'start', 'step', 'back', 'profit', 'perc', 'volume']
if os.path.isfile(main_path_data + "\\all_data.csv"):
    final2 = pd.read_csv(main_path_data + "\\all_data.csv")
    if final2.shape[0] > 0:
        final2['rates_y'] = final2['rates_y'].map('{:,.2f}'.format)
        final2['rates_x'] = final2['rates_x'].map('{:,.2f}'.format)
        final2['start'] = final2['start'].map('{:,.6f}'.format)
        final2['step'] = final2['step'].map('{:,.6f}'.format)
        final2['back'] = final2['back'].map('{:,.6f}'.format)
        final2['profit'] = final2['profit'].map('{:,.6f}'.format)
        final2['perc'] = final2['perc'].map('{:,.3f}%'.format)
    else:
        pass


    pass
else:
    final2 = pd.DataFrame(columns=my_col)
    final2.to_csv(main_path_data + "\\all_data.csv", header=True)
    pass

f = open(main_path_data + "\\commis.json")
com = json.load(f)


########  MAIN PAGE MY  ##############

def keys():
    if os.path.isfile(main_path_data + "\\keys.json"):
        pass
    else:

        dictionary = {"1": {"key": "BtuWYH7DbtNLREeRUdfjfAxEiS71Lq6Wn2kyyoxS9zkiiVo2HtvZUg1CaMdJiuRHDUum9HutR",
                            "api": "4Bmhw5cz4f5QzoXt8XbnEMwoapYFirS6ozkD11Q7RiuYg7DidgTdnJLf8MUU8Bb6YAL5D5m65uvBR4JTavip5uA6"},
                      "2": {"key": "gT5fA5uh2f3vbkYxprGU6UYmQxD7uQA4",
                            "api": "dV3dGBU6zC85WE53ezNBZSKRVTkA8hxG"},
                      "3": {"key": "7df7baa8-ae73-ddd1-2e8f6968ed3d5a89",
                            "api": "37dfc47b7ef13b296f7011dad71a5775"},
                      "4": {"key": "Chat id", "api": "Token"}}

        keys1 = json.dumps(dictionary, indent=4)
        # print(' JSON DOESNT EXIST :', keys1)
        # Writing to sample.json
        with open(main_path_data + "\\keys.json", "w") as outfile:
            outfile.write(keys1)
            outfile.close()
            pass

def tab_keys():


    a_file = open(main_path_data + "\\keys.json", "r")
    keys8 = json.load(a_file)
    a_file.close()

    # print(' JSON EXISTS :', keys8)

    tab_keys = [ddk.Card(style={'width': '50%', 'margin': '5px', 'background-color': '#e4e7e7a6'},
                         card_hover=True,
                         children=ddk.Block(width=100,
                                            style={'justify-content': 'center'},
                                            children=[
                                                ddk.Block(width=20,
                                                          children=html.H2('btc-Alpha',
                                                                           style={
                                                                               'text-align': 'center',
                                                                               'justify': 'center'})),
                                                ddk.Block(width=50,
                                                          children=[ddk.Block(width=100,
                                                                              children=dcc.Input(
                                                                                  placeholder=keys8["1"]['key'],
                                                                                  id={
                                                                                      'type': 'key',
                                                                                      'index': '1'
                                                                                  },
                                                                                  style={
                                                                                      'border': 'double',
                                                                                      'margin': '0',
                                                                                      'background-color': 'ivory',
                                                                                      'width': '-webkit-fill-available'})),
                                                                    ddk.Block(width=100,
                                                                              children=dcc.Input(
                                                                                  placeholder=keys8["1"]['api'],
                                                                                  id={
                                                                                      'type': 'api',
                                                                                      'index': '1'
                                                                                  },
                                                                                  style={
                                                                                      'border': 'double',
                                                                                      'margin': '0',
                                                                                      'background-color': 'ivory',
                                                                                      'width': '-webkit-fill-available'}))]),
                                                ddk.Block(width=30,
                                                          children=html.Button('Сохранить',
                                                                               id={
                                                                                   'type': 'save_btn',
                                                                                   'index': '1'
                                                                               },
                                                                               style={
                                                                                   'text-align': 'center',
                                                                                   'justify': 'center'})),
                                            ])),

                ddk.Card(style={'width': '50%', 'margin': '5px', 'background-color': '#e4e7e7a6'},
                         card_hover=True,
                         children=ddk.Block(width=100,
                                            style={'justify-content': 'center'},
                                            children=[ddk.Block(width=20, children=html.H2('Livecoin',
                                                                                           style={
                                                                                               'text-align': 'center',
                                                                                               'justify': 'center'})),
                                                      ddk.Block(width=50,
                                                                children=[ddk.Block(width=100,
                                                                                    children=dcc.Input(
                                                                                        placeholder=keys8["2"]['key'],
                                                                                        id={
                                                                                            'type': 'key',
                                                                                            'index': '2'
                                                                                        },
                                                                                        style={
                                                                                            'border': 'double',
                                                                                            'margin': '0',
                                                                                            'background-color': 'ivory',
                                                                                            'width': '-webkit-fill-available'})),
                                                                          ddk.Block(width=100,
                                                                                    children=dcc.Input(
                                                                                        placeholder=keys8["2"]['api'],
                                                                                        id={
                                                                                            'type': 'api',
                                                                                            'index': '2'
                                                                                        },
                                                                                        style={
                                                                                            'border': 'double',
                                                                                            'margin': '0',
                                                                                            'background-color': 'ivory',
                                                                                            'width': '-webkit-fill-available'}))]),
                                                      ddk.Block(width=30,
                                                                children=html.Button('Сохранить',
                                                                                     id={
                                                                                         'type': 'save_btn',
                                                                                         'index': '2'
                                                                                     },
                                                                                     style={
                                                                                         'text-align': 'center',
                                                                                         'justify': 'center'})),
                                                      ])),
                ddk.Card(style={'width': '50%', 'margin': '5px', 'background-color': '#e4e7e7a6'},
                         card_hover=True,
                         children=ddk.Block(width=100,
                                            style={'justify-content': 'center'},
                                            children=[ddk.Block(width=20, children=html.H2('Hotbit',
                                                                                           style={
                                                                                               'text-align': 'center',
                                                                                               'justify': 'center'})),
                                                      ddk.Block(width=50,
                                                                children=[ddk.Block(width=100,
                                                                                    children=dcc.Input(
                                                                                        placeholder=keys8["3"]['key'],
                                                                                        id={
                                                                                            'type': 'key',
                                                                                            'index': '3'
                                                                                        },
                                                                                        style={
                                                                                            'border': 'double',
                                                                                            'margin': '0',
                                                                                            'background-color': 'ivory',
                                                                                            'width': '-webkit-fill-available'})),
                                                                          ddk.Block(width=100,
                                                                                    children=dcc.Input(
                                                                                        placeholder=keys8["3"]['api'],
                                                                                        id={
                                                                                            'type': 'api',
                                                                                            'index': '3'
                                                                                        },
                                                                                        style={
                                                                                            'border': 'double',
                                                                                            'margin': '0',
                                                                                            'background-color': 'ivory',
                                                                                            'width': '-webkit-fill-available'}))]),
                                                      ddk.Block(width=30,
                                                                children=html.Button('Сохранить',
                                                                                     id={
                                                                                         'type': 'save_btn',
                                                                                         'index': '3'
                                                                                     },
                                                                                     style={
                                                                                         'text-align': 'center',
                                                                                         'justify': 'center'})),
                                                      ])),
                ddk.Card(style={'width': '50%', 'margin': '5px', 'background-color': '#e4e7e7a6'},
                         card_hover=True, children=ddk.Block(width=100,
                                                             style={'justify-content': 'center'},
                                                             children=[ddk.Block(width=20,
                                                                                 children=html.H2(
                                                                                     'TELEGRAM')),
                                                                       ddk.Block(width=50, children=[
                                                                           ddk.Block(width=100,
                                                                                     children=dcc.Input(
                                                                                         placeholder=keys8["4"]['key'],
                                                                                         id={
                                                                                             'type': 'key',
                                                                                             'index': '4'
                                                                                         },
                                                                                         style={
                                                                                             'border': 'double',
                                                                                             'margin': '0',
                                                                                             'background-color': 'ivory',
                                                                                             'width': '-webkit-fill-available'})),
                                                                           ddk.Block(width=100,
                                                                                     children=dcc.Input(
                                                                                         placeholder=keys8["4"]['api'],
                                                                                         id={
                                                                                             'type': 'api',
                                                                                             'index': '4'
                                                                                         },
                                                                                         style={
                                                                                             'border': 'double',
                                                                                             'margin': '0',
                                                                                             'background-color': 'ivory',
                                                                                             'width': '-webkit-fill-available'}))]),
                                                                       ddk.Block(width=30,
                                                                                 children=html.Button(
                                                                                     'Сохранить',
                                                                                     id={
                                                                                         'type': 'save_btn',
                                                                                         'index': '4'
                                                                                     },
                                                                                     style={
                                                                                         'text-align': 'center',
                                                                                         'justify': 'center'})),
                                                                       ])),
                ddk.Card(style={'width': '50%', 'margin': '5px', 'background-color': '#e4e7e7a6'},
                         card_hover=True, children=ddk.Block(width=100,
                                                             style={'justify-content': 'center'},
                                                             children=[
                                                                 ddk.Block(width=100,
                                                                           children=[
                                                                               ddk.Block(width=20,
                                                                                         children=html.H2(
                                                                                             'Alpha Комиссия')),
                                                                               ddk.Block(width=20,
                                                                                         children=[
                                                                                             dcc.Input(
                                                                                                 id='Alpha_com',
                                                                                                 placeholder="1,002 = 0.2%",
                                                                                                 style={
                                                                                                     'border': 'double',
                                                                                                     'margin': '0',
                                                                                                     'background-color': 'ivory',
                                                                                                     'width': '-webkit-fill-available'})]),
                                                                               ddk.Block(width=25,
                                                                                         children=html.Button(
                                                                                             'Сохранить',
                                                                                             id='Alpha_btn')),
                                                                               ddk.Block(width=35,
                                                                                         children=html.Div(
                                                                                             id='output-alpha',
                                                                                             children=float(
                                                                                                 com[
                                                                                                     'main'][
                                                                                                     'alfa'])))
                                                                           ]),
                                                                 ddk.Block(width=100,
                                                                           children=[
                                                                               ddk.Block(width=20,
                                                                                         children=html.H2(
                                                                                             'LiveCoin Комиссия')),
                                                                               ddk.Block(width=20,
                                                                                         children=[
                                                                                             dcc.Input(
                                                                                                 id='Live_com',
                                                                                                 placeholder=" 1,002 = 0.2% ",
                                                                                                 style={
                                                                                                     'border': 'double',
                                                                                                     'margin': '0',
                                                                                                     'background-color': 'ivory',
                                                                                                     'width': '-webkit-fill-available'})]),
                                                                               ddk.Block(width=25,
                                                                                         children=html.Button(
                                                                                             'Сохранить',
                                                                                             id='LiveCoin_btn'),
                                                                                         ),
                                                                               ddk.Block(width=35,
                                                                                         children=html.Div(
                                                                                             id='output-live',
                                                                                             children=float(
                                                                                                 com[
                                                                                                     'main'][
                                                                                                     'live'])))
                                                                           ]),
                                                                 ddk.Block(width=100,
                                                                           children=[
                                                                               ddk.Block(width=20,
                                                                                         children=html.H2(
                                                                                             'HOTBIT Комиссия')),
                                                                               ddk.Block(width=20,
                                                                                         children=[
                                                                                             dcc.Input(
                                                                                                 id='Hot_com',
                                                                                                 placeholder="1,002 = 0.2%",
                                                                                                 style={
                                                                                                     'border': 'double',
                                                                                                     'margin': '0',
                                                                                                     'background-color': 'ivory',
                                                                                                     'width': '-webkit-fill-available'})]),
                                                                               ddk.Block(width=25,
                                                                                         children=html.Button(
                                                                                             'Сохранить',
                                                                                             id='Hot_btn')),
                                                                               ddk.Block(width=35,
                                                                                         children=html.Div(
                                                                                             id='output-hot',
                                                                                             children=float(
                                                                                                 com[
                                                                                                     'main'][
                                                                                                     'hot'])))
                                                                           ]),

                                                             ]))]


    return tab_keys

def group_of_regims():
    # main_path_data = os.path.abspath("./data")
    d = open(main_path_data + "\\regim.json")
    com2 = json.load(d)

    group_of_regims = []
    html.Div(id='hidden-div')

    param_head = ddk.Card(style={'width': '100%', 'line-height': '1',
                                 'height': '70px', 'margin': '0', 'max-height': 'fit-content',
                                 'background-color': '#fff'},
                          shadow_weight='heavy',
                          children=ddk.Block(width=100,
                                             style={'justify-content': 'center'},
                                             children=[ddk.Block(width=5,
                                                                 style={'vertical-align': '-webkit-baseline-middle'},
                                                                 children=html.H2('Active',
                                                                                  style={'margin': '0',
                                                                                         'text-align': 'center',
                                                                                         'justify': 'center'})),
                                                       ddk.Block(width=45,
                                                                 style={'vertical-align': '-webkit-baseline-middle'},
                                                                 children=[
                                                                     ddk.Block(width=33,
                                                                               children=html.H2('',
                                                                                                style={'margin': '0',
                                                                                                       'text-align': 'center',
                                                                                                       'justify': 'center'})),
                                                                     ddk.Block(width=33,
                                                                               children=html.H2('',
                                                                                                style={'margin': '0',
                                                                                                       'text-align': 'center',
                                                                                                       'justify': 'center'})),
                                                                     ddk.Block(width=33,
                                                                               children=html.H2('',
                                                                                                style={'margin': '0',
                                                                                                       'text-align': 'center',
                                                                                                       'justify': 'center'}))]),
                                                       ddk.Block(width=45,
                                                                 style={'vertical-align': '-webkit-baseline-middle'},
                                                                 children=html.H2('PARAMETERS',
                                                                                  style={'margin': '0',
                                                                                         'text-align': 'center',
                                                                                         'justify': 'center'})),
                                                       ddk.Block(width=5,
                                                                 style={'vertical-align': '-webkit-baseline-middle'},
                                                                 children=html.H2('Signal (on/off)',
                                                                                  style={'margin': '0',
                                                                                         'text-align': 'center',
                                                                                         'justify': 'center'}))]))

    group_of_regims.append(param_head)

    for k, v in com2.items():
        list_item = dbc.ListGroupItem(style={
            'line-height': '1', 'margin': '0', 'margin-right': '0',
            'height': 'fit-content', 'justify-content': 'center',
            'vertical-align': '-webkit-baseline-middle',
            'max-height': 'fit-content', 'padding': '0px',
            'list-style': 'none',
            'align-items': 'center'},
            children=ddk.Card(
                style={'width': '100%',
                       'margin': '0',
                       'margin-top': '10px',
                       'background-color': '#e4e7e7a6'},
                card_hover=True,
                children=ddk.Block(
                    id={
                        'type': 'rgm_block',
                        'index': k
                    },
                    width=100,
                    style={'justify-content': 'center',
                           'vertical-align': '-webkit-baseline-middle'},
                    children=[ddk.Block(width=5,
                                        style={'vertical-align': '-webkit-baseline-middle'},
                                        children=[html.H2(
                                            id={
                                                 'type': 'option',
                                                 'index': k
                                             },
                                            style={'margin': '0',
                                                'text-align': 'center',
                                                'vertical-align': '-webkit-baseline-middle',
                                                'justify-content': 'center'},
                                            children=[v['option']]),

                                            html.Button('Удалить',
                                                        style={'font-size':"8px", "max-width":"50px",
                                                               'padding': '1px',
                                                                'color': 'white',
                                                                'background-color': 'orangered',
                                                                'max-height': '30px',
                                                                'cursor': 'grab',
                                                               'margin-top': '10px',
                                                               'border-radius': '10px'
                                                                },
                                                        id={'type': 'delet_rgm_btn', 'index': k}),


                                                  ]),
                              ddk.Block(width=35,
                                        style={'vertical-align': '-webkit-baseline-middle'},
                                        children=[ddk.Block(width=100,
                                                            style={'vertical-align': '-webkit-baseline-middle'},
                                                            children=[ddk.Block(width=30,
                                                                                style={'margin': '5px'},
                                                                                children=
                                                                                dcc.Dropdown(
                                                                                    id={
                                                                                        'type': 'val1',
                                                                                        'index': k
                                                                                    },
                                                                                    style={
                                                                                        'background-color': '#fff'},
                                                                                    options=[
                                                                                        {'label': 'BTC',
                                                                                         'value': 'BTC'},
                                                                                        {'label': 'USD',
                                                                                         'value': 'USD'},
                                                                                        {'label': 'USDT',
                                                                                         'value': 'USDT'},
                                                                                        {'label': 'ETH',
                                                                                         'value': 'ETH'},
                                                                                        {'label': 'PZM',
                                                                                         'value': 'PZM'},

                                                                                    ],
                                                                                    value='{}'.format(v["val1"]))),

                                                                      ddk.Block(width=30,
                                                                                style={'margin': '5px'},
                                                                                children=
                                                                                dcc.Dropdown(
                                                                                    id={
                                                                                        'type': 'val2',
                                                                                        'index': k
                                                                                    },
                                                                                    style={
                                                                                        'background-color': '#fff'},
                                                                                    options=[
                                                                                        {'label': 'BTC',
                                                                                         'value': 'BTC'},
                                                                                        {'label': 'USD',
                                                                                         'value': 'USD'},
                                                                                        {'label': 'USDT',
                                                                                         'value': 'USDT'},
                                                                                        {'label': 'ETH',
                                                                                         'value': 'ETH'},
                                                                                        {'label': 'PZM',
                                                                                         'value': 'PZM'},
                                                                                    ],
                                                                                    value='{}'.format(v["val2"]))),
                                                                      ddk.Block(width=30,
                                                                                style={'margin': '5px'},
                                                                                children=dcc.Dropdown(
                                                                                    id={
                                                                                        'type': 'val3',
                                                                                        'index': k
                                                                                    },
                                                                                    style={
                                                                                        'background-color': '#fff'},
                                                                                    options=[
                                                                                        {'label': 'BTC',
                                                                                         'value': 'BTC'},
                                                                                        {'label': 'USD',
                                                                                         'value': 'USD'},
                                                                                        {'label': 'USDT',
                                                                                         'value': 'USDT'},
                                                                                        {'label': 'ETH',
                                                                                         'value': 'ETH'},
                                                                                        {'label': 'PZM',
                                                                                         'value': 'PZM'},
                                                                                    ],
                                                                                    value='{}'.format(v["val3"])))

                                                                      ]),
                                                  ddk.Block(width=100,
                                                            style={'vertical-align': '-webkit-baseline-middle'},
                                                            children=[
                                                                ddk.Block(width=40,
                                                                          style={'margin': '5px'},
                                                                          children=dcc.Dropdown(
                                                                              id={
                                                                                  'type': 'birga1',
                                                                                  'index': k
                                                                              },
                                                                              style={'background-color': '#fff'},
                                                                              placeholder="БИРЖА 1",
                                                                              options=[
                                                                                  {
                                                                                      'label': 'alfa',
                                                                                      'value': 'alfa'},
                                                                                  {
                                                                                      'label': 'hot',
                                                                                      'value': 'hot'},
                                                                                  {
                                                                                      'label': 'live',
                                                                                      'value': 'live'},

                                                                              ],
                                                                              value='{}'.format(v["birga1"]))),
                                                                ddk.Block(width=40,
                                                                          style={
                                                                              'margin': '5px'},
                                                                          children=dcc.Dropdown(
                                                                              id={
                                                                                  'type': 'birga2',
                                                                                  'index': k
                                                                              },
                                                                              placeholder="БИРЖА 2",
                                                                              style={'background-color': '#fff'},
                                                                              options=[
                                                                                  {
                                                                                      'label': 'alfa',
                                                                                      'value': 'alfa'},
                                                                                  {
                                                                                      'label': 'hot',
                                                                                      'value': 'hot'},
                                                                                  {
                                                                                      'label': 'live',
                                                                                      'value': 'live'},
                                                                              ],
                                                                              value='{}'.format(v["birga2"])))
                                                            ]),
                                                  ]),

                              ddk.Block(width=60,
                                        style={'vertical-align': '-webkit-baseline-middle'},
                                        children=[ddk.Block(width=100,
                                                            style={'vertical-align': '-webkit-baseline-middle'},
                                                            children=[ddk.Block(width=27,
                                                                                children=[
                                                                                    ddk.Block(
                                                                                        width=35,
                                                                                        style={
                                                                                            'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            html.H5('% profit',
                                                                                                    style={
                                                                                                        'text-align': 'right',
                                                                                                        'justify-content': 'center'})]),
                                                                                    ddk.Block(
                                                                                        width=65,
                                                                                        style={'text-align': 'left',
                                                                                               'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            dcc.Input(
                                                                                                value='{}'.format(v["profit"]),
                                                                                                id={
                                                                                                    'type': 'profit',
                                                                                                    'index': k
                                                                                                },
                                                                                                placeholder=v[
                                                                                                    'profit'],
                                                                                                style={
                                                                                                    'border': 'double',
                                                                                                    'margin': '0',
                                                                                                    'text-align': 'left',
                                                                                                    'background-color': 'ivory',
                                                                                                    'width': '-webkit-fill-available',
                                                                                                    })])]),
                                                                      ddk.Block(width=27,
                                                                                children=[
                                                                                    ddk.Block(
                                                                                        width=35, style={
                                                                                            'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            html.H5(
                                                                                                'V ордера',
                                                                                                style={
                                                                                                    'text-align': 'right',
                                                                                                    'justify-content': 'center'})]),
                                                                                    ddk.Block(
                                                                                        width=65,
                                                                                        style={'text-align': 'left',
                                                                                               'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            dcc.Input(
                                                                                                value='{}'.format(
                                                                                                    v["order"]),
                                                                                                placeholder=v[
                                                                                                    'order'],
                                                                                                id={
                                                                                                    'type': 'order',
                                                                                                    'index': k
                                                                                                },
                                                                                                style={
                                                                                                    'border': 'double',
                                                                                                    'margin': '0',
                                                                                                    'text-align': 'left',
                                                                                                    'background-color': 'ivory',
                                                                                                    'width': '-webkit-fill-available',
                                                                                                    })])]),
                                                                      ddk.Block(width=27,
                                                                                children=[
                                                                                    ddk.Block(
                                                                                        width=35, style={
                                                                                            'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            html.H5(
                                                                                                '% ордера',
                                                                                                style={
                                                                                                    'text-align': 'right',
                                                                                                    'justify-content': 'center'})]),
                                                                                    ddk.Block(
                                                                                        width=65,
                                                                                        style={'text-align': 'left',
                                                                                               'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            dcc.Input(
                                                                                                value='{}'.format(
                                                                                                    v["per"]),
                                                                                                placeholder=v['per'],
                                                                                                id={
                                                                                                    'type': 'percent',
                                                                                                    'index': k
                                                                                                },
                                                                                                style={
                                                                'border': 'double',
                                                                'text-align': 'left',
                                                                'margin': '0',
                                                                'background-color': 'ivory',
                                                                'width': '-webkit-fill-available',
                                                                })])]),
                                                                      ddk.Block(width=30,
                                                                                style={'margin': '2px'},
                                                                                children=
                                                                                dcc.Dropdown(
                                                                                    id={
                                                                                        'type': 'avtomat',
                                                                                        'index': k
                                                                                    },
                                                                                    style={
                                                                                        'background-color': '#fff'},
                                                                                    options=[
                                                                                        {'label': 'off',
                                                                                         'value': 'off'},
                                                                                        {'label': 'on',
                                                                                         'value': 'on'}
                                                                                    ],
                                                                                    value='{}'.format(v["avtomat"]))),
                                                                      ddk.Block(width=20,
                                                                                style={'margin-left':'30px'},
                                                                                children=[

                                                                dcc.Checklist(
                                                                    id={
                                                                    'type': 'checklist',
                                                                    'index': k
                                                                },
                                                                options=[
                                                                    {"label": "on/off",
                                                                     "value": "active"},
                                                                ],
                                                                value=[],
                                                                # style={"display": "inline"},
                                                                # labelStyle={"display": "inline"}

                                                                )

                                                                                ])]),
                                                  ddk.Block(width=100,
                                                            style={'margin-top': '5px',
                                                                   'margin-bottom': '5px',
                                                                   'vertical-align': '-webkit-baseline-middle',
                                                                   'border-top-style': 'groove',
                                                                   'border-bottom-style': 'groove'},
                                                            children=[
                                                                ddk.Block(width=100,
                                                                          style={
                                                                              'vertical-align': '-webkit-baseline-middle'},
                                                                          children=[ddk.Block(
                                                                              width=30,
                                                                              children=[
                                                                                  ddk.Block(
                                                                                      width=50,
                                                                                      style={
                                                                                          'vertical-align': '-webkit-baseline-middle'},
                                                                                      children=[
                                                                                          html.H5(
                                                                                              '% profit',
                                                                                              style={
                                                                                                  'text-align': 'right',
                                                                                                  'justify-content': 'center'})]),
                                                                                  ddk.Block(
                                                                                      width=50,
                                                                                      style={
                                                                                          'text-align': 'left',
                                                                                          'vertical-align': '-webkit-baseline-middle'},
                                                                                      children=[
                                                                                          dcc.Input(
                                                                                              style={
                                                                                                  'border': 'double',
                                                                                                  'margin': '0',
                                                                                                  'text-align': 'left',
                                                                                                  'background-color': 'ivory',
                                                                                                  'width': '-webkit-fill-available',
                                                                                                  })])]),
                                                                              ddk.Block(
                                                                                  width=30,
                                                                                  children=[
                                                                                      ddk.Block(
                                                                                          width=50,
                                                                                          style={
                                                                                              'vertical-align': '-webkit-baseline-middle'},
                                                                                          children=[
                                                                                              html.H5(
                                                                                                  'V ордера',
                                                                                                  style={
                                                                                                      'text-align': 'right',
                                                                                                      'justify-content': 'center'})]),
                                                                                      ddk.Block(
                                                                                          width=50,
                                                                                          style={
                                                                                              'text-align': 'left',
                                                                                              'vertical-align': '-webkit-baseline-middle'},
                                                                                          children=[
                                                                                              dcc.Input(
                                                                                                  style={
                                                                                                      'border': 'double',
                                                                                                      'margin': '0',
                                                                                                      'text-align': 'left',
                                                                                                      'background-color': 'ivory',
                                                                                                      'width': '-webkit-fill-available',
                                                                                                      })])]),
                                                                              ddk.Block(
                                                                                  width=30,
                                                                                  children=[
                                                                                      ddk.Block(
                                                                                          width=50,
                                                                                          style={
                                                                                              'vertical-align': '-webkit-baseline-middle'},
                                                                                          children=[
                                                                                              html.H5(
                                                                                                  '% ордера',
                                                                                                  style={
                                                                                                      'text-align': 'right',
                                                                                                      'justify-content': 'center'})]),
                                                                                      ddk.Block(
                                                                                          width=50,
                                                                                          style={
                                                                                              'text-align': 'left',
                                                                                              'vertical-align': '-webkit-baseline-middle'},
                                                                                          children=[
                                                                                              dcc.Input(
                                                                                                  style={
                                                                                                      'border': 'double',
                                                                                                      'text-align': 'left',
                                                                                                      'margin': '0',
                                                                                                      'background-color': 'ivory',
                                                                                                      'width': '-webkit-fill-available',
                                                                                                      })])]),
                                                                              ddk.Block(
                                                                                  width=10,
                                                                                  children=[])]),
                                                                ddk.Block(width=100,
                                                                          style={
                                                                              'vertical-align': '-webkit-baseline-middle'},
                                                                          children=[ddk.Block(width=30,
                                                                                              style={
                                                                                                  'margin-top': '5px',
                                                                                                  'margin-bottom': '5px'},
                                                                                              children=[
                                                                                                  ddk.Block(
                                                                                                      width=50,
                                                                                                      style={
                                                                                                          'vertical-align': '-webkit-baseline-middle'},
                                                                                                      children=[
                                                                                                          html.H5(
                                                                                                              'секунд',
                                                                                                              style={
                                                                                                                  'text-align': 'right',
                                                                                                                  'justify-content': 'center'})]),
                                                                                                  ddk.Block(
                                                                                                      width=50,
                                                                                                      style={
                                                                                                          'text-align': 'left',
                                                                                                          'vertical-align':
                                                                                                              '-webkit-baseline-middle'},
                                                                                                      children=[
                                                                                                          dcc.Input(
                                                                                                              style={
                                                                                                                  'border': 'double',
                                                                                                                  'margin': '0',
                                                                                                                  'text-align': 'left',
                                                                                                                  'background-color': 'ivory',
                                                                                                                  'width': '-webkit-fill-available',
                                                                                                                  })])]),
                                                                                    ddk.Block(width=30,
                                                                                              style={
                                                                                                  'margin-top': '5px',
                                                                                                  'margin-bottom': '5px'},
                                                                                              children=[
                                                                                                  ddk.Block(
                                                                                                      width=50,
                                                                                                      style={
                                                                                                          'vertical-align': '-webkit-baseline-middle'},
                                                                                                      children=[
                                                                                                          html.H5(
                                                                                                              '1я Ставка (%)',
                                                                                                              style={
                                                                                                                  'text-align': 'right',
                                                                                                                  'justify-content': 'center'})]),
                                                                                                  ddk.Block(
                                                                                                      width=50,
                                                                                                      style={
                                                                                                          'text-align': 'left',
                                                                                                          'vertical-align': '-webkit-baseline-middle'},
                                                                                                      children=[
                                                                                                          dcc.Input(
                                                                                                              style={
                                                                                                                  'border': 'double',
                                                                                                                  'margin': '0',
                                                                                                                  'text-align': 'left',
                                                                                                                  'background-color': 'ivory',
                                                                                                                  'width': '-webkit-fill-available',
                                                                                                                  })])]),
                                                                                    ddk.Block(width=30,
                                                                                              style={
                                                                                                  'margin-top': '5px',
                                                                                                  'margin-bottom': '5px'},
                                                                                              children=[
                                                                                                  ddk.Block(
                                                                                                      width=50,
                                                                                                      style={
                                                                                                          'vertical-align': '-webkit-baseline-middle'},
                                                                                                      children=[
                                                                                                          html.H5(
                                                                                                              '2я Ставка (%)',
                                                                                                              style={
                                                                                                                  'text-align': 'right',
                                                                                                                  'justify-content': 'center'})]),
                                                                                                  ddk.Block(
                                                                                                      width=50,
                                                                                                      style={
                                                                                                          'text-align': 'left',
                                                                                                          'vertical-align': '-webkit-baseline-middle'},
                                                                                                      children=[
                                                                                                          dcc.Input(
                                                                                                              style={
                                                                                                                  'border': 'double',
                                                                                                                  'text-align': 'left',
                                                                                                                  'margin': '0',
                                                                                                                  'background-color': 'ivory',
                                                                                                                  'width': '-webkit-fill-available',
                                                                                                                  })])]),
                                                                                    ddk.Block(width=10,
                                                                                              style={
                                                                                                  'margin-top': '5px',
                                                                                                  'margin-bottom': '5px'},
                                                                                              children=[
                                                                                                  dbc.Checklist(
                                                                                                      style={
                                                                                                          'text-align': 'center',
                                                                                                          'border': '#333',
                                                                                                          'vertical-align': '-webkit-baseline-middle',
                                                                                                          'justify-content': 'center'},
                                                                                                      options=[
                                                                                                          {
                                                                                                              "label": "Off",
                                                                                                              "value": 1}
                                                                                                      ],
                                                                                                      value=[],
                                                                                                      id="checklist-r2-input{}".format(
                                                                                                          k),
                                                                                                      inline=True)

                                                                                              ])])
                                                            ]),
                                                  ddk.Block(width=100,
                                                            style={'vertical-align': '-webkit-baseline-middle'},
                                                            children=[ddk.Block(width=30,
                                                                                children=[
                                                                                    ddk.Block(
                                                                                        width=50, style={
                                                                                            'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            html.H5(
                                                                                                '% profit',
                                                                                                style={
                                                                                                    'text-align': 'right',
                                                                                                    'justify-content': 'center'})]),
                                                                                    ddk.Block(
                                                                                        width=50,
                                                                                        style={'text-align': 'left',
                                                                                               'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            dcc.Input(
                                                                                                style={
                                                                                                    'border': 'double',
                                                                                                    'margin': '0',
                                                                                                    'text-align': 'left',
                                                                                                    'background-color': 'ivory',
                                                                                                    'width': '-webkit-fill-available',
                                                                                                    })])]),
                                                                      ddk.Block(width=30,
                                                                                children=[
                                                                                    ddk.Block(
                                                                                        width=50, style={
                                                                                            'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            html.H5(
                                                                                                'V ордера',
                                                                                                style={
                                                                                                    'text-align': 'right',
                                                                                                    'justify-content': 'center'})]),
                                                                                    ddk.Block(
                                                                                        width=50,
                                                                                        style={'text-align': 'left',
                                                                                               'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            dcc.Input(
                                                                                                style={
                                                                                                    'border': 'double',
                                                                                                    'margin': '0',
                                                                                                    'text-align': 'left',
                                                                                                    'background-color': 'ivory',
                                                                                                    'width': '-webkit-fill-available',
                                                                                                    })])]),
                                                                      ddk.Block(width=30,
                                                                                children=[
                                                                                    ddk.Block(
                                                                                        width=50, style={
                                                                                            'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            html.H5(
                                                                                                '% ордера',
                                                                                                style={
                                                                                                    'text-align': 'right',
                                                                                                    'justify-content': 'center'})]),
                                                                                    ddk.Block(
                                                                                        width=50,
                                                                                        style={'text-align': 'left',
                                                                                               'vertical-align': '-webkit-baseline-middle'},
                                                                                        children=[
                                                                                            dcc.Input(
                                                                                                style={
                                                                                                    'border': 'double',
                                                                                                    'text-align': 'left',
                                                                                                    'margin': '0',
                                                                                                    'background-color': 'ivory',
                                                                                                    'width': '-webkit-fill-available',
                                                                                                    })])]),
                                                                      ddk.Block(width=10,
                                                                                children=[dbc.Checklist(
                                                                                    style={'text-align': 'center',
                                                                                           'border': '#333',
                                                                                           'vertical-align': '-webkit-baseline-middle',
                                                                                           'justify-content': 'center'},
                                                                                    options=[
                                                                                        {"label": "Off",
                                                                                         "value": 1}
                                                                                    ],
                                                                                    value=[],
                                                                                    id="checklist-r3-input{}".format(
                                                                                        k),
                                                                                    inline=True)

                                                                                ])])]
                                        )])))

        group_of_regims.append(list_item)
    return group_of_regims

def serve_layout():

    # print(tab_keys())

    session_id = str(uuid.uuid1())
    # store the session id in a dcc.Store component (invisible component for storing data)
    store_session_id_div = dcc.Store(id='session_id_div_id',
                                     storage_type='session',  # IMPORTANT! see docstring of dcc.Store
                                     data=session_id)

    interval = dcc.Interval(id='interval', interval=1000, n_intervals=0)

    valuta = pd.read_csv(main_path_data + "\\balance.csv")


#     alfa_card = ddk.Card(width=30,
#                          style={'background-color': '#fff', 'max-height': '30vh', 'overflowY':'scroll'},
#                          shadow_weight='heavy',
#                          children=[ddk.Block(width=100,
#                                              style={'margin':'0'},
#                                              children=dbc.ListGroup([
#                                                  dbc.ListGroupItem(style={'line-height': '1',
#                                                                   'margin': '0', 'margin-right': '0',
#                                                                    'justify-content': 'center',
#                                                                    'vertical-align': '-webkit-baseline-middle',
#                                                                    'max-height': 'fit-content', 'padding': '0px',
#                                                                    'list-style': 'none',
#                                                                    'align-items': 'center'},
#                                                                    active=True,
#                                                                    action=True,
#                                                                    children= ddk.Block(width=100,
#                                                                    children=[ddk.Block(width=20,
#                                                                             children=[html.P('Время')]),
#                                                                   ddk.Block(width=20,
#                                                                             children=[html.P('ПАРА')]),
#                                                                   ddk.Block(width=15,
#                                                                             children=[html.P('Направление')]),
#                                                                   ddk.Block(width=15,
#                                                                             children=[html.P('Цена')]),
#                                                                   ddk.Block(width=15,
#                                                                             children=[html.P('Количество')]),
#                                                                   ddk.Block(width=15,
#                                                                             children=[html.P('Стоимость')])])),
#                              dbc.ListGroupItem(style={'line-height': '1',
#                                                       'margin': '0',
#                                                       'margin-right': '0',
#                'justify-content': 'center',
#                'vertical-align': '-webkit-baseline-middle',
#                'max-height': 'fit-content', 'padding': '0px',
#                'list-style': 'none',
#                'align-items': 'center'},
#                                                action=True,
#                                                children=ddk.Block(width=100,
#                                                                   children=[ddk.Block(width=20,
#                                                                 children=[html.P('08:54:40')]),
#                                                       ddk.Block(width=20,
#                                                                 children=[html.P('USD/USDT')]),
#                                                       ddk.Block(width=15,
#                                                                 children=[html.P('sell')]),
#                                                       ddk.Block(width=15,
#                                                                 children=[html.P('0,99400000')]),
#                                                       ddk.Block(width=15,
#                                                                 children=[html.P('5,04100000')]),
#                                                       ddk.Block(width=15,
#                                                                 children=[html.P('5,01075400')])])),
#                                                  dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
#                'justify-content': 'center',
#                'vertical-align': '-webkit-baseline-middle',
#                'max-height': 'fit-content', 'padding': '0px',
#                'list-style': 'none',
#                'align-items': 'center'},action=True,
#                                                                    children=ddk.Block(width=100,
#                                                                             children=[ddk.Block(width=20,
#                                                                                                 children=[html.P('08:54:40')]),
#                                                                                       ddk.Block(width=20,
#                                                                                                 children=[html.P('USD/USDT')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('sell')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('0,99400000')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('5,04100000')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('5,01075400')])])),
#                                                  dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
#                'justify-content': 'center',
#                'vertical-align': '-webkit-baseline-middle',
#                'max-height': 'fit-content', 'padding': '0px',
#                'list-style': 'none',
#                'align-items': 'center'},action=True,
#                                                                    children=ddk.Block(width=100,
#                                                         children=[ddk.Block(width=20,
#                                                                             children=[html.P('08:54:40')]),
#                                                                   ddk.Block(width=20,
#                                                                             children=[html.P('USD/USDT')]),
#                                                                   ddk.Block(width=15,
#                                                                             children=[html.P('sell')]),
#                                                                   ddk.Block(width=15,
#                                                                             children=[html.P('0,99400000')]),
#                                                                   ddk.Block(width=15,
#                                                                             children=[html.P('5,04100000')]),
#                                                                   ddk.Block(width=15,
#                                                                             children=[html.P('5,01075400')])])),
#                              dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
# 'justify-content': 'center',
# 'vertical-align': '-webkit-baseline-middle',
# 'max-height': 'fit-content', 'padding': '0px',
# 'list-style': 'none',
# 'align-items': 'center'},action=True,
#                                                children=ddk.Block(width=100,
#                                                         children=[ddk.Block(width=20,
#                                                                             children=[html.P('08:54:40')]),
#                                                                   ddk.Block(width=20,
#                                                                             children=[html.P('USD/USDT')]),
#                                                                   ddk.Block(width=15,
#                                                                             children=[html.P('sell')]),
#                                                                   ddk.Block(width=15,
#                                                                             children=[html.P('0,99400000')]),
#                                                                   ddk.Block(width=15,
#                                                                             children=[html.P('5,04100000')]),
#                                                                   ddk.Block(width=15,
#                                                                             children=[html.P('5,01075400')])])),
#                              dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
# 'justify-content': 'center',
# 'vertical-align': '-webkit-baseline-middle',
# 'max-height': 'fit-content', 'padding': '0px',
# 'list-style': 'none',
# 'align-items': 'center'},action=True,
#                                                children=ddk.Block(width=100,
#                                                         children=[ddk.Block(width=20,
#                                                                             children=[html.P('08:54:40')]),
#                                                                   ddk.Block(width=20,
#                                                                             children=[html.P('USD/USDT')]),
#                                                                   ddk.Block(width=15,
#                                                                             children=[html.P('sell')]),
#                                                                   ddk.Block(width=15,
#                                                                             children=[html.P('0,99400000')]),
#                                                                   ddk.Block(width=15,
#                                                                             children=[html.P('5,04100000')]),
#                                                                   ddk.Block(width=15,
#                                                                             children=[html.P('5,01075400')])])),
#                              dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
# 'justify-content': 'center',
# 'vertical-align': '-webkit-baseline-middle',
# 'max-height': 'fit-content', 'padding': '0px',
# 'list-style': 'none',
# 'align-items': 'center'},action=True,
#                                                children=ddk.Block(width=100,
#                                                         children=[ddk.Block(width=20,
#                                                                             children=[html.P('08:54:40')]),
#                                                                   ddk.Block(width=20,
#                                                                             children=[html.P('USD/USDT')]),
#                                                                   ddk.Block(width=15,
#                                                                             children=[html.P('sell')]),
#                                                                   ddk.Block(width=15,
#                                                                             children=[html.P('0,99400000')]),
#                                                                   ddk.Block(width=15,
#                                                                             children=[html.P('5,04100000')]),
#                                                                   ddk.Block(width=15,
#                                                                             children=[html.P('5,01075400')])])),
#
#                                                 ]))
#                                    ])
#     live_card = ddk.Card(width=30,
#                          style={'background-color': '#fff', 'max-height': '30vh', 'overflowY':'scroll'},
#                          shadow_weight='heavy',
#                          children=[ddk.Block(width=100,
#                                              style={'margin':'0px'},
#                                              children=dbc.ListGroup([
#                                                  dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
#                'justify-content': 'center',
#                'vertical-align': '-webkit-baseline-middle', 'max-width': '-webkit-fill-available',
#                'max-height': 'fit-content', 'padding': '0px',
#                'list-style': 'none',
#                'align-items': 'center'},
#                                                                    active=True,
#                                                                    action=True,
#                                                                    children= ddk.Block(width=100,
#                                                                            children=[ddk.Block(width=20,
#                                                                                     children=[html.P('Время')]),
#                                                                           ddk.Block(width=20,
#                                                                                     children=[html.P('ПАРА')]),
#                                                                           ddk.Block(width=15,
#                                                                                     children=[html.P('Направление')]),
#                                                                           ddk.Block(width=15,
#                                                                                     children=[html.P('Цена')]),
#                                                                           ddk.Block(width=15,
#                                                                                     children=[html.P('Количество')]),
#                                                                           ddk.Block(width=15,
#                                                                                     children=[html.P('Стоимость')])])),
#                                                  dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
#                'justify-content': 'center', 'max-width': '-webkit-fill-available',
#                'vertical-align': '-webkit-baseline-middle',
#                'max-height': 'fit-content', 'padding': '0px',
#                'list-style': 'none',
#                'align-items': 'center'},action=True,
#                                                                    children=ddk.Block(width=100,
#                                                                             children=[ddk.Block(width=20,
#                                                                                                 children=[html.P('08:54:40')]),
#                                                                                       ddk.Block(width=20,
#                                                                                                 children=[html.P('USD/USDT')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('sell')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('0,99400000')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('5,04100000')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('5,01075400')])])),
#                                                  dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
#                'justify-content': 'center',
#                'vertical-align': '-webkit-baseline-middle', 'max-width': '-webkit-fill-available',
#                'max-height': 'fit-content', 'padding': '0px',
#                'list-style': 'none',
#                'align-items': 'center'},action=True,
#                                                                    children=ddk.Block(width=100,
#                                                                             children=[ddk.Block(width=20,
#                                                                                                 children=[html.P('08:54:40')]),
#                                                                                       ddk.Block(width=20,
#                                                                                                 children=[html.P('USD/USDT')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('sell')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('0,99400000')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('5,04100000')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('5,01075400')])])),
#                                                  dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
#                'justify-content': 'center',
#                'vertical-align': '-webkit-baseline-middle', 'max-width': '-webkit-fill-available',
#                'max-height': 'fit-content', 'padding': '0px',
#                'list-style': 'none',
#                'align-items': 'center'},action=True,
#                                                                    children=ddk.Block(width=100,
#                                                                             children=[ddk.Block(width=20,
#                                                                                                 children=[html.P('08:54:40')]),
#                                                                                       ddk.Block(width=20,
#                                                                                                 children=[html.P('USD/USDT')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('sell')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('0,99400000')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('5,04100000')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('5,01075400')])])),
#                                                  dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
#                'justify-content': 'center',
#                'vertical-align': '-webkit-baseline-middle', 'max-width': '-webkit-fill-available',
#                'max-height': 'fit-content', 'padding': '0px',
#                'list-style': 'none',
#                'align-items': 'center'},action=True,
#                                                                    children=ddk.Block(width=100,
#                                                                             children=[ddk.Block(width=20,
#                                                                                                 children=[html.P('08:54:40')]),
#                                                                                       ddk.Block(width=20,
#                                                                                                 children=[html.P('USD/USDT')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('sell')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('0,99400000')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('5,04100000')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('5,01075400')])])),
#                                                  dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
#                'justify-content': 'center',
#                'vertical-align': '-webkit-baseline-middle', 'max-width': '-webkit-fill-available',
#                'max-height': 'fit-content', 'padding': '0px',
#                'list-style': 'none',
#                'align-items': 'center'},action=True,
#                                                                    children=ddk.Block(width=100,
#                                                                             children=[ddk.Block(width=20,
#                                                                                                 children=[html.P('08:54:40')]),
#                                                                                       ddk.Block(width=20,
#                                                                                                 children=[html.P('USD/USDT')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('sell')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('0,99400000')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('5,04100000')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('5,01075400')])])),
#                                                  dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
#                'justify-content': 'center',
#                'vertical-align': '-webkit-baseline-middle', 'max-width': '-webkit-fill-available',
#                'max-height': 'fit-content', 'padding': '0px',
#                'list-style': 'none',
#                'align-items': 'center'},action=True,
#                                                                    children=ddk.Block(width=100,
#                                                                             children=[ddk.Block(width=20,
#                                                                                                 children=[html.P('08:54:40')]),
#                                                                                       ddk.Block(width=20,
#                                                                                                 children=[html.P('USD/USDT')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('sell')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('0,99400000')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('5,04100000')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('5,01075400')])])),
#
#                                                 ]))
#                                    ])
#     hotbit_card = ddk.Card(width=30,
#                          style={'background-color': '#fff', 'max-height': '30vh', 'overflowY':'scroll'},
#                          shadow_weight='heavy',
#                          children=[ddk.Block(width=100,
#                                              style={'margin':'0px'},
#                                              children=dbc.ListGroup([
#                                                  dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
#                'justify-content': 'center',
#                'vertical-align': '-webkit-baseline-middle', 'max-width': '-webkit-fill-available',
#                'max-height': 'fit-content', 'padding': '0px',
#                'list-style': 'none',
#                'align-items': 'center'},
#                                                                    active=True,
#                                                                    action=True,
#                                                                    children= ddk.Block(width=100,
#                                                                                        children=[ddk.Block(width=20,
#                                                                                                 children=[html.P('Время')]),
#                                                                                       ddk.Block(width=20,
#                                                                                                 children=[html.P('ПАРА')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('Направление')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('Цена')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('Количество')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('Стоимость')])])),
#                                                  dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
#                'justify-content': 'center', 'max-width': '-webkit-fill-available',
#                'vertical-align': '-webkit-baseline-middle',
#                'max-height': 'fit-content', 'padding': '0px',
#                'list-style': 'none',
#                'align-items': 'center'},action=True,
#                                                                    children=ddk.Block(width=100,
#                                                                             children=[ddk.Block(width=20,
#                                                                                                 children=[html.P('08:54:40')]),
#                                                                                       ddk.Block(width=20,
#                                                                                                 children=[html.P('USD/USDT')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('sell')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('0,99400000')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('5,04100000')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('5,01075400')])])),
#                                                  dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
#                'justify-content': 'center',
#                'vertical-align': '-webkit-baseline-middle', 'max-width': '-webkit-fill-available',
#                'max-height': 'fit-content', 'padding': '0px',
#                'list-style': 'none',
#                'align-items': 'center'},action=True,
#                                                                    children=ddk.Block(width=100,
#                                                                             children=[ddk.Block(width=20,
#                                                                                                 children=[html.P('08:54:40')]),
#                                                                                       ddk.Block(width=20,
#                                                                                                 children=[html.P('USD/USDT')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('sell')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('0,99400000')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('5,04100000')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('5,01075400')])])),
#                                                  dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
#                'justify-content': 'center',
#                'vertical-align': '-webkit-baseline-middle', 'max-width': '-webkit-fill-available',
#                'max-height': 'fit-content', 'padding': '0px',
#                'list-style': 'none',
#                'align-items': 'center'},action=True,
#                                                                    children=ddk.Block(width=100,
#                                                                             children=[ddk.Block(width=20,
#                                                                                                 children=[html.P('08:54:40')]),
#                                                                                       ddk.Block(width=20,
#                                                                                                 children=[html.P('USD/USDT')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('sell')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('0,99400000')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('5,04100000')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('5,01075400')])])),
#                                                  dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
#                'justify-content': 'center',
#                'vertical-align': '-webkit-baseline-middle', 'max-width': '-webkit-fill-available',
#                'max-height': 'fit-content', 'padding': '0px',
#                'list-style': 'none',
#                'align-items': 'center'},action=True,
#                                                                    children=ddk.Block(width=100,
#                                                                             children=[ddk.Block(width=20,
#                                                                                                 children=[html.P('08:54:40')]),
#                                                                                       ddk.Block(width=20,
#                                                                                                 children=[html.P('USD/USDT')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('sell')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('0,99400000')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('5,04100000')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('5,01075400')])])),
#                                                  dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
#                'justify-content': 'center',
#                'vertical-align': '-webkit-baseline-middle', 'max-width': '-webkit-fill-available',
#                'max-height': 'fit-content', 'padding': '0px',
#                'list-style': 'none',
#                'align-items': 'center'},action=True,
#                                                                    children=ddk.Block(width=100,
#                                                                             children=[ddk.Block(width=20,
#                                                                                                 children=[html.P('08:54:40')]),
#                                                                                       ddk.Block(width=20,
#                                                                                                 children=[html.P('USD/USDT')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('sell')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('0,99400000')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('5,04100000')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('5,01075400')])])),
#                                                  dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
#                'justify-content': 'center',
#                'vertical-align': '-webkit-baseline-middle', 'max-width': '-webkit-fill-available',
#                'max-height': 'fit-content', 'padding': '0px',
#                'list-style': 'none',
#                'align-items': 'center'},action=True,
#                                                                    children=ddk.Block(width=100,
#                                                                             children=[ddk.Block(width=20,
#                                                                                                 children=[html.P('08:54:40')]),
#                                                                                       ddk.Block(width=20,
#                                                                                                 children=[html.P('USD/USDT')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('sell')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('0,99400000')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('5,04100000')]),
#                                                                                       ddk.Block(width=15,
#                                                                                                 children=[html.P('5,01075400')])])),
#
#                                                 ]))
#                                    ])


    first_tab = dcc.Tab(label="Ключи",
                        selected_style={'border': '2px solid #1f78b4'},
                        style={'background-color': '#ebeded'},
                        children=[
                            html.Button('Refresh-keys', id='ref_keys_btn'),
                            ddk.Block(id='tab_keys88',
                                      children=
                                      tab_keys()
                        )])

    # print("Я тут   SECOND TAB")
    # create tab to retrieve the value entered in the other tab
    second_tab = dcc.Tab(label="Настройки",
                         style={'background-color': '#ebeded'},
                        selected_style={'border': '2px solid #1f78b4'},
                         children=ddk.Card(
                             shadow_weight='heavy',
                             children=[html.Button('Refresh', id='ref_Regim_btn', n_clicks=0),
                                       dbc.ListGroup(
                                 id="listcardreg",
                                 children=[i for i in group_of_regims()]),
                                 html.Button('Добавить Режим', id='New_Regim_btn', n_clicks=0)]))

    # print("Я тут   THIRD TAB")
    # create tab to retrieve the value entered in the other tab
    third_tab = dcc.Tab(label="Статистика",
                        selected_style={'border': '2px solid #1f78b4'},
                        style={'background-color': '#ebeded'},
                         children=[
                             # ddk.Block(width=100, children=[alfa_card, live_card, hotbit_card]),
                             ddk.Card(children=[dash_table.DataTable(
                                 id="valuta",
                                 data=valuta.to_dict('records'),
                                 columns=[{'id': c, 'name': c} for c in valuta.columns],
                                 page_action='native',
                                 filter_action='native',
                                 filter_query='',
                                 sort_action='native',
                                 sort_mode='multi',
                                 sort_by=[],
                                 style_cell_conditional=[
                                     {
                                         'if': {'column_id': c},
                                         # 'pd.options.display.float_format': '{:.5f}'.format,
                                         'textAlign': 'center'
                                     } for c in ['SUMMA']
                                 ],
                                 style_data_conditional=[
                                     {
                                         'if': {'row_index': 'odd'},
                                         'backgroundColor': 'rgb(248, 248, 248)'
                                     }
                                 ],
                                 style_header={
                                     'backgroundColor': 'rgb(230, 230, 230)',
                                     'fontWeight': 'bold'
                                 }
                             ),
                             ]),

                             ddk.Card(style={'text-align': 'center'},
                                      children=[
                                          html.Button("START !",
                                                      style={'text-align': 'center', 'max-width': '150px',
                                                             "background-color": "palegreen",
                                                             "border-radius": "20px",
                                                             'margin-left':'20px',
                                                             'margin-right': '20px',
                                                             'font-size': '15px'},
                                                      n_clicks=0,
                                                      id="btn_start"),
                                          html.Button("STOP",
                                                      style={'text-align': 'center', 'max-width': '150px',
                                                             "background-color": "tomato",
                                                             "border-radius": "20px",
                                                             'margin-left':'20px',
                                                             'margin-right': '20px',
                                                             'font-size': '15px'},
                                                      n_clicks=0,
                                                      id="btn_stop")
                                      ]),

                             ddk.Card(id="table", style={'text-align': 'center'}, children=[New_chains.film_start()]),

                             ddk.Card(id="test_order_card",
                                      style={'text-align': 'center'},
                                      children=test_order.order_card()),
                             ddk.Card(children=[dash_table.DataTable(
                                 id="table_all",
                                 data=final2.to_dict('records'),
                                 columns=[{'id': c, 'name': c} for c in final2.columns],
                                 page_action='native',
                                 filter_action='native',
                                 filter_query='',
                                 sort_action='native',
                                 sort_mode='multi',
                                 sort_by=[],
                                 export_format='xlsx',
                                 export_headers='display',
                                 merge_duplicate_headers=True,
                                 style_cell={
                                     'minHeight': '20px', 'height': 'auto', 'maxHeight': '30px',
                                     # 'height': '20px',
                                     # all three widths are needed
                                     'minWidth': '50px', 'width': 'auto', 'maxWidth': '100px',
                                     # 'whiteSpace': 'normal'
                                 },
                                 style_data_conditional=[
                                     {
                                         'if': {'row_index': 'odd'},
                                         'backgroundColor': 'rgb(248, 248, 248)'
                                     }
                                 ],
                                 style_header={
                                     'backgroundColor': 'rgb(230, 230, 230)',
                                     'fontWeight': 'bold'
                                 }
                             ),
                             ])
                         ]
                        )


    # assemble tabs in dcc.Tabs object
    tabs = dcc.Tabs(children=[third_tab, second_tab, first_tab])
    # create layout
    layout = html.Div(children=[tabs, store_session_id_div, interval])
    # print("Я тут   RETURN TABs")
    return layout


layout_main = serve_layout()


