pip install matplotlib
pip install seaborn
import pandas as pd
data = pd.read_csv('data.csv')
import pandas as pd
data = pd.read_csv('data_startup_final.csv')
!pwd
import pandas as pd
data = pd.read_csv('data/data_startup_final.csv')
data.head()
import matplotlib.pyplot as plt
plt.plot(data['x'], data['y'])
plt.show()
data.count()
df['Y'] =(df.went_public_on.notnull()) | (df.exited_on.notnull())
data['Y'] =(df.went_public_on.notnull()) | (df.exited_on.notnull())
data['Y'] =(data.went_public_on.notnull()) | (data.exited_on.notnull())
df = data
df = data
df['Y'] =(df.went_public_on.notnull()) | (df.exited_on.notnull())
df['Y'] =(df.went_public_on.notnull()) | (df.exited_on.notnull())
df_target_value.counts()
df['Y'].counts()
df['Y'] = target_values
target_values = df['Y']
target_values.counts()
import pandas as pd
df = pd.read_csv('data/data_startup_final.csv')
df.head()
df.count()
df['Y'] = df['went_public_on'].fillna(df['exited_on'])
df['Y']
df['Y'] = df['went_public_on'].notnull() | df['exited_on'].notnull()
df['Y'].count()
grouped = df.groupby(['industry_name', pd.Grouper(key='Y', freq='Y')])['name'].count().reset_index()
df['Y'] = pd.to_datetime(df['Y'], errors='coerce')
grouped = df.groupby(['industry_name', pd.Grouper(key='Y', freq='Y')])['name'].count().reset_index()
default_date = pd.to_datetime(df['founded_on'].min(), format='%Y-%m-%d')
df['Y'] = df['Y'].fillna(default_date)
df['Y'] = pd.to_datetime(df['Y'], errors='coerce')
grouped = df.groupby(['industry_name', pd.Grouper(key='Y', freq='Y')])['name'].count().reset_index()
pivoted = grouped.pivot(index='industry_name', columns='Y', values='name').reset_index()
pivoted.plot.bar(x='industry_name', stacked=True)
plt.xlabel('Industry')
plt.ylabel('Count')
plt.title('Counts of Companies by Industry and Y Variable Value')
plt.show()
top_categories = counts.head(3).index.tolist()
top_categories = industry_name.counts.head(3).index.tolist()
top_categories = industry_name.counts(3).index.tolist()
top_categories = ['industry_name'].counts(3).index.tolist()
top_categories = ['industry_name'].counts(3)
top_categories = ['industry_name'].counts(3)
pivoted = pivoted.sort_values(by=pivoted.columns[1:].sum(), ascending=False)
pivoted = pivoted.head(3)
ax = pivoted.plot.bar(x='industry_name', stacked=True)
plt.xlabel('Industry')
plt.ylabel('Count')
plt.title('Counts of Companies by Industry and Y Variable Value (Top 3 Categories)')
for i, patch in enumerate(ax.patches):
    if i % 3 == 0:
        patch.set_facecolor('#1f77b4')
    elif i % 3 == 1:
        patch.set_facecolor('#ff7f0e')
    else:
        patch.set_facecolor('#2ca02c')

plt.show()
for i, patch in enumerate(ax.patches):
    if i % 3 == 0:
        patch.set_facecolor('#1f77b4')
    elif i % 3 == 1:
        patch.set_facecolor('#ff7f0e')
    else:
        patch.set_facecolor('#2ca02c')

plt.show()
plt.xlabel('Industry')
plt.ylabel('Count')
plt.title('Counts of Companies by Industry and Y Variable Value (Top 3 Categories)')
for i, patch in enumerate(ax.patches):
    if i % 3 == 0:
        patch.set_facecolor('#1f77b4')
    elif i % 3 == 1:
        patch.set_facecolor('#ff7f0e')
    else:
        patch.set_facecolor('#2ca02c')

plt.show()
top_categories = ['healthcare', 'consumer electronics', 'financial services']
df_top_categories = df[df['industry_name'].isin(top_categories)]
grouped = df_top_categories.groupby(['industry_name', pd.Grouper(key='Y', freq='Y')])['name'].count().reset_index()
pivoted = grouped.pivot(index='industry_name', columns='Y', values='name').reset_index()
pivoted = pivoted.sort_values(by=pivoted.columns[1:].sum(), ascending=False)
pivoted = grouped.pivot(index='industry_name', columns='Y', values='name').reset_index()
pivoted = pivoted.sort_values(by=pivoted.columns[1:].sum(), ascending=False)
ax = pivoted.plot.bar(x='industry_name', stacked=True)
import matplotlib.pyplot as plt

plt.hist(df['employeeCount'], bins=30)
plt.xlabel('Number of employees')
plt.ylabel('Frequency')
plt.title('Distribution of Employee Count')
plt.show()
import matplotlib.pyplot as plt

plt.hist(df['employeeCount'], bins=50)
plt.xlabel('Number of employees')
plt.ylabel('Frequency')
plt.title('Distribution of Employee Count')
plt.show()
import matplotlib.pyplot as plt

plt.hist(df['employeeCount'], bins=1000)
plt.xlabel('Number of employees')
plt.ylabel('Frequency')
plt.title('Distribution of Employee Count')
plt.show()
import matplotlib.pyplot as plt

plt.hist(df['employeeCount'], bins=100)
plt.xlabel('Number of employees')
plt.ylabel('Frequency')
plt.title('Distribution of Employee Count')
plt.show()
import matplotlib.pyplot as plt

plt.hist(df['employeeCount'], bins=10)
plt.xlabel('Number of employees')
plt.ylabel('Frequency')
plt.title('Distribution of Employee Count')
plt.show()
import matplotlib.pyplot as plt

plt.hist(df['employeeCount'], bins=10)
plt.xlabel('Number of employees')
plt.ylabel('Frequency')
plt.title('Distribution of Employee Count')
plt.xlim([0, 10000])
plt.show()
import matplotlib.pyplot as plt

plt.hist(df['employeeCount'], bins=10)
plt.xlabel('Number of employees')
plt.ylabel('Frequency')
plt.title('Distribution of Employee Count')
plt.xlim([0, 8000])
plt.show()
import matplotlib.pyplot as plt

plt.hist(df['employeeCount'], bins=10)
plt.xlabel('Number of employees')
plt.ylabel('Frequency')
plt.title('Distribution of Employee Count')
plt.xlim([0, 5000])
plt.show()
import matplotlib.pyplot as plt

plt.hist(df['employeeCount'], bins=10)
plt.xlabel('Number of employees')
plt.ylabel('Frequency')
plt.title('Distribution of Employee Count')
plt.xlim([0, 5000])
plt.ylim([0, 100000])
plt.show()
import matplotlib.pyplot as plt

plt.hist(df['employeeCount'], bins=10)
plt.xlabel('Number of employees')
plt.ylabel('Frequency')
plt.title('Distribution of Employee Count')
plt.xlim([0, 5000])
plt.ylim([0, 10])
plt.show()
import matplotlib.pyplot as plt

plt.hist(df['employeeCount'], bins=10)
plt.xlabel('Number of employees')
plt.ylabel('Frequency')
plt.title('Distribution of Employee Count')
plt.xlim([0, 5000])
plt.ylim([0, 300])
plt.show()
import matplotlib.pyplot as plt

plt.hist(df['employeeCount'], bins=10)
plt.xlabel('Number of employees')
plt.ylabel('Frequency')
plt.title('Distribution of Employee Count')
plt.xlim([0, 5000])
plt.ylim([0, 100])
plt.show()
import matplotlib.pyplot as plt

plt.hist(df['employeeCount'], bins=10)
plt.xlabel('Number of employees')
plt.ylabel('Frequency')
plt.title('Distribution of Employee Count')
plt.xlim([0, 5000])
plt.ylim([0, 1000])
plt.show()
import matplotlib.pyplot as plt

