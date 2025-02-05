import matplotlib.pyplot as plt
import pandas as pd

# Data source: https://data.nasa.gov/resource/eva.json (with modifications)
# Open the input JSON file and the output CSV file
input_file = open('./eva-data.json', 'r')
output_file = open('./eva-data.csv', 'w')
graph_file = './cumulative_eva_graph.png'

# Converting the JSON to a dataframe and remove any missing values
eva_df = pd.read_json(input_file, convert_dates=['date'])
eva_df['eva'] = eva_df['eva'].astype(float)
eva_df.dropna(axis=0, inplace=True)

# Sort the data by date to maintain chronological order
eva_df.sort_values('date', inplace=True)

# Save the cleaned data to a CSV file
eva_df.to_csv(output_file, index=False)

# Convert duration from HH:MM format into total hours
eva_df['duration_hours'] = eva_df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
eva_df['cumulative_time'] = eva_df['duration_hours'].cumsum()

# Plotting
plt.plot(eva_df['date'], eva_df['cumulative_time'], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()

# Save and display the graph
plt.savefig(graph_file)
plt.show()