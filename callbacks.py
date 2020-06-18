from dash.dependencies import Input, Output, State, MATCH
from app import dash_app
from dash.exceptions import PreventUpdate
import dash
import os
import json
import pandas as pd
import base64
import MAIN_TAB
import refBalance
import sys
import logging
import logging.config
import dash_html_components as html
# import dash_design_kit as ddk
import layouts
import dash_audio_components
#
# import Orders
# import datetime as dt
#
# from decimal import ROUND_UP,Context



dash_app.config['suppress_callback_exceptions'] = True
# dash_app.config['serve_locally'] = True
main_path_data = os.path.abspath("./data")
dash_app.scripts.config.serve_locally = True
# Encode the local sound file.
sound_filename = (main_path_data + "\\signal.mp3")  # replace with your own .mp3 file
encoded_sound = base64.b64encode(open(sound_filename, 'rb').read())



def refresh(app: dash.Dash):
    ###############################    RESTART ALL FUNCTIONS     ########################################
    @app.callback([Output('table', 'data'),
                   Output('valuta', 'data'),
                   Output('table_all', 'data'),
                   Output('placeholder1', 'children'),
                   ],
                  [
                      Input('interval', 'n_intervals'),
                  ],
                  [State('newval1_btn', "value"),
                   State('newval2_btn', "value"),
                   State('newval3_btn', "value"),
                   State('newbirga1_btn', "value"),
                   State('newbirga2_btn', "value"),
                   State('newbirga1_com_btn', "value"),
                   State('newbirga2_com_btn', "value"),
                   State('newprofit_btn', "value"),
                   State('neworder_com_btn', "value"),
                   State('newper_btn', "value"),
                   ]
                  )
    def trigger_by_modify(n_clicks, val1, val2, val3, birga1, birga2,birga1_com, birga2_com, profit, order, percent):

        ctx = dash.callback_context
        button_id = ctx.triggered[0]['prop_id'].split('.')
        # print('button_id :', button_id[0])
        # # print('n :', n)
        # print('n_clicks :',  n_clicks)

        valuta = pd.read_csv(main_path_data + "\\balance.csv")
        try:
            vilki = pd.read_csv(main_path_data + "\\vilki.csv")
        except Exception as e:
            vilki = pd.read_csv(main_path_data + "\\vilki.csv")
            pass
        final2 = pd.read_csv(main_path_data + "\\all_data.csv")

        # print(vilki)



        vilki['profit'] = vilki['profit'].map('{:,.2f}%'.format)
        vilki['kurs1'] = vilki['kurs1'].map('{:,.8f}'.format)
        vilki['kurs2'] = vilki['kurs2'].map('{:,.8f}'.format)
        vilki['Vol1'] = vilki['Vol1'].map('{:,.6f}'.format)
        vilki['Vol2'] = vilki['Vol2'].map('{:,.6f}'.format)
        vilki['Vol3'] = vilki['Vol3'].map('{:,.6f}'.format)
        vilki['Vol4'] = vilki['Vol4'].map('{:,.6f}'.format)

        valuta['alfa'] = valuta['alfa'].map('{:,.6f}'.format)
        valuta['live'] = valuta['live'].map('{:,.6f}'.format)
        valuta['hot'] = valuta['hot'].map('{:,.6f}'.format)
        valuta['Summa'] = valuta['Summa'].map('{:,.6f}'.format)

        final2['profit'] = final2['profit'].map('{:,.6f}'.format)
        final2['start'] = final2['start'].map('{:,.6f}'.format)
        final2['step'] = final2['step'].map('{:,.6f}'.format)
        final2['back'] = final2['back'].map('{:,.6f}'.format)
        final2['rates_x'] = final2['rates_x'].map('{:,.8f}'.format)
        final2['rates_y'] = final2['rates_y'].map('{:,.8f}'.format)
        final2['perc'] = final2['perc'].map('{:,.2f}%'.format)


        if button_id[0] == 'interval':
            print(" ##########   REFRESH  ################")
            if float(vilki.iloc[0]['kurs1']) > 0:
                print(" ##########   1  ################")
                return vilki.to_dict('records'),valuta.to_dict('records'),final2.to_dict('records'), layouts.sound(0)
            else:
                print(" ##########   2  ################")
                return vilki.to_dict('records'), valuta.to_dict('records'), final2.to_dict('records'), layouts.sound(1)

        else:
            raise PreventUpdate

def refresh2(app: dash.Dash):
    ###############################    RESTART ALL FUNCTIONS     ########################################
    @app.callback([Output('vilki2_table', 'data'),
                   Output('vilki2_all_table', 'data'),
                   ],
                  [
                      Input('interval2', 'n_intervals'),
                  ],
                  [State('newval1_btn_reg2', "value"),
                   State('newval2_btn_reg2', "value"),
                   State('newval3_btn_reg2', "value"),
                   State('newbirga1_btn_reg2', "value"),
                   State('newbirga2_btn_reg2', "value"),
                   State('newbirga1_com_btn_reg2', "value"),
                   State('newbirga2_com_btn_reg2', "value"),
                   State('newprofit_btn_reg2', "value"),
                   State('neworder_com_btn_reg2', "value"),
                   State('newper_btn_reg2', "value"),
                   ]
                  )
    def trigger_by_modify(n_clicks, val1, val2, val3, birga1, birga2,birga1_com, birga2_com, profit, order, percent):

        ctx = dash.callback_context
        button_id = ctx.triggered[0]['prop_id'].split('.')
        # print('button_id :', button_id[0])
        # # print('n :', n)
        # print('n_clicks :',  n_clicks)


        try:
            vilki = pd.read_csv(main_path_data + "\\vilki2.csv")
        except Exception as e:
            vilki = pd.read_csv(main_path_data + "\\vilki2.csv")
            pass
        final2 = pd.read_csv(main_path_data + "\\vilki2_all.csv")

        # print(vilki)


        #
        # vilki['profit'] = vilki['profit'].map('{:,.2f}%'.format)
        # vilki['kurs1'] = vilki['kurs1'].map('{:,.8f}'.format)
        # vilki['kurs2'] = vilki['kurs2'].map('{:,.8f}'.format)
        # vilki['Vol1'] = vilki['Vol1'].map('{:,.6f}'.format)
        # vilki['Vol2'] = vilki['Vol2'].map('{:,.6f}'.format)
        # vilki['Vol3'] = vilki['Vol3'].map('{:,.6f}'.format)
        # vilki['Vol4'] = vilki['Vol4'].map('{:,.6f}'.format)
        #
        #
        # final2['profit'] = final2['profit'].map('{:,.6f}'.format)
        # final2['start'] = final2['start'].map('{:,.6f}'.format)
        # final2['step'] = final2['step'].map('{:,.6f}'.format)
        # final2['back'] = final2['back'].map('{:,.6f}'.format)
        # final2['rates_x'] = final2['rates_x'].map('{:,.8f}'.format)
        # final2['rates_y'] = final2['rates_y'].map('{:,.8f}'.format)
        # final2['perc'] = final2['perc'].map('{:,.2f}%'.format)


        if button_id[0] == 'interval2':
            print(" ##########   REFRESH  ################")

            return vilki.to_dict('records'),final2.to_dict('records')


        else:
            raise PreventUpdate

