import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from math import floor

''' 
# Business constants
max_level = 125
start_deposit = 2
degree_of_level = 2
degree_of_dependence = 2
start_time = 1
end_time = 20160
'''

# Factory constants
max_level = 125
start_deposit = 2
degree_of_level = 2
degree_of_dependence = 2
start_time = 1
end_time = 20160

levels = list()
upgrade_values = list()
production = list()
time_minutes = list()
time_hours = list()
time_days = list()

for level in range(max_level):
    levels.append(level + 1)
    time_minutes.append(1 + (levels[level] / max_level) ** degree_of_dependence * (end_time - start_time))
    production.append(floor(levels[level] ** degree_of_level * start_deposit))
    upgrade_values.append(floor(time_minutes[level] * levels[level] ** degree_of_level * start_deposit))
    time_hours.append(floor(time_minutes[level] / 60))
    time_days.append(floor(time_minutes[level] / 1440))

fig = go.Figure(data=[go.Table(header=dict(values=['Level', 'Production', 'Value for upgrade',
                                                   'Time to next level (minutes)',
                                                   'Time to next level (hours)', 'Time to next level (days)']),
                               cells=dict(values=[levels, production, upgrade_values, time_minutes, time_hours, time_days]))
                      ])

fig.update_layout(width=1920, height=1080)

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter

