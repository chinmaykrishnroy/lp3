# %% [markdown]
# # Given a bank customer, build a neural network-based classifier that can determine whether they will leave or not in the next 6 months.
# Dataset Description: The case study is from an open-source dataset from Kaggle. The dataset contains 10,000 sample points with 14 distinct features such as CustomerId, CreditScore, Geography, Gender, Age, Tenure, Balance, etc.
# Link to the Kaggle project: https://www.kaggle.com/barelydedicated/bank-customer-churn-modeling Perform following steps:
# 1.	Read the dataset.
# 2.	Distinguish the feature and target set and divide the data set into training and test sets.
# 3.	Normalize the train and test data.
# 4.	Initialize and build the model. Identify the points of improvement and implement the same.
# 5.	Print the accuracy score and confusion matrix.
#  

# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt #Importing the libraries

# %%
df = pd.read_csv("Churn_Modelling.csv")

# %% [markdown]
# # Preprocessing. 

# %%
df.head()

# %%
df.shape

# %%
df.describe()

# %%
df.isnull()

# %%
df.isnull().sum()

# %%
df.info()

# %%
df.dtypes

# %%
df.columns

# %%
df = df.drop(['RowNumber', 'Surname', 'CustomerId'], axis= 1) #Dropping the unnecessary columns 

# %%
df.head()

# %% [markdown]
# # Visualization

# %%
def visualization(x, y, xlabel):
    plt.figure(figsize=(10,5))
    plt.hist([x, y], color=['red', 'green'], label = ['exit', 'not_exit'])
    plt.xlabel(xlabel,fontsize=20)
    plt.ylabel("No. of customers", fontsize=20)
    plt.legend()

# %%
df_churn_exited = df[df['Exited']==1]['Tenure']
df_churn_not_exited = df[df['Exited']==0]['Tenure']

# %%
visualization(df_churn_exited, df_churn_not_exited, "Tenure")

# %%
df_churn_exited2 = df[df['Exited']==1]['Age']
df_churn_not_exited2 = df[df['Exited']==0]['Age']

# %%
visualization(df_churn_exited2, df_churn_not_exited2, "Age")

# %% [markdown]
# # Converting the Categorical Variables

# %%
X = df[['CreditScore','Gender','Age','Tenure','Balance','NumOfProducts','HasCrCard','IsActiveMember','EstimatedSalary']]
states = pd.get_dummies(df['Geography'],drop_first = True)
gender = pd.get_dummies(df['Gender'],drop_first = True)

# %%

df = pd.concat([df,gender,states], axis = 1)

# %% [markdown]
# # Splitting the training and testing Dataset

# %%
df.head()

# %%
X = df[['CreditScore','Age','Tenure','Balance','NumOfProducts','HasCrCard','IsActiveMember','EstimatedSalary','Male','Germany','Spain']]

# %%
y = df['Exited']

# %%
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.30)

# %% [markdown]
# # Normalizing the values with mean as 0 and Standard Deviation as 1

# %%
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

# %%
X_train  = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# %%
X_train

# %%
X_test

# %% [markdown]
# # Building the Classifier Model using Keras 

# %%
import keras #Keras is the wrapper on the top of tenserflow
#Can use Tenserflow as well but won't be able to understand the errors initially. 

# %%
from keras.models import Sequential #To create sequential neural network
from keras.layers import Dense #To create hidden layers

# %%
classifier = Sequential()

# %%
#To add the layers
#Dense helps to contruct the neurons
#Input Dimension means we have 11 features 
# Units is to create the hidden layers
#Uniform helps to distribute the weight uniformly
classifier.add(Dense(activation = "relu",input_dim = 11,units = 6,kernel_initializer = "uniform")) 

# %%
classifier.add(Dense(activation = "relu",units = 6,kernel_initializer = "uniform"))   #Adding second hidden layers

# %%
classifier.add(Dense(activation = "sigmoid",units = 1,kernel_initializer = "uniform")) #Final neuron will be having siigmoid function

# %%
classifier.compile(optimizer="adam",loss = 'binary_crossentropy',metrics = ['accuracy']) #To compile the Artificial Neural Network. Ussed Binary crossentropy as we just have only two output

# %%
classifier.summary() #3 layers created. 6 neurons in 1st,6neurons in 2nd layer and 1 neuron in last

# %%
classifier.fit(X_train,y_train,batch_size=10,epochs=50) #Fitting the ANN to training dataset

# %%
y_pred =classifier.predict(X_test)
y_pred = (y_pred > 0.5) #Predicting the result

# %%
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report

# %%
cm = confusion_matrix(y_test,y_pred)

# %%
cm

# %%
accuracy = accuracy_score(y_test,y_pred)

# %%
accuracy

# %%
plt.figure(figsize = (10,7))
sns.heatmap(cm,annot = True)
plt.xlabel('Predicted')
plt.ylabel('Truth')

# %%
print(classification_report(y_test,y_pred))

# %%



