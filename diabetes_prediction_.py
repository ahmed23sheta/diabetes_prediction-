# -*- coding: utf-8 -*-
"""diabetes prediction .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yv7Jluglo2zlvAyYHcKr_LT44bYSOvF6
"""

#import libraries:
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn .metrics import accuracy_score

# upload dataset:
df = pd.read_csv('/content/diabetes.csv')

# show data:
df.head()

# show statistics values:
df.describe()

df.shape

# show all columns names:
print(df.columns.values)

# count outcome value (0,1):
df['Outcome'].value_counts()

"""

```
0--> non_diabetic
1--> diabetic
```

"""

# mean value of all columns group by diabetic & non_diabetic:
df.groupby('Outcome').mean()

# separating data & labels:
x= df.drop(columns=['Outcome'])
y= df['Outcome']

x

y

x.shape

"""**check null values in dataset:**"""

df.isnull().sum()

import numpy as np

df_copy = df.copy(deep=True)

df.columns

df_copy[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age']]=df_copy[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age']].replace(0,np.nan)

df_copy.isnull().sum()

"""replace null values with mean value of data:"""

df['Pregnancies']=df['Pregnancies'].replace(0,df['Pregnancies'].mean())
df['Glucose']=df['Glucose'].replace(0,df['Glucose'].mean())
df['BloodPressure']=df['BloodPressure'].replace(0,df['BloodPressure'].mean())
df['SkinThickness']=df['SkinThickness'].replace(0,df['SkinThickness'].mean())
df['Insulin']=df['Insulin'].replace(0,df['Insulin'].mean())
df['BMI']=df['BMI'].replace(0,df['BMI'].mean())

df.isnull().sum()

"""now we donot have any null values"""



"""**standardization data**"""

scaler=StandardScaler()

scaler.fit(x)

stander_df=scaler.transform(x)

stander_df

"""
 we notice that all data becomes between [0,1]"""

x= stander_df
y= df['Outcome']

print(x)
print('-'*40)
print(y)

"""**train_test_split**

"""

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.25,random_state=2,stratify=y)

print(x.shape,x_train.shape,x_test.shape)

"""**training the model**"""

classifier = svm.SVC(kernel='linear')

classifier.fit(x_train,y_train)

"""## model evaluation:

**accuracy_score**
"""

#accuracy score on training data
x_train_prediction= classifier.predict(x_train)
train_accuracy=accuracy_score(x_train_prediction,y_train)

print('accuracy score on training data: ',train_accuracy)

"""accuracy score on training data:  0.7881944444444444




"""

#accuracy score on test data
x_test_prediction= classifier.predict(x_test)
test_accuracy=accuracy_score(x_test_prediction,y_test)

print('accuracy score on test data: ',test_accuracy)

"""accuracy score on test data:  0.765625

**Making a Predictive System:**
"""

input_data = (5,166,72,19,175,25.8,0.587,51)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardize the input data
std_data = scaler.transform(input_data_reshaped)
print(std_data)

prediction = classifier.predict(std_data)
print(prediction)

if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')

