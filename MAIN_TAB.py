import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
import os
import json


main_path_data = os.path.abspath("./data")

new_regims_f = open(main_path_data + "\\new_regims.json", 'r')
new_regims = json.load(new_regims_f)


def regims():
    regims=[]
    for k, v in new_regims.items():
        regim_card = ddk.Card(width=100,
                          style={'margin':'0',
                                 'padding':'0'},
                          card_hover=True,
                          children=[
                            dcc.Interval(id={'type': 'new_interval','index': k}, interval=2000, n_intervals=0),
                            dbc.Row(
                                style={'margin': '0',
                                       'padding': '0'},
                                children=[
                                    dbc.Col(style={'width':'5%','margin': '0',
                                                'padding': '0'},
                                            children=[html.H2(
                                            id={
                                                 'type': 'new_regim_num',
                                                 'index': k
                                             },
                                            style={'margin': '0',
                                                'text-align': 'center',
                                                'vertical-align': '-webkit-baseline-middle',
                                                'justify-content': 'center'},
                                            children=k)]

                                            ),
                                    dbc.Col(
                                        style={'width':'95%','margin': '0',
                                                'padding': '0'},
                                        children=[
                                        dbc.Row(
                                            style={'margin': '0',
                                                   'padding': '0'},
                                            children=[
                                                dbc.Col(style={'width':'16%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[dbc.Row(dcc.Dropdown(
                                                                              id={
                                                                                  'type': 'newbirga1',
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
                                                            dbc.Row(dcc.Input(
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
                                                dbc.Col(style={'width':'16%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[dbc.Row(dcc.Dropdown(
                                                                              id={
                                                                                  'type': 'newbirga2',
                                                                                  'index': k
                                                                              },
                                                                              style={'background-color': '#fff'},
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
                                                                              value='{}'.format(v["birga1"]))),
                                                            dbc.Row(dcc.Input(
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
                                                dbc.Col(style={'width':'16%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[dbc.Row(dcc.Dropdown(
                                                                                    id={
                                                                                        'type': 'newval1',
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
                                                            dbc.Row(dcc.Input(
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
                                                dbc.Col(style={'width':'16%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[dbc.Row(dcc.Dropdown(
                                                                                    id={
                                                                                        'type': 'newval2',
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
                                                            dbc.Row(dcc.Input(
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
                                                dbc.Col(style={'width':'16%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[dbc.Row(dcc.Dropdown(
                                                                                    id={
                                                                                        'type': 'newval3',
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
                                                                                    value='{}'.format(v["val3"]))),
                                                            dbc.Row(dcc.Input(
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
                                                        children=[html.Button('SAVE',
                                                                              id={'type': 'Save_NewRegim_btn',
                                                                                  'index': k},
                                                                              n_clicks=0)]),

                                            ]),




                                        dbc.Row(
                                            style={'margin': '0',
                                                   'padding': '0'},
                                            children=[
                                                dbc.Col(style={'width': '35%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[
                                                            dbc.Row(style={'margin': '0',
                                                                           'padding': '0'},
                                                                    children=[html.H2(
                                                                        id={'type': 'REG_KURS1',
                                                                            'index': k},
                                                                        children=''
                                                                    )]),
                                                            dbc.Row(style={'margin': '0',
                                                                           'padding': '0'},
                                                                    children=[
                                                                        dbc.Col(style={'width': '50%',
                                                                                       'margin': '0',
                                                                                       'padding': '0'},
                                                                                children=[html.P(
                                                                        id={'type': 'REG_vol1',
                                                                            'index': k},
                                                                        children=''
                                                                    )]),
                                                                        dbc.Col(style={'width': '50%',
                                                                                       'margin': '0',
                                                                                       'padding': '0'},
                                                                                children=[html.P(
                                                                        id={'type': 'REG_vol2',
                                                                            'index': k},
                                                                        children=''
                                                                    )])
                                                                    ])]),
                                                dbc.Col(style={'width': '35%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[
                                                            dbc.Row(style={'margin': '0',
                                                                           'padding': '0'},
                                                                    children=[html.H2(
                                                                        id={'type': 'REG_KURS2',
                                                                            'index': k},
                                                                        children=''
                                                                    )]),
                                                            dbc.Row(style={'margin': '0',
                                                                           'padding': '0'},
                                                                    children=[
                                                                        dbc.Col(style={'width': '50%',
                                                                                       'margin': '0',
                                                                                       'padding': '0'},
                                                                                children=[html.P(
                                                                        id={'type': 'REG_vol3',
                                                                            'index': k},
                                                                        children=''
                                                                    )]),
                                                                        dbc.Col(style={'width': '50%',
                                                                                       'margin': '0',
                                                                                       'padding': '0'},
                                                                                children=[html.P(
                                                                        id={'type': 'REG_vol3',
                                                                            'index': k},
                                                                        children=''
                                                                    )])])]),
                                                dbc.Col(style={'width': '10%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[
                                                            dbc.Row(style={'margin': '0',
                                                                           'padding': '0'},
                                                                    children=[html.H2(
                                                                        id={'type': 'REG_PROF',
                                                                            'index': k},
                                                                        children=''
                                                                    )]),
                                                            dbc.Row(style={'margin': '0',
                                                                           'padding': '0'},
                                                                    children=[html.P(
                                                                        id={'type': 'REG_AMOUNT',
                                                                            'index': k},
                                                                        children=''
                                                                    )])]),




                                                dbc.Col(style={'width': '20%',
                                                               'margin': '0',
                                                               'padding': '0'},
                                                        children=[html.Button(value=v['avtomat'],
                                                                              style={'text-align': 'center', 'max-width': '100px',
                                                                                     "background-color": "palegreen",
                                                                                     "border-radius": "20px",
                                                                                     'font-size': '15px'},
                                                                              id={'type': 'Turn_Avtomat_btn',
                                                                                  'index': k},
                                                                              n_clicks=0)]),


                                            ]),

                                    ]),
                                ]
                            )
                          ])
        regims.append(regim_card)
    return regims