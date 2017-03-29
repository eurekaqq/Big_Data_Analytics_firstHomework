import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel

data = pd.read_csv("../dataset/LargeTrain.csv")

columnsName = data.columns

X = np.array(data.ix[:,0:1804])
y = np.array(data.ix[:,1804:1805]).ravel()

clf = ExtraTreesClassifier()
clf = clf.fit(X,y)

result = sorted(zip(columnsName,clf.feature_importances_), key = lambda x : -x[1])

print("Feature ranking:")
for i in range(8):
        print("{0}. {1} ({2})".format(i+1,result[i][0],round(result[i][1],4)))
                  
plt.figure(1)
plt.title("Feature importances")
plt.bar(range(8),[result[i][1]for i in range(8)],color="r", align="center")
plt.savefig("../picture/randomforest.png")
