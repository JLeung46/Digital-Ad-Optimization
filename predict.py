import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc


def read_data():
	'''
	Reads in train and test data.
	Returns
	-------
	train (DataFrame): train DataFrame
	test (DataFrame): test DataFrame
	'''
	train = pd.read_csv(os.path.join(settings.PROCESSED_DIR,"train.csv"))
	test = pd.read_csv(os.path.join(settings.PROCESSED_DIR,"test.csv"))

	# Use only rows with labels
	train = train[train['object_type'] == 3]
	test = test[test['object_type'] == 3]
	return (train,test)

def predict(train,test):
	'''
	Trains model and make predictions.
	Parameters
	----------
	train (DataFrame): train DataFrame
	test (DataFrame): test DataFrame
	Returns
	-------
	result: AUC score.
	'''
	features = settings.FEATURES

	train_y = train['is_click']
	test_y = test['is_click']

	model = LogisticRegression()

	model.fit(train[features], train_y)

	probs_test = model.predict_proba(test[features])[:,1]
	fpr_test, tpr_test, thresholds_test = roc_curve(test_y, probs_test)
	result = auc(fpr_test, tpr_test)
	print result


if __name__ == '__main__':
	data = read_data()
	predict(data[0],data[1])

