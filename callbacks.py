from dash.dependencies import Input, Output, State, MATCH
from app import dash_app, dash_db
import dash_html_components as html
import VILKA
from dash.exceptions import PreventUpdate
from dash_database import DashDatabase
import dash
import os
import json
import dash_design_kit as ddk
import layouts
import pandas as pd
import New_chains
import time
import Orders
import datetime as dt
import requests
import base64
from decimal import ROUND_UP,Context

dash_app.config['suppress_callback_exceptions'] = True
main_path_data = os.path.abspath("./data")
# Encode the local sound file.
sound_filename = (main_path_data + "\\signal.mp3")  # replace with your own .mp3 file
encoded_sound = base64.b64encode(open(sound_filename, 'rb').read())



def bot_sendtext(bot_message):
    ##########################    Telegram    ################################

    ad = open(main_path_data + "\\keys.json", "r")
    js_object = json.load(ad)
    ad.close()
    input1 = js_object["4"]['key']
    input2 = js_object["4"]['api']

    ### Send text message
    bot_token = input1
    bot_chatID = input2
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    requests.get(send_text)
    return
def all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol, reponse_b1, reponse_b2):
    ###################    APPEND to CSV   all_data    #####################
    import time
    if reponse_b1 != 'Not Enough Money' or reponse_b2 != 'Not Enough Money':
        now = dt.datetime.now()
        done = int(round(time.time() * 1000))
        df_all = pd.read_csv(main_path_data + "\\all_data.csv")
        timer2 = now.strftime("%H:%M:%S")
        df2 = pd.DataFrame({"TIME": [timer2],
                            "birga_x": [birga_1],
                            "birga_y": [birga_2],
                            "rates_x": [rate1],
                            "rates_y": [rate2],
                            "valin_x": [val1],
                            "valin_y": [val2],
                            "valout_y": [val4],
                            "start": [val1_vol],
                            "step": [val2_vol],
                            "back": [val4_vol],
                            "profit": [(float(val4_vol) - float(val1_vol))],
                            "perc": [(((float(val4_vol) - float(val1_vol)) / float(val1_vol)) * 100)],
                            "res_birga1": [reponse_b1],
                            "res_birga2": [reponse_b2],
                            "timer":[done]
                            }, index=[0])
        df_all = df2.append(df_all)
        df_all.to_csv(main_path_data + "\\all_data.csv", header=True, index=False)

        # ##########           Change CSV BALANCE        ###################
        # valuta = pd.read_csv(main_path_data + "\\balance.csv")
        # valuta[birga_1] = valuta[birga_1].apply(pd.to_numeric, errors='coerce')
        # valuta[birga_2] = valuta[birga_2].apply(pd.to_numeric, errors='coerce')
        #
        # filter1 = valuta[valuta['Valuta'] == val1].index
        # filter3 = valuta[valuta['Valuta'] == val2].index
        # valuta.loc[filter1, birga_1] = valuta.loc[filter1, birga_1] - float(val1_vol) - ((float(val1_vol) * 1) / 100)
        # valuta.loc[filter3, birga_2] = valuta.loc[filter3, birga_2] - float(val2_vol) - ((float(val2_vol) * 1) / 100)
        #
        # fil1 = valuta[valuta['Valuta'] == 'USD']
        # fil2 = valuta[valuta['Valuta'] == 'USDT']
        #
        # al = (float(fil1.iloc[0]['alfa']) + float(fil2.iloc[0]['alfa']))
        # li = (float(fil1.iloc[0]['live']) + float(fil2.iloc[0]['live']))
        # ho = (float(fil1.iloc[0]['hot']) + float(fil2.iloc[0]['hot']))
        #
        # filter = valuta[valuta['Valuta'] == 'USDT + USD'].index
        # valuta.loc[filter, "alfa"] = al
        # valuta.loc[filter, "live"] = li
        # valuta.loc[filter, "hot"] = ho
        #
        # valuta.loc[:, "Summa"] = (valuta.loc[:, "alfa"] + valuta.loc[:, "live"] + valuta.loc[:, "hot"])
        # valuta.to_csv(main_path_data + "\\balance.csv", index=False)

        #################    TELEGRAM    #########################
        profit = (float(val4_vol) - float(val1_vol))
        perc = (((float(val4_vol) - float(val1_vol)) / float(val1_vol)) * 100)
        nl = '\n'
        val1_vol = ("{:.6f}".format(val1_vol))
        val2_vol = ("{:.6f}".format(val2_vol))
        val4_vol = ("{:.6f}".format(val4_vol))
        profit = ("{:.6f}".format(profit))
        perc = ("{:.2f}".format(perc))
        bot_sendtext(
            f" ЕСТЬ ВИЛКА: {nl} {birga_1} / {birga_2} {nl} {reponse_b1} / {reponse_b2} {nl} {val1} -> {val2} -> {val4} {nl} {val1_vol} -> {val2_vol} -> {val4_vol} {nl} {profit} {nl} {perc} {nl} ")

        print('---------   OUT  from CSV  --------')
        return
    else:
        pass
    return



