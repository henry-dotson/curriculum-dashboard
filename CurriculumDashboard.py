'''Imports'''

import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go

'''Model'''

# [√] TODO Create class to wrap pandas + plotly

"""
MyPlot is a class that, given a file, performs pandas and plotly
methods to the file.
@param file The csv file you wish to use as a data source.
"""

class MyPlot:

    def __init__(self, file):
        self.df = pd.read_csv(file)

    def count_unique(self, column):
        self.count = self.df[column].value_counts()

    def count_x_group(self):
        self.axes = pd.DataFrame({'Group':self.count.index, 'Count':self.count.values})

    def pie_chart_plot(self):
        self.chart = px.pie(self.axes, names='Group', values='Count')

    def funnel_plot(self):
        self.chart = px.funnel(self.axes, x='Group', y='Count')

    def bar_chart_plot(self, x, y):
        self.chart = px.bar(self.df, x, y)

    def plotme(self):
        return self.chart

# [√] TODO Piechart plot of errors by category

pie_errors_category = MyPlot('CurricData.csv')
pie_errors_category.count_unique('Assessment SubCategory')
pie_errors_category.count_x_group()
pie_errors_category.pie_chart_plot()

# [√] TODO Funnel plot of errors by course

funnel_errors_course = MyPlot('CurricData.csv')
funnel_errors_course.count_unique('CDS Course Name')
funnel_errors_course.count_x_group()
funnel_errors_course.funnel_plot()

# [√] TODO Barchart plot of time to resolve errors by course

bar_errors_resolvetime = MyPlot('CurricData.csv')
bar_errors_resolvetime.bar_chart_plot('Subject', 'TimeToResolution')                        

'''View'''

# [√] TODO Create Dashboard

external_stylesheets = ['https://codepen.io/hdotsone/pen/bGRaroj.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
colors = {
    'background': '#F0F8FF',
    'text': '#00008B'
}

app.layout = html.Div(children=[
    html.H1(children="Curriculum Data Dashboard"),
    html.Div(children="Count of Issue By Assessment Subcategory"),
    dcc.Graph(id="pie1", figure = pie_errors_category.plotme()),
    html.Div(children="Courses by Issue Count"),
    dcc.Graph(id="funnel1", figure = funnel_errors_course.plotme()),
    html.Div(children="Total Time To Resolution (Minutes)"),
    dcc.Graph(id="bar1", figure = bar_errors_resolvetime.plotme())
])

# [√] TODO Deploy on Flask

if "__main__" == __name__:
    app.run_server(debug=True)
