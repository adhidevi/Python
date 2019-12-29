import numpy as np#for multidimensional array support#
import pandas as pd#Data manipulation and analysis#
content = pd.read_csv('summary.txt', sep = '\t')
print('all content:')
print(content)#prints all the information in content#
##print('only the first few rows:') 
##print(content.head())#prints only first 5 rows by default#
##print('only the first 3 rows:')
##print(content.head(3))#prints only first 3 raws#
##content = content.rename(columns = {'Run':'MyRun'})
##print(content)
##single_column = content.Run#to read a single specified column#
##print(single_column)
##my_columns = content[['Run','HV']]#to read multiple specified columns#
##print(my_columns)
##single_row = content[content.Run == 3364]#to read single specified row#
##print(single_row)
##a_value = content.loc[2,'Run']#loc is used to refer to the row/column label names. The first argument with in [] refers to the label name for the specified row while the second argument refers to the label name for the specified column#
##print(a_value)
##values = content.loc[2,['Run','PreAmp']]#to read content of more than one column for a specified row#
##print(values)
##values = content.loc[[2,5],['Run','PreAmp']]#to read content of more than one column for more than one specified rows#
##print(values)
##values = content.loc[2:7,['Run','PreAmp']]#to read content of given columns for a given range in row#
##print(values)
##values = content.loc[2:,:]#to read all the columns for the given range in rows#
##print(values)
##values = content.iloc[2:7,3]#iloc is used to refer to the integer label names. It provides integer label names for rows and columns both starting from 0. Note:: iloc excludes the last integer in the given range while loc includes it. E.g in this case it excludes the row 7#
##print(values)
values = content.iloc[2:,3:]#similar to loc, iloc also uses open ranges#
print(values)
details = content.describe()#to display the statistics of the contents#
print(details)