# putting your callbacks in functions is a nice trick to be able to move them in other modules and import them
def create_callback_save_value(app: dash.Dash, dash_db: DashDatabase):
    @app.callback(Output('success_value_saved', 'children'),
                  [Input('ok_button', 'n_clicks')],  # the button triggers the callback
                  [State('input_div', 'value'),  # additional info that does not trigger the callback
                   State('session_id_div_id', 'data')])  # used to identify the user and save its data
    def save_value(n_clicks, value, session_id):
        # when the app starts all callbacks are triggered by default.
        # raise a PreventUpdate to avoid the callback trigger at start (n_clicks is None at this point)
        if n_clicks is None:
            raise PreventUpdate

        # save value
        dash_db.store_user_value(user_id=session_id,
                                 key_name='value',
                                 value=value)

        # return success message
        return "Your value was sucessfully saved. Try to retrieve it in the other tab now :)!"

def create_callback_retrieve_value(app: dash.Dash, dash_db: DashDatabase):
    @app.callback(Output('show_value_div', 'children'),
                  [Input('show_value_button', 'n_clicks')],
                  [State('session_id_div_id', 'data')])
    def retrieve_value(n_clicks, session_id):
        # when the app starts all callbacks are triggered by default.
        # raise a PreventUpdate to avoid the callback trigger at start (n_clicks is 0 at this point)
        if n_clicks is None:
            raise PreventUpdate

        # save value
        value = dash_db.get_user_value(user_id=session_id,
                                       key_name='value')

        # return success message
        return f"Your value is {value}"


def refresh(app: dash.Dash):

    ###############################    RESTART ALL FUNCTIONS     ########################################
    @app.callback([Output('table', 'children'),
                   Output('valuta', 'data'),
                   Output('table_all', 'data')],
                  [Input('interval', 'n_intervals')])
    def trigger_by_modify(n):
        if n is None:
            raise PreventUpdate
        start11 = time.process_time()
        df10 = pd.read_csv(main_path_data + "\\chains.csv")
        valuta = pd.read_csv(main_path_data + "\\balance.csv")
        if valuta.shape[0]>0:
            pass
        else:
            valuta = pd.read_csv(main_path_data + "\\balance2.csv")

        df_all = pd.read_csv(main_path_data + "\\all_data.csv")
        # print('VALUTA  :', valuta)
        My_chains = New_chains.film_list(df10)

        f22 = open(main_path_data + "\\w_status.json")
        w_status = json.load(f22)

        activ_alfa = w_status['alfa'][1]
        activ_hot = w_status['hot'][1]
        activ_live = w_status['live'][1]

        if df_all.shape[0] > 0:
            df_all['rates_y'] = df_all['rates_y'].map('{:,.6f}'.format)
            df_all['rates_x'] = df_all['rates_x'].map('{:,.6f}'.format)
            df_all['start'] = df_all['start'].map('{:,.6f}'.format)
            df_all['step'] = df_all['step'].map('{:,.6f}'.format)
            df_all['back'] = df_all['back'].map('{:,.6f}'.format)
            df_all['profit'] = df_all['profit'].map('{:,.6f}'.format)
            df_all['perc'] = df_all['perc'].map('{:,.3f}%'.format)
        else:
            pass

        now = dt.datetime.now()
        done = (time.process_time() - start11)
        if df10.shape[0] > 0:
            my_signal = html.Audio(src='data:audio/mpeg;base64,{}'.format(encoded_sound.decode()),
                                   controls=False,
                                   autoPlay=True,
                                   )
            print("###############      df10  BIGGER    #########################")
            if valuta.shape[0] > 0:
                return [ddk.Block(width=100,
                                  children="{},   ___СКОРОСТЬ : {},  ____ALFA: {},  ___HOT:  {},  ___LIVE: {}".format(
                                      now.strftime("%H:%M:%S"), done, activ_alfa, activ_hot, activ_live)), my_signal,
                        ddk.Block(width=100, children=My_chains)], valuta.to_dict('records'), df_all.to_dict('records')
            else:
                my_col = ['Valuta', 'alfa', 'hot', 'live', 'Summa']
                valuta = pd.DataFrame(columns=my_col)
                return [ddk.Block(width=100,
                                  children="{},   ___СКОРОСТЬ : {}, ____ALFA: {},  ___HOT:  {},  ___LIVE: {}".format(
                                      now.strftime("%H:%M:%S"), done, activ_alfa, activ_hot, activ_live)), my_signal,
                        ddk.Block(width=100, children=My_chains)], valuta.to_dict('records'), df_all.to_dict('records')
        else:

            print("###############      df10  SMALLER    #########################")
            if valuta.shape[0] > 0:
                my_col = ['TIME', 'birga_x', 'birga_y', 'rates_x', 'rates_y', 'valin_x', 'valin_y', 'valout_y',
                          'volume_x',
                          'volume_y', 'start', 'step', 'back', 'profit', 'perc', 'volume']
                df10 = pd.DataFrame(columns=my_col)
                return [ddk.Block(width=100,
                                  children="{},   ___СКОРОСТЬ : {}, ____ALFA: {},  ___HOT:  {},  ___LIVE: {}".format(
                                      now.strftime("%H:%M:%S"), done, activ_alfa, activ_hot, activ_live)),
                        ddk.Block(width=100, children=My_chains)], valuta.to_dict('records'), df_all.to_dict('records')
            else:
                my_col1 = ['TIME', 'birga_x', 'birga_y', 'rates_x', 'rates_y', 'valin_x', 'valin_y', 'valout_y',
                           'volume_x',
                           'volume_y', 'start', 'step', 'back', 'profit', 'perc', 'volume']
                df10 = pd.DataFrame(columns=my_col1)
                my_col = ['Valuta', 'alfa', 'hot', 'live', 'Summa']
                valuta = pd.DataFrame(columns=my_col)
                return [ddk.Block(width=100,
                                  children="{},   ___СКОРОСТЬ : {}, ____ALFA: {},  ___HOT:  {},  ___LIVE: {}".format(
                                      now.strftime("%H:%M:%S"), done, activ_alfa, activ_hot, activ_live)),
                        ddk.Block(width=100, children=My_chains)], valuta.to_dict('records'), df_all.to_dict('records')

