#the first part of the challenge was to assemble the files with '_DLI' and export them back to CSV

import pandas as pd 
import glob, os
#creating the light variable assembles all the files with _DLI in the name
light = glob.glob("*_DLI")
#I then created a variable named dli 
dli = pd.concat([pd.read_csv(file) for file in light])
#sort by date 
dli.sort_values(by=['Date'], inplace=True, ascending=True)
#convert to csv file 
dli.to_csv('only_dli_asendingdate.csv')

#then we needed to clean the data to make sure we had the relevant columns

#Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Reading the data
df = pd.read_csv('only_dli_asendingdate.csv')
print(df.shape)
print(df.info())

#this provides a statistical summary of all the quantitative variables.
df.describe()

#deleting an unwanted column
df = df.drop(columns=['Unnamed: 0'])

#used the IQR to find any outliers 
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print(IQR)

#

#the second part of the challenge was to assemble the files without '_DLI' and export them back to CSV

#created a dark variable to assemble all the files without _DLI in the name

dark = set(glob.glob("*")) - set(glob.glob("*_DLI*"))

#there was a problem with this, so created a for loop to find out there the error occurred

df = pd.DataFrame()
for file in dark:
    print(file)
    df = pd.concat([pd.read_csv(file, delimiter='\t', encoding='UTF-8')])

#this allowed me to spot the file which couldn't be read so we now had to work out how to clean the files

#created the variable experiment to concatenate the files with a for loop 
experiment = pd.concat([pd.read_csv(file) for file in dark])

#this produced NaN values and created unwanted column that i needed to clean - i had to split the weird column i got after generating the non-dli df

#Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Reading the data
df2 = pd.read_csv('non_dli_dates.csv')
print(df2.shape)
print(df2.info())

#print df2
df2

#isolate the unwanted column
df2 = df2["Date\tTimestamp\t?moles"]

#get rid of all the NaN values in a row

df2 = df2.dropna(axis='rows')

#convert to a string then split it by /t
split = df2.str.split('\t')
split

#created a new df 
df_split = pd.DataFrame(split)

#spliting the column into seperate columns
df_split[['Date','Timestamp','μmoles']] = pd.DataFrame(df_split['Date\tTimestamp\t?moles'].tolist(), index= df_split.index)

#dropped the column in favour for our three new ones
df_split = df_split.drop(columns=['Date\tTimestamp\t?moles'])
df_split

#date formatting from dd/mm/yyyy to yyyy-mm-dd (standard)

df_split['Date'] = pd.to_datetime(df_split['Date'])

#this saved 4310 which would have been lost 

#then created df3 because now we need to combine the two dataframes which we initally split up

#Reading the data
df3 = pd.read_csv('non_dli_dates.csv')
print(df3.shape)
print(df3.info())

#dropped a column
df3 = df3.drop(columns=['Date\tTimestamp\t?moles','Dates','?moles'])

#dropped another column 

df3 = df3.drop(columns=['Unnamed: 0'])

#deleted all NaN values
df3 = df3.dropna(axis='rows')

#have all the data now minus the 4310 which was split

#created a variable called anotherone to concatenate df3 and df_split

anotherone = pd.concat([df3, df_split], ignore_index=True)

#produced unwanted 00:00:00 for some od the files 

anotherone['Date'] = pd.to_datetime(anotherone['Date'])

anotherone['new_date_column'] = anotherone['Date'].dt.date

anotherone.loc[anotherone['Date']=='2019-10-10', ['Date']]

#this got rid of the 00:00:00 and created a new_date_column column that needed to be dropped 

anotherone = anotherone.drop(columns=['new_date_column'])

#converted that into a CSV file 
anotherone.to_csv('non-dli-final.csv')