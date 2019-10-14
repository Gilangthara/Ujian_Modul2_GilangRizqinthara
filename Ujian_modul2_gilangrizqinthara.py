import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)
dftsa_claims=pd.read_csv('tsa_claims_ujian.csv.csv')

app.layout = html.Div(children = [
    html.H1('Ini Dashboard'),
    html.P('Created by : Gilang'),
    
    dcc.Tabs(value ="tabs", id = 'tabs-1', children = [
        dcc.Tab(label = 'Bar-Chart', value = 'tab-satu',children = [
            #Dropdown
            html.Div(children = [
            html.Div(children = [
            html.P('X1:'),
            dcc.Dropdown(id = 'x-axis-1', options = [{'label': i,'value' : i} for i in dftsa_claims.select_dtypes('number').columns],
            value = 'Attack')
            ], className = 'col-3')
            
            html.Div(children = [
            html.P('X2:'),
            dcc.Dropdown(id = 'x-axis-1', options = [{'label': i,'value' : i} for i in dftsa_claims.select_dtypes('number').columns],
            value = 'Attack')
            ], className = 'col-3')
            ], className = 'row'),

            #Graf Bar
            html.Div([
            dcc.Graph(
            id='contoh-graph-bar',
            figure={
                'data':[
                    
                ],
                'layout': {'title': 'Dashboard Pokemon'}
                }
                )], className = 'col-12'),
        ]),


                dcc.Tab(label = 'Scatter-Chart', value = 'tab-dua',children = [
                    html.Div(children=dcc.Graph(
                    id = 'graph.scatter',
                    figure = {'data':[
                    go.Scatter(
                        x = dfPokemon[dfPokemon['Generaton'] == i,]['Attack'],
                        y = dfPokemon[dfPokemon['Generaton'] == i,]['Speed'],
                        type = dfPokemon[dfPokemon['Generaton'] == i,]['Name'],
                        name = 'Generation {}'.format(i)
                        mode = 'markers'
                        ) for i in dfPokemon['Generation'].unique() 
                    ],
                    'layout':go.Layout(
                        xaxis={'title':'Attack Pokemon'},
                        yaxis={'title':'Speed Pokemon'},
                        hovermode='closest'
                    )
                    }
                    ),className='col-12')
                    ]),

                dcc.Tab(label = 'Pie-Chart', value = 'tab-tiga',children = [
                    html.Div(children=dcc.Graph(
                    id = 'contoh-graph-pie',
                    figure = {
                    'data':[
                    go.Pie(labels = ['Generation{}'.format(i) for i in list(dfPokemon['Generation'].unique())],
                                    values = [dfPokemon.groupby('Generation').mean()['Attack'][i] for i in list(dfPokemon['Generation'].unique())],
                                    sort = False)
                    ],
                    'layout': {'tittle': 'Mean Pie Chart'}
                    }
                    ), className = 'col-12')
                    ]),

        ], 
        ## Tabs Conten Style
        content_style = {
        'frontFamily':'Arial',
        'borderBottom': '1px solid #d6d6d6',
        'borderLeft': '1px solid #d6d6d6',
        'borderRight': '1px solid #d6d6d6',
        'padding': '44px'
        })
],style = {
    'maxwidth': '1200px',
    'margin': '0 auto' 
    
])

if __name__ == '__main__':
    app.run_server(debug=True)