def commis(app: dash.Dash):
    ###############################    ADD Commis     ########################################
    @app.callback(
        dash.dependencies.Output('output-alpha', 'children'),
        [dash.dependencies.Input('Alpha_btn', 'n_clicks')],
        [dash.dependencies.State('Alpha_com', 'value')])
    def update_Alpha(n_clicks, value):
        if n_clicks is None:
            raise PreventUpdate

        main_path_data = os.path.abspath("./data")
        f = open(main_path_data + "\\commis.json")
        compp = json.load(f)
        f.close()

        compp['main']["alfa"] = float(value)

        f = open(main_path_data + "\\commis.json", "w")
        json.dump(compp, f)
        f.close()

        return "{}".format(value)

    ###############################    ADD Commis     ########################################
    @app.callback(
        dash.dependencies.Output('output-live', 'children'),
        [dash.dependencies.Input('Live_btn', 'n_clicks')],
        [dash.dependencies.State('Live_com', 'value')])
    def update_Alpha(n_clicks, value):
        if n_clicks is None:
            raise PreventUpdate
        main_path_data = os.path.abspath("./data")
        f = open(main_path_data + "\\commis.json")
        compp = json.load(f)
        f.close()

        compp['main']["live"] = float(value)

        f = open(main_path_data + "\\commis.json", "w")
        json.dump(compp, f)
        f.close()

        return "{}".format(value)


    ###############################    ADD Commis     ########################################
    @app.callback(
        dash.dependencies.Output('output-hot', 'children'),
        [dash.dependencies.Input('Hot_btn', 'n_clicks')],
        [dash.dependencies.State('Hot_com', 'value')])
    def update_Alpha(n_clicks, value):
        if n_clicks is None:
            raise PreventUpdate
        main_path_data = os.path.abspath("./data")
        f = open(main_path_data + "\\commis.json")
        compp = json.load(f)
        f.close()

        compp['main']["hot"] = float(value)

        f = open(main_path_data + "\\commis.json", "w")
        json.dump(compp, f)
        f.close()

        return "{}".format(value)

def creat_reg(app: dash.Dash):

    @app.callback(
        dash.dependencies.Output('listcardreg', 'children'),
        [dash.dependencies.Input('New_Regim_btn', 'n_clicks'),
         dash.dependencies.Input('ref_Regim_btn', 'n_clicks')])

    def create(n_clicks, n):

        # ctx = dash.callback_context
        #
        # if not ctx.triggered:
        #     raise dash.exceptions.PreventUpdate
        # else:
        #     pass

        # if n_clicks and n is None:
        #     raise PreventUpdate

        if n_clicks > 0:
            with open(main_path_data + "\\regim.json", "r") as file:
                param = []
                data = json.load(file)
                file.close()
                for k, v in data.items():
                    param.append(k)

                if not param:
                    next_id = 1
                    data[next_id] = {"option": "off", "avtomat": "off", "val1": "", "val2": "", "val3": "", "birga1": "", "birga2": "",
                                     "profit": "",
                                     "order": "", "per": ""}
                    f = open(main_path_data + "\\regim.json", "w")
                    json.dump(data, f)
                    # print("BEFORE2 :", data)
                    f.close()
                else:
                    next_id = str(int(param[-1]) + 1)
                    data[next_id] = {"option": "off", "avtomat": "off", "val1": "", "val2": "", "val3": "", "birga1": "", "birga2": "",
                                     "profit": "",
                                     "order": "", "per": ""}
                    f = open(main_path_data + "\\regim.json", "w")
                    json.dump(data, f)
                    # print("BEFORE2 :", data)
                    f.close()


            list_group = [i for i in layouts.group_of_regims()]
            return list_group

        elif n > 0:
            list_group = [i for i in layouts.group_of_regims()]
            return list_group

