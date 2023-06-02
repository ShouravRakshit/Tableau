import pandas as pd

data = pd.read_csv("Uber Data Analysis Project/uber_data.csv")
# print(type(data["tpep_pickup_datetime"]))
# print(data.info())

data['tpep_pickup_datetime'] = pd.to_datetime(data['tpep_pickup_datetime'])
data['tpep_dropoff_datetime'] = pd.to_datetime(data['tpep_dropoff_datetime'])

# print(data.info())
# is_duplicate = []
# Checking which columns have duplicate values
# for i in range(len(data.columns)):
#     has_duplicates = data[f'{data.columns[i]}'].duplicated().any()
#     is_duplicate.append(has_duplicates)


# Removing duplicates values from tpep_pickup_datetime and tpep_dropoff_datetime column.
datetime_dim = data.drop_duplicates(['tpep_pickup_datetime', 'tpep_dropoff_datetime'])
# print(len(data["tpep_pickup_datetime"]))

print(datetime_dim.columns)
