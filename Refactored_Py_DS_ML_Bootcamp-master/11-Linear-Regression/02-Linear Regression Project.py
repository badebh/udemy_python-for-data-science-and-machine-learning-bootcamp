#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# # Linear Regression Project
# 
# Congratulations! You just got some contract work with an Ecommerce company based in New York City that sells 
# clothing online but they also have in-store style and clothing advice sessions. Customers come in to the store, 
# have sessions/meetings with a personal stylist, then they can go home and order either on a mobile app or website for the clothes they want.
# 
# The company is trying to decide whether to focus their efforts on their mobile app experience or their website. 
# They've hired you on contract to help them figure it out! Let's get started!
# 
# Just follow the steps below to analyze the customer data (it's fake, don't worry I didn't give you real credit card numbers or emails).

# ## Imports
# ** Import pandas, numpy, matplotlib,and seaborn. Then set %matplotlib inline 
# (You'll import sklearn as you need it.)**
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ## Get the Data
# 
# We'll work with the Ecommerce Customers csv file from the company. 
# It has Customer info, suchas Email, Address, and their color Avatar. 
# Then it also has numerical value columns:
# 
# * Avg. Session Length: Average session of in-store style advice sessions.
# * Time on App: Average time spent on App in minutes
# * Time on Website: Average time spent on Website in minutes
# * Length of Membership: How many years the customer has been a member. 
# 
# ** Read in the Ecommerce Customers csv file as a DataFrame called customers.**
customers = pd.read_csv('Ecommerce Customers.csv')


# **Check the head of customers, and check out its info() and describe() methods.**
#print(customers.head())
#print(customers.describe())
#print(customers.info())


# ## Exploratory Data Analysis
# 
# **Let's explore the data!**
# 
# For the rest of the exercise we'll only be using the numerical data of the csv file.
# ___
# **Use seaborn to create a jointplot to compare the Time on Website and Yearly Amount Spent columns. Does the correlation make sense?**
#sns.jointplot(customers['Time on Website'], customers['Yearly Amount Spent'])

# ** Do the same but with the Time on App column instead. **
#sns.jointplot(customers['Time on App'], customers['Yearly Amount Spent'])

# ** Use jointplot to create a 2D hex bin plot comparing Time on App and Length of Membership.**
#sns.jointplot(customers['Time on App'], customers['Length of Membership'], kind='hex')


# **Let's explore these types of relationships across the entire data set. 
# Use [pairplot](https://stanford.edu/~mwaskom/software/seaborn/tutorial/axis_grids.html#plotting-pairwise-relationships-with-pairgrid-and-pairplot) 
# to recreate the plot below.(Don't worry about the the colors)**
#sns.pairplot(customers)

# **Based off this plot what looks to be the most correlated feature with Yearly Amount Spent?**
# Length of membership

# **Create a linear model plot (using seaborn's lmplot) of  Yearly Amount Spent vs. Length of Membership. **
#sns.lmplot('Length of Membership', 'Yearly Amount Spent', customers)
#plt.show()


# ## Training and Testing Data
# 
# Now that we've explored the data a bit, let's go ahead and split the data into training and testing sets.
# ** Set a variable X equal to the numerical features of the customers and a variable y equal to the "Yearly Amount Spent" column. **
x = customers[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
y = customers['Yearly Amount Spent']

# ** Use model_selection.train_test_split from sklearn to split the data into training and testing sets. 
# Set test_size=0.3 and random_state=101**
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=101)


# ## Training the Model
# 
# Now its time to train our model on our training data!
# 
# ** Import LinearRegression from sklearn.linear_model **
from sklearn.linear_model import LinearRegression

# **Create an instance of a LinearRegression() model named lm.**
lm = LinearRegression()

# ** Train/fit lm on the training data.**
lm.fit(x_train, y_train)


# **Print out the coefficients of the model**
coeff_df = pd.DataFrame(lm.coef_, x.columns, columns=['coeff'])
print(coeff_df)


# ## Predicting Test Data
# Now that we have fit our model, let's evaluate its performance by predicting off the test values!
# 
# ** Use lm.predict() to predict off the X_test set of the data.**
predictions = lm.predict(x_test)

# ** Create a scatterplot of the real test values versus the predicted values. **
#sns.scatterplot(y_test, predictions)
#plt.show()


# ## Evaluating the Model
# 
# Let's evaluate our model performance by calculating the residual sum of squares and the explained variance score (R^2).
# 
# ** Calculate the Mean Absolute Error, Mean Squared Error, and the Root Mean Squared Error. 
# Refer to the lecture or to Wikipedia for the formulas**
from sklearn import metrics
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))
print('R^2:', metrics.explained_variance_score(y_test, predictions))


# ## Residuals
# 
# You should have gotten a very good model with a good fit. Let's quickly explore the residuals to make sure everything was okay with our data. 
# 
# **Plot a histogram of the residuals and make sure it looks normally distributed. Use either seaborn distplot, or just plt.hist().**
sns.distplot((y_test-predictions),bins=50)
plt.show()


# ## Conclusion
# We still want to figure out the answer to the original question, do we focus our efforst on mobile app or website development? 
# Or maybe that doesn't even really matter, and Membership Time is what is really important.  
# Let's see if we can interpret the coefficients at all to get an idea.
# 
# ** Recreate the dataframe below. **
# see coeff_df

# ** How can you interpret these coefficients? **
# For a 1 unit increase in avg. session length we expect a 25.98 unit increase in yearly amount spent
# same for the next three columns

# **Do you think the company should focus more on their mobile app or on their website?**
# the app (coeff of 38.59 for app vs. 0.19 for website)