def save_reg_data(app: dash.Dash):
    @app.callback(
        [Output({'type': 'option', 'index': MATCH}, 'children')],
       [Input({'type': 'checklist', 'index': MATCH}, 'value')],
        [State({'type': 'checklist', 'index': MATCH}, 'id'),

         State({'type': 'val1', 'index': MATCH}, "value"),
         State({'type': 'val2', 'index': MATCH}, "value"),
         State({'type': 'val3', 'index': MATCH}, "value"),
         State({'type': 'birga1', 'index': MATCH}, "value"),
         State({'type': 'birga2', 'index': MATCH}, "value"),

         State({'type': 'profit', 'index': MATCH}, "value"),
         State({'type': 'order', 'index': MATCH}, "value"),
         State({'type': 'percent', 'index': MATCH}, "value"),
         State({'type': 'avtomat', 'index': MATCH}, "value"),
         ]
    )
    def display_output(value,id, val1, val2, val3, birga1, birga2, profit, order, percent, avtomat):
        ctx = dash.callback_context

        if not ctx.triggered:
            raise dash.exceptions.PreventUpdate
        else:
            pass

        if order is None:
            order = ""
        else:
            order = float(order)

        if percent is None:
            percent = ""
        else:
            percent = percent

        if not value:
            # Change "option" in Regim

            print("#########     OFF    ##############")



            a_file = open(main_path_data + "\\regim.json", "r")
            json_object = json.load(a_file)
            a_file.close()



            json_object[id['index']]['option'] = "OFF"
            print("  REGIM JSON :", '\n', json_object)

            a_file = open(main_path_data + "\\regim.json", "w")
            json.dump(json_object, a_file)
            a_file.close()

            return ["{}".format(json_object[id['index']]['option'])]

        else:

            print ("#########     ON    ##############")

            a_file = open(main_path_data + "\\regim.json", "r")
            json_object = json.load(a_file)
            a_file.close()


            json_object[id['index']]['avtomat'] = avtomat
            json_object[id['index']]['option'] = "active"
            json_object[id['index']]['val1'] = val1
            json_object[id['index']]['val2'] = val2
            json_object[id['index']]['val3'] = val3
            json_object[id['index']]['birga1'] = birga1
            json_object[id['index']]['birga2'] = birga2
            json_object[id['index']]['profit'] = float(profit)
            json_object[id['index']]['order'] = order
            json_object[id['index']]['per'] = percent
            print("  REGIM JSON :", '\n', json_object)

            a_file = open(main_path_data + "\\regim.json", "w")
            json.dump(json_object, a_file)
            a_file.close()

            return ["{}".format(json_object[id['index']]['option'])]

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

def ref_key_data(app: dash.Dash):
    @app.callback(

        [Output('tab_keys88', 'children')],
        [Input('ref_keys_btn', 'n_clicks')])
    def display_output(n_clicks):

        if n_clicks is None:
            raise PreventUpdate

        else:
            tab = layouts.tab_keys()
            return [tab]

def del_rgm_data(app: dash.Dash):
    @app.callback(

        [Output({'type': 'rgm_block', 'index': MATCH}, 'children')],
        [Input({'type': 'delet_rgm_btn', 'index': MATCH}, 'n_clicks')],
        [State({'type': 'delet_rgm_btn', 'index': MATCH}, 'id')])

    def display_output(n_clicks, id):

        ctx = dash.callback_context

        if not ctx.triggered:
            raise dash.exceptions.PreventUpdate
        else:
            pass

        if n_clicks > 0:

            print("DELETE BTN #########################", id['index'])

            a_file = open(main_path_data + "\\regim.json", "r")
            json_object = json.load(a_file)
            a_file.close()

            json_object.pop(id['index'])
            a_file = open(main_path_data + "\\regim.json", "w")
            json.dump(json_object, a_file)
            a_file.close()
            return [ddk.Block('ПУСТО')]

def new_order(app: dash.Dash):

    @app.callback(
        [Output({'type': 'uorder_result', 'index': MATCH}, 'children')],
        [Input({'type': 'uorder_btn', 'index': MATCH}, 'n_clicks')],
        [dash.dependencies.State({'type': 'uorder_btn', 'index': MATCH}, 'id'),
         dash.dependencies.State({'type': 'ubirga_1', 'index': MATCH}, 'children'),
         dash.dependencies.State({'type': 'ubirga_2', 'index': MATCH}, 'children'),
         dash.dependencies.State({'type': 'uval1', 'index': MATCH}, 'children'),
         dash.dependencies.State({'type': 'uval2', 'index': MATCH}, 'children'),
         dash.dependencies.State({'type': 'uval3', 'index': MATCH}, 'children'),
         dash.dependencies.State({'type': 'uval4', 'index': MATCH}, 'children'),
         dash.dependencies.State({'type': 'uval1_vol', 'index': MATCH}, 'children'),
         dash.dependencies.State({'type': 'uval2_vol', 'index': MATCH}, 'children'),
         dash.dependencies.State({'type': 'uval3_vol', 'index': MATCH}, 'children'),
         dash.dependencies.State({'type': 'uval4_vol', 'index': MATCH}, 'children'),
         dash.dependencies.State({'type': 'urate1', 'index': MATCH}, 'children'),
         dash.dependencies.State({'type': 'urate2', 'index': MATCH}, 'children'),
         dash.dependencies.State({'type': 'uregim', 'index': MATCH}, 'children'),
         ])

    def display_output2(n_clicks,
                        id, birga_1, birga_2,
                       val1, val2, val3, val4, val1_vol,
                       val2_vol, val3_vol, val4_vol,
                        rate1, rate2,regims):

        ctx = dash.callback_context
        if not ctx.triggered:
            raise dash.exceptions.PreventUpdate
        else:
            now = dt.datetime.now()
            df_all = pd.read_csv(main_path_data + "\\all_data.csv")
            timer = now.strftime("%H:%M:%S")
            # df2 = pd.DataFrame({"TIME": [timer],
            #                     "birga_x": [birga_1],
            #                     "birga_y": [birga_2],
            #                     "rates_x": [rate1],
            #                     "rates_y": [rate2],
            #                     "valin_x": [val1],
            #                     "valin_y": [val2],
            #                     "valout_y": [val4],
            #                     "start": [val1_vol],
            #                     "step": [val2_vol],
            #                     "back": [val4_vol],
            #                     "profit": [(val4_vol - val1_vol)],
            #                     "perc": [(((val4_vol - val1_vol) / val1_vol) * 100)],
            #                     }, index=[0])
            # df_all = df2.append(df_all)
            # df_all.to_csv(main_path_data + "\\all_data.csv", header=True, index=False)
            valutadf = pd.read_csv(main_path_data + "\\balance.csv")


            filter1 = valutadf[valutadf['Valuta'] == val1]
            filter3 = valutadf[valutadf['Valuta'] == val3]

            # print(filter1.iloc[0][birga_1])
            # print(filter3.iloc[0][birga_2])

            a_file = open(main_path_data + "\\regim.json", "r")
            regim = json.load(a_file)
            a_file.close()


            parametr1 = "{}/{}".format(val1, val2)
            para1 = ['BTC/USD','LTC/USD','ETH/USD','XRP/USD','USDT/USD','BTC/USDT','ETH/USDT','XRP/BTC','ETH/BTC','LTC/BTC','BCH/BTC','ZEC/BTC', 'PZM/USD', 'PZM/USDT', 'PZM/BTC',]

            for i in para1:
                if i == parametr1:
                    parad = "ok"
                    pass
                else:
                    parad = "no"
                    pass



            if parad == 'ok':
                kurs = (float(rate1) / float(val1_vol))
                kurs2 = (float(val3_vol) / float(val4_vol))
                kurs0 = (float(val2_vol) / float(val1_vol))
                minA = regim[str(regims)]["order"]
                minB = minA * kurs0

                minbeta = (((float(val1_vol) - float(val2_vol) * float(rate1)) / (
                            float(val2_vol) * float(rate1))) * 100)
                minbeta = Context(prec=3, rounding=ROUND_UP).create_decimal(minbeta)
                minbeta = float(minbeta)

