# %% [markdown]
# ## Assignment 2
# 2.	Classify the email using the binary classification method. Email Spam detection has two states: a) Normal State – Not Spam, b) Abnormal State – Spam. Use K-Nearest Neighbors and Support Vector Machine for classification. Analyze their performance.
# Dataset link: The emails.csv dataset on the Kaggle https://www.kaggle.com/datasets/balaka18/email-spam-classification-dataset-csv
# 
# 

# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics

# %%
df=pd.read_csv('emails.csv')

# %%
df.head()

# %%
df.columns

# %%
df.isnull().sum()

# %%
df.dropna(inplace = True)

# %%
df.drop(['Email No.'],axis=1,inplace=True)
X = df.drop(['Prediction'],axis = 1)
y = df['Prediction']

# %%
from sklearn.preprocessing import scale
X = scale(X)
# split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)

# %% [markdown]
# ##KNN classifier

# %%
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=7)
 
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

# %%
print("Prediction",y_pred)

# %%
print("KNN accuracy = ",metrics.accuracy_score(y_test,y_pred))

# %%
print("Confusion matrix",metrics.confusion_matrix(y_test,y_pred))

# %% [markdown]
# ## SVM classifier

# %%
# cost C = 1
model = SVC(C = 1)

# fit
model.fit(X_train, y_train)

# predict
y_pred = model.predict(X_test)

# %%
metrics.confusion_matrix(y_true=y_test, y_pred=y_pred)

# %%
print("SVM accuracy = ",metrics.accuracy_score(y_test,y_pred))


