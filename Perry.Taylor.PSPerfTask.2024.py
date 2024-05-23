import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = "2023 Spring Alumni Survey Data - Sheet1.csv"
df = pd.read_csv(file, index_col=1, dtype={'race (populated from SIS)': 'category',
                 'gender': 'category'}, parse_dates=['degree conferral date (populated from SIS)'])
'''
raceDF = df[['race (populated from SIS)', 'satisfied with preparation at Relay']].dropna().groupby('race (populated from SIS)').mean().dropna()
genderDF = df[['gender (populated from SIS)', 'satisfied with preparation at Relay']].dropna()

genderDF.plot.hist(by='gender (populated from SIS)', legend=False, figsize=(6.4, 9.6))
plt.tight_layout(pad=1.3)
plt.xlabel('Satisfaction Rating')
plt.show()


raceDF.plot.barh(legend=False)
plt.xlabel('Average Satisfaction Rating')
plt.ylabel('Race')
plt.show()

filter = (df['Please select the position that best describes your current professional role.'] != 'Other role outside the field of PK-12 education') & (df['intention to work in PK-12 education'].isna() == False) & (df['intention to work in PK-12 education'] != 'Not returning')
df2 = df[filter]

description = {61: 'Mission of social justice/improving outcomes for kids',
               62: 'I am happy at my school/district',
               63: 'I love the art of teaching',
               64: 'I love working with kids',
               65: 'I am loyal to school staff/leadership',
               66: 'It supports the lifestyle I want to lead',
               67: 'I am committed to my community and the families I work with'}
series = pd.Series()
for column in range(61, 68):
    series[description[column]] = (len(df2.iloc[:, column].str.match('.').dropna()) / len(df2)) * 100
'''

