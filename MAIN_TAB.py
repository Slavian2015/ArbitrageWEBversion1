import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
import os
import json


main_path_data = os.path.abspath("./data")

def regims():
    new_regims_f = open(main_path_data + "\\new_regims.json", 'r')
    new_regims = json.load(new_regims_f)
    regims=[]
    for k, v in new_regims.items():
        if v['avtomat'] == 'off':
            Turn_Avtomat_btn = html.Button(children=v['avtomat'],
                        style={'text-align': 'center','padding': '0',
                               "background-color": "tomato",
                               "border-radius": "20px",
                               'max-width': '50px',
                               'max-height': '50px',
                               'font-size': '10px'},
                        id={'type': 'Turn_Avtomat_btn',
                            'index': k},
                        n_clicks=0)
        else:
            Turn_Avtomat_btn = html.Button(children=v['avtomat'],
                                           style={'text-align': 'center',
                                                  "background-color": "palegreen",
                                                  "border-radius": "20px",
                               'max-width': '50px','padding': '0',
                               'max-height': '50px',
                               'font-size': '10px'},
                                           id={'type': 'Turn_Avtomat_btn',
                                               'index': k},
                                           n_clicks=0)
        regim_card = ddk.Card(id={
                                'type': 'new_regcard',
                                'index': k},

                          style={'padding-left': '2px',
                                 'margin': '2px',
                                 'margin-left': '10px',
                                 'padding': '2px'},
                          children=[
                              html.Div(id={
                                        'type': 'hidden_newreg',
                                        'index': k
                                                                }),
                              dbc.Row(
                                            style={'margin': '0',
                                                   'padding': '0'},
                                            children=[
                                                dbc.Col(style={'width': '4%',
                                                               'max-width': 'fit-content',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[
                                                            html.H2(
                                                                id={
                                                                    'type': 'new_regim_num',
                                                                    'index': k
                                                                },
                                                                style={'margin': '0',
                                                                       'font-size': 'xx-large',
                                                                       'text-align': 'center',
                                                                       'vertical-align': '-webkit-baseline-middle',
                                                                       'justify-content': 'center'},
                                                                children=k)
                                                        ]),
                                                dbc.Col(style={'width': '4%',
                                                               'max-width': 'fit-content',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[html.Button('del',
                                                                                style={'margin': '0','padding': '0',
                                                                       'font-size': '5px',
                                                                       'max-width': '10px',
                                                                       'max-height': '7px',
                                                                       "background-color": "tomato",
                                                                                       },
                                                                        id={'type': 'Delete_NewRegim_btn',
                                                                            'index': k},
                                                                        n_clicks=0)]),
                                                dbc.Col(style={'width': '7%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[dcc.Dropdown(
                                                                              id={
                                                                                  'type': 'newbirga1',
                                                                                  'index': k
                                                                              },
                                                                              style={'width':'100%',
                                                                                     'max-width': '50px',
                                                                                      'max-height': '10px',
                                                                                     'margin': '0',
                                                                                     'padding': '0',
                                                                                    'font-size': '10px',

                                                                                     'background-color': '#fff'},
                                                                              placeholder="БИРЖА 1",
                                                                              clearable=False,
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
                                                                              value='{}'.format(v["birga1"]))]),

                                                # dbc.Col(style={'width':'7%',
                                                #                'margin': '0',
                                                #                'padding': '0'},
                                                #         children=[dbc.Input(
                                                #                         value='{}'.format(v["birga1_com"]),
                                                #                         id={'type': 'newbirga1_com',
                                                #                             'index': k},
                                                #                         placeholder="Комисия",
                                                #                         style={
                                                #                             # 'border': 'double',
                                                #                             'margin': '0',
                                                #                             'max-width': '50px',
                                                #                             'max-height': '50px',
                                                #                             'text-align': 'left',
                                                #                             'background-color': 'ivory',
                                                #                             'width': '-webkit-fill-available',
                                                #                             })]),
                                                dbc.Col(style={'width': '7%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[dcc.Dropdown(
                                                                              id={
                                                                                  'type': 'newbirga2',
                                                                                  'index': k
                                                                              },
                                                            style={'width': '100%',
                                                                   'max-width': '50px',
                                                                   'max-height': '10px',
                                                                   'margin': '0',
                                                                   'padding': '0',
                                                                   'font-size': '10px',

                                                                   'background-color': '#fff'},
                                                                              placeholder="БИРЖА 2",
                                                                              clearable=False,
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
                                                                              value='{}'.format(v["birga2"]))]),
                                                # dbc.Col(style={'width':'7%',
                                                #                'margin': '0',
                                                #                'padding': '0'},
                                                #         children=[dbc.Input(
                                                #                         value='{}'.format(v["birga2_com"]),
                                                #                         id={'type': 'newbirga2_com',
                                                #                             'index': k},
                                                #                         placeholder="Комисия",
                                                #                         style={
                                                #                             # 'border': 'double',
                                                #                             'margin': '0',
                                                #                             'max-width': '50px',
                                                #                             'max-height': '50px',
                                                #                             'text-align': 'left',
                                                #                             'background-color': 'ivory',
                                                #                             'width': '-webkit-fill-available',
                                                #                             })]),
                                                dbc.Col(style={'width': '7%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[dcc.Dropdown(
                                                                                    id={
                                                                                        'type': 'newval1',
                                                                                        'index': k
                                                                                    },
                                                            style={'width': '100%',
                                                                   'max-width': '50px',
                                                                   'max-height': '10px',
                                                                   'margin': '0',
                                                                   'padding': '0',
                                                                   'font-size': '10px',
                                                                   'background-color': '#fff'},
                                                                              clearable=False,
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
                                                                                    value='{}'.format(v["val1"]))]),
                                                dbc.Col(style={'width': '7%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[dcc.Dropdown(
                                                            id={
                                                                'type': 'newval2',
                                                                'index': k
                                                            },
                                                            style={'width': '100%',
                                                                   'max-width': '50px',
                                                                   'max-height': '10px',
                                                                   'margin': '0',
                                                                   'padding': '0',
                                                                   'font-size': '10px',
                                                                   'background-color': '#fff'},
                                                                              clearable=False,
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
                                                                 'value': 'PZM'}, ],
                                                            value='{}'.format(v["val2"]))]),
                                                dbc.Col(style={'width': '7%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[dcc.Dropdown(
                                                            id={
                                                                'type': 'newval3',
                                                                'index': k
                                                            },
                                                            style={'width': '100%',
                                                                   'max-width': '50px',
                                                                   'max-height': '10px',
                                                                   'margin': '0',
                                                                   'padding': '0',
                                                                   'font-size': '10px',
                                                                   'background-color': '#fff'},
                                                                              clearable=False,
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
                                                            value='{}'.format(v["val3"]))]),
                                                dbc.Col(style={'width':'7%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[dbc.Input(
                                                                        value='{}'.format(v["order"]),
                                                                        id={'type': 'neworder_com',
                                                                            'index': k},
                                                                        placeholder="Минималка",
                                                                        style={
                                                                            'margin': '0',
                                                                            'font-size': '14px',
                                                                            'max-width': '50px',
                                                                            'max-height': '50px',
                                                                            'text-align': 'left',
                                                                            'background-color': 'ivory',
                                                                            'width': '-webkit-fill-available',
                                                                            })]),
                                                dbc.Col(style={'width':'7%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[dbc.Input(
                                                                        value='{}'.format(v["per"]),
                                                                        id={'type': 'newper',
                                                                            'index': k},
                                                                        placeholder="% ордера",
                                                                        style={
                                                                            'margin': '0',
                                                                            'font-size': '14px',
                                                                            'max-width': '50px',
                                                                            'max-height': '50px',
                                                                            'text-align': 'left',
                                                                            'background-color': 'ivory',
                                                                            'width': '-webkit-fill-available',
                                                                            })]),
                                                dbc.Col(style={'width':'7%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[dbc.Input(
                                                                        value='{}'.format(v["profit"]),
                                                                        id={'type': 'newprofit',
                                                                            'index': k},
                                                                        placeholder=v['profit'],
                                                                        style={
                                                                            'margin': '0',
                                                                            'max-width': '50px',
                                                                            'max-height': '50px',
                                                                            'font-size': '14px',
                                                                            'text-align': 'left',
                                                                            'background-color': 'ivory',
                                                                            'width': '-webkit-fill-available',
                                                                            })]),
                                                dbc.Col(style={'width': '13%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[html.Button('save',style={
                                                                            'margin': '0','padding': '0',
                                                                            'max-width': '45px',
                                                                            'max-height': '40px'},
                                                                              id={'type': 'Save_NewRegim_btn',
                                                                                  'index': k},
                                                                              n_clicks=0)]),
                                                dbc.Col(style={'width':'13%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[Turn_Avtomat_btn])])



                            ])
        regims.append(regim_card)
    return regims

