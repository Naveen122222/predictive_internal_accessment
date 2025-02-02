# -*- coding: utf-8 -*-
"""LVADSUSR100_Naveen_lab1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hVLea1w0IqOnsjcmPTNYOGIqD1uxgLru
"""

import pandas as pd

data=pd.read_csv('/content/expenses.csv')
df=pd.DataFrame(data)
df.head()

# Here we Don't Have any null values

df.isnull().sum()

df=df.dropna()

import matplotlib.pyplot as plt
plt.boxplot(df['bmi'])
plt.show()

# here it is showing that threshold value as nearly 47

#removing outliers
threshold_value=47
df=df[df['bmi']<=47]
print(df)

df.head()

from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
df['sex']=encoder.fit_transform(df['sex'])
df['smoker']=encoder.fit_transform(df['smoker'])
df['region_encoder']=encoder.fit_transform(df['region'])

df.head()
regions=df['region']
df=df.drop(['region'],axis=1)
df.head()

df.head()

# to remove duplicate rows we have one function

df.drop_duplicates()
# we have any duplicate rows, so it will remove rows from the data

X=df.drop(['charges'],axis=1)
y=df['charges']

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=42,test_size=0.3)

from sklearn.linear_model import LinearRegression

linear=LinearRegression()

linear.fit(X_train,y_train)

predictions=linear.predict(X_test)
print(predictions)

from sklearn.metrics import mean_squared_error,r2_score,accuracy_score,classification_report,mean_absolute_error
import numpy as np

print("Mean Square Error is : ",mean_squared_error(predictions,y_test))


print("r2_Score is  : ",r2_score(predictions,y_test))

print("Root Mean Square Error is  : ",np.sqrt(mean_squared_error(predictions,y_test)))

print("Mean_absolute_Error : ",mean_absolute_error(predictions,y_test))