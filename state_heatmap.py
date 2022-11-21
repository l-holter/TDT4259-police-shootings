# Shootings per state total
import plotly.express as px
import pandas as pd

df = pd.read_csv('datasets/fatal-police-shootings-data.csv')

series = df['state'].value_counts()


heatmap_df = pd.DataFrame({'state':series.index, 'shootings':series.values})

fig = px.choropleth(heatmap_df,
                    locations='state', 
                    locationmode="USA-states",
                    color='shootings',
                    scope="usa",
                    color_continuous_scale="reds", 
                   )
fig.show()
