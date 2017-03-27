import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
from sklearn.feature_selection import *

data = pd.read_csv("LargeTrain.csv")
names = data.columns
X = np.array(data.ix[:,0:1804])
y = np.array(data.ix[:,1804:1805]).ravel()

feature = SelectKBest(f_classif,k = 1)
feature = feature.fit_transform(X,y)
result = zip(names,feature)
sorted(result,key = lambda x : -x[1])
result