def save_key_data(app: dash.Dash):
    @app.callback(

        [Output({'type': 'key', 'index': MATCH}, 'placeholder'),
         Output({'type': 'api', 'index': MATCH}, 'placeholder')],
        [Input({'type': 'save_btn', 'index': MATCH}, 'n_clicks')],
        [State({'type': 'save_btn', 'index': MATCH}, 'id'),
         State({'type': 'key', 'index': MATCH}, 'value'),
         State({'type': 'api', 'index': MATCH}, 'value'),
         ])
    def display_output(n_clicks, id, key, api):
        if n_clicks is None:
            raise PreventUpdate

        else:


            a_file = open(main_path_data + "\\keys.json", "r")
            json_object = json.load(a_file)
            a_file.close()
            json_object[str(id['index'])]['key'] = key
            json_object[str(id['index'])]['api'] = api
            print("###################################  keys JSON NEW:", '\n', json_object)
            a_file = open(main_path_data + "\\keys.json", "w")
            json.dump(json_object, a_file)
            a_file.close()
            return "{}".format(key), "{}".format(api)

def creat_reg(app: dash.Dash):

    @app.callback([Output('listcardreg', 'children')],
        [Input('Create_NewRegim_btn', 'n_clicks'),
         Input('On_Avtomat_btn', 'n_clicks'),
         Input('Off_Avtomat_btn', 'n_clicks')],
                  [State('newval1_btn', "value"),
                   State('newval2_btn', "value"),
                   State('newval3_btn', "value"),
                   State('newbirga1_btn', "value"),
                   State('newbirga2_btn', "value"),
                   State('newbirga1_com_btn', "value"),
                   State('newbirga2_com_btn', "value"),
                   State('newprofit_btn', "value"),
                   State('neworder_com_btn', "value"),
                   State('newper_btn', "value"),
                   ])

    def create(n_clicks, n_clicks2,n_clicks3, val1, val2, val3, birga1, birga2,birga1_com, birga2_com, profit, order, percent):

        ctx = dash.callback_context
        button_id = ctx.triggered[0]['prop_id'].split('.')
        print('button_id  1:', button_id[0])
        print('n_clicks 1 :',  n_clicks)

        if button_id[0] == 'Create_NewRegim_btn':
            if n_clicks > 0:
                print('\n', '\n',"##########################  NEW REGIM:", '\n', '\n')
                # with open(main_path_data + "\\new_regims.json", "r") as file:
                file = open(main_path_data + "\\new_regims.json", "r")
                param = []
                data = json.load(file)
                file.close()
                for k, v in data.items():
                    param.append(k)

                if not param:
                    next_id = 1
                    data[next_id] = {"birga1": birga1,
                     "birga2": birga2,
                     "val1": val1,
                     "val2": val2,
                     "val3": val3,
                     "birga1_com": birga1_com,
                     "birga2_com": birga2_com,
                     "profit": profit,
                     "order": order,
                     "per": percent,
                     "avtomat": "off"
                     }
                    f = open(main_path_data + "\\new_regims.json", "w")
                    json.dump(data, f)
                    f.close()
                    list_group = [i for i in MAIN_TAB.regims()]
                    return [list_group]
                else:
                    next_id = str(int(param[-1]) + 1)
                    data[next_id] = {"birga1": birga1,
                     "birga2": birga2,
                     "val1": val1,
                     "val2": val2,
                     "val3": val3,
                     "birga1_com": birga1_com,
                     "birga2_com": birga2_com,
                     "profit": profit,
                     "order": order,
                     "per": percent,
                     "avtomat": "off"
                     }
                    f = open(main_path_data + "\\new_regims.json", "w")
                    json.dump(data, f)
                    f.close()
                    list_group = [i for i in MAIN_TAB.regims()]
                    return [list_group]
            else:
                raise PreventUpdate
        elif button_id[0] == 'On_Avtomat_btn':
            print("AVTOMAT ON")
            # with open(main_path_data + "\\new_regims.json", "r") as file:
            file = open(main_path_data + "\\new_regims.json", "r")
            data = json.load(file)
            file.close()
            for k, v in data.items():
                v['avtomat'] = 'on'

            f = open(main_path_data + "\\new_regims.json", "w")
            json.dump(data, f)
            f.close()
            list_group = [i for i in MAIN_TAB.regims()]
            return [list_group]
        elif button_id[0] == 'Off_Avtomat_btn':
            print("AVTOMAT OFF")
            # with open(main_path_data + "\\new_regims.json", "r") as file:
            file = open(main_path_data + "\\new_regims.json", "r")
            data = json.load(file)
            file.close()
            for k, v in data.items():
                v['avtomat'] = 'off'

            f = open(main_path_data + "\\new_regims.json", "w")
            json.dump(data, f)
            f.close()
            list_group = [i for i in MAIN_TAB.regims()]
            return [list_group]
        else:
            raise PreventUpdate
def creat_reg2(app: dash.Dash):

    @app.callback([Output('listcardreg2', 'children')],
        [Input('Create_NewRegim_btn_reg2', 'n_clicks'),
         Input('On_Avtomat_btn', 'n_clicks'),
         Input('Off_Avtomat_btn', 'n_clicks')],
                  [State('newval1_btn_reg2', "value"),
                   State('newval2_btn_reg2', "value"),
                   State('newval3_btn_reg2', "value"),
                   State('newbirga1_btn_reg2', "value"),
                   State('newbirga2_btn_reg2', "value"),
                   State('newbirga1_com_btn_reg2', "value"),
                   State('newbirga2_com_btn_reg2', "value"),
                   State('newprofit_btn_reg2', "value"),
                   State('neworder_com_btn_reg2', "value"),
                   State('newper_btn_reg2', "value"),
                   ])

    def create(n_clicks, n_clicks2,n_clicks3, val1, val2, val3, birga1, birga2,birga1_com, birga2_com, profit, order, percent):

        ctx = dash.callback_context
        button_id = ctx.triggered[0]['prop_id'].split('.')

        if button_id[0] == 'Create_NewRegim_btn_reg2':
            if n_clicks > 0:
                print('\n', '\n',"##########################  NEW REGIM:", '\n', '\n')
                # with open(main_path_data + "\\new_regims.json", "r") as file:
                file = open(main_path_data + "\\regims2.json", "r")
                param = []
                data = json.load(file)
                file.close()
                for k, v in data.items():
                    param.append(k)

                if not param:
                    next_id = 1
                    data[next_id] = {"birga1": birga1,
                     "birga2": birga2,
                     "val1": val1,
                     "val2": val2,
                     "val3": val3,
                     "birga1_com": birga1_com,
                     "birga2_com": birga2_com,
                     "profit": profit,
                     "order": order,
                     "per": percent,
                     "avtomat": "off"
                     }
                    f = open(main_path_data + "\\regims2.json", "w")
                    json.dump(data, f)
                    f.close()
                    list_group = [i for i in MAIN_TAB.regims2()]
                    return [list_group]
                else:
                    next_id = str(int(param[-1]) + 1)
                    data[next_id] = {"birga1": birga1,
                     "birga2": birga2,
                     "val1": val1,
                     "val2": val2,
                     "val3": val3,
                     "birga1_com": birga1_com,
                     "birga2_com": birga2_com,
                     "profit": profit,
                     "order": order,
                     "per": percent,
                     "avtomat": "off"
                     }
                    f = open(main_path_data + "\\regims2.json", "w")
                    json.dump(data, f)
                    f.close()
                    list_group = [i for i in MAIN_TAB.regims2()]
                    return [list_group]
            else:
                raise PreventUpdate
        elif button_id[0] == 'On_Avtomat_btn':
            print("AVTOMAT ON")
            # with open(main_path_data + "\\new_regims.json", "r") as file:
            file = open(main_path_data + "\\regims2.json", "r")
            data = json.load(file)
            file.close()
            for k, v in data.items():
                v['avtomat'] = 'on'

            f = open(main_path_data + "\\regims2.json", "w")
            json.dump(data, f)
            f.close()
            list_group = [i for i in MAIN_TAB.regims2()]
            return [list_group]
        elif button_id[0] == 'Off_Avtomat_btn':
            print("AVTOMAT OFF")
            # with open(main_path_data + "\\new_regims.json", "r") as file:
            file = open(main_path_data + "\\regims2.json", "r")
            data = json.load(file)
            file.close()
            for k, v in data.items():
                v['avtomat'] = 'off'

            f = open(main_path_data + "\\regims2.json", "w")
            json.dump(data, f)
            f.close()
            list_group = [i for i in MAIN_TAB.regims2()]
            return [list_group]
        else:
            raise PreventUpdate

