# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 13:56:51 2022

@author: ABOCHI
"""

import pandas as pd
data = pd.read_csv("transaction.csv", sep=";")
data.info()
CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

ProfitPerItem = SellingPricePerItem - CostPerItem
CostPerTransaction = CostPerItem * NumberOfItemsPurchased
ProfitPerTransaction = ProfitPerItem * NumberOfItemsPurchased
SalesPerTransaction = SellingPricePerItem * NumberOfItemsPurchased

data["ProfitPerItem"] = data["SellingPricePerItem"] - data["CostPerItem"]
data["ProfitPerTransaction"]=data["ProfitPerItem"]*data["NumberOfItemsPurchased"]
data['CostPerTransaction']=data['CostPerItem']*data['NumberOfItemsPurchased']
data['SalesPerTransaction']=data['SellingPricePerItem']*data['NumberOfItemsPurchased']
data['MarkUp']=(data['SalesPerTransaction']-data['CostPerTransaction'])/data['CostPerTransaction']

data['MarkUp'] = round(data['MarkUp'], 2)

day=data['Day'].astype(str)
print(day.dtype)
year=data['Year'].astype(str)
Date = day + '-' + data['Month'] + '-' + year
data['Date'] = Date
data.info()

#data.drop(data[Date])

#Using the "split" function
SplitColumn = data['ClientKeywords'].str.split(',', expand = True)
data['ClientAge'] = SplitColumn[0]
data['ClientType'] = SplitColumn[1]
data['LengthOfContract'] = SplitColumn[2]

#Using the "replace" function
data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']', '')

#Using the "lower" function
data['ItemDescription'] = data['ItemDescription'].str.lower()

#HOW TO MERGE FILES
#Bringing in a new dataset
seasons = pd.read_csv('value_inc_seasons.csv', sep = ';') 

#Using the "merge" function
#merge_df = pd.merge(old_df, new_df, on = "key")
data = pd.merge(data, seasons, on = 'Month')

#Dropping columns
#df = df.drop("column_name", axis = 1)
data = data.drop('ClientKeywords', axis = 1)
data = data.drop(['Year', 'Month', 'Day'], axis = 1)

#Export into csv
#df.to_csv("filename.csv", index = false/true)
data.to_csv('ValueIncSales_Cleaned.csv', index = False)
