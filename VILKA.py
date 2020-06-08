import pandas as pd
import json
import Balance
import os
import datetime as dt
import Hot_parser
import Live_parser
import A_parser
import requests
import Avtomat
import time


##################################   SHOW ALL ROWS & COLS   ####################################
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None)

main_path_data = os.path.abspath("./data")
#################################   COMMISSIONS   ##########################################
if os.path.isfile(main_path_data + "\\commis.json"):
    f = open(main_path_data + "\\commis.json")
    com = json.load(f)
    pass
else:
    dictionary= {"main": {
        "hot": 1.0006,
        "alfa": 1.002,
        "live": 1.0018
                        }}
    com = json.dumps(dictionary, indent=4)

    # Writing to sample.json
    with open(main_path_data + "\\commis.json", "w") as outfile:
        outfile.write(com)
        outfile.close()
        pass

def restart():
    start11 = time.process_time()
    my_col = ['TIME', 'birga_x', 'birga_y', 'rates_x', 'rates_y', 'valin_x', 'valin_y', 'valout_y', 'volume_x',
              'volume_y', 'start', 'step', 'back', 'profit', 'perc', 'volume']

    if os.path.isfile(main_path_data + "\\all_data.csv"):
        pass
    else:
        final2 = pd.DataFrame(columns=my_col)
        final2.to_csv(main_path_data + "\\all_data.csv", header=True)
        pass

    hot = Hot_parser.loadRSS()
    live = Live_parser.restart()
    alfa = A_parser.loadRSS()

    birgi = {'alfa': alfa, 'live': live, 'hot': hot}

    birga = []
    valin = []
    valout = []
    rates = []
    volume = []


    ###########   Collected all kurses  ############
    def tab(item, value):

        for k, v in item.items():
            list = k.split('/')


            abc = [0, 1, 2]
            for i in abc:
                birga.append(value)
                valin.append(list[0])
                valout.append(list[1])


                r = ("{0:,.10f}".format(float((item[k]['buy'][i][0]))))
                r2 = r.replace(',', '')
                v = ("{0:,.10f}".format(float((item[k]['buy'][i][1]))))
                v2 = v.replace(',', '')

                rates.append(r2)
                volume.append(v2)

                birga.append(value)
                valin.append(list[1])
                valout.append(list[0])
                r21 = ("{0:,.10f}".format(float((item[k]['sell'][i][0]))))
                r22 = r21.replace(',', '')
                v21 = ("{0:,.10f}".format(float((item[k]['sell'][i][1]))))
                v22 = v21.replace(',', '')
                rates.append(r22)
                volume.append(v22)

        return


    for value, item in birgi.items():
        tab(item,value)


    dw = {'birga': birga, 'valin': valin, 'valout': valout, 'rates': rates, 'volume': volume}
    df = pd.DataFrame(data=dw)

    dfs2 = pd.merge(df, df, left_on=df['valout'], right_on=df['valin'], how='outer')
    dfs2['rates_x'] = dfs2['rates_x'].apply(pd.to_numeric, errors='coerce')
    dfs2['rates_y'] = dfs2['rates_y'].apply(pd.to_numeric, errors='coerce')
    dfs2['volume_x'] = dfs2['volume_x'].apply(pd.to_numeric, errors='coerce')
    dfs2['volume_y'] = dfs2['volume_y'].apply(pd.to_numeric, errors='coerce')
    dfs2.drop(['key_0'], axis = 1, inplace = True)
    dfs2['rates_y'] = dfs2['rates_y'].map('{:,.10f}'.format)
    dfs2['rates_x'] = dfs2['rates_x'].map('{:,.10f}'.format)



    ###############       Main dataframe with all data      ####################
    result = dfs2[(dfs2['valin_x'] == dfs2['valout_y'])]
    usdt = dfs2[(dfs2['valin_x'] == 'USD') & (dfs2['valout_y'] == 'USDT')]
    usd = dfs2[(dfs2['valin_x'] == 'USDT') & (dfs2['valout_y'] == 'USD')]
    final = result.append([usdt, usd])
    final.reset_index(inplace=True, drop = True)
    final.reset_index(level=0, inplace=True)
    filter = final[(final['birga_x'] == final['birga_y']) &
                   (final['rates_x'] < final['rates_y']) &
                   (final['valin_x'] == final['valout_y'])]
    final = final.drop(filter['index'], axis=0)





    ########################      ADD  COMMISSION       ##############################

    var1 = final[final["valin_x"].isin(["USD", "USDT"])]
    var2 = final[final["valin_y"].isin(["USD", "USDT"])]
    var3 = final[(final["valin_x"] == "BTC") & (~final["valin_y"].isin(["USD", "USDT"]))]
    var4 = final[(final["valin_y"] == "BTC") & (~final["valin_x"].isin(["USD", "USDT"]))]

    var = {'var1': var1, 'var2': var2, 'var3': var3, 'var4': var4}



    def calc1(result):
        f = open(main_path_data + "\\commis.json")
        com = json.load(f)
        result.loc[:, 'start'] = "100"
        result.loc[:, "start"] = result["start"].str.replace(",", "").astype(float)
        result.loc[:, "rates_x"] = result["rates_x"].str.replace(",", "").astype(float)
        result.loc[:, "rates_y"] = result["rates_y"].str.replace(",", "").astype(float)
        result.loc[:, 'step'] = (result['start']) / ((result['rates_x'] * com['main'][result.iloc[0]['birga_x']]))
        result.loc[:, 'back'] = result['step'] * ((result['rates_y']) / com['main'][result.iloc[0]['birga_y']])
        result.loc[:, 'profit'] = result['back'] - result['start']
        result.loc[:, 'perc'] = (((result['profit']) / (result['start'])) * 100)
        f.close()
        return result
    def calc2(result):

        f = open(main_path_data + "\\commis.json")
        com = json.load(f)

        result.loc[:, 'start'] = "100"
        result.loc[:, "start"] = result["start"].str.replace(",", "").astype(float)
        result.loc[:, "rates_x"] = result["rates_x"].str.replace(",", "").astype(float)
        result.loc[:, "rates_y"] = result["rates_y"].str.replace(",", "").astype(float)
        result.loc[:, 'step'] = (result['start']) * ((result['rates_x'] / com['main'][result.iloc[0]['birga_x']]))
        result.loc[:, 'back'] = result['step'] / ((result['rates_y']) * com['main'][result.iloc[0]['birga_y']])
        result.loc[:, 'profit'] = result['back'] - result['start']
        result.loc[:, 'perc'] = (((result['profit']) / (result['start'])) * 100)
        f.close()
        return result





    dft = pd.DataFrame()
    for i, v in var.items():
        if v.shape[0] > 0:
            if i == 'var1' or i == 'var3':
                dft = dft.append(calc1(v))
            else:
                dft = dft.append(calc2(v))


    now = dt.datetime.now()
    dft.loc[:, 'TIME'] = now.strftime("%H:%M:%S")
    dft.drop(['index'], axis=1, inplace=True)
    dft = dft[['TIME', 'birga_x', 'birga_y', 'rates_x', 'rates_y','valin_x','valin_y','valout_y','volume_x','volume_y','start','step','back','profit','perc']]
    dfs = dft


    valuta_main = Balance.balance()
    # valuta_main.to_csv(main_path_data + "\\balance.csv", index=False)

    def regim_filter():
        fids = pd.DataFrame()

        #################################      REGIMS      ##########################################

        if os.path.isfile(main_path_data + "\\new_regims.json"):
            f = open(main_path_data + "\\new_regims.json")
            regim = json.load(f)
            pass
        else:
            regim = {1: {"option": "off",
                         "avtomat": "off",
                         "val1": "",
                         "val2": "",
                         "val3": "",
                         "birga1": "",
                         "birga2": "",
                         "profit": "",
                         "order": "",
                         "per": ""}}
            ooo = json.dumps(regim, indent=4)
            # Writing to sample.json
            with open(main_path_data + "\\new_regims.json", "w") as outfile:
                outfile.write(ooo)
                outfile.close()
                pass

        dfs['volume_x'] = dfs['volume_x'].apply(pd.to_numeric, errors='coerce')
        dfs['volume_y'] = dfs['volume_y'].apply(pd.to_numeric, errors='coerce')

        for i in regim:
            if regim[i]["option"] == 'active':
                if not regim[i]["per"]:
                    dfs["volume_x"] = dfs["volume_x"].astype(float)
                    dfs["volume_y"] = dfs["volume_y"].astype(float)
                    filterx = dfs[dfs["volume_x"] < dfs["volume_y"]].index
                    dfs.loc[filterx, "volume"] = dfs.loc[filterx, "volume_x"]
                    filtery = dfs[dfs["volume_x"] > dfs["volume_y"]].index
                    dfs.loc[filtery, "volume"] = dfs.loc[filtery, "volume_y"]
                    dfs["volume"] = dfs["volume"].astype(float)

                    dft = dfs[(dfs["birga_x"] == regim[i]["birga1"]) &
                              (dfs["birga_y"] == regim[i]["birga2"]) &
                              (dfs["valin_x"] == regim[i]["val1"]) &
                              (dfs["valin_y"] == regim[i]["val2"]) &
                              (dfs["valout_y"] == regim[i]["val3"]) &
                              (dfs["perc"] > regim[i]["profit"]) &
                              (dfs["volume"] > float(regim[i]["order"]))]

                    if dft.shape[0] > 0:
                        dft = dft[dft['volume'] == dft['volume'].max()]
                        dft = dft.head(n=1)
                        dft["regim"] = i
                        if regim[i]["avtomat"] == 'on':
                            if fids.shape[0] > 0:
                                done = (time.process_time() - start11)
                                dft["timer"] = done

                                fids_b1 = fids[(fids['birga_x'] == dft.iloc[0]['birga_x']) & (fids['valin_x'] == dft.iloc[0]['valin_x']) & (fids['valin_y'] == dft.iloc[0]['valin_y'])]
                                fids_b11 = fids[(fids['birga_x'] == dft.iloc[0]['birga_y']) & (fids['valin_x'] == dft.iloc[0]['valin_y']) & (fids['valin_y'] == dft.iloc[0]['valout_y'])]
                                fids_b2 = fids[(fids['birga_y'] == dft.iloc[0]['birga_y']) & (fids['valin_x'] == dft.iloc[0]['valin_x']) & (fids['valin_y'] == dft.iloc[0]['valin_y'])]
                                fids_b22 = fids[(fids['birga_y'] == dft.iloc[0]['birga_x']) & (fids['valin_y'] == dft.iloc[0]['valin_x']) & (fids['valout_y'] == dft.iloc[0]['valin_y'])]

                                if fids_b1.shape[0] > 0:
                                    add_vol1 = float(fids_b1.iloc[0]['volume'])
                                else:
                                    add_vol1 = 0
                                if fids_b11.shape[0] > 0:
                                    add_vol11 = float(fids_b1.iloc[0]['volume'])
                                else:
                                    add_vol11 = 0
                                if fids_b2.shape[0] > 0:
                                    add_vol2 = float(fids_b1.iloc[0]['volume'])
                                else:
                                    add_vol2 = 0
                                if fids_b22.shape[0] > 0:
                                    add_vol22 = float(fids_b1.iloc[0]['volume'])
                                else:
                                    add_vol22 = 0

                                dft['volume'] = float(dft.iloc[0]['volume']) - add_vol1 - add_vol11 - add_vol2 - add_vol22
                                if dft.iloc[0]['volume'] > 0:
                                    valuta_new = pd.read_csv(main_path_data + "\\balance.csv")
                                    Avtomat.avtomat(dft, valuta_new, start11)
                                    fids = pd.concat([dft, fids], ignore_index=True, join='outer')
                                    continue
                                else:
                                    continue
                            else:
                                done = (time.process_time() - start11)
                                dft["timer"] = done
                                valuta_new = pd.read_csv(main_path_data + "\\balance.csv")
                                Avtomat.avtomat(dft, valuta_new, start11)
                                fids = pd.concat([dft, fids], ignore_index=True, join='outer')
                                continue
                        else:
                            done = (time.process_time() - start11)
                            dft["timer"] = done
                            fids = pd.concat([dft, fids], ignore_index=True, join='outer')
                            continue
                    else:
                        continue
                else:
                    dfs["volume_x"] = dfs["volume_x"].astype(float)
                    dfs["volume_y"] = dfs["volume_y"].astype(float)
                    filterx = dfs[dfs["volume_x"] < dfs["volume_y"]].index
                    dfs.loc[filterx, "volume"] = dfs.loc[filterx, "volume_x"] * float(regim[i]["per"]) / 100
                    filtery = dfs[dfs["volume_x"] > dfs["volume_y"]].index
                    dfs.loc[filtery, "volume"] = dfs.loc[filtery, "volume_y"] * float(regim[i]["per"]) / 100
                    dfs["volume"] = dfs["volume"].astype(float)
                    dft = dfs[(dfs["birga_x"] == regim[i]["birga1"]) &
                              (dfs["birga_y"] == regim[i]["birga2"]) &
                              (dfs["valin_x"] == regim[i]["val1"]) &
                              (dfs["valin_y"] == regim[i]["val2"]) &
                              (dfs["valout_y"] == regim[i]["val3"]) &
                              (dfs["perc"] > regim[i]["profit"]) &
                              (dfs["volume"] > float(regim[i]["order"]))]

                    if dft.shape[0] > 0:
                        dft = dft[dft['volume'] == dft['volume'].max()]
                        dft = dft.head(n=1)
                        dft["regim"] = i
                        if regim[i]["avtomat"] == 'on':
                            if fids.shape[0] > 0:
                                done = (time.process_time() - start11)
                                dft["timer"] = done

                                fids_b1 = fids[(fids['birga_x'] == dft.iloc[0]['birga_x']) & (
                                            fids['valin_x'] == dft.iloc[0]['valin_x']) & (
                                                       fids['valin_y'] == dft.iloc[0]['valin_y'])]
                                fids_b11 = fids[(fids['birga_x'] == dft.iloc[0]['birga_y']) & (
                                            fids['valin_x'] == dft.iloc[0]['valin_y']) & (
                                                        fids['valin_y'] == dft.iloc[0]['valout_y'])]
                                fids_b2 = fids[(fids['birga_y'] == dft.iloc[0]['birga_y']) & (
                                            fids['valin_x'] == dft.iloc[0]['valin_x']) & (
                                                       fids['valin_y'] == dft.iloc[0]['valin_y'])]
                                fids_b22 = fids[(fids['birga_y'] == dft.iloc[0]['birga_x']) & (
                                            fids['valin_y'] == dft.iloc[0]['valin_x']) & (
                                                        fids['valout_y'] == dft.iloc[0]['valin_y'])]

                                if fids_b1.shape[0] > 0:
                                    add_vol1 = float(fids_b1.iloc[0]['volume'])
                                else:
                                    add_vol1 = 0
                                if fids_b11.shape[0] > 0:
                                    add_vol11 = float(fids_b1.iloc[0]['volume'])
                                else:
                                    add_vol11 = 0
                                if fids_b2.shape[0] > 0:
                                    add_vol2 = float(fids_b1.iloc[0]['volume'])
                                else:
                                    add_vol2 = 0
                                if fids_b22.shape[0] > 0:
                                    add_vol22 = float(fids_b1.iloc[0]['volume'])
                                else:
                                    add_vol22 = 0

                                dft['volume'] = float(dft['volume']) - add_vol1 - add_vol11 - add_vol2 - add_vol22
                                if dft.iloc[0]['volume'] > 0:
                                    valuta_new = pd.read_csv(main_path_data + "\\balance.csv")
                                    Avtomat.avtomat(dft, valuta_new, start11)
                                    fids = pd.concat([dft, fids], ignore_index=True, join='outer')
                                    continue
                                else:
                                    continue
                            else:
                                done = (time.process_time() - start11)
                                dft["timer"] = done
                                valuta_new = pd.read_csv(main_path_data + "\\balance.csv")
                                Avtomat.avtomat(dft, valuta_new, start11)
                                fids = pd.concat([dft, fids], ignore_index=True, join='outer')
                                continue
                        else:
                            done = (time.process_time() - start11)
                            dft["timer"] = done
                            fids = pd.concat([dft, fids], ignore_index=True, join='outer')
                            continue
                    else:
                        continue
            else:
                continue
        return fids

    fdf = regim_filter()


    df_all = pd.read_csv(main_path_data + "\\all_data.csv")
    valuta = pd.read_csv(main_path_data + "\\balance.csv")

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

    return fdf, valuta, df_all