def save_newreg_data(app: dash.Dash):
    @app.callback(
        [Output({'type': 'hidden_newreg', 'index': MATCH}, 'children'),
         Output({'type': 'Turn_Avtomat_btn', 'index': MATCH}, 'style'),
         Output({'type': 'Turn_Avtomat_btn', 'index': MATCH}, 'children')],
        [Input({'type': 'Save_NewRegim_btn', 'index': MATCH}, 'n_clicks'),
         Input({'type': 'Turn_Avtomat_btn', 'index': MATCH}, 'n_clicks'),
         Input({'type': 'Delete_NewRegim_btn', 'index': MATCH}, 'n_clicks')],
        [State({'type': 'Save_NewRegim_btn', 'index': MATCH}, 'id'),
         State({'type': 'newval1', 'index': MATCH}, "value"),
         State({'type': 'newval2', 'index': MATCH}, "value"),
         State({'type': 'newval3', 'index': MATCH}, "value"),
         State({'type': 'newbirga1', 'index': MATCH}, "value"),
         State({'type': 'newbirga2', 'index': MATCH}, "value"),
         # State({'type': 'newbirga1_com', 'index': MATCH}, "value"),
         # State({'type': 'newbirga2_com', 'index': MATCH}, "value"),
         State({'type': 'newprofit', 'index': MATCH}, "value"),
         State({'type': 'neworder_com', 'index': MATCH}, "value"),
         State({'type': 'newper', 'index': MATCH}, "value"),
         ]
    )


    def save_output(n_clicks, n_clicks2, n_clicks3, id, val1, val2, val3, birga1, birga2,profit, order, percent):
        ctx = dash.callback_context
        button_id = ctx.triggered[0]['prop_id'].split('.')

        if not ctx.triggered:
            raise dash.exceptions.PreventUpdate
        elif n_clicks> 0 or n_clicks2> 0 or n_clicks3> 0:
            pass
        else:
            raise dash.exceptions.PreventUpdate


        # print('button_id 2 :', button_id[0])

        bb = button_id[0]
        d = json.loads(bb)


        if order is None:
            order = ""
        else:
            order = order

        if percent is None:
            percent = ""
        else:
            percent = percent



        if d['type'] == 'Save_NewRegim_btn':
            print("#########     SAVED    ##############")
            a_file = open(main_path_data + "\\new_regims.json", "r")
            json_object = json.load(a_file)
            a_file.close()
            json_object[d['index']]['val1'] = val1
            json_object[d['index']]['val2'] = val2
            json_object[d['index']]['val3'] = val3
            json_object[d['index']]['birga1'] = birga1
            json_object[d['index']]['birga2'] = birga2
            # json_object[d['index']]['birga1_com'] = birga1_com
            # json_object[d['index']]['birga2_com'] = birga2_com
            json_object[d['index']]['profit'] = float(profit)
            json_object[d['index']]['order'] = order
            json_object[d['index']]['per'] = percent

            if json_object[d['index']]['avtomat'] == 'on':
                style = {'text-align': 'center',
                         "background-color": "palegreen",
                               'max-width': '50px','padding': '0',
                               'max-height': '50px',
                               'font-size': '10px'}
                butt = 'on'
            else:
                style = {'text-align': 'center',
                         "background-color": "tomato",
                         "border-radius": "20px",'padding': '0',
                               'max-width': '50px',
                               'max-height': '50px',
                               'font-size': '10px'}
                butt = 'off'

            a_file = open(main_path_data + "\\new_regims.json", "w")
            json.dump(json_object, a_file)
            a_file.close()

            return [""], style, butt
        elif d['type'] == 'Turn_Avtomat_btn':
            print("#########     AVTOMAT    ##############")
            a_file = open(main_path_data + "\\new_regims.json", "r")
            json_object = json.load(a_file)
            a_file.close()
            if json_object[d['index']]['avtomat'] == 'on':
                json_object[d['index']]['avtomat'] = 'off'
                style = {'text-align': 'center',
                         "background-color": "tomato",
                         "border-radius": "20px",'padding': '0',
                               'max-width': '50px',
                               'max-height': '50px',
                               'font-size': '10px'}
                butt = 'off'
            else:
                json_object[d['index']]['avtomat'] = 'on'
                style = {'text-align': 'center',
                         "background-color": "palegreen",
                         "border-radius": "20px",'padding': '0',
                               'max-width': '50px',
                               'max-height': '50px',
                               'font-size': '10px'}
                butt = 'on'


            a_file = open(main_path_data + "\\new_regims.json", "w")
            json.dump(json_object, a_file)
            a_file.close()
            return [""], style, butt
        elif d['type'] == 'Delete_NewRegim_btn':
            print("#########     DELETED    ##############")
            a_file = open(main_path_data + "\\new_regims.json", "r")
            json_object = json.load(a_file)
            a_file.close()

            del json_object[d['index']]
            style = {'text-align': 'center',
                     "background-color": "tomato",
                     "border-radius": "20px",'padding': '0',
                               'max-width': '50px',
                               'max-height': '50px',
                               'font-size': '10px'}
            butt = 'DELETED'
            a_file = open(main_path_data + "\\new_regims.json", "w")
            json.dump(json_object, a_file)
            a_file.close()
            return [""], style, butt
        else:
            raise dash.exceptions.PreventUpdate