################################################################################################################
                if filter1.iloc[0][birga_1] > val1_vol and filter3.iloc[0][birga_2] > val3_vol:

                    if val1 == 'USD' or val1 == 'USDT' or val2 == 'USD' or val2 == 'USDT':
                        if birga_1 == 'alfa' and birga_2 == 'live':
                            if val2 != 'USD' or val2 != 'USDT':
                                val2_vol = val2_vol + (val2_vol * minbeta / 100)
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                            else:
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                        elif birga_1 == 'live' and birga_2 == 'alfa':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                            else:
                                reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                        elif birga_1 == 'alfa' and birga_2 == 'hot':
                            if val2 != 'USD' or val2 != 'USDT':
                                val2_vol = val2_vol + (val2_vol * minbeta / 100)
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                            else:
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                        elif birga_1 == 'hot' and birga_2 == 'alfa':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                            else:
                                reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                        elif birga_1 == 'hot' and birga_2 == 'live':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                            else:
                                reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                        elif birga_1 == 'live' and birga_2 == 'hot':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                            else:
                                reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                        else:
                            return ["No Such Command"]
                    elif val1 != 'USD' or val1 != 'USDT' or val2 != 'USD' or val2 != 'USDT':
                        if birga_1 == 'alfa' and birga_2 == 'live':
                            if val2 != "BTC":
                                val2_vol = val2_vol + (val2_vol * minbeta / 100)
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                            else:
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                        elif birga_1 == 'live' and birga_2 == 'alfa':
                            if val2 != "BTC":
                                reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                            else:
                                reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                        elif birga_1 == 'alfa' and birga_2 == 'hot':
                            if val2 != "BTC":
                                val2_vol = val2_vol + (val2_vol * minbeta / 100)
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                            else:
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                        elif birga_1 == 'hot' and birga_2 == 'alfa':
                            if val2 != "BTC":
                                reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return ["{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                            else:
                                reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                        elif birga_1 == 'hot' and birga_2 == 'live':
                            if val2 != "BTC":
                                reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                            else:
                                reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                        elif birga_1 == 'live' and birga_2 == 'hot':
                            if val2 != "BTC":
                                reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                            else:
                                reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                        else:
                            return ["No Such Command"]


################################################################################################################
                elif filter1.iloc[0][birga_1] < val1_vol and filter3.iloc[0][birga_2] > minB and filter1.iloc[0][birga_1] > minA or \
                        filter3.iloc[0][birga_2] < val3_vol and filter3.iloc[0][birga_2] > minB and filter1.iloc[0][birga_1] > minA:

                    minOrder1 = float(filter1.iloc[0][birga_1] * kurs)
                    minOrder2 = float(filter3.iloc[0][birga_2])
                    if minOrder2 > minOrder1:
                        val1_vol = filter1.iloc[0][birga_1]
                        val2_vol = minOrder1
                        val3_vol = minOrder1
                        val4_vol = minOrder1/kurs2

                        if val1 == 'USD' or val1 == 'USDT' or val2 == 'USD' or val2 == 'USDT':
                            if birga_1 == 'alfa' and birga_2 == 'live':
                                if val2 != 'USD' or val2 != 'USDT':
                                    val2_vol = val2_vol + (val2_vol * minbeta / 100)
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val3_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'live' and birga_2 == 'alfa':
                                if val2 != 'USD' or val2 != 'USDT':
                                    reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'alfa' and birga_2 == 'hot':
                                if val2 != 'USD' or val2 != 'USDT':
                                    val2_vol = val2_vol + (val2_vol * minbeta / 100)
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val3_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'hot' and birga_2 == 'alfa':
                                if val2 != 'USD' or val2 != 'USDT':
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val3_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                                else:
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'hot' and birga_2 == 'live':
                                if val2 != 'USD' or val2 != 'USDT':
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val3_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'live' and birga_2 == 'hot':
                                if val2 != 'USD' or val2 != 'USDT':
                                    reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val3_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            else:
                                return ["No Such Command"]
                        elif val1 != 'USD' or val1 != 'USDT' or val2 != 'USD' or val2 != 'USDT':
                            if birga_1 == 'alfa' and birga_2 == 'live':
                                if val2 != "BTC":
                                    val2_vol = val2_vol + (val2_vol * minbeta / 100)
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val3_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'live' and birga_2 == 'alfa':
                                if val2 != "BTC":
                                    reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val3_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'alfa' and birga_2 == 'hot':
                                if val2 != "BTC":
                                    val2_vol = val2_vol + (val2_vol * minbeta / 100)
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val3_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'hot' and birga_2 == 'alfa':
                                if val2 != "BTC":
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val3_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                                else:
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'hot' and birga_2 == 'live':
                                if val2 != "BTC":
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'live' and birga_2 == 'hot':
                                if val2 != "BTC":
                                    reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            else:
                                return ["No Such Command"]
                    elif minOrder2 < minOrder1:
                        val1_vol = minOrder2 / kurs
                        val2_vol = minOrder2
                        val3_vol = minOrder2
                        val4_vol = minOrder2 / kurs2


                        if val1 == 'USD' or val1 == 'USDT' or val2 == 'USD' or val2 == 'USDT':
                            if birga_1 == 'alfa' and birga_2 == 'live':
                                if val2 != 'USD' or val2 != 'USDT':
                                    val2_vol = val2_vol + (val2_vol * minbeta / 100)
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val3_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'live' and birga_2 == 'alfa':
                                if val2 != 'USD' or val2 != 'USDT':
                                    reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val3_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'alfa' and birga_2 == 'hot':
                                if val2 != 'USD' or val2 != 'USDT':
                                    val2_vol = val2_vol + (val2_vol * minbeta / 100)
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val3_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'hot' and birga_2 == 'alfa':
                                if val2 != 'USD' or val2 != 'USDT':
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val3_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                                else:
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'hot' and birga_2 == 'live':
                                if val2 != 'USD' or val2 != 'USDT':
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val3_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'live' and birga_2 == 'hot':
                                if val2 != 'USD' or val2 != 'USDT':
                                    reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val3_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            else:
                                return ["No Such Command"]
                        elif val1 != 'USD' or val1 != 'USDT' or val2 != 'USD' or val2 != 'USDT':
                            if birga_1 == 'alfa' and birga_2 == 'live':
                                if val2 != "BTC":
                                    val2_vol = val2_vol + (val2_vol * minbeta / 100)
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'live' and birga_2 == 'alfa':
                                if val2 != "BTC":
                                    reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'alfa' and birga_2 == 'hot':
                                if val2 != "BTC":
                                    val2_vol = val2_vol + (val2_vol * minbeta / 100)
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'hot' and birga_2 == 'alfa':
                                if val2 != "BTC":
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                                else:
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'hot' and birga_2 == 'live':
                                if val2 != "BTC":
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'live' and birga_2 == 'hot':
                                if val2 != "BTC":
                                    reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            else:
                                return ["No Such Command"]
                    else:
                        return ["Not Enough Money"]




################################################################################################################
                elif filter1.iloc[0][birga_1] < minA or filter3.iloc[0][birga_2] < minB:
                    return ["Not Enough Money"]
                else:
                    return ["Not Enough Money"]



################################################################################################################
################################################################################################################
################################################################################################################

            elif parad == 'no':
                kurs = (float(val1_vol) * float(val2_vol))
                kurs2 = (float(val4_vol) / float(val3_vol))
                kurs0 = (float(val1_vol) / float(val2_vol))
                minB = regim[str(regims)]["order"]
                minA = minB * kurs0

                minbeta = (((float(val1_vol) - float(val2_vol) * float(rate1)) / (
                        float(val2_vol) * float(rate1))) * 100)
                minbeta = Context(prec=3, rounding=ROUND_UP).create_decimal(minbeta)
                minbeta = float(minbeta)
                min1 = (float(filter1.iloc[0][birga_1]) - (float(filter1.iloc[0][birga_1]) * minbeta / 100)) / float(rate1)
                min2 = float(filter3.iloc[0][birga_2])


################################################################################################################
                if filter1.iloc[0][birga_1] > val1_vol and filter3.iloc[0][birga_2] > val3_vol:
                    if val1 == 'USD' or val1 == 'USDT' or val2 == 'USD' or val2 == 'USDT':
                        if birga_1 == 'alfa' and birga_2 == 'live':
                            if val2 != 'USD' or val2 != 'USDT':
                                val2_vol = val2_vol + (val2_vol * minbeta / 100)
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                            else:
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                        elif birga_1 == 'live' and birga_2 == 'alfa':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                            else:
                                val4_vol = val4_vol + (val4_vol * minbeta / 100)
                                reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                        elif birga_1 == 'alfa' and birga_2 == 'hot':
                            if val2 != 'USD' or val2 != 'USDT':
                                val2_vol = val2_vol + (val2_vol * minbeta / 100)
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                            else:
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                        elif birga_1 == 'hot' and birga_2 == 'alfa':

                            # print('HOT1 before :', val2_vol)
                            # # val2_vol = val2_vol + (val2_vol * minbeta / 100)
                            # print('HOT1  after:', val2_vol)
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                            else:
                                val4_vol = val4_vol + (val4_vol * minbeta / 100)
                                reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                        elif birga_1 == 'hot' and birga_2 == 'live':
                            # print('HOT1 before :', val2_vol)
                            # val2_vol = val2_vol + (val2_vol * minbeta / 100)
                            # print('HOT1 after :', val2_vol)
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                            else:
                                reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                        elif birga_1 == 'live' and birga_2 == 'hot':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                            else:
                                reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                        else:
                            return ["No Such Command"]
                    elif val1 != 'USD' or val1 != 'USDT' or val2 != 'USD' or val2 != 'USDT':
                        if birga_1 == 'alfa' and birga_2 == 'live':
                            if val2 != "BTC":
                                val2_vol = val2_vol + (val2_vol * minbeta / 100)
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                            else:
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                        elif birga_1 == 'live' and birga_2 == 'alfa':
                            if val2 != "BTC":
                                reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                            else:
                                val4_vol = val4_vol + (val4_vol * minbeta / 100)
                                reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                        elif birga_1 == 'alfa' and birga_2 == 'hot':
                            if val2 != "BTC":
                                val2_vol = val2_vol + (val2_vol * minbeta / 100)
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                            else:
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                        elif birga_1 == 'hot' and birga_2 == 'alfa':
                            val2_vol = val2_vol - (val2_vol * minbeta / 100)
                            if val2 != "BTC":
                                reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                            else:
                                val4_vol = val4_vol + (val4_vol * minbeta / 100)
                                reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                        elif birga_1 == 'hot' and birga_2 == 'live':
                            if val2 != "BTC":
                                reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                            else:
                                reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                        elif birga_1 == 'live' and birga_2 == 'hot':
                            if val2 != "BTC":
                                reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                            else:
                                reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return [
                                    "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                        else:
                            return ["No Such Command"]




################################################################################################################
                elif filter1.iloc[0][birga_1] < val1_vol and filter3.iloc[0][birga_2] > minB and filter1.iloc[0][birga_1] > minA or filter3.iloc[0][birga_2] < val3_vol and filter3.iloc[0][birga_2] > minB and filter1.iloc[0][birga_1] > minA:

                    if min2 > min1:
                        val1_vol = filter1.iloc[0][birga_1]
                        val2_vol = min1
                        val3_vol = min1
                        val4_vol = min1 * kurs2

                        if val1 == 'USD' or val1 == 'USDT' or val2 == 'USD' or val2 == 'USDT':
                            if birga_1 == 'alfa' and birga_2 == 'live':
                                if val2 != 'USD' or val2 != 'USDT':
                                    val2_vol = val2_vol + (val2_vol * minbeta / 100)
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'live' and birga_2 == 'alfa':
                                # val3_vol = min1 - (min1 * minbeta / 100)
                                if val2 != 'USD' or val2 != 'USDT':
                                    reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    val4_vol = val4_vol + (val4_vol * minbeta / 100)
                                    reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'alfa' and birga_2 == 'hot':
                                if val2 != 'USD' or val2 != 'USDT':
                                    val2_vol = val2_vol + (val2_vol * minbeta / 100)
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'hot' and birga_2 == 'alfa':
                                # val3_vol = min1 - (min1 * minbeta / 100)
                                if val2 != 'USD' or val2 != 'USDT':
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                                else:
                                    val4_vol = val4_vol + (val4_vol * minbeta / 100)
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'hot' and birga_2 == 'live':
                                if val2 != 'USD' or val2 != 'USDT':
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'live' and birga_2 == 'hot':
                                if val2 != 'USD' or val2 != 'USDT':
                                    reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            else:
                                return ["No Such Command"]
                        elif val1 != 'USD' or val1 != 'USDT' or val2 != 'USD' or val2 != 'USDT':
                            if birga_1 == 'alfa' and birga_2 == 'live':
                                if val2 != "BTC":
                                    val2_vol = val2_vol + (val2_vol * minbeta / 100)
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'live' and birga_2 == 'alfa':
                                val3_vol = min1 - (min1 * minbeta / 100)
                                if val2 != "BTC":
                                    reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'alfa' and birga_2 == 'hot':
                                if val2 != "BTC":
                                    val2_vol = val2_vol + (val2_vol * minbeta / 100)
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'hot' and birga_2 == 'alfa':
                                val3_vol = min1 - (min1 * minbeta / 100)
                                if val2 != "BTC":
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                                else:
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'hot' and birga_2 == 'live':
                                if val2 != "BTC":
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'live' and birga_2 == 'hot':
                                if val2 != "BTC":
                                    reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            else:
                                return ["No Such Command"]
                    elif min2 < min1:
                        val1_vol = (float(filter3.iloc[0][birga_2]) + (float(filter3.iloc[0][birga_2]) * minbeta / 100)) * float(rate1)
                        val2_vol = float(filter3.iloc[0][birga_2])
                        val3_vol = float(filter3.iloc[0][birga_2])
                        val4_vol = float(filter3.iloc[0][birga_2]) * kurs2

                        if val1 == 'USD' or val1 == 'USDT' or val2 == 'USD' or val2 == 'USDT':
                            if birga_1 == 'alfa' and birga_2 == 'live':
                                if val2 != 'USD' or val2 != 'USDT':
                                    val2_vol = val2_vol + (val2_vol * minbeta / 100)
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'live' and birga_2 == 'alfa':
                                if val2 != 'USD' or val2 != 'USDT':
                                    reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    val4_vol = val4_vol + (val4_vol * minbeta / 100)
                                    reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'alfa' and birga_2 == 'hot':
                                if val2 != 'USD' or val2 != 'USDT':
                                    val2_vol = val2_vol + (val2_vol * minbeta / 100)
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'hot' and birga_2 == 'alfa':
                                if val2 != 'USD' or val2 != 'USDT':
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                                else:
                                    val4_vol = val4_vol + (val4_vol * minbeta / 100)
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'hot' and birga_2 == 'live':
                                if val2 != 'USD' or val2 != 'USDT':
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'live' and birga_2 == 'hot':
                                if val2 != 'USD' or val2 != 'USDT':
                                    reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            else:
                                return ["No Such Command"]
                        elif val1 != 'USD' or val1 != 'USDT' or val2 != 'USD' or val2 != 'USDT':
                            if birga_1 == 'alfa' and birga_2 == 'live':
                                if val2 != "BTC":
                                    val2_vol = val2_vol + (val2_vol * minbeta / 100)
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'live' and birga_2 == 'alfa':
                                if val2 != "BTC":
                                    reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'alfa' and birga_2 == 'hot':
                                if val2 != "BTC":
                                    val2_vol = val2_vol + (val2_vol * minbeta / 100)
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'hot' and birga_2 == 'alfa':
                                if val2 != "BTC":
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2, reponse_b2)]
                                else:
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'hot' and birga_2 == 'live':
                                if val2 != "BTC":
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val3_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            elif birga_1 == 'live' and birga_2 == 'hot':
                                if val2 != "BTC":
                                    reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                                else:
                                    reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                    reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                    return [
                                        "{}  :  {}, '\n', {}  : {}".format(birga_1, reponse_b1, birga_2,
                                                                           reponse_b2)]
                            else:
                                return ["No Such Command"]
                    else:
                        return ["Not Enough Money"]


