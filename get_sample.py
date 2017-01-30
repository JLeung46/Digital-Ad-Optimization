import sqlite3
from pandas.io import sql
import pandas as pd


def sample_data():
	'''
	Connects to database and samples 1M rows,
	saves sample as csv file.
	'''

	file = os.listdir(settings.DATA_DIR)

	conn = sqlite3.connect('file')

	conn.execute('CREATE TABLE SAMPLE AS SELECT * FROM trainSearchStream JOIN SearchInfo ON trainSearchStream.SearchID = SearchInfo.SearchID')

	conn.execute('CREATE TABLE SAMPLE_1M AS SELECT * FROM (SELECT * FROM SAMPLE ORDER BY sample.UserID ASC LIMIT 1000000) AS subsample LEFT JOIN AdsInfo ON subsample.AdID = AdsInfo.AdID')

	data = conn.execute('SELECT * FROM SAMPLE_1M')

	df = pd.DataFrame(data.fetchall())

	df.to_csv(os.path.join(settings,PROCESSED_DIR, "{}.csv"),encoding='utf-8')

if __name__ == "__main__":
	sample_data()