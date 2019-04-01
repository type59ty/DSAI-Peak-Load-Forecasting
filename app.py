import csv
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.svm import SVC
from math import sqrt
import warnings
warnings.filterwarnings('ignore')

def read_data():
    max_peak  = []
    peak_load = []
    nxweek_max_peak  = []
    nxweek_peak_load = []
    with open("power_dataset.csv", newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            max_peak.append (float(row['max_peak']))
            peak_load.append(float(row['peak_load']))
    
    with open("next_week.csv", newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            nxweek_max_peak.append (float(row['max_peak'])*10)
            nxweek_peak_load.append(float(row['peak_load'])*10)
    
    X_train = np.array(max_peak ).reshape(-1,1)
    y_train = np.array(peak_load).reshape(-1,1)
    X_test  = np.array(nxweek_max_peak).reshape(-1,1)
    y_test  = np.array(nxweek_peak_load).reshape(-1,1)
    return X_train,y_train,X_test,y_test

def training(X_train,y_train,X_test,y_test):
    model = SVC(kernel='poly' ,gamma='scale', degree=9, C=1.0, max_iter=20000).fit(X_train, y_train)
    nxweek_pred = model.predict(X_test)
    result = sqrt(mean_squared_error(y_test, nxweek_pred))
    print("predicted RMSE: {}".format(result))
    print("score: {}".format(model.score(X_train,y_train)))
    return nxweek_pred

def output(nxweek_pred):
    with open('submission.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['date','peak_load(MW)'])
        for i in range(20190402,20190409):
            writer.writerow([i, int(nxweek_pred[i-20190402])])
    print("\nOutput file: submission.csv")


if __name__=='__main__':
    X_train,y_train,X_test,y_test = read_data()
    nxweek_pred = training(X_train,y_train,X_test,y_test)
    output(nxweek_pred)


