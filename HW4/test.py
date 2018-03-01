import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

import numpy as np
import pandas as pd
import scipy
import peakutils


milk_data = pd.read_csv('production.csv')
time_series = milk_data['Monthly milk production (pounds per cow)']
time_series = time_series.tolist()

df = milk_data[0:15]

table = FF.create_table(df)
py.offline.iplot(table, filename='milk-production-dataframe')


trace = go.Scatter(
    x = [j for j in range(len(time_series))],
    y = time_series,
    mode = 'lines'
)

data = [trace]
py.iplot(data, filename='milk-production-plot')