################################################################################################################
                elif filter1.iloc[0][birga_1] < minA or filter3.iloc[0][birga_2] < minB:
                    return ["Not Enough Money"]
                else:
                    return ["Not Enough Money"]






def test_order(app: dash.Dash):

    @app.callback(
        [Output({'type': 'show_test_order', 'index': MATCH}, 'children')],
        [dash.dependencies.Input({'type': 'tbuy_btn', 'index': MATCH}, 'n_clicks'),
         dash.dependencies.Input({'type': 'tsell_btn', 'index': MATCH}, 'n_clicks')],
        [dash.dependencies.State({'type': 'tamount', 'index': MATCH}, 'value'),
         dash.dependencies.State({'type': 'tprice', 'index': MATCH}, 'value'),
         dash.dependencies.State({'type': 'tbuy_btn', 'index': MATCH}, 'id'),
         dash.dependencies.State({'type': 'tsell_btn', 'index': MATCH}, 'id')])

    def display_output2(n_clicks, n,
                       val1, val2, idbuy, idsell):

        ctx = dash.callback_context

        if not ctx.triggered:
            raise dash.exceptions.PreventUpdate

        else:
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            res = json.loads(button_id)
            if res['index'] == '1':
                if res['type'] == 'tbuy_btn':
                    reponse_b1 = Orders.alfa('USD', 'BTC', val2, val1)
                    return [reponse_b1]
                else:
                    reponse_b1 = Orders.alfa('BTC', 'USD', val2, val1)
                    return [reponse_b1]
            elif res['index'] == '2':
                if res['type'] == 'tbuy_btn':
                    reponse_b1 = Orders.live("USD", "BTC", val2, val1)
                    return [reponse_b1]
                else:
                    reponse_b1 = Orders.live('BTC', 'USD', val2, val1)
                    return [reponse_b1]
            elif res['index'] == '3':
                if res['type'] == 'tbuy_btn':
                    reponse_b1 = Orders.hot('USD', 'BTC', str(val2), str(val1))
                    return [reponse_b1]
                else:
                    reponse_b1 = Orders.hot('BTC', 'USD', str(val2), str(val1))
                    return [reponse_b1]


