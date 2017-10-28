import pandas as pd
import os.path
import matplotlib.pyplot as plt

import numpy as np
import datetime
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import Ridge


df=pd.read_csv(os.path.dirname(__file__)+'/flights_fet_sel.csv')


#Drop rows that has nan in any of the column values
df= df.dropna() 
#Collect all the str values 
df_str = df.filter(["ACTL_ARR_ARPT_CD","ACTL_DPRT_ARPT_CD","DOM_INTL_TYP_CD","FLT_LEG_ADD_RSN_CD","SCH_ARR_ARPT_CD","SCH_DPRT_ARPT_CD"], axis=1)
#Create categorical values into dummy variables
df_dummy  = pd.get_dummies(df_str)
#Drop the columns for which dummy columns are created
df = df.drop(["ACTL_ARR_ARPT_CD","ACTL_DPRT_ARPT_CD","DOM_INTL_TYP_CD","FLT_LEG_ADD_RSN_CD","SCH_ARR_ARPT_CD","SCH_DPRT_ARPT_CD"], axis=1)
#Join dummy columns with the original df
df=pd.concat([df,df_dummy], axis=1)



#Split the flight data into train and test. Train data is FLT_ORIG_DT < 2017, 1, 31
df_train_X = df[pd.to_datetime(df['FLT_ORIG_DT']).apply(lambda x:x.date()) < datetime.date(2017, 1, 31)]
df_train_X=df_train_X.drop('FLT_ORIG_DT', 1)
#Create train Y with ARR_TIME_DELAY
df_train_Y = np.array(df_train_X['ARR_TIME_DELAY'])
#Remove ARR_TIME_DELAY from the input feature 
df_train_X = df_train_X.drop('ARR_TIME_DELAY', 1)
df_train_X=np.array(df_train_X)

#Test data is FLT_ORIG_DT >= 2017, 1, 31
df_test_X  = df[pd.to_datetime(df['FLT_ORIG_DT']).apply(lambda x:x.date()) >= datetime.date(2017, 1, 31)]
df_test_X=df_test_X.drop('FLT_ORIG_DT', 1)
#Create train Y with ARR_TIME_DELAY
df_test_Y = np.array(df_test_X['ARR_TIME_DELAY'])
#Remove ARR_TIME_DELAY from the input feature 
df_test_X = df_test_X.drop('ARR_TIME_DELAY', 1)
df_test_X=np.array(df_test_X)

# Create Ridge regression object  
ridge = Ridge(alpha=4000)
ridge.fit(df_train_X, df_train_Y)

# Make predictions using the testing set
df_test_Y_pred = ridge.predict(df_test_X)


# The mean squared error, lower the better
print("Mean squared error: %.2f"
      % mean_squared_error(df_test_Y, df_test_Y_pred))
# Explained variance score: 1 is perfect prediction
print('r2 Variance score: %.2f' % r2_score(df_test_Y, df_test_Y_pred))


#print("Accuracy Score=",lasso.score(df_test_Y.reshape(-1,1), df_test_Y_pred.reshape(-1,1)))

# Plot outputs
plt.scatter(df_test_X[:,0], df_test_Y,  color='black')
plt.plot(df_test_X[:,0], df_test_Y_pred, color='blue', linewidth=1)
plt.xlabel("Test Departure Delay (Hours)")
plt.ylabel("Test Arrival Delay (Hours)")


plt.show()
