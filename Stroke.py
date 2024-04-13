# Data source: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset

# Findings from this analysis indicate that less than 5% of stroke victims were under the age of 50, the probability of getting a stroke increases exponentially as age increases, and this study could be used to conduct 
# hypothesis testing for the proportion of any age group that is at risk of a stroke.


df = pd.read_csv(filepath_or_buffer='Practice Datasets/Dataset.csv', index_col=0, na_filter=False)
df['Decade'] = (df['age'] - (df['age'] % 10)) 
df = df.rename(columns=str.capitalize)
decadeCount = df[['Decade', 'Stroke']].groupby(['Decade']).value_counts()
currentDecade = 0.0
print('Likelihood of stroke by age group')
ages = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90'];
percentages = []
for i in range(0, 9):
    print((str(int(currentDecade)) + ' - ' + str(int(currentDecade + 10))).ljust(7), end='')
    try:
        total = decadeCount.loc[(currentDecade, 0)] + decadeCount.loc[(currentDecade, 1)]
    except KeyError:
        percentage = 0
    else:
        percentage = decadeCount.loc[(currentDecade, 1)] / total
    percentages.append(percentage)
    print(str(round(percentage * 100, 1)).rjust(32), end='')
    print('%')
    currentDecade += 10
plt.xlabel('Age Group')
plt.ylabel('Probability of Stroke')
plt.bar(ages, percentages, color='r')
