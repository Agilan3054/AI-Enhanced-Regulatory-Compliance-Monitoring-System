import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

# Example data for the dashboard
data = pd.DataFrame({
    'Compliance Status': ['Breach', 'No Breach'],
    'Count': [10, 50]
})

fig = px.bar(data, x='Compliance Status', y='Count', title='Compliance Breach Statistics')

app.layout = html.Div(children=[
    html.H1(children='Regulatory Compliance Monitoring Dashboard'),
    dcc.Graph(
        id='compliance-graph',
        figure=fig
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