plt.hist(df['employeeCount'], bins=10)
plt.xlabel('Number of employees')
plt.ylabel('Frequency')
plt.title('Distribution of Employee Count')
plt.xlim([0, 5000])
plt.ylim([0, 10000])
plt.show()
counts = df['employee_count'].value_counts().to_frame()
counts = df['employeeCount'].value_counts().to_frame()
counts.plot(kind='bar')
plt.xlabel('Industry')
plt.ylabel('Number of Companies')
plt.title('Number of Companies by Industry')
plt.show()
counts.plot(kind='bar')
plt.xlabel('Industry')
plt.ylabel('Number of Companies')
plt.title('Number of Companies by Industry')
plt.show()
for i, v in enumerate(counts.sort_values(by='employeeCount', ascending=False)['employeeCount']):
    plt.text(v + 3, i + .25, str(v), color='black', fontsize=10)
counts.sort_values(by='employeeCount', ascending=False).plot(kind='barh', figsize=(6,4), legend=False)
for i, v in enumerate(counts.sort_values(by='employeeCount', ascending=False)['employeeCount']):
    plt.text(v + 3, i + .25, str(v), color='black', fontsize=10)
for i, v in enumerate(counts.sort_values(by='employeeCount', ascending=False)['employeeCount']):
    plt.text(v + 2, i + .15, str(v), color='black', fontsize=10)
plt.xlabel('Number of Employees')
plt.ylabel('Company')
plt.title('Number of Employees by Company')
counts = df.groupby('industry_name')['employeeCount'].count()
counts = counts.sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(10,8))
counts.plot(kind='barh', color='blue')
df = df.dropna(subset=['exited_on', 'founded_on'])
df['founded_year'] = pd.DatetimeIndex(df['founded_on']).year
df['exited_year'] = pd.DatetimeIndex(df['exited_on']).year
count_by_founded_year = df.groupby(['founded_year']).size()
count_by_exited_year = df.groupby(['exited_year']).size()
plt.bar(count_by_founded_year.index, count_by_founded_year.values, alpha=0.5, label='Founded')
plt.bar(count_by_exited_year.index, count_by_exited_year.values, alpha=0.5, label='Exited')
plt.xlabel('Year')
plt.ylabel('Count')
plt.legend()
plt.show()
plt.bar(df['founded_on'], df['exited_on'])
count_by_exited_year = df.groupby(['exited_year']).size()
plt.bar(df['founded_on'], df['exited_on'])
plt.xlim(min(df['founded_on']), max(df['founded_on']) + 1)
plt.bar(df['founded_on'], df['exited_on'])
count_by_exited_year = df.groupby(['exited_year']).size()
plt.xlim(min(df['founded_on']), max(df['founded_on']) + 1)
plt.xlim(min(df['founded_on']), max(df['founded_on']) + str(10))
plt.bar(count_by_founded_year.index, count_by_founded_year.values, alpha=0.5, label='Founded')
plt.bar(count_by_exited_year.index, count_by_exited_year.values, alpha=0.5, label='Exited')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Relationship between Exited On and Founded On')
plt.legend()
plt.show()
plt.bar(count_by_founded_year.index, count_by_founded_year.values, alpha=0.5, label='Founded')
plt.bar(count_by_exited_year.index, count_by_exited_year.values, alpha=0.5, label='Exited')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Relationship between Exited On and Founded On')
plt.xlim(min(df['founded_on']), max(df['founded_on']) + str(10))
plt.legend()
plt.show()
plt.bar(count_by_founded_year.index, count_by_founded_year.values, alpha=0.5, label='Founded')
plt.bar(count_by_exited_year.index, count_by_exited_year.values, alpha=0.5, label='Exited')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Relationship between Exited On and Founded On')
plt.legend()
plt.show()
plt.bar(count_by_founded_year.index, count_by_founded_year.values, alpha=0.5, label='Founded')
plt.bar(count_by_exited_year.index, count_by_exited_year.values, alpha=0.5, label='Exited')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Relationship between Exited On and Founded On')
plt.legend()
plt.xlim(2000, 2030)
plt.show()
plt.bar(count_by_founded_year.index, count_by_founded_year.values, alpha=0.5, label='Founded')
plt.bar(count_by_exited_year.index, count_by_exited_year.values, alpha=0.5, label='Exited')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Relationship between Exited On and Founded On')
plt.legend()
plt.xlim(2000, 2025)
plt.show()
plt.bar(count_by_founded_year.index, count_by_founded_year.values, alpha=0.5, label='Founded')
plt.bar(count_by_exited_year.index, count_by_exited_year.values, alpha=0.5, label='Exited')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Relationship between Exited On and Founded On')
plt.legend()
plt.xlim(2015, 2025)
plt.xlim(0, 9000)
plt.show()
plt.bar(count_by_founded_year.index, count_by_founded_year.values, alpha=0.5, label='Founded')
plt.bar(count_by_exited_year.index, count_by_exited_year.values, alpha=0.5, label='Exited')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Relationship between Exited On and Founded On')
plt.legend()
plt.xlim(2015, 2025)
plt.ylim(0, 9000)
plt.show()
plt.bar(count_by_founded_year.index, count_by_founded_year.values, alpha=0.5, label='Founded')
plt.bar(count_by_exited_year.index, count_by_exited_year.values, alpha=0.5, label='Exited')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Relationship between Exited On and Founded On')
plt.legend()
plt.xlim(2015, 2025)
plt.ylim(0, 10000)
plt.show()
plt.bar(count_by_founded_year.index, count_by_founded_year.values, alpha=0.5, label='Founded')
plt.bar(count_by_exited_year.index, count_by_exited_year.values, alpha=0.5, label='Exited')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Relationship between Exited On and Founded On')
plt.legend()
plt.xlim(2015, 2025)
plt.show()
plt.bar(count_by_founded_year.index, count_by_founded_year.values, alpha=0.5, label='Founded')
plt.bar(count_by_exited_year.index, count_by_exited_year.values, alpha=0.5, label='Exited')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Relationship between Exited On and Founded On')
plt.legend()
plt.xlim(2015, 2024)
plt.show()
plt.bar(count_by_founded_year.index, count_by_founded_year.values, alpha=0.5, label='Founded')
plt.bar(count_by_exited_year.index, count_by_exited_year.values, alpha=0.5, label='Exited')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Relationship between Exited On and Founded On')
plt.legend()
plt.xlim(2014, 2024)
plt.show()
plt.bar(count_by_founded_year.index, count_by_founded_year.values, alpha=0.5, label='Founded')
plt.bar(count_by_exited_year.index, count_by_exited_year.values, alpha=0.5, label='Exited')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Relationship between Founded Date and Exit')
plt.legend()
plt.xlim(2014, 2024)
plt.show()
import seaborn as sns

