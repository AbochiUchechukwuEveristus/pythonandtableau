# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 23:40:43 2022

@author: ABOCHI
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


#Reading excel or xlsx files
data = pd.read_excel('articles.xlsx')

#summary of data
data.describe()
#summary of column
data.info()

#counting number of articles per source
data.groupby(['source_id']) ['article_id'].count()
#number of reaction by publisher
data.groupby(['source_id']) ['engagement_reaction_count'].sum() 

#dropping a column
data = data.drop('engagement_comment_plugin_count', axis = 1)

#creating a python function
#def AboutMe(name, surname, location):
    #print('My name is ' + name + ' my surname is ' + surname + ' i am from ' + location)
    #return name, surname, location
#aboutMe = AboutMe('Uchechukwu', 'Abochi', 'Enugu')

#FastFood = ['Noodles', 'bread', 'snacks']
#def FavFood(food):
    #for x in food:
        #print('My top food is ' + x)        
#FavFood(FastFood)        

# keyword = 'crash'
# length = len(data )
# keyword_flag = []
# for x in range(0, length):
#     heading = data['title'] [x]
#     if keyword in heading:
#         flag = 1
#     else:
#         flag = 0
#     keyword_flag.append(flag)


def KeywordFlag(keyword):
    length = len(data)
    keyword_flag = []
    for x in range(0, length):
        heading = data['title'] [x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag

keyword_flag = KeywordFlag('murder')

data['keyword_flag'] = pd.Series(keyword_flag)

#SentimentIntensityAnalyzer

sent_int = SentimentIntensityAnalyzer()
text = data['title'][15]
sent = sent_int.polarity_scores(text)
pos = sent['pos']
neg = sent['neg']
neu = sent['neu']



title_pos_sentiment = []
title_neg_sentiment = []
title_neu_sentiment = []

length = len(data)

for x in range(0, length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        pos = sent['pos']
        neg = sent['neg']
        neu = sent['neu'] 
    except:
        pos = 0
        neg = 0
        neu = 0
    title_pos_sentiment.append(pos)
    title_neg_sentiment.append(neg)
    title_neu_sentiment.append(neu)
    
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neg_sentiment = pd.Series(title_neg_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

data['title_pos_sentiment'] = title_pos_sentiment
data['title_neg_sentiment'] = title_neg_sentiment
data['title_neu_sentiment'] = title_neu_sentiment




data.to_excel('blogme_clean.xlsx', sheet_name='blogmedata', index = False)













