# Shootings per state per capita
import plotly.express as px
import pandas as pd


def per_capita(count, population):
    return count / (population / 1000000)

# Shootings database
df_shootings = pd.read_csv('datasets/fatal-police-shootings-data.csv')
# Population database
df_population = pd.read_csv('datasets/us_pop_by_state.csv')
#Count by states and shootings
series = df_shootings['state'].value_counts()
# Convert to dataframe
heatmap_df = pd.DataFrame({'state':series.index, 'shootings':series.values})
# Pro-gamer move with columns
df_population.columns = ['rank','state_code','state','2020_census','percent_of_total']

# Join dataframes
join_df = heatmap_df.merge(df_population, on='state', how='left')

# Add per capita column with map
join_df['rate'] = join_df.apply(lambda row : per_capita(row['shootings'],
                     row['2020_census']), axis = 1)

# Sort by rate
final_df = join_df.sort_values('rate', ascending=False)
#print(final_df)
# Plot rates
fig = px.choropleth(join_df,
                    locations='state', 
                    locationmode="USA-states",
                    color='rate',
                    scope="usa",
                    color_continuous_scale="reds", 
                )

fig.update_layout(
      title_text = 'Lethal police shootings per state per capita',
      title_font_family="Times New Roman",
      title_font_size = 22,
      title_font_color="black", 
      title_x=0.45,
    )

fig.show()