# create a bar plot
sns.barplot(x='ipo_status', y='num_funding_rounds', data=df)

# set plot title and axis labels
plt.title('Number of funding rounds vs IPO status')
plt.xlabel('IPO status')
plt.ylabel('Number of funding rounds')

# show the plot
plt.show()
import seaborn as sns

colors = ['blue', 'green', 'yellow']

# create a bar plot
sns.barplot(x='ipo_status', y='num_funding_rounds', data=df, colors=colors)

# set plot title and axis labels
plt.title('Number of Funding rounds vs IPO status')
plt.xlabel('IPO status')
plt.ylabel('Number of funding rounds')

# show the plot
plt.show()
import seaborn as sns

# create a bar plot
sns.barplot(x='ipo_status', y='num_funding_rounds', data=df)

# set plot title and axis labels
plt.title('Number of Funding rounds vs IPO status')
plt.xlabel('IPO status')
plt.ylabel('Number of funding rounds')

# show the plot
plt.show()
import seaborn as sns

colors = ['blue', 'green', 'yellow']
sns.set_palette(sns.color_palette(colors))

# create a bar plot
sns.barplot(x='ipo_status', y='num_funding_rounds', data=df)

# set plot title and axis labels
plt.title('Number of Funding rounds vs IPO status')
plt.xlabel('IPO status')
plt.ylabel('Number of funding rounds')

# show the plot
plt.show()
import seaborn as sns

