import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
import pandas as pd
import dash_table
import os
import json
import MAIN_TAB

import base64


main_path_data = os.path.abspath("./data")
pd.options.display.float_format = '${:.6f}'.format
# Encode the local sound file.
sound_filename = (main_path_data + "\\signal.mp3")  # replace with your own .mp3 file
encoded_sound = base64.b64encode(open(sound_filename, 'rb').read())

########  MAIN PAGE MY  ##############

def tab_keys():


    a_file = open(main_path_data + "\\keys.json", "r")
    keys8 = json.load(a_file)
    a_file.close()
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
                                            children=[ddk.Block(width=20,
                                                                children=html.H2('Livecoin',
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
                                                                       ]))]

    return tab_keys

def group_of_regims():
    d = open(main_path_data + "\\regim.json")
    com2 = json.load(d)

    group_of_regims = []
    # html.Div(id='hidden-div')

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
    interval = dcc.Interval(id='interval', interval=1000, n_intervals=0)
    valuta = pd.read_csv(main_path_data + "\\balance.csv")
    vilki = pd.read_csv(main_path_data + "\\vilki.csv")
    final2 = pd.read_csv(main_path_data + "\\all_data.csv")


    # sound = html.Div(id='hidden-div', style={"display": "none"})


    layout = [interval,
              # sound,
              dbc.Row(style={'padding':'0','margin':'0'},
                      children=[
                  dbc.Col(
                        style={'height': '93vh',
                               'max-height': '93vh',
                               'text-align': 'center',
                               'padding':'0',
                               'margin':'0',
                               'width':'60%',
                               'overflowY': "hidden"},
                        children=[

                            dbc.Row(style={'min-height': '40vh', 'max-height': '40vh',
                               'padding':'0',
                               'margin':'0',
                                           'overflowY': 'scroll'},
                                    children=[
                                        ddk.Card(style={
                                           'padding':'0',
                                           'margin':'0',
                                           'overflowY': 'hidden'},
                                            children=[
                                            dash_table.DataTable(
                                                id="table",
                                                data=vilki.to_dict('records'),
                                                columns=[{'id': c, 'name': c} for c in vilki.columns],
                                                sort_action='native',
                                                style_cell_conditional=[
                                                    {
                                                        'if': {'column_id': 'regim'},
                                                        'font-size': '11px',
                                                        'fontWeight': 'bold'
                                                    },
                                                    {
                                                        'if': {'column_id': 'timed'},
                                                        'font-size': '11px',
                                                        'max-width': 'fit-content',
                                                    },
                                                    {
                                                        'if': {'column_id': 'b1'},
                                                        'font-size': '11px',
                                                        'max-width': 'fit-content',
                                                        'padding':'0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'b2'},
                                                        'font-size': '11px',
                                                        'max-width': 'fit-content',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'val1'},
                                                        'font-size': '11px',
                                                        'max-width': 'fit-content',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'val2'},
                                                        'font-size': '11px',
                                                        'max-width': 'fit-content',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'val3'},
                                                        'font-size': '11px',
                                                        'max-width': 'fit-content',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'kurs1'},
                                                        'font-size': '12px',
                                                        'fontWeight': 'bold'
                                                    },
                                                    {
                                                        'if': {'column_id': 'kurs2'},
                                                        'font-size': '12px',
                                                        'fontWeight': 'bold'
                                                    },
                                                    {
                                                        'if': {'column_id': 'profit'},
                                                        'font-size': '12px',
                                                        'fontWeight': 'bold'
                                                    }




                                                    # {
                                                    #     'if': {'column_id': c},
                                                    #     'font-size': '9px',
                                                    #     'max-width': 'fit-content',
                                                    # } for c in
                                                    # ['regim', 'timed', 'b1', 'b2', 'val1', 'val2', 'val3',
                                                    #  'Go']
                                                ],
                                                style_data_conditional=[
                                                    {
                                                        'if': {'row_index': 'odd'},
                                                        'backgroundColor': 'rgb(248, 248, 248)'
                                                    },
                                                ],
                                                style_table={
                                                    'maxHeight': '100%',
                                                    'overflowY': 'scroll',
                                                    'width': '100%',
                                                    'minWidth': '100%',
                                                },
                                                style_cell={
                                                    'fontSize': '10px',
                                                    'fontFamily': 'Open Sans',
                                                    'textAlign': 'center',
                                                    'height': '30px',
                                                    'maxHeight': '30px',
                                                    'whiteSpace': 'inherit',
                                                    'overflow': 'hidden',
                                                    'textOverflow': 'ellipsis',
                                                },

                                                style_header={
                                                    'fontSize': '10px',
                                                    'backgroundColor': 'rgb(230, 230, 230)',
                                                    'fontWeight': 'bold'
                                                })
                                        ])
                                    ]),
                            dbc.Row(style={
                                # "width": "100%",
                                           'max-height': '58vh',
                                           'overflowY': 'scroll',
                               'padding':'0',
                               'margin':'0',
                                           },
                                    children=[

                                        ddk.Card(
                                            style={"width": "100%", 'min-height': '48vh', 'max-height': '48vh',
                               'padding':'0',
                               'margin':'0','margin-top':'10px',
                                                   'overflowY': 'scroll'},
                                            children=[dash_table.DataTable(
                                                id="table_all",
                                                data=final2.to_dict('records'),
                                                columns=[{'id': c, 'name': c} for c in final2.columns],
                                                # page_action='native',
                                                # filter_action='native',
                                                # filter_query='',
                                                # sort_action='native',
                                                # sort_mode='multi',
                                                # sort_by=[],
                                                export_format='xlsx',
                                                # export_headers='display',
                                                # merge_duplicate_headers=True,
                                                style_cell_conditional=[
                                                    {
                                                        'if': {'column_id': 'birga_x'},
                                                        # 'font-size': '11px',
                                                        'max-width': '30px',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'birga_y'},
                                                        # 'font-size': '11px',
                                                        'max-width': '30px',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'valin_x'},
                                                        # 'font-size': '11px',
                                                        'max-width': '30px',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'valin_y'},
                                                        # 'font-size': '11px',
                                                        'max-width': '30px',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'valout_x'},
                                                        # 'font-size': '11px',
                                                        'max-width': '30px',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'res_birga1'},
                                                        # 'font-size': '11px',
                                                        'max-width': '30px',
                                                        'overflow': 'hidden',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'res_birga2'},
                                                        # 'font-size': '11px',
                                                        'max-width': '30px',
                                                        'overflow': 'hidden',
                                                        'padding': '0',
                                                    },
                                                    {
                                                        'if': {'column_id': 'TIME'},
                                                        # 'font-size': '11px',
                                                        'max-width': 'fit-content',
                                                        'textOverflow': 'ellipsis',
                                                        'padding': '0',
                                                    },
                                                ],
                                                style_data_conditional=[
                                                    {
                                                        'if': {'row_index': 'odd'},
                                                        'backgroundColor': 'rgb(248, 248, 248)'
                                                    }
                                                ],
                                                style_table={
                                                    'maxHeight': '100%',
                                                    'overflowY': 'scroll',
                                                    'width': '100%',
                                                    'minWidth': '100%',
                                                },
                                                style_cell={
                                                    'fontSize': '10px',
                                                    'fontFamily': 'Open Sans',
                                                    'textAlign': 'center',
                                                    'height': '30px',
                                                    'maxHeight': '30px',
                                                    # 'width': '30px',
                                                    # 'maxWidth': '30px',
                                                    'padding': '0',
                                                    'whiteSpace': 'inherit',
                                                    'overflow': 'hidden',
                                                    # 'textOverflow': 'ellipsis',
                                                    # 'pd.options.display.float_format': '{:.5f}'.format,
                                                },
                                                style_header={
                                                    'fontSize': '10px',
                                                    'backgroundColor': 'rgb(230, 230, 230)',
                                                    'fontWeight': 'bold'
                                                }
                                            ),
                                            ])
                                        ]),
                            ]),
                  dbc.Col(
                        style={'height': '93vh',
                               'max-height': '93vh',
                               'text-align': 'center',
                               'padding':'0',
                               'margin':'0',
                               'max-width': '40%',
                               'width':'40%',
                       'overflowY': "hidden"},
                        children=[
                            dbc.Row(style={
                                # "width": "100%",
                                'min-height': '40vh', 'max-height': '40vh',
                               'padding':'0',
                               'margin':'0',
                                           'overflowY': 'hidden'},
                                    children=[
                                        ddk.Card(
                                            style={
                                                "width": "100%", 'min-height': '38vh', 'max-height': '38vh',
                                                   'padding':'0',
                                                   'margin':'0',
                                                   'overflowY': 'scroll'},
                                            children=[
                                                dash_table.DataTable(
                                                    id="valuta",
                                                    data=valuta.to_dict('records'),
                                                    columns=[{'id': c, 'name': c} for c in valuta.columns],
                                                    # page_action='native',
                                                    # filter_action='native',
                                                    # filter_query='',
                                                    # sort_action='native',
                                                    # sort_mode='multi',
                                                    # sort_by=[],
                                                    style_cell_conditional=[
                                                        {'if': {'column_id': 'Valuta'},
                                                         'fontWeight': 'bold',
                                                         'maxWidth': '30px',
                                                         'textOverflow': 'ellipsis',
                                                         },
                                                        {'if': {'column_id': 'Summa'},
                                                         'fontWeight': 'bold',
                                                         }
                                                    ],
                                                    style_data_conditional=[
                                                        {
                                                            'if': {'row_index': 'odd'},
                                                            'backgroundColor': 'rgb(248, 248, 248)'
                                                        }
                                                    ],
                                                    style_table={
                                                        'maxHeight': '100%',
                                                        'overflowY': 'scroll',
                                                        'width': '100%',
                                                        'minWidth': '100%',
                                                    },
                                                    style_cell={
                                                        'fontSize': '12px',
                                                        'fontFamily': 'Open Sans',
                                                        'textAlign': 'center',
                                                        'height': '15px',
                                                        'maxHeight': '20px',
                                                        'width': '30px',
                                                        # 'maxWidth': '30px',
                                                        # 'padding': '2px 22px',
                                                        'whiteSpace': 'inherit',
                                                        'overflow': 'hidden',
                                                        'textOverflow': 'ellipsis',
                                                    },
                                                    style_header={
                                                        'fontSize': '14px',
                                                        'backgroundColor': 'rgb(230, 230, 230)',
                                                        'fontWeight': 'bold'
                                                    }
                                                ),
                                            ]),

                                    ]),
                            dbc.Row(style={"width": "100%", 'min-height': '50vh', 'max-height': '50vh',
                                           'overflowY': 'scroll'},
                                    children=[
                                        dbc.Row(html.Div(
                                            # width=100,
                                            style={'padding-left': '0px'},
                                            children=[
                                                dbc.Row(
                                                    style={'margin': '0',
                                                           'padding': '0'},
                                                    children=[
                                                        dbc.Row(
                                                            style={'margin': '0',
                                                                   'margin-left': '10px',
                                                                   'padding': '0'},
                                                            children=[
                                                                dbc.Col(style={'width': '16%',
                                                                               'margin': '0',
                                                                               'padding': '0'},
                                                                        children=[
                                                                            dbc.Row(dcc.Dropdown(
                                                                                id='newbirga1_btn',
                                                                                style={'width': '100%',
                                                                                       'background-color': '#fff'},
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
                                                                                value='')),
                                                                            dbc.Row(dcc.Input(
                                                                                value='',
                                                                                id='newbirga1_com_btn',
                                                                                placeholder="Комисия",
                                                                                style={
                                                                                    'margin': '0',
                                                                                    'text-align': 'left',
                                                                                    'background-color': 'ivory',
                                                                                    'width': '-webkit-fill-available',
                                                                                }))]),
                                                                dbc.Col(style={'width': '16%',
                                                                               'margin': '0',
                                                                               'padding': '0'},
                                                                        children=[dbc.Row(dcc.Dropdown(
                                                                            id='newbirga2_btn',
                                                                            style={'width': '100%',
                                                                                   'background-color': '#fff'},
                                                                            placeholder="БИРЖА 2",
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
                                                                            value='')),
                                                                            dbc.Row(dcc.Input(
                                                                                value='',
                                                                                id='newbirga2_com_btn',
                                                                                placeholder="Комисия",
                                                                                style={
                                                                                    'margin': '0',
                                                                                    'text-align': 'left',
                                                                                    'background-color': 'ivory',
                                                                                    'width': '-webkit-fill-available',
                                                                                }))]),
                                                                dbc.Col(style={'width': '16%',
                                                                               'margin': '0',
                                                                               'padding': '0'},
                                                                        children=[dbc.Row(dcc.Dropdown(
                                                                            id='newval1_btn',
                                                                            style={'width': '100%',
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
                                                                            value='', )),
                                                                            dbc.Row(dcc.Input(
                                                                                value='',
                                                                                id='neworder_com_btn',
                                                                                placeholder="Минималка",
                                                                                style={
                                                                                    'margin': '0',
                                                                                    'text-align': 'left',
                                                                                    'background-color': 'ivory',
                                                                                    'width': '-webkit-fill-available',
                                                                                }))]),
                                                                dbc.Col(style={'width': '16%',
                                                                               'margin': '0',
                                                                               'padding': '0'},
                                                                        children=[dbc.Row(dcc.Dropdown(
                                                                            id='newval2_btn',
                                                                            style={'width': '100%',
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
                                                                            value='')),
                                                                            dbc.Row(dcc.Input(
                                                                                value='',
                                                                                id='newper_btn',
                                                                                placeholder="% ордера",
                                                                                style={
                                                                                    'margin': '0',
                                                                                    'text-align': 'left',
                                                                                    'background-color': 'ivory',
                                                                                    'width': '-webkit-fill-available',
                                                                                }))]),
                                                                dbc.Col(style={'width': '16%',
                                                                               'margin': '0',
                                                                               'padding': '0'},
                                                                        children=[dbc.Row(dcc.Dropdown(
                                                                            id='newval3_btn',
                                                                            style={'width': '100%',
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
                                                                            value='')),
                                                                            dbc.Row(dcc.Input(
                                                                                value='',
                                                                                id='newprofit_btn',
                                                                                placeholder='% профита',
                                                                                style={
                                                                                    'margin': '0',
                                                                                    'text-align': 'left',
                                                                                    'background-color': 'ivory',
                                                                                    'width': '-webkit-fill-available',
                                                                                }))]),
                                                                dbc.Col(style={'width': '25%',
                                                                               'margin': '0',
                                                                               'padding': '0'},
                                                                        children=[html.Button('SAVE',
                                                                                              id='Create_NewRegim_btn',
                                                                                              n_clicks=0)]),

                                                            ])
                                                    ]
                                                )
                                            ])),
                                        dbc.Row(id="listcardreg",
                                                style={"width": "100%",
                                                       # 'min-height': '50vh',
                                                       # 'max-height': '45vh',
                                                       # 'overflowY': 'scroll'
                                                       },
                                                children=[i for i in MAIN_TAB.regims()])

                                    ])])

              ])
              ]

    return layout

def ring(i):
    if i == 0:
        return html.Audio(src='data:audio/mpeg;base64,{}'.format(encoded_sound.decode('utf-8')),
                   controls=False,
                   autoPlay=True,)
    else:
        return html.Div(id='ring', style={"display": "none"})

def sound(i):

    sound = html.Div(id='placeholder', style={"display": "none"}, children=ring(i))
    return sound

