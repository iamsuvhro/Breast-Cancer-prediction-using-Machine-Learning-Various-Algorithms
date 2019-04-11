import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
import seaborn as sns # used for plot interactive graph. I like it most for plot
from sklearn.linear_model import LogisticRegression # to apply the Logistic regression
from sklearn.model_selection import train_test_split # to split the data into two parts
from sklearn.cross_validation import KFold # use for cross validation
from sklearn.model_selection import GridSearchCV# for tuning parameter
from sklearn.ensemble import RandomForestClassifier # for random forest classifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm # for Support Vector Machine
from sklearn import metrics # for the check the error and accuracy of the model
%matplotlib inline
import warnings
warnings.filterwarnings("ignore")

#df is dataframe and its self a variable & here i import the dataset into this variable
df=pd.read_csv("cancer.csv")
#it will show top 5 data rows

#deleting the useless columns
df.drop(['id'], 1, inplace=True)
df.drop(['Unnamed: 32'], 1, inplace=True)
y=df['diagnosis']
main_pred_var = ['texture_mean','perimeter_mean','smoothness_mean','compactness_mean','symmetry_mean']

# spliting the dataset into two part
train_set,test_set=train_test_split(df, test_size=0.2)

x_train=train_set[main_pred_var]
y_train=train_set.diagnosis

x_test=test_set[main_pred_var]
y_test=test_set.diagnosis