colors = ['blue', 'green', 'yellow']
sns.set_palette(sns.color_palette(colors))

# create a bar plot
sns.barplot(x='ipo_status', y='num_funding_rounds', data=df)

# set plot title and axis labels
plt.title('Number of Funding rounds vs IPO status')
plt.xlabel('IPO status')
plt.ylabel('Number of funding rounds')
sns.set_style('whitegrid')
sns.set_palette('pastel')
ax = sns.barplot(x=x, y=y, width=0.5)

# show the plot
plt.show()
import seaborn as sns

colors = ['blue', 'green', 'yellow']
sns.set_palette(sns.color_palette(colors))
sns.set_style('whitegrid')
sns.set_palette('pastel')

# create a bar plot
sns.barplot(x='ipo_status', y='num_funding_rounds', data=df)

# set plot title and axis labels
plt.title('Number of Funding rounds vs IPO status')
plt.xlabel('IPO status')
plt.ylabel('Number of funding rounds')

# show the plot
plt.show()
import seaborn as sns

colors = ['blue', 'green', 'yellow']
sns.set_palette(sns.color_palette(colors))
sns.set_style('whitegrid')
sns.set_palette('pastel')

# create a bar plot
sns.barplot(x='ipo_status', y='num_funding_rounds', data=df, width=0.5)

# set plot title and axis labels
plt.title('Number of Funding rounds vs IPO status')
plt.xlabel('IPO status')
plt.ylabel('Number of funding rounds')

# show the plot
plt.show()
import seaborn as sns

colors = ['blue', 'green', 'yellow']
sns.set_palette(sns.color_palette(colors))
sns.set_style('whitegrid')
sns.set_palette('pastel')

# create a bar plot
sns.barplot(x='ipo_status', y='num_funding_rounds', data=df)

# set plot title and axis labels
plt.title('Number of Funding rounds vs IPO status')
plt.xlabel('IPO status')
plt.ylabel('Number of funding rounds')