def save_newreg2_data(app: dash.Dash):
    @app.callback(
        [Output({'type': 'hidden_newreg_reg2', 'index': MATCH}, 'children'),
         Output({'type': 'Turn_Avtomat_btn_reg2', 'index': MATCH}, 'style'),
         Output({'type': 'Turn_Avtomat_btn_reg2', 'index': MATCH}, 'children')],
        [Input({'type': 'Save_NewRegim_btn_reg2', 'index': MATCH}, 'n_clicks'),
         Input({'type': 'Turn_Avtomat_btn_reg2', 'index': MATCH}, 'n_clicks'),
         Input({'type': 'Delete_NewRegim_btn_reg2', 'index': MATCH}, 'n_clicks')],
        [State({'type': 'Save_NewRegim_btn_reg2', 'index': MATCH}, 'id'),
         State({'type': 'newval1_reg2', 'index': MATCH}, "value"),
         State({'type': 'newval2_reg2', 'index': MATCH}, "value"),
         State({'type': 'newval3_reg2', 'index': MATCH}, "value"),
         State({'type': 'newbirga1_reg2', 'index': MATCH}, "value"),
         State({'type': 'newbirga2_reg2', 'index': MATCH}, "value"),
         # State({'type': 'newbirga1_com', 'index': MATCH}, "value"),
         # State({'type': 'newbirga2_com', 'index': MATCH}, "value"),
         State({'type': 'newprofit_reg2', 'index': MATCH}, "value"),
         State({'type': 'neworder_com_reg2', 'index': MATCH}, "value"),
         State({'type': 'newper_reg2', 'index': MATCH}, "value"),
         ]
    )


    def save_output(n_clicks, n_clicks2, n_clicks3, id, val1, val2, val3, birga1, birga2,profit, order, percent):
        ctx = dash.callback_context
        button_id = ctx.triggered[0]['prop_id'].split('.')

        if not ctx.triggered:
            raise dash.exceptions.PreventUpdate
        elif n_clicks> 0 or n_clicks2> 0 or n_clicks3> 0:
            pass
        else:
            raise dash.exceptions.PreventUpdate


        bb = button_id[0]
        d = json.loads(bb)


        if order is None:
            order = ""
        else:
            order = order

        if percent is None:
            percent = ""
        else:
            percent = percent



        if d['type'] == 'Save_NewRegim_btn_reg2':
            print("#########     SAVED    ##############")
            a_file = open(main_path_data + "\\regims2.json", "r")
            json_object = json.load(a_file)
            a_file.close()
            json_object[d['index']]['val1'] = val1
            json_object[d['index']]['val2'] = val2
            json_object[d['index']]['val3'] = val3
            json_object[d['index']]['birga1'] = birga1
            json_object[d['index']]['birga2'] = birga2
            # json_object[d['index']]['birga1_com'] = birga1_com
            # json_object[d['index']]['birga2_com'] = birga2_com
            json_object[d['index']]['profit'] = float(profit)
            json_object[d['index']]['order'] = order
            json_object[d['index']]['per'] = percent

            if json_object[d['index']]['avtomat'] == 'on':
                style = {'text-align': 'center',
                         "background-color": "palegreen",
                               'max-width': '50px','padding': '0',
                               'max-height': '50px',
                               'font-size': '10px'}
                butt = 'on'
            else:
                style = {'text-align': 'center',
                         "background-color": "tomato",
                         "border-radius": "20px",'padding': '0',
                               'max-width': '50px',
                               'max-height': '50px',
                               'font-size': '10px'}
                butt = 'off'

            a_file = open(main_path_data + "\\regims2.json", "w")
            json.dump(json_object, a_file)
            a_file.close()

            return [""], style, butt
        elif d['type'] == 'Turn_Avtomat_btn_reg2':
            print("#########     AVTOMAT  2  ##############")
            a_file = open(main_path_data + "\\regims2.json", "r")
            json_object = json.load(a_file)
            a_file.close()
            if json_object[d['index']]['avtomat'] == 'on':
                json_object[d['index']]['avtomat'] = 'off'
                style = {'text-align': 'center',
                         "background-color": "tomato",
                         "border-radius": "20px",'padding': '0',
                               'max-width': '50px',
                               'max-height': '50px',
                               'font-size': '10px'}
                butt = 'off'
            else:
                json_object[d['index']]['avtomat'] = 'on'
                style = {'text-align': 'center',
                         "background-color": "palegreen",
                         "border-radius": "20px",'padding': '0',
                               'max-width': '50px',
                               'max-height': '50px',
                               'font-size': '10px'}
                butt = 'on'


            a_file = open(main_path_data + "\\regims2.json", "w")
            json.dump(json_object, a_file)
            a_file.close()
            return [""], style, butt
        elif d['type'] == 'Delete_NewRegim_btn_reg2':
            print("#########     DELETED    ##############")
            a_file = open(main_path_data + "\\regims2.json", "r")
            json_object = json.load(a_file)
            a_file.close()

            del json_object[d['index']]
            style = {'text-align': 'center',
                     "background-color": "tomato",
                     "border-radius": "20px",'padding': '0',
                               'max-width': '50px',
                               'max-height': '50px',
                               'font-size': '10px'}
            butt = 'DELETED'
            a_file = open(main_path_data + "\\regims2.json", "w")
            json.dump(json_object, a_file)
            a_file.close()
            return [""], style, butt
        else:
            raise dash.exceptions.PreventUpdate


def ref_balance(app: dash.Dash):
    @app.callback(
        [Output('BALANCE-content', 'children')],
        [Input('Ref_balance_btn', 'n_clicks')])
    def display_output(n_clicks):

        if n_clicks is None:
            raise PreventUpdate
        elif n_clicks > 0:
            print("REFRESHED BALANCE")
            refBalance.NewBalance()
            return ["0"]
        else:
            raise PreventUpdate









