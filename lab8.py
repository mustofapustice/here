import numpy as np
import pandas as pd
df=pd.read_csv('Social_Network_Ads.csv')
print(df)
df.shape
x=df.iloc[:,[0,1]]
print(x)
y=df.iloc[:,2]
print(y)

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=.40,random_state=1)

print('Training data : ',xtrain.shape)
print('Testing data : ',xtest.shape)
print(xtrain)
print(xtest)
print(ytrain)
print(ytest)
model=SVC(gamma='auto')
model.fit(xtrain,ytrain)
aa=model.score(xtest,ytest)
print(aa)