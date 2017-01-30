import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc


def read_data():
	train = pd.read_csv(os.path.join(settings.PROCESSED_DIR,"train.csv"))
	test = pd.read_csv(os.path.join(settings.PROCESSED_DIR,"test.csv"))
	return (train,test)

def predict():
	features = settings.FEATURES

