import pandas as pd

#create and loading different dataset
data = {'Name':['jai','princi','gaurav','anju','ravi','natasha','riya'],
        'Age':[17,17,18,17,18,17,17],
        'Gender': ['M','F','M','M','M','F','F'],
        'Marks':[90,76,'nan',74,65,'nan',71]}
a = pd.DataFrame(data)
a.to_csv("mustofa.csv")#creaate csv file save as mustofa.csv
print(a,"\n")

#loading database from csv type dataset
b = pd.read_csv('mustofa.csv')
print("Read Dataset from csv file \n")
print(b)


#question ii


import numpy as np
import statistics as stats
import pandas as pd

dd = {'roll':[1,2,4,5,3,2,4,5,2,3]}
cdd = pd.DataFrame(dd)
cdd.to_csv('cdata.csv')
print(cdd)
cdata = pd.read_csv('cdata.csv')

#finding mean
mean = np.mean(cdata)
print("\n")
print("mean",mean)

#finding  median
median = np.median(cdata)
print("median:",median)

#finding mode
mode = stats.mode(cdata['roll'])
print("mode:",mode)

#finding variance
variance = np.var(cdata['roll'])
variance = round(variance,2)
print('variance:',variance)

#finding standard deviation
std_dev = np.std(cdata['roll'])
std_dev = round(std_dev,2)
print('standard Deviation:',std_dev)