# show the plot
plt.show()
plt.bar(count_by_founded_year.index, count_by_founded_year.values, alpha=0.5, label='Founded')
plt.bar(count_by_exited_year.index, count_by_exited_year.values, alpha=0.5, label='Exited')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Relationship between Founded Date and Exit')
plt.legend()
plt.xlim(2014, 2024)
plt.set_style('whitegrid')
plt.set_palette('pastel')
plt.show()
plt.bar(count_by_founded_year.index, count_by_founded_year.values, alpha=0.5, label='Founded')
plt.bar(count_by_exited_year.index, count_by_exited_year.values, alpha=0.5, label='Exited')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Relationship between Founded Date and Exit')
plt.legend()
plt.xlim(2014, 2024)
plt.set_palette('pastel')
plt.show()
plt.bar(count_by_founded_year.index, count_by_founded_year.values, alpha=0.5, label='Founded')
plt.bar(count_by_exited_year.index, count_by_exited_year.values, alpha=0.5, label='Exited')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Relationship between Founded Date and Exit')
plt.legend()
plt.xlim(2014, 2024)
plt.show()
plt.bar(count_by_founded_year.index, count_by_founded_year.values, alpha=0.5, label='Founded')
plt.bar(count_by_exited_year.index, count_by_exited_year.values, alpha=0.5, label='Exited')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Relationship between Founded Date and Exit')
plt.legend()
plt.xlim(2014, 2024)
plt.show()
fig, ax = plt.subplots(figsize=(10,8))
counts.plot(kind='barh', color='green')
colors = colors = ['blue', 'green']
plt.bar(count_by_founded_year.index, count_by_founded_year.values, alpha=0.5, label='Founded')
plt.bar(count_by_exited_year.index, count_by_exited_year.values, alpha=0.5, label='Exited')
plt.bar(color=colors)
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Relationship between Founded Date and Exit')
plt.legend()
plt.xlim(2014, 2024)
plt.show()
plt.bar(count_by_founded_year.index, count_by_founded_year.values, alpha=0.5, label='Founded')
plt.bar(count_by_exited_year.index, count_by_exited_year.values, alpha=0.5, label='Exited')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Relationship between Founded Date and Exit')
plt.legend()
plt.xlim(2014, 2024)
plt.show()
plt.bar(count_by_founded_year.index, count_by_founded_year.values, alpha=0.5, label='Founded')
plt.bar(count_by_exited_year.index, count_by_exited_year.values, alpha=0.5, label='Exited')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Relationship between Founded Date and Exit')
plt.legend()
plt.xlim(2014, 2024)
plt.show()
fig, ax = plt.subplots(figsize=(10,8))
counts.plot(kind='barh', color='green')
plt.set_palette('pastel')
fig, ax = plt.subplots(figsize=(10,8))
counts.plot(kind='barh', color='green')
import seaborn as sns
sns.set_palette('pastel')
grouped = df.groupby('employeeCount')['num_funding_rounds'].mean()
plt.bar(grouped.index, grouped.values, color='b')
plt.bar(grouped.index, grouped.values, color='blue')
plt.bar(grouped.index, grouped.values, color='blue')
plt.xlabel('Employee Count')
plt.ylabel('Average Funding Rounds')
plt.title('Relationship between Employee Count and Funding Rounds')
plt.show()
grouped = df.groupby('stage')['num_funding_rounds'].mean()
plt.bar(grouped.index, grouped.values, color='blue')
plt.xlabel('Employee Count')
plt.ylabel('Average Funding Rounds')
plt.title('Relationship between Employee Count and Funding Rounds')
plt.show()
plt.bar(grouped.index, grouped.values, color='green')
plt.xlabel('Total Money Raised')
plt.ylabel('Number of Funding Rounds')
plt.title('Relationship between Capital Raised and Funding Rounds')
plt.show()
plt.bar(grouped.index, grouped.values, color='green')
plt.xlabel('Total Money Raised')
plt.ylabel('Number of Funding Rounds')
plt.title('Relationship between Capital Raised and Funding Rounds')
plt.figure(figsize = (8,6))
plt.show()
plt.bar(grouped.index, grouped.values, color='green')
plt.xlabel('Total Money Raised')
plt.ylabel('Number of Funding Rounds')
plt.title('Relationship between Capital Raised and Funding Rounds')
plt.figure(figsize = (10,6))
plt.show()
plt.bar(grouped.index, grouped.values, color='green')
plt.xlabel('Total Money Raised')
plt.ylabel('Number of Funding Rounds')
plt.title('Relationship between Capital Raised and Funding Rounds')
plt.figure(figsize = (15,6))
plt.show()
plt.figure(figsize = (15,6))
plt.bar(grouped.index, grouped.values, color='green')
plt.xlabel('Total Money Raised')
plt.ylabel('Number of Funding Rounds')
plt.title('Relationship between Capital Raised and Funding Rounds')
plt.show()
grouped = df.groupby('stage')['moneyRaised'].mean()
grouped = df.groupby('moneyRaised')['num_funding_rounds'].mean()
plt.figure(figsize = (15,6))
plt.bar(grouped.index, grouped.values, color='green')
plt.xlabel('Funding Stages')
plt.ylabel('Average Number of Rounds')
plt.title('Avergae number of rounds per stages')
plt.show()
grouped = df.groupby('moneyRaised')['num_funding_rounds'].mean()
plt.figure(figsize = (15,6))
plt.bar(grouped.index, grouped.values, color='green')
plt.xlabel('Funding Stages')
plt.ylabel('Average Number of Rounds')
plt.title('Avergae number of rounds per stages')
plt.show()
plt.figure(figsize = (15,6))
plt.bar(grouped.index, grouped.values, color='g')
plt.xlabel('Funding Stages')
plt.ylabel('Average Number of Rounds')
plt.title('Avergae number of rounds per stages')
plt.show()
plt.bar(grouped.index, grouped.values, color='green')
plt.xlabel('Total Money Raised')
plt.ylabel('Number of Funding Rounds')
plt.title('Relationship between Capital Raised and Funding Rounds')
plt.figure(figsize = (15,6))
plt.show()
grouped = df.groupby('stage')['num_funding_rounds'].sum()
grouped.plot(kind='bar', color=['red', 'blue', 'green', 'purple'])
grouped = df.groupby('moneyRaised')['num_funding_rounds'].mean()
plt.bar(grouped.index, grouped.values, color='green')
plt.xlabel('Total Money Raised')
plt.ylabel('Number of Funding Rounds')
plt.title('Relationship between Capital Raised and Funding Rounds')
plt.figure(figsize = (8,6))
plt.show()
grouped = df.groupby('moneyRaised')['stage'].mean()
grouped = df.groupby('stage')['moneyRaised'].mean()
grouped = df.groupby('num_funding_rounds')['moneyRaised'].mean()
grouped = df.groupby('num_funding_rounds')['moneyRaised'].mean()
%history -f myhistory.py
grouped = df.groupby('stage')['num_funding_rounds'].mean()
plt.bar(grouped.index, grouped.values, color='blue')
plt.xlabel('Employee Count')
plt.ylabel('Average Funding Rounds')
plt.title('Relationship between Employee Count and Funding Rounds')
plt.show()
plt.figure(figsize = (15,6))
plt.bar(grouped.index, grouped.values, color='green')
plt.xlabel('Employee Count')
plt.ylabel('Average Funding Rounds')
plt.title('Relationship between Employee Count and Funding Rounds')
plt.show()
plt.figure(figsize = (15,6))
plt.bar(grouped.index, grouped.values, color='green')
plt.xlabel('Funding Stage')
plt.ylabel('Average Number of Rounds')
plt.title('Number of Rounds per Stage')
plt.show()
grouped = df.groupby('stage')['moneyRaised'].mean()
grouped = df.groupby('stage')[moneyRaised].mean()
grouped = df.groupby('stage')['moneyRaised'].mean()
df['moneyRaised'] = df['moneyRaised'].astype(str)
grouped = df.groupby('stage')['moneyRaised'].mean()
import json

