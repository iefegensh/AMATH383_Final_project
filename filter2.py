import pandas as pd
df = pd.read_csv('C:/Users/86130/Desktop/AMATH383/project/ddd1.csv')
selected_columns = [
    "location_name", "date", "cumulative_cases", "daily_deaths", "daily_cases", "cumulative_all_vaccinated",
    "hospital_beds_mean", "infection_fatality", "cumulative_deaths","mask_use_mean"
]
filtered_df = df[selected_columns]
filtered_df.to_csv('ddd2.csv', index=False)
