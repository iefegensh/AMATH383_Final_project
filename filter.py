import pandas as pd
df = pd.read_csv('C:/Users/86130/Desktop/AMATH383/project/data_download_file_global_antivirals_2020.csv')
filtered_df = df[df['location_name'] == 'United States of America']
filtered_df.to_csv('ddd1.csv', index=False)