# def commis(app: dash.Dash):
#     ###############################    ADD Commis     ########################################
#     @app.callback(
#         dash.dependencies.Output('output-alpha', 'children'),
#         [dash.dependencies.Input('Alpha_btn', 'n_clicks')],
#         [dash.dependencies.State('Alpha_com', 'value')])
#     def update_Alpha(n_clicks, value):
#         if n_clicks is None:
#             raise PreventUpdate
#
#         main_path_data = os.path.abspath("./data")
#         f = open(main_path_data + "\\commis.json")
#         compp = json.load(f)
#         f.close()
#
#         compp['main']["alfa"] = float(value)
#
#         f = open(main_path_data + "\\commis.json", "w")
#         json.dump(compp, f)
#         f.close()
#
#         return "{}".format(value)
#
#     ###############################    ADD Commis     ########################################
#     @app.callback(
#         dash.dependencies.Output('output-live', 'children'),
#         [dash.dependencies.Input('Live_btn', 'n_clicks')],
#         [dash.dependencies.State('Live_com', 'value')])
#     def update_Alpha(n_clicks, value):
#         if n_clicks is None:
#             raise PreventUpdate
#         main_path_data = os.path.abspath("./data")
#         f = open(main_path_data + "\\commis.json")
#         compp = json.load(f)
#         f.close()
#
#         compp['main']["live"] = float(value)
#
#         f = open(main_path_data + "\\commis.json", "w")
#         json.dump(compp, f)
#         f.close()
#
#         return "{}".format(value)
#
#
#     ###############################    ADD Commis     ########################################
#     @app.callback(
#         dash.dependencies.Output('output-hot', 'children'),
#         [dash.dependencies.Input('Hot_btn', 'n_clicks')],
#         [dash.dependencies.State('Hot_com', 'value')])
#     def update_Alpha(n_clicks, value):
#         if n_clicks is None:
#             raise PreventUpdate
#         main_path_data = os.path.abspath("./data")
#         f = open(main_path_data + "\\commis.json")
#         compp = json.load(f)
#         f.close()
#
#         compp['main']["hot"] = float(value)
#
#         f = open(main_path_data + "\\commis.json", "w")
#         json.dump(compp, f)
#         f.close()
#
#         return "{}".format(value)
#
# def save_reg_data(app: dash.Dash):
#     @app.callback(
#         [Output({'type': 'option', 'index': MATCH}, 'children')],
#        [Input({'type': 'checklist', 'index': MATCH}, 'value')],
#         [State({'type': 'checklist', 'index': MATCH}, 'id'),
#
#          State({'type': 'val1', 'index': MATCH}, "value"),
#          State({'type': 'val2', 'index': MATCH}, "value"),
#          State({'type': 'val3', 'index': MATCH}, "value"),
#          State({'type': 'birga1', 'index': MATCH}, "value"),
#          State({'type': 'birga2', 'index': MATCH}, "value"),
#
#          State({'type': 'profit', 'index': MATCH}, "value"),
#          State({'type': 'order', 'index': MATCH}, "value"),
#          State({'type': 'percent', 'index': MATCH}, "value"),
#          State({'type': 'avtomat', 'index': MATCH}, "value"),
#          ]
#     )
#     def display_output(value,id, val1, val2, val3, birga1, birga2, profit, order, percent, avtomat):
#         ctx = dash.callback_context
#
#         if not ctx.triggered:
#             raise dash.exceptions.PreventUpdate
#         else:
#             pass
#
#         if order is None:
#             order = ""
#         else:
#             order = float(order)
#
#         if percent is None:
#             percent = ""
#         else:
#             percent = percent
#
#         if not value:
#             # Change "option" in Regim
#
#             print("#########     OFF    ##############")
#
#
#
#             a_file = open(main_path_data + "\\regim.json", "r")
#             json_object = json.load(a_file)
#             a_file.close()
#
#
#
#             json_object[id['index']]['option'] = "OFF"
#             print("  REGIM JSON :", '\n', json_object)
#
#             a_file = open(main_path_data + "\\regim.json", "w")
#             json.dump(json_object, a_file)
#             a_file.close()
#
#             return ["{}".format(json_object[id['index']]['option'])]
#
#         else:
#
#             print ("#########     ON    ##############")
#
#             a_file = open(main_path_data + "\\regim.json", "r")
#             json_object = json.load(a_file)
#             a_file.close()
#
#
#             json_object[id['index']]['avtomat'] = avtomat
#             json_object[id['index']]['option'] = "active"
#             json_object[id['index']]['val1'] = val1
#             json_object[id['index']]['val2'] = val2
#             json_object[id['index']]['val3'] = val3
#             json_object[id['index']]['birga1'] = birga1
#             json_object[id['index']]['birga2'] = birga2
#             json_object[id['index']]['profit'] = float(profit)
#             json_object[id['index']]['order'] = order
#             json_object[id['index']]['per'] = percent
#             print("  REGIM JSON :", '\n', json_object)
#
#             a_file = open(main_path_data + "\\regim.json", "w")
#             json.dump(json_object, a_file)
#             a_file.close()
#
#             return ["{}".format(json_object[id['index']]['option'])]
#
# def ref_key_data(app: dash.Dash):
#     @app.callback(
#
#         [Output('tab_keys88', 'children')],
#         [Input('ref_keys_btn', 'n_clicks')])
#     def display_output(n_clicks):
#
#         if n_clicks is None:
#             raise PreventUpdate
#
#         else:
#             tab = layouts.tab_keys()
#             return [tab]
#
# def del_rgm_data(app: dash.Dash):
#     @app.callback(
#
#         [Output({'type': 'rgm_block', 'index': MATCH}, 'children')],
#         [Input({'type': 'delet_rgm_btn', 'index': MATCH}, 'n_clicks')],
#         [State({'type': 'delet_rgm_btn', 'index': MATCH}, 'id')])
#
#     def display_output(n_clicks, id):
#
#         ctx = dash.callback_context
#
#         if not ctx.triggered:
#             raise dash.exceptions.PreventUpdate
#         else:
#             pass
#         if n_clicks > 0:
#
#             print("DELETE BTN #########################", id['index'])
#
#             a_file = open(main_path_data + "\\regim.json", "r")
#             json_object = json.load(a_file)
#             a_file.close()
#
#             json_object.pop(id['index'])
#             a_file = open(main_path_data + "\\regim.json", "w")
#             json.dump(json_object, a_file)
#             a_file.close()
#             return [ddk.Block('ПУСТО')]
#
# def new_order(app: dash.Dash):
#
#     @app.callback(
#         [Output({'type': 'uorder_result', 'index': MATCH}, 'children')],
#         [Input({'type': 'uorder_btn', 'index': MATCH}, 'n_clicks')],
#         [dash.dependencies.State({'type': 'uorder_btn', 'index': MATCH}, 'id'),
#          dash.dependencies.State({'type': 'ubirga_1', 'index': MATCH}, 'children'),
#          dash.dependencies.State({'type': 'ubirga_2', 'index': MATCH}, 'children'),
#          dash.dependencies.State({'type': 'uval1', 'index': MATCH}, 'children'),
#          dash.dependencies.State({'type': 'uval2', 'index': MATCH}, 'children'),
#          dash.dependencies.State({'type': 'uval3', 'index': MATCH}, 'children'),
#          dash.dependencies.State({'type': 'uval4', 'index': MATCH}, 'children'),
#          dash.dependencies.State({'type': 'uval1_vol', 'index': MATCH}, 'children'),
#          dash.dependencies.State({'type': 'uval2_vol', 'index': MATCH}, 'children'),
#          dash.dependencies.State({'type': 'uval3_vol', 'index': MATCH}, 'children'),
#          dash.dependencies.State({'type': 'uval4_vol', 'index': MATCH}, 'children'),
#          dash.dependencies.State({'type': 'urate1', 'index': MATCH}, 'children'),
#          dash.dependencies.State({'type': 'urate2', 'index': MATCH}, 'children'),
#          dash.dependencies.State({'type': 'uregim', 'index': MATCH}, 'children'),
#          ])
#
#     def display_output2(n_clicks,
#                         id, birga_1, birga_2,
#                        val1, val2, val3, val4, val1_vol,
#                        val2_vol, val3_vol, val4_vol,
#                         rate1, rate2,regims):
#
#         ctx = dash.callback_context
#         if not ctx.triggered:
#             raise dash.exceptions.PreventUpdate
#         else:
#             now = dt.datetime.now()
#             df_all = pd.read_csv(main_path_data + "\\all_data.csv")
#             timer = now.strftime("%H:%M:%S")
#             df2 = pd.DataFrame({"TIME": [timer],
#                                 "birga_x": [birga_1],
#                                 "birga_y": [birga_2],
#                                 "rates_x": [rate1],
#                                 "rates_y": [rate2],
#                                 "valin_x": [val1],
#                                 "valin_y": [val2],
#                                 "valout_y": [val4],
#                                 "start": [val1_vol],
#                                 "step": [val2_vol],
#                                 "back": [val4_vol],
#                                 "profit": [(val4_vol - val1_vol)],
#                                 "perc": [(((val4_vol - val1_vol) / val1_vol) * 100)],
#                                 }, index=[0])
#             df_all = df2.append(df_all)
#             df_all.to_csv(main_path_data + "\\all_data.csv", header=True, index=False)
#             valutadf = pd.read_csv(main_path_data + "\\balance.csv")
#
#
#             filter1 = valutadf[valutadf['Valuta'] == val1]
#             filter3 = valutadf[valutadf['Valuta'] == val3]
#
#             a_file = open(main_path_data + "\\regim.json", "r")
#             regim = json.load(a_file)
#             a_file.close()
#
#
#             parametr1 = "{}/{}".format(val1, val2)
#             para1 = ['BTC/USD','LTC/USD','ETH/USD','XRP/USD','USDT/USD','BTC/USDT','ETH/USDT','XRP/BTC','ETH/BTC','LTC/BTC','BCH/BTC','ZEC/BTC', 'PZM/USD', 'PZM/USDT', 'PZM/BTC',]
#
#             for i in para1:
#                 if i == parametr1:
#                     parad = "ok"
#                     pass
#                 else:
#                     parad = "no"
#                     pass
#
#
#
#             if parad == 'ok':
#                 kurs = (float(rate1) / float(val1_vol))
#                 kurs2 = (float(val3_vol) / float(val4_vol))
#                 kurs0 = (float(val2_vol) / float(val1_vol))
#                 minA = regim[regims]["order"]
#                 minB = minA * kurs0
#
#                 minbeta = (((float(val1_vol) - float(val2_vol) * float(rate1)) / (
#                             float(val2_vol) * float(rate1))) * 100)
#                 minbeta = Context(prec=3, rounding=ROUND_UP).create_decimal(minbeta)
#                 minbeta = float(minbeta)
#
# ################################################################################################################
#                 if filter1.iloc[0][birga_1] > val1_vol and filter3.iloc[0][birga_2] > val3_vol:
#
#                     if val1 == 'USD' or val1 == 'USDT' or val2 == 'USD' or val2 == 'USDT':
#                         if birga_1 == 'alfa' and birga_2 == 'live':
#                             if val2 != 'USD' or val2 != 'USDT':
#                                 val2_vol = val2_vol + (val2_vol * minbeta / 100)
#                                 reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
#                                 reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                             else:
#                                 reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
#                                 reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                         elif birga_1 == 'live' and birga_2 == 'alfa':
#                             if val2 != 'USD' or val2 != 'USDT':
#                                 reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
#                                 reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                             else:
#                                 reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
#                                 reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                         elif birga_1 == 'alfa' and birga_2 == 'hot':
#                             if val2 != 'USD' or val2 != 'USDT':
#                                 val2_vol = val2_vol + (val2_vol * minbeta / 100)
#                                 reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
#                                 reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                             else:
#                                 reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
#                                 reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                         elif birga_1 == 'hot' and birga_2 == 'alfa':
#                             if val2 != 'USD' or val2 != 'USDT':
#                                 reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
#                                 reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                             else:
#                                 reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
#                                 reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                         elif birga_1 == 'hot' and birga_2 == 'live':
#                             if val2 != 'USD' or val2 != 'USDT':
#                                 reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
#                                 reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                             else:
#                                 reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
#                                 reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                         elif birga_1 == 'live' and birga_2 == 'hot':
#                             if val2 != 'USD' or val2 != 'USDT':
#                                 reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
#                                 reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                             else:
#                                 reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
#                                 reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                         else:
#                             return ["No Such Command"]
#                     elif val1 != 'USD' or val1 != 'USDT' or val2 != 'USD' or val2 != 'USDT':
#                         if birga_1 == 'alfa' and birga_2 == 'live':
#                             if val2 != "BTC":
#                                 val2_vol = val2_vol + (val2_vol * minbeta / 100)
#                                 reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
#                                 reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                             else:
#                                 reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
#                                 reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                         elif birga_1 == 'live' and birga_2 == 'alfa':
#                             if val2 != "BTC":
#                                 reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
#                                 reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                             else:
#                                 reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
#                                 reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                         elif birga_1 == 'alfa' and birga_2 == 'hot':
#                             if val2 != "BTC":
#                                 val2_vol = val2_vol + (val2_vol * minbeta / 100)
#                                 reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
#                                 reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                             else:
#                                 reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
#                                 reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                         elif birga_1 == 'hot' and birga_2 == 'alfa':
#                             if val2 != "BTC":
#                                 reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
#                                 reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
#                                 return ["{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                             else:
#                                 reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
#                                 reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                         elif birga_1 == 'hot' and birga_2 == 'live':
#                             if val2 != "BTC":
#                                 reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
#                                 reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                             else:
#                                 reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
#                                 reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                         elif birga_1 == 'live' and birga_2 == 'hot':
#                             if val2 != "BTC":
#                                 reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
#                                 reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                             else:
#                                 reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
#                                 reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                         else:
#                             return ["No Such Command"]
#
#
# ################################################################################################################
#                 elif filter1.iloc[0][birga_1] < val1_vol and filter3.iloc[0][birga_2] > minB and filter1.iloc[0][birga_1] > minA or \
#                         filter3.iloc[0][birga_2] < val3_vol and filter3.iloc[0][birga_2] > minB and filter1.iloc[0][birga_1] > minA:
#
#                     minOrder1 = float(filter1.iloc[0][birga_1] * kurs)
#                     minOrder2 = float(filter3.iloc[0][birga_2])
#                     if minOrder2 > minOrder1:
#                         val1_vol = filter1.iloc[0][birga_1]
#                         val2_vol = minOrder1
#                         val3_vol = minOrder1
#                         val4_vol = minOrder1/kurs2
#
#                         if val1 == 'USD' or val1 == 'USDT' or val2 == 'USD' or val2 == 'USDT':
#                             if birga_1 == 'alfa' and birga_2 == 'live':
#                                 if val2 != 'USD' or val2 != 'USDT':
#                                     val2_vol = val2_vol + (val2_vol * minbeta / 100)
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'live' and birga_2 == 'alfa':
#                                 if val2 != 'USD' or val2 != 'USDT':
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'alfa' and birga_2 == 'hot':
#                                 if val2 != 'USD' or val2 != 'USDT':
#                                     val2_vol = val2_vol + (val2_vol * minbeta / 100)
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'hot' and birga_2 == 'alfa':
#                                 if val2 != 'USD' or val2 != 'USDT':
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'hot' and birga_2 == 'live':
#                                 if val2 != 'USD' or val2 != 'USDT':
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'live' and birga_2 == 'hot':
#                                 if val2 != 'USD' or val2 != 'USDT':
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             else:
#                                 return ["No Such Command"]
#                         elif val1 != 'USD' or val1 != 'USDT' or val2 != 'USD' or val2 != 'USDT':
#                             if birga_1 == 'alfa' and birga_2 == 'live':
#                                 if val2 != "BTC":
#                                     val2_vol = val2_vol + (val2_vol * minbeta / 100)
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'live' and birga_2 == 'alfa':
#                                 if val2 != "BTC":
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'alfa' and birga_2 == 'hot':
#                                 if val2 != "BTC":
#                                     val2_vol = val2_vol + (val2_vol * minbeta / 100)
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'hot' and birga_2 == 'alfa':
#                                 if val2 != "BTC":
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'hot' and birga_2 == 'live':
#                                 if val2 != "BTC":
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'live' and birga_2 == 'hot':
#                                 if val2 != "BTC":
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             else:
#                                 return ["No Such Command"]
#                     elif minOrder2 < minOrder1:
#                         val1_vol = minOrder2 / kurs
#                         val2_vol = minOrder2
#                         val3_vol = minOrder2
#                         val4_vol = minOrder2 / kurs2
#
#
#                         if val1 == 'USD' or val1 == 'USDT' or val2 == 'USD' or val2 == 'USDT':
#                             if birga_1 == 'alfa' and birga_2 == 'live':
#                                 if val2 != 'USD' or val2 != 'USDT':
#                                     val2_vol = val2_vol + (val2_vol * minbeta / 100)
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'live' and birga_2 == 'alfa':
#                                 if val2 != 'USD' or val2 != 'USDT':
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'alfa' and birga_2 == 'hot':
#                                 if val2 != 'USD' or val2 != 'USDT':
#                                     val2_vol = val2_vol + (val2_vol * minbeta / 100)
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'hot' and birga_2 == 'alfa':
#                                 if val2 != 'USD' or val2 != 'USDT':
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'hot' and birga_2 == 'live':
#                                 if val2 != 'USD' or val2 != 'USDT':
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'live' and birga_2 == 'hot':
#                                 if val2 != 'USD' or val2 != 'USDT':
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             else:
#                                 return ["No Such Command"]
#                         elif val1 != 'USD' or val1 != 'USDT' or val2 != 'USD' or val2 != 'USDT':
#                             if birga_1 == 'alfa' and birga_2 == 'live':
#                                 if val2 != "BTC":
#                                     val2_vol = val2_vol + (val2_vol * minbeta / 100)
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'live' and birga_2 == 'alfa':
#                                 if val2 != "BTC":
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'alfa' and birga_2 == 'hot':
#                                 if val2 != "BTC":
#                                     val2_vol = val2_vol + (val2_vol * minbeta / 100)
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'hot' and birga_2 == 'alfa':
#                                 if val2 != "BTC":
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'hot' and birga_2 == 'live':
#                                 if val2 != "BTC":
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'live' and birga_2 == 'hot':
#                                 if val2 != "BTC":
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             else:
#                                 return ["No Such Command"]
#                     else:
#                         return ["Not Enough Money"]
#
#
#
#
# ################################################################################################################
#                 elif filter1.iloc[0][birga_1] < minA or filter3.iloc[0][birga_2] < minB:
#                     return ["Not Enough Money"]
#                 else:
#                     return ["Not Enough Money"]
#             elif parad == 'no':
#                 kurs = (float(val1_vol) * float(val2_vol))
#                 kurs2 = (float(val4_vol) / float(val3_vol))
#                 kurs0 = (float(val1_vol) / float(val2_vol))
#                 minB = regim[regims]["order"]
#                 minA = minB * kurs0
#
#                 minbeta = (((float(val1_vol) - float(val2_vol) * float(rate1)) / (
#                         float(val2_vol) * float(rate1))) * 100)
#                 minbeta = Context(prec=3, rounding=ROUND_UP).create_decimal(minbeta)
#                 minbeta = float(minbeta)
#                 min1 = (float(filter1.iloc[0][birga_1]) - (float(filter1.iloc[0][birga_1]) * minbeta / 100)) / float(rate1)
#                 min2 = float(filter3.iloc[0][birga_2])
#
#
# ################################################################################################################
#                 if filter1.iloc[0][birga_1] > val1_vol and filter3.iloc[0][birga_2] > val3_vol:
#                     if val1 == 'USD' or val1 == 'USDT' or val2 == 'USD' or val2 == 'USDT':
#                         if birga_1 == 'alfa' and birga_2 == 'live':
#                             if val2 != 'USD' or val2 != 'USDT':
#                                 val2_vol = val2_vol + (val2_vol * minbeta / 100)
#                                 reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
#                                 reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                             else:
#                                 reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
#                                 reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                         elif birga_1 == 'live' and birga_2 == 'alfa':
#                             if val2 != 'USD' or val2 != 'USDT':
#                                 reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
#                                 reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                             else:
#                                 val4_vol = val4_vol + (val4_vol * minbeta / 100)
#                                 reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
#                                 reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                         elif birga_1 == 'alfa' and birga_2 == 'hot':
#                             if val2 != 'USD' or val2 != 'USDT':
#                                 val2_vol = val2_vol + (val2_vol * minbeta / 100)
#                                 reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
#                                 reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                             else:
#                                 reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
#                                 reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                         elif birga_1 == 'hot' and birga_2 == 'alfa':
#                             if val2 != 'USD' or val2 != 'USDT':
#                                 reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
#                                 reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                             else:
#                                 val4_vol = val4_vol + (val4_vol * minbeta / 100)
#                                 reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
#                                 reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                         elif birga_1 == 'hot' and birga_2 == 'live':
#                             if val2 != 'USD' or val2 != 'USDT':
#                                 reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
#                                 reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                             else:
#                                 reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
#                                 reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                         elif birga_1 == 'live' and birga_2 == 'hot':
#                             if val2 != 'USD' or val2 != 'USDT':
#                                 reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
#                                 reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                             else:
#                                 reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
#                                 reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                         else:
#                             return ["No Such Command"]
#                     elif val1 != 'USD' or val1 != 'USDT' or val2 != 'USD' or val2 != 'USDT':
#                         if birga_1 == 'alfa' and birga_2 == 'live':
#                             if val2 != "BTC":
#                                 val2_vol = val2_vol + (val2_vol * minbeta / 100)
#                                 reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
#                                 reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                             else:
#                                 reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
#                                 reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                         elif birga_1 == 'live' and birga_2 == 'alfa':
#                             if val2 != "BTC":
#                                 reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
#                                 reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                             else:
#                                 val4_vol = val4_vol + (val4_vol * minbeta / 100)
#                                 reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
#                                 reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                         elif birga_1 == 'alfa' and birga_2 == 'hot':
#                             if val2 != "BTC":
#                                 val2_vol = val2_vol + (val2_vol * minbeta / 100)
#                                 reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
#                                 reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                             else:
#                                 reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
#                                 reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                         elif birga_1 == 'hot' and birga_2 == 'alfa':
#                             if val2 != "BTC":
#                                 reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
#                                 reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                             else:
#                                 val4_vol = val4_vol + (val4_vol * minbeta / 100)
#                                 reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
#                                 reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                         elif birga_1 == 'hot' and birga_2 == 'live':
#                             if val2 != "BTC":
#                                 reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
#                                 reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                             else:
#                                 reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
#                                 reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                         elif birga_1 == 'live' and birga_2 == 'hot':
#                             if val2 != "BTC":
#                                 reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
#                                 reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                             else:
#                                 reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
#                                 reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
#                                 return [
#                                     "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                         else:
#                             return ["No Such Command"]
#
#
#
#
# ################################################################################################################
#                 elif filter1.iloc[0][birga_1] < val1_vol and filter3.iloc[0][birga_2] > minB and filter1.iloc[0][birga_1] > minA or filter3.iloc[0][birga_2] < val3_vol and filter3.iloc[0][birga_2] > minB and filter1.iloc[0][birga_1] > minA:
#
#                     if min2 > min1:
#                         val1_vol = filter1.iloc[0][birga_1]
#                         val2_vol = min1
#                         val3_vol = min1
#                         val4_vol = min1 * kurs2
#
#                         if val1 == 'USD' or val1 == 'USDT' or val2 == 'USD' or val2 == 'USDT':
#                             if birga_1 == 'alfa' and birga_2 == 'live':
#                                 if val2 != 'USD' or val2 != 'USDT':
#                                     val2_vol = val2_vol + (val2_vol * minbeta / 100)
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'live' and birga_2 == 'alfa':
#                                 # val3_vol = min1 - (min1 * minbeta / 100)
#                                 if val2 != 'USD' or val2 != 'USDT':
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     val4_vol = val4_vol + (val4_vol * minbeta / 100)
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'alfa' and birga_2 == 'hot':
#                                 if val2 != 'USD' or val2 != 'USDT':
#                                     val2_vol = val2_vol + (val2_vol * minbeta / 100)
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'hot' and birga_2 == 'alfa':
#                                 # val3_vol = min1 - (min1 * minbeta / 100)
#                                 if val2 != 'USD' or val2 != 'USDT':
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                                 else:
#                                     val4_vol = val4_vol + (val4_vol * minbeta / 100)
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'hot' and birga_2 == 'live':
#                                 if val2 != 'USD' or val2 != 'USDT':
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'live' and birga_2 == 'hot':
#                                 if val2 != 'USD' or val2 != 'USDT':
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             else:
#                                 return ["No Such Command"]
#                         elif val1 != 'USD' or val1 != 'USDT' or val2 != 'USD' or val2 != 'USDT':
#                             if birga_1 == 'alfa' and birga_2 == 'live':
#                                 if val2 != "BTC":
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'live' and birga_2 == 'alfa':
#                                 val3_vol = min1 - (min1 * minbeta / 100)
#                                 if val2 != "BTC":
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'alfa' and birga_2 == 'hot':
#                                 if val2 != "BTC":
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'hot' and birga_2 == 'alfa':
#                                 val3_vol = min1 - (min1 * minbeta / 100)
#                                 if val2 != "BTC":
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'hot' and birga_2 == 'live':
#                                 if val2 != "BTC":
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'live' and birga_2 == 'hot':
#                                 if val2 != "BTC":
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             else:
#                                 return ["No Such Command"]
#                     elif min2 < min1:
#                         val1_vol = (float(filter3.iloc[0][birga_2]) + (float(filter3.iloc[0][birga_2]) * minbeta / 100)) * float(rate1)
#                         val2_vol = float(filter3.iloc[0][birga_2])
#                         val3_vol = float(filter3.iloc[0][birga_2])
#                         val4_vol = float(filter3.iloc[0][birga_2]) * kurs2
#
#                         if val1 == 'USD' or val1 == 'USDT' or val2 == 'USD' or val2 == 'USDT':
#                             if birga_1 == 'alfa' and birga_2 == 'live':
#                                 if val2 != 'USD' or val2 != 'USDT':
#                                     val2_vol = val2_vol + (val2_vol * minbeta / 100)
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'live' and birga_2 == 'alfa':
#                                 if val2 != 'USD' or val2 != 'USDT':
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     val4_vol = val4_vol + (val4_vol * minbeta / 100)
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'alfa' and birga_2 == 'hot':
#                                 if val2 != 'USD' or val2 != 'USDT':
#                                     val2_vol = val2_vol + (val2_vol * minbeta / 100)
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'hot' and birga_2 == 'alfa':
#                                 if val2 != 'USD' or val2 != 'USDT':
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                                 else:
#                                     val4_vol = val4_vol + (val4_vol * minbeta / 100)
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'hot' and birga_2 == 'live':
#                                 if val2 != 'USD' or val2 != 'USDT':
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'live' and birga_2 == 'hot':
#                                 if val2 != 'USD' or val2 != 'USDT':
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             else:
#                                 return ["No Such Command"]
#                         elif val1 != 'USD' or val1 != 'USDT' or val2 != 'USD' or val2 != 'USDT':
#                             if birga_1 == 'alfa' and birga_2 == 'live':
#                                 if val2 != "BTC":
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'live' and birga_2 == 'alfa':
#                                 if val2 != "BTC":
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'alfa' and birga_2 == 'hot':
#                                 if val2 != "BTC":
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'hot' and birga_2 == 'alfa':
#                                 if val2 != "BTC":
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'hot' and birga_2 == 'live':
#                                 if val2 != "BTC":
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             elif birga_1 == 'live' and birga_2 == 'hot':
#                                 if val2 != "BTC":
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                                 else:
#                                     reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
#                                     reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
#                                     return [
#                                         "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
#                                                                            reponse_b2)]
#                             else:
#                                 return ["No Such Command"]
#                     else:
#                         return ["Not Enough Money"]
#
#
# ################################################################################################################
#                 elif filter1.iloc[0][birga_1] < minA or filter3.iloc[0][birga_2] < minB:
#                     return ["Not Enough Money"]
#                 else:
#                     return ["Not Enough Money"]
#
# def test_order(app: dash.Dash):
#
#     @app.callback(
#         [Output({'type': 'show_test_order', 'index': MATCH}, 'children')],
#         [dash.dependencies.Input({'type': 'tbuy_btn', 'index': MATCH}, 'n_clicks'),
#          dash.dependencies.Input({'type': 'tsell_btn', 'index': MATCH}, 'n_clicks')],
#         [dash.dependencies.State({'type': 'tamount', 'index': MATCH}, 'value'),
#          dash.dependencies.State({'type': 'tprice', 'index': MATCH}, 'value'),
#          dash.dependencies.State({'type': 'tbuy_btn', 'index': MATCH}, 'id'),
#          dash.dependencies.State({'type': 'tsell_btn', 'index': MATCH}, 'id')])
#
#     def display_output2(n_clicks, n,
#                        val1, val2, idbuy, idsell):
#
#         ctx = dash.callback_context
#
#         if not ctx.triggered:
#             raise dash.exceptions.PreventUpdate
#
#         else:
#             button_id = ctx.triggered[0]['prop_id'].split('.')[0]
#             res = json.loads(button_id)
#             if res['index'] == '1':
#                 if res['type'] == 'tbuy_btn':
#                     reponse_b1 = Orders.alfa('USD', 'BTC', val2, val1)
#                     return [reponse_b1]
#                 else:
#                     reponse_b1 = Orders.alfa('BTC', 'USD', val2, val1)
#                     return [reponse_b1]
#             elif res['index'] == '2':
#                 if res['type'] == 'tbuy_btn':
#                     reponse_b1 = Orders.live("USD", "BTC", val2, val1)
#                     return [reponse_b1]
#                 else:
#                     reponse_b1 = Orders.live('BTC', 'USD', val2, val1)
#                     return [reponse_b1]
#             elif res['index'] == '3':
#                 if res['type'] == 'tbuy_btn':
#                     reponse_b1 = Orders.hot('USD', 'BTC', str(val2), str(val1))
#                     return [reponse_b1]
#                 else:
#                     reponse_b1 = Orders.hot('BTC', 'USD', str(val2), str(val1))
#                     return [reponse_b1]

refresh(dash_app)
refresh2(dash_app)
save_key_data(dash_app)
creat_reg(dash_app)
creat_reg2(dash_app)
save_newreg_data(dash_app)
save_newreg2_data(dash_app)
ref_balance(dash_app)




# commis(dash_app)
# save_reg_data(dash_app)
#
# ref_key_data(dash_app)
# del_rgm_data(dash_app)
# new_order(dash_app)
# test_order(dash_app)