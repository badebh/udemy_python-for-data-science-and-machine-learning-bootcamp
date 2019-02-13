#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../../Pierian_Data_Logo.png' /></a>
# ___

# # SF Salaries Exercise 
# 
# Welcome to a quick exercise for you to practice your pandas skills! We will be using the [SF Salaries Dataset](https://www.kaggle.com/kaggle/sf-salaries) from Kaggle! Just follow along and complete the tasks outlined in bold below. The tasks will get harder and harder as you go along.

# ** Import pandas as pd.**
import pandas as pd


# ** Read Salaries.csv as a dataframe called sal.**
sal = pd.read_csv('Salaries.csv')


# ** Check the head of the DataFrame. **
#sal.head()


# ** Use the .info() method to find out how many entries there are.**
# why not use .shape?


# **What is the average BasePay ?**
sal['BasePay'].mean()


# ** What is the highest amount of OvertimePay in the dataset ? **
sal['OvertimePay'].max()


# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **
sal.loc[sal['EmployeeName']=='JOSEPH DRISCOLL', 'JobTitle']
# CAPTAIN, FIRE SUPPRESSION


# ** How much does JOSEPH DRISCOLL make (including benefits)? **
sal.loc[sal['EmployeeName']=='JOSEPH DRISCOLL', 'TotalPayBenefits']
# 270324.91


# ** What is the name of highest paid person (including benefits)?**
sal.iloc[sal['TotalPayBenefits'].idxmax()]['EmployeeName']
# NATHANIEL FORD


# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**
sal.iloc[sal['TotalPayBenefits'].idxmin()]['EmployeeName']
# Joe Lopez, he is paid -618.13 (odd)


# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **
sal.groupby('Year').mean()['BasePay']


# ** How many unique job titles are there? **
sal['JobTitle'].nunique()
# 2159


# ** What are the top 5 most common jobs? **
sal['JobTitle'].value_counts().head()
# Transit Operator, Special Nurse, Registered Nurse, Public..., Police Officer 3


# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **
s_vc = sal.loc[sal['Year'] == 2013, 'JobTitle'].value_counts()
s_vc.loc[s_vc == 1].shape
# (202,)


# ** How many people have the word Chief in their job title? (This is pretty tricky) **
sal.loc[sal['JobTitle'].str.contains('Chief', case=False)==True, 'JobTitle'].shape
# 627 (note his solution is wrong per the course article)


# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **
sal['title_len'] = sal['JobTitle'].apply(len)
sal[['title_len','TotalPayBenefits']].corr()