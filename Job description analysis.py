import pandas as pd
import numpy as np
import re

def countWords(series, job_description):
    for word in re.split('[,\s\-!?:()]+', job_description):
        if word.capitalize() in series.index:
            series[word.capitalize()] += 1
        else:
            series[word.capitalize()] = 1
            
df = pd.read_csv('Practice Datasets/archive/postings.csv', dtype={'job title': 'string', 
                'company': 'string', 'job location': 'string', 'job link': 'string', 
                'first_seen': 'string', 'search_city': 'string', 'search country': 'category', 
                'job level': 'category', 'job type': 'category', 'job summary': 'string'}, 
                 parse_dates=['first_seen'])

filter = df['job_summary'].isna() == False
df = df[filter]
seriesList = []
for category in df['job level'].dtype.categories:
    list = []
    series = pd.Series(dtype='int64', name=category)
    filter = df['job level'] == category
    tempDF = df[filter]
    for i in range(0, len(tempDF)):
        countWords(series, tempDF.iloc[i, 9])
    seriesList.append(series)


skillDF = pd.DataFrame(seriesList)
skillDF.fillna(0, inplace=True)
skillDF = skillDF.T
