import pandas as pd
import numpy as np
import datetime

# Utility functions


def get_date_time(str_date):
	'''
	Converts string date to date time object
	'''
    if len(str_date) == 0:
        return 'None'
    else:
        dt_format = "%Y-%m-%d %H:%M:%S.%f"
        return datetime.datetime.strptime(str_date, dt_format)


def read_raw():
	'''
	Reads in raw data file
	'''
	df = pd.read_csv(os.path.join(settings.PROCESSED_DIR,"sample1M.csv"))
	return df


def process(df):
	'''
	Takes in the raw data and performs data processing & feature engineering
	Input: Raw dataframe
	Output: Processed csv file
	'''
	df['search_date'] = df['search_date'].map(lambda x:get_date_time(x))
	df['month'] = df['search_date'].map(lambda x: x.month)
	df['day'] = df['search_date'].map(lambda x: x.day)
	df['weekday'] = df['search_date'].map(lambda x: x.weekday())
	df['hour'] = df['search_date'].map(lambda x: x.hour)
	df['is_query'] = df['search_query'].map(lambda x: 1 if str(x) != 'nan' else 0 )
	df['ads_shown'] = df.groupby('search_id')['ad_id'].transform("count")
	df.to_csv(os.path.join(settings.PROCESSED_DIR, "processed_data.csv"))

if __name__ == '__main__':
	data = read_raw()
	process(data)
	print 'Data Processed..!'