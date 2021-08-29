import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from math import floor

''' 
# Business constants
start_deposit = 2
degree_of_level = 2
degree_of_dependence = 2
start_time = 1
end_time = 20160
max_level = 125
'''

# Factory constants
# Production speed
degree_of_level = 1.5
start_deposit = 2
# Time
degree_of_dependence = 2
start_time = 2
end_time = 43200

max_level = 80

levels = list()
upgrade_values = list()
production = list()
time_minutes = list()
time_hours = list()
time_days = list()

for level in range(max_level):
    levels.append(level + 1)
    # Linear interpolation between start and end time
    time_minutes.append(1 + (levels[level] / max_level) ** degree_of_dependence * (end_time - start_time))
    # Production = level^a * b
    production.append(floor(levels[level] ** degree_of_level * start_deposit))
    # S = Production * Time
    upgrade_values.append(floor(time_minutes[level] * production[level]))
    # Time representation
    time_hours.append(floor(time_minutes[level] / 60))
    time_days.append(floor(time_minutes[level] / 1440))

fig = go.Figure(data=[go.Table(header=dict(values=['Level', 'Production', 'Value for upgrade',
                                                   'Time to next level (minutes)',
                                                   'Time to next level (hours)',
                                                   'Time to next level (days)'],
                                           fill_color='paleturquoise',
                                           align='right'),
                               cells=dict(values=[levels, production, upgrade_values,
                                                  time_minutes, time_hours, time_days],
                                          fill_color='lavender',
                                          align='right'))
                      ])

fig.update_layout(width=1280, height=720)

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter

