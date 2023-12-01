import pandas as pd

data = pd.read_csv('C:/Users/86130/Desktop/AMATH383/project/ddd2.csv')
data['date'] = pd.to_datetime(data['date'])
start_date = '2020-02-28'
end_date = '2020-04-28'
data = data[(data['date'] >= start_date) & (data['date'] <= end_date)]
data['sequential_number'] = range(1, len(data) + 1)
data.to_csv('ddd3.csv', index=False)