money_str = '{"amount": 5995500, "currency": "USD", "amountUSD": 5995500}'
money_dict = json.loads(money_str)
money_float = float(money_dict['amount'])

print(money_float)
grouped = df.groupby('stage')['money_float'].mean()
grouped = df.groupby('stage')[money_float].mean()
df['moneyRaised'] = pd.to_numeric(df['moneyRaised'], errors='coerce')
df.dropna(subset=['moneyRaised'], inplace=True)
grouped = df.groupby('stage')['moneyRaised'].mean()
grouped = df.groupby(['stage', 'num_funding_rounds'])['moneyRaised'].mean()
grouped = df.groupby('stage')['moneyRaised'].mean()
plt.figure(figsize = (15,6))
plt.bar(grouped.index, grouped.values, color='green')
plt.xlabel('Funding Stage')
plt.ylabel('Average Size of Funding Rounds')
plt.title('Size of rounds per stage')
plt.show()
grouped = df.groupby(['stage', 'num_funding_rounds'])['moneyRaised'].mean()
plt.figure(figsize = (15,6))
plt.bar(grouped.index, grouped.values, color='green')
plt.xlabel('Funding Stage')
plt.ylabel('Average Size of Funding Rounds')
plt.title('Size of rounds per stage')
plt.show()
plt.figure(figsize = (15,6))
plt.bar(grouped.index, grouped.values, color='green')
plt.xlabel('Funding Stage')
plt.ylabel('Average Number of Rounds')
plt.title('Average Rounds per Stage')
plt.show()
plt.figure(figsize = (15,6))
plt.bar(grouped.index, grouped.values, color='green')
plt.xlabel('Funding Stage')
plt.ylabel('Average Number of Rounds')
plt.title('Number of Rounds per Stage')
plt.show()
grouped = df.groupby('stage')['num_funding_rounds'].mean()
plt.figure(figsize = (15,6))
plt.bar(grouped.index, grouped.values, color='green')
plt.xlabel('Funding Stage')
plt.ylabel('Average Number of Rounds')
plt.title('Relationship between Employee Count and Funding Rounds')
plt.show()
%history -f myhistory.py