def alert_btn(app: dash.Dash):
    @app.callback(

        [Output("hidden-div", 'children')],
        [Input("btn_start", 'n_clicks'),
         Input("btn_stop", 'n_clicks')]
       )

    def display_output(btn_start, btn_stop):

        ctx = dash.callback_context

        if not ctx.triggered:
            raise dash.exceptions.PreventUpdate
        else:
            pass

        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        # res = json.loads(button_id)
        print("button_id", button_id)
        # print("RES", res)

        if button_id == "btn_start":
            if btn_start >0:
                a_file = open(main_path_data + "\\regim.json", "r")
                json_object = json.load(a_file)
                a_file.close()
                for i in json_object:
                    json_object[i]["avtomat"] = "on"

                print(" ___  ON  _____")

                a_file = open(main_path_data + "\\regim.json", "w")
                json.dump(json_object, a_file)
                a_file.close()
                btn_start = 0
        elif button_id == "btn_stop":
            a_file = open(main_path_data + "\\regim.json", "r")
            json_object = json.load(a_file)
            a_file.close()
            for i in json_object:
                json_object[i]["avtomat"] = "off"
            print(" ___  OFF  _____")
            a_file = open(main_path_data + "\\regim.json", "w")
            json.dump(json_object, a_file)
            a_file.close()
        else:
            pass

        return [""]



create_callback_save_value(dash_app, dash_db)
create_callback_retrieve_value(dash_app, dash_db)
refresh(dash_app)
commis(dash_app)
creat_reg(dash_app)
save_reg_data(dash_app)
save_key_data(dash_app)
ref_key_data(dash_app)
del_rgm_data(dash_app)
new_order(dash_app)
test_order(dash_app)
alert_btn(dash_app)