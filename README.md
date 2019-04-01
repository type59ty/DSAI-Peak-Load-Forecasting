# DSAI - Peak Load Forecasting

## Files
- **README. md**
This file
- **requirements.txt**
The packages you need to install at first.
- **forecasting.ipynb**
The main program built in jupyter-notebook.
- **app. py**
The main program. 
- **next_week.csv**
The [estimated results](https://data.gov.tw/dataset/33462) of power supply for the next week from Taiwan Power Company.
- **power_dataset.csv**
The [power usage dateset](https://data.gov.tw/dataset/19995)  ( 2017/01/01 ~ 2019/02/28 ) from Taiwan Power Company.
- **submission.csv**
The predicted peak load for the next week. ( 2019/04/02 ~ 2019/04/08 )



## Predicting method
Use svm-svc model from scikit-learn. The training data is '淨尖峰供電能力' and '尖峰負載' from the power_data set. 
The reason of choosing these feature is that '淨尖峰供電能力' is the estimated value of maximum of '尖峰負載' from Taiwan Power Company. So it is the most related feature to the '尖峰負載', which we want to predict.


