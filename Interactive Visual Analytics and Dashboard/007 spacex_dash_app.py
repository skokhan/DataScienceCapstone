# Import required libraries
import pandas as pd
import dash
#import dash_html_components as html
#import dash_core_components as dcc
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("007 spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()
#payload_marks = {i: '{}'.format(i) for i in spacex_df['Payload Mass (kg)'].unique()}
#launch_sites = spacex_df['Launch Site'].unique()

launch_sites = [{'label':'All Sites','value':'ALL'}]
for ls in spacex_df['Launch Site'].unique():
    launch_sites.append({'label':ls, 'value':ls})

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                # dcc.Dropdown(id='site-dropdown',...)
                                dcc.Dropdown(options=launch_sites, id='site-dropdown', value='ALL', clearable=False, searchable=True),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart', style={'width':'90%','height':'60vh','margin':'0 auto'})),
                                #html.Div(dcc.Graph(id='success-pie-chart', style={'height': '60vh'})),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                #dcc.RangeSlider(id='payload-slider',...)
                                #dcc.RangeSlider(id='payload-slider', min=min_payload, max=max_payload, marks=payload_marks, value=[min_payload, max_payload]),
                                dcc.RangeSlider(id='payload-slider', min=0, max=10000, step=1000, value=[min_payload, max_payload]),
                                html.Br(),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                #html.Div(dcc.Graph(id='success-payload-scatter-chart', style={'height': '45vh'})),
                                #html.Div(dcc.Graph(id='success-payload-scatter-chart', {'width':'90%','height': '45vh','margin':'0 auto'})),
                                html.Div(dcc.Graph(id='success-payload-scatter-chart', style={'width':'90%','height':'45vh','margin':'0 auto'})),
                                ], style={'width':'90%', 'margin':'0 auto'})

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
# Function decorator to specify function input and output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))

def get_pie_chart(entered_site):
    # return the outcomes piechart for a selected site
    filtered_df = spacex_df
    if entered_site == 'ALL':
        fig = px.pie(filtered_df, 
            values='class', 
            names='Launch Site',
            labels={'class':'Success Launches'}, 
            title='Total Success Launches by Site'
            )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        return fig
    else:
        #filtered_df = spacex_df[spacex_df['Launch Site']==entered_site].sort_values(by=['class'])
        filtered_df = spacex_df[spacex_df['Launch Site']==entered_site]
        filtered_df.loc[filtered_df['class'] == 0, 'label'] = 'Fail'
        filtered_df.loc[filtered_df['class'] == 1, 'label'] = 'Success'
        filtered_df = filtered_df[['class','label']].groupby(by='label', as_index=False).count()
        fig = px.pie(filtered_df, 
            values=filtered_df['class'],
            names=filtered_df['label'],
            color=filtered_df['label'],
            labels={'class':'Launches'}, 
            title='Total Success Launches for Site '+entered_site
            )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        return fig

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
# Function decorator to specify function input and output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'),
              Input(component_id='payload-slider', component_property='value'))

def get_scatter_chart(entered_site, slider_range):
    # return the outcomes scatter for a selected site and payload mass
    low, high = slider_range
    mask = (spacex_df['Payload Mass (kg)']>=low) & (spacex_df['Payload Mass (kg)']<=high)
    filtered_df = spacex_df[mask]
    if entered_site == 'ALL':
        #fig = px.scatter(filtered_df, 
        fig = px.strip(filtered_df, 
            x='Payload Mass (kg)', 
            y='class', 
            color='Booster Version Category', 
            stripmode='group',
            #symbol='Booster Version Category', 
            #size='Payload Mass (kg)', 
            labels={'class':'Success'}, 
            title='Correlation betweeen Payload and Success for All Sites'
            )
        #fig.update_xaxes(type='category')
        fig.update_traces(marker=dict(size=15, opacity=0.6, line=dict(width=1, color='DarkSlateGrey')))
        fig.update_traces(width=30, jitter=1)
        fig.update_yaxes(type='category')
        return fig
    else:
        filtered_df = filtered_df[filtered_df['Launch Site']==entered_site].sort_values(by='class', ascending=True)
        #fig = px.scatter(filtered_df, 
        fig = px.strip(filtered_df, 
            x='Payload Mass (kg)', 
            y='class', 
            color='Booster Version Category', 
            stripmode='group',
            #symbol='Booster Version Category', 
            #size='Payload Mass (kg)', 
            labels={'class':'Success'}, 
            title='Correlation betweeen Payload and Success for Site '+entered_site
            )
        #fig.update_xaxes(type='category')
        fig.update_traces(marker=dict(size=15, opacity=0.6, line=dict(width=1, color='DarkSlateGrey')))
        fig.update_traces(width=30, jitter=1)
        fig.update_yaxes(type='category')        
        return fig

# Run the app
if __name__ == '__main__':
    #app.run_server()
    #app.run()
    app.run(debug=False, port=8050)