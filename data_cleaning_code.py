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


# Removing duplicates values from tpep_pickup_datetime and tpep_dropoff_datetime column and fixing the index.
data = data.drop_duplicates(['tpep_pickup_datetime', 'tpep_dropoff_datetime']).reset_index(drop=True)
# print(len(data["tpep_pickup_datetime"]))

# print(datetime_dim.columns)

# Just adding some columns.
data.loc[:, "pick_hour"] = data["tpep_pickup_datetime"].dt.hour
# print(data["pick_hour"])
data.loc[:, "pick_day"] = data["tpep_pickup_datetime"].dt.day
data.loc[:, "pick_weekday"] = data["tpep_pickup_datetime"].dt.weekday
data.loc[:, "pick_month"] = data["tpep_pickup_datetime"].dt.month
data.loc[:, "pick_year"] = data["tpep_pickup_datetime"].dt.year

# print(data.info())

data.loc[:, "drop_hour"] = data["tpep_pickup_datetime"].dt.hour
data.loc[:, "drop_day"] = data["tpep_pickup_datetime"].dt.day
data.loc[:, "drop_weekday"] = data["tpep_pickup_datetime"].dt.weekday
data.loc[:, "drop_month"] = data["tpep_pickup_datetime"].dt.month
data.loc[:, "drop_year"] = data["tpep_pickup_datetime"].dt.year

# print(data.info())

data["datetime_id"] = data.index
# print(data["datetime_id"])