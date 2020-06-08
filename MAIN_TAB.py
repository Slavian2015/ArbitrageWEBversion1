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
                        style={'text-align': 'center', 'max-width': '100px',
                               "background-color": "tomato",
                               "border-radius": "20px",
                               'font-size': '15px'},
                        id={'type': 'Turn_Avtomat_btn',
                            'index': k},
                        n_clicks=0)
        else:
            Turn_Avtomat_btn = html.Button(children=v['avtomat'],
                                           style={'text-align': 'center', 'max-width': '100px',
                                                  "background-color": "palegreen",
                                                  "border-radius": "20px",
                                                  'font-size': '15px'},
                                           id={'type': 'Turn_Avtomat_btn',
                                               'index': k},
                                           n_clicks=0)
        regim_card = ddk.Card(id={
                                'type': 'new_regcard',
                                'index': k},

                          style={'padding-left': '10px',
                                 'margin': '2px',
                                 'margin-left': '10px',
                                 'padding': '5px'},
                          children=[
                              html.Div(id={
                                        'type': 'hidden_newreg',
                                        'index': k
                                                                }),
                              dbc.Row(
                                            style={'margin': '0',
                                                   'padding': '0'},
                                            children=[
                                                dbc.Col(style={'width': '5%',
                                                               'max-width': 'fit-content',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[dbc.Row(

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
                                                            ),

                                                            dbc.Row(html.Button('DEL',
                                                                        id={'type': 'Delete_NewRegim_btn',
                                                                            'index': k},
                                                                        n_clicks=0))
                                                        ]),


                                                dbc.Col(style={'width':'15%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[dbc.Row(dcc.Dropdown(
                                                                              id={
                                                                                  'type': 'newbirga1',
                                                                                  'index': k
                                                                              },
                                                                              style={'width':'100%','background-color': '#fff'},
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
                                                            dbc.Row(dbc.Input(
                                                                        value='{}'.format(v["birga1_com"]),
                                                                        id={'type': 'newbirga1_com',
                                                                            'index': k},
                                                                        placeholder="Комисия",
                                                                        style={
                                                                            # 'border': 'double',
                                                                            'margin': '0',
                                                                            'text-align': 'left',
                                                                            'background-color': 'ivory',
                                                                            'width': '-webkit-fill-available',
                                                                            }))]),
                                                dbc.Col(style={'width':'15%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[dbc.Row(dcc.Dropdown(
                                                                              id={
                                                                                  'type': 'newbirga2',
                                                                                  'index': k
                                                                              },
                                                                              style={'width':'100%','background-color': '#fff'},
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
                                                                              value='{}'.format(v["birga2"]))),
                                                            dbc.Row(dbc.Input(
                                                                        value='{}'.format(v["birga2_com"]),
                                                                        id={'type': 'newbirga2_com',
                                                                            'index': k},
                                                                        placeholder="Комисия",
                                                                        style={
                                                                            # 'border': 'double',
                                                                            'margin': '0',
                                                                            'text-align': 'left',
                                                                            'background-color': 'ivory',
                                                                            'width': '-webkit-fill-available',
                                                                            }))]),
                                                dbc.Col(style={'width':'15%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[dbc.Row(dcc.Dropdown(
                                                                                    id={
                                                                                        'type': 'newval1',
                                                                                        'index': k
                                                                                    },
                                                                                    style={'width':'100%',
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
                                                            dbc.Row(dbc.Input(
                                                                        value='{}'.format(v["order"]),
                                                                        id={'type': 'neworder_com',
                                                                            'index': k},
                                                                        placeholder="Минималка",
                                                                        style={
                                                                            # 'border': 'double',
                                                                            'margin': '0',
                                                                            'text-align': 'left',
                                                                            'background-color': 'ivory',
                                                                            'width': '-webkit-fill-available',
                                                                            }))]),
                                                dbc.Col(style={'width':'15%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[dbc.Row(dcc.Dropdown(
                                                                                    id={
                                                                                        'type': 'newval2',
                                                                                        'index': k
                                                                                    },
                                                                                    style={'width':'100%',
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
                                                            dbc.Row(dbc.Input(
                                                                        value='{}'.format(v["per"]),
                                                                        id={'type': 'newper',
                                                                            'index': k},
                                                                        placeholder="Минималка",
                                                                        style={
                                                                            # 'border': 'double',
                                                                            'margin': '0',
                                                                            'text-align': 'left',
                                                                            'background-color': 'ivory',
                                                                            'width': '-webkit-fill-available',
                                                                            }))]),
                                                dbc.Col(style={'width':'15%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[dbc.Row(dcc.Dropdown(
                                                                                    id={
                                                                                        'type': 'newval3',
                                                                                        'index': k
                                                                                    },
                                                                                    style={'width':'100%',
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
                                                                                    value='{}'.format(v["val3"]))),
                                                            dbc.Row(dbc.Input(
                                                                        value='{}'.format(v["profit"]),
                                                                        id={'type': 'newprofit',
                                                                            'index': k},
                                                                        placeholder=v['profit'],
                                                                        style={
                                                                            # 'border': 'double',
                                                                            'margin': '0',
                                                                            'text-align': 'left',
                                                                            'background-color': 'ivory',
                                                                            'width': '-webkit-fill-available',
                                                                            }))]),
                                                dbc.Col(style={'width':'20%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[
                                                            dbc.Row(
                                                                html.Button('SAVE',
                                                                              id={'type': 'Save_NewRegim_btn',
                                                                                  'index': k},
                                                                              n_clicks=0)),
                                                            dbc.Row(Turn_Avtomat_btn)

                                                        ])])



                            ])
        regims.append(regim_card)
    return regims