def regims2():
    new_regims_f = open(main_path_data + "\\regims2.json", 'r')
    new_regims = json.load(new_regims_f)
    regims=[]
    for k, v in new_regims.items():
        if v['avtomat'] == 'off':
            Turn_Avtomat_btn = html.Button(children=v['avtomat'],
                        style={'text-align': 'center','padding': '0',
                               "background-color": "tomato",
                               "border-radius": "20px",
                               'max-width': '50px',
                               'max-height': '50px',
                               'font-size': '10px'},
                        id={'type': 'Turn_Avtomat_btn_reg2',
                            'index': k},
                        n_clicks=0)
        else:
            Turn_Avtomat_btn = html.Button(children=v['avtomat'],
                                           style={'text-align': 'center',
                                                  "background-color": "palegreen",
                                                  "border-radius": "20px",
                               'max-width': '50px','padding': '0',
                               'max-height': '50px',
                               'font-size': '10px'},
                                           id={'type': 'Turn_Avtomat_btn_reg2',
                                               'index': k},
                                           n_clicks=0)
        regim_card = ddk.Card(id={
                                'type': 'new_regcard_reg2',
                                'index': k},

                          style={'padding-left': '2px',
                                 'margin': '2px',
                                 'margin-left': '10px',
                                 'padding': '2px'},
                          children=[
                              html.Div(id={
                                        'type': 'hidden_newreg_reg2',
                                        'index': k
                                                                }),
                              dbc.Row(
                                            style={'margin': '0',
                                                   'padding': '0'},
                                            children=[
                                                dbc.Col(style={'width': '4%',
                                                               'max-width': 'fit-content',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[
                                                            html.H2(
                                                                id={
                                                                    'type': 'new_regim_num_reg2',
                                                                    'index': k
                                                                },
                                                                style={'margin': '0',
                                                                       'font-size': 'xx-large',
                                                                       'text-align': 'center',
                                                                       'vertical-align': '-webkit-baseline-middle',
                                                                       'justify-content': 'center'},
                                                                children=k)
                                                        ]),
                                                dbc.Col(style={'width': '4%',
                                                               'max-width': 'fit-content',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[html.Button('del',
                                                                                style={'margin': '0','padding': '0',
                                                                       'font-size': '5px',
                                                                       'max-width': '10px',
                                                                       'max-height': '7px',
                                                                       "background-color": "tomato",
                                                                                       },
                                                                        id={'type': 'Delete_NewRegim_btn_reg2',
                                                                            'index': k},
                                                                        n_clicks=0)]),
                                                dbc.Col(style={'width': '7%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[dcc.Dropdown(
                                                                              id={
                                                                                  'type': 'newbirga1_reg2',
                                                                                  'index': k
                                                                              },
                                                                              style={'width':'100%',
                                                                                     'max-width': '50px',
                                                                                      'max-height': '10px',
                                                                                     'margin': '0',
                                                                                     'padding': '0',
                                                                                    'font-size': '10px',

                                                                                     'background-color': '#fff'},
                                                                              placeholder="БИРЖА 1",
                                                                              clearable=False,
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
                                                                              value='{}'.format(v["birga1"]))]),

                                                # dbc.Col(style={'width':'7%',
                                                #                'margin': '0',
                                                #                'padding': '0'},
                                                #         children=[dbc.Input(
                                                #                         value='{}'.format(v["birga1_com"]),
                                                #                         id={'type': 'newbirga1_com',
                                                #                             'index': k},
                                                #                         placeholder="Комисия",
                                                #                         style={
                                                #                             # 'border': 'double',
                                                #                             'margin': '0',
                                                #                             'max-width': '50px',
                                                #                             'max-height': '50px',
                                                #                             'text-align': 'left',
                                                #                             'background-color': 'ivory',
                                                #                             'width': '-webkit-fill-available',
                                                #                             })]),
                                                dbc.Col(style={'width': '7%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[dcc.Dropdown(
                                                                              id={
                                                                                  'type': 'newbirga2_reg2',
                                                                                  'index': k
                                                                              },
                                                            style={'width': '100%',
                                                                   'max-width': '50px',
                                                                   'max-height': '10px',
                                                                   'margin': '0',
                                                                   'padding': '0',
                                                                   'font-size': '10px',

                                                                   'background-color': '#fff'},
                                                                              placeholder="БИРЖА 2",
                                                                              clearable=False,
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
                                                                              value='{}'.format(v["birga2"]))]),
                                                # dbc.Col(style={'width':'7%',
                                                #                'margin': '0',
                                                #                'padding': '0'},
                                                #         children=[dbc.Input(
                                                #                         value='{}'.format(v["birga2_com"]),
                                                #                         id={'type': 'newbirga2_com',
                                                #                             'index': k},
                                                #                         placeholder="Комисия",
                                                #                         style={
                                                #                             # 'border': 'double',
                                                #                             'margin': '0',
                                                #                             'max-width': '50px',
                                                #                             'max-height': '50px',
                                                #                             'text-align': 'left',
                                                #                             'background-color': 'ivory',
                                                #                             'width': '-webkit-fill-available',
                                                #                             })]),
                                                dbc.Col(style={'width': '7%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[dcc.Dropdown(
                                                                                    id={
                                                                                        'type': 'newval1_reg2',
                                                                                        'index': k
                                                                                    },
                                                            style={'width': '100%',
                                                                   'max-width': '50px',
                                                                   'max-height': '10px',
                                                                   'margin': '0',
                                                                   'padding': '0',
                                                                   'font-size': '10px',
                                                                   'background-color': '#fff'},
                                                                              clearable=False,
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
                                                                                    value='{}'.format(v["val1"]))]),
                                                dbc.Col(style={'width': '7%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[dcc.Dropdown(
                                                            id={
                                                                'type': 'newval2_reg2',
                                                                'index': k
                                                            },
                                                            style={'width': '100%',
                                                                   'max-width': '50px',
                                                                   'max-height': '10px',
                                                                   'margin': '0',
                                                                   'padding': '0',
                                                                   'font-size': '10px',
                                                                   'background-color': '#fff'},
                                                                              clearable=False,
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
                                                                 'value': 'PZM'}, ],
                                                            value='{}'.format(v["val2"]))]),
                                                dbc.Col(style={'width': '7%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[dcc.Dropdown(
                                                            id={
                                                                'type': 'newval3_reg2',
                                                                'index': k
                                                            },
                                                            style={'width': '100%',
                                                                   'max-width': '50px',
                                                                   'max-height': '10px',
                                                                   'margin': '0',
                                                                   'padding': '0',
                                                                   'font-size': '10px',
                                                                   'background-color': '#fff'},
                                                                              clearable=False,
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
                                                            value='{}'.format(v["val3"]))]),
                                                dbc.Col(style={'width':'7%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[dbc.Input(
                                                                        value='{}'.format(v["order"]),
                                                                        id={'type': 'neworder_com_reg2',
                                                                            'index': k},
                                                                        placeholder="Минималка",
                                                                        style={
                                                                            'margin': '0',
                                                                            'font-size': '14px',
                                                                            'max-width': '50px',
                                                                            'max-height': '50px',
                                                                            'text-align': 'left',
                                                                            'background-color': 'ivory',
                                                                            'width': '-webkit-fill-available',
                                                                            })]),
                                                dbc.Col(style={'width':'7%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[dbc.Input(
                                                                        value='{}'.format(v["per"]),
                                                                        id={'type': 'newper_reg2',
                                                                            'index': k},
                                                                        placeholder="% ордера",
                                                                        style={
                                                                            'margin': '0',
                                                                            'font-size': '14px',
                                                                            'max-width': '50px',
                                                                            'max-height': '50px',
                                                                            'text-align': 'left',
                                                                            'background-color': 'ivory',
                                                                            'width': '-webkit-fill-available',
                                                                            })]),
                                                dbc.Col(style={'width':'7%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[dbc.Input(
                                                                        value='{}'.format(v["profit"]),
                                                                        id={'type': 'newprofit_reg2',
                                                                            'index': k},
                                                                        placeholder=v['profit'],
                                                                        style={
                                                                            'margin': '0',
                                                                            'max-width': '50px',
                                                                            'max-height': '50px',
                                                                            'font-size': '14px',
                                                                            'text-align': 'left',
                                                                            'background-color': 'ivory',
                                                                            'width': '-webkit-fill-available',
                                                                            })]),
                                                dbc.Col(style={'width': '13%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[html.Button('save',style={
                                                                            'margin': '0','padding': '0',
                                                                            'max-width': '45px',
                                                                            'max-height': '40px'},
                                                                              id={'type': 'Save_NewRegim_btn_reg2',
                                                                                  'index': k},
                                                                              n_clicks=0)]),
                                                dbc.Col(style={'width':'13%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[Turn_Avtomat_btn])])



                            ])
        regims.append(regim_card)
    return regims