import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv("data.csv")
fig = ff.create_distplot([df["AVG(Rating)"].tolist()], ["AVG"], show_hist=False)
fig.show()