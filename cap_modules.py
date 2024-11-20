import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def count_plot_multi(dataset_arr, title, row, col):
  titles = []
  for ar in dataset_arr:
    titles.append(ar['title'])
    print(titles)
  fig = make_subplots(rows=row, cols=col, subplot_titles=titles)

  for idx, ar in enumerate(dataset_arr):
    print(idx)
    fig.append_trace(go.Bar(
      ar['data'],
      x= ar['x']
    ), row=idx+1, col=col )
    # fig.append_trace(go.Scatter(
    #     x=[3, 4, 5],
    #     y=[1000, 1100, 1200],
    # ), row=idx+1, col=col)

  fig.update_layout(height=600, width=600, title_text=title)
  fig.show()

def count_plot(dataset, x, title, sort=True):
  fig = px.histogram(dataset, x= x, title= title, text_auto=True)
  if sort:
    fig.update_layout(xaxis={'categoryorder': 'total descending'})
  fig.show()

  # __all__ = ["count_plot", "count_plot_multi"]