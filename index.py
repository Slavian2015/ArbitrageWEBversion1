from app import dash_app, app
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_design_kit as ddk
import layouts
import os
import base64

# git push heroku master
import callbacks
#heroku logs --tail

main_path_data = os.path.abspath("./data")
sound_filename = (main_path_data + "\\signal.mp3")  # replace with your own .mp3 file
encoded_sound = base64.b64encode(open(sound_filename, 'rb').read())

# def sound(i):
#
#     sound = html.Div(id='sound', children=[i])
#     return sound


dash_app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    ddk.App(style={'background-color': 'transparent'},
                     children=[
                         ddk.Header(style={'height': '7vh',
                                           # 'background-color': '#0e4e70',
                                           'background-color': '#163d47', 'opacity': '1', 'margin': '0px'},
                                    children=[
                                        ddk.Block(
                                            width=33,
                                            style={'text-align': 'left'},
                                                  children=[
                                                      html.Div(id='placeholder1', style={"display": "none"}, children=layouts.sound(0)),
                                                      html.Div(id='on-content', style={'display': 'none'}),
                                                      html.Div(id='off-content', style={'display': 'none'}),
                                                      html.Button(children="TURN ON",
                                                                  style={'text-align': 'center',
                                                                         # 'max-width': '100px',
                                                                         "background-color": "palegreen",
                                                                         "border-radius": "20px",'margin': '10px',
                                                                         'font-size': '15px'},
                                                                  id='On_Avtomat_btn',
                                                                  n_clicks=0),
                                                      html.Button(children="ALERT",
                                                                  style={'text-align': 'center',
                                                                         # 'max-width': '100px',
                                                                         "background-color": "tomato",
                                                                         "border-radius": "20px",'margin': '10px',
                                                                         'font-size': '15px'},
                                                                  id='Off_Avtomat_btn',
                                                                  n_clicks=0)]),
                                        ddk.Block(
                                            width=33,
                                            style={'text-align': 'center'},
                                                  children=[
                                                      html.Button(children="REFRESH BALANCE",
                                                                  style={'text-align': 'center',
                                                                         # 'max-width': '100px',
                                                                         "background-color": "palegreen",
                                                                         "border-radius": "20px", 'margin': '10px',
                                                                         'font-size': '15px'},
                                                                  id='Ref_balance_btn',
                                                                  n_clicks=0),
                                                  html.Div(id='BALANCE-content', style={'display': 'none'}),]),
                                        ddk.Block(
                                            width=33,
                                            style={'text-align': 'right'},
                                                  children=[
                                                      dcc.Link('ГЛАВНАЯ', style={'color': 'azure', 'margin': '10px'}, href='/'),
                                                      dcc.Link('REGIM 2', style={'color': 'azure', 'margin': '10px'}, href='/regim2'),
                                                      dcc.Link('КЛЮЧИ', style={'color': 'azure', 'margin': '10px'}, href='/keys')])]),
                         html.Div(id='page-content'),


])])





@dash_app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
         return layouts.serve_layout()
    elif pathname == '/keys':
         return layouts.tab_keys()
    elif pathname == '/regim2':
         return layouts.serve_layout2()
    else:
        return '404'

if __name__ == "__main__":
    # app.run_server(debug=True)
    app.run(debug=False)