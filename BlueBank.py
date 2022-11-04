# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 23:09:02 2022

@author: ABOCHI
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#pd.read_json('loan_data_json.json')

json_file = open('loan_data_json.json')
data = json.load(json_file)


#Lists = ['apple', 'mango', 'pear', 'banana']
#print(Lists[1])

#coverting list to dataframe
loandata = pd.DataFrame(data)

#finding unique values for the purpose
loandata["purpose"].unique()
loandata.describe()
loandata['fico'].describe()
loandata['dti'].describe()

income = np.exp(loandata["log.annual.inc"])
loandata['annualincome'] = income

#working with if statements on FICO

# fico >= 300 and < 400: 'Very Poor' 
# fico >= 400 and ficoscore < 600: 'Poor' 
# fico >= 601 and ficoscore < 660: 'Fair' 
# fico >= 660 and ficoscore < 780: 'Good' 
# fico >=780: 'Excellent'

length = len(loandata)
ficocat = []
for x in range(0, length):
    category = loandata['fico'][x]
    try:
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 600 and category < 660:
            cat = 'Fair'        
        elif category >= 660 and category < 780:
            cat = 'Good'        
        elif category >= 780:
            cat = 'Excellent'        
        else:
            cat = 'Unknown'
    except:
        cat = 'Unknown'
            
    ficocat.append(cat)    
        
ficocat = pd.Series(ficocat)
        
        
loandata['fico.category'] = ficocat        
        
        
#df.loc[df [Column_Name] Condition, 'New_Column_Name'] = 'Value'        
loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type' ] = 'High'        
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type' ] = 'Low'  
      
#Number of loans/rows by fico.category
catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'blue', width = 0.1)
plt.show()

purplot = loandata.groupby(['purpose']).size()
purplot.plot.bar(color = 'red', width = 0.2)
plt.show()

#Scatter Plots
ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = 'red')
plt.show()

#Writing to CSV
loandata.to_csv('BlueBank_Cleaned.csv', index = True)