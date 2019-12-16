import io
import pandas as pd
import os.path
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#Read in the Subject Measures .csv file into a pandas dataframe and parse the dates
my_path = os.path.abspath(os.path.dirname(__file__))
csv_path = os.path.join(my_path, 'subj_measures.csv')
df = pd.read_csv(csv_path, parse_dates=['date'])

#Seperate out each indiviuals data by their user id
gk = df.groupby(['user_id'])

#For this example, we select a single user_id
id = 2012 #597 is another exaple
pk =  gk.get_group((id))

#Further group the data by the attribute type, and month
#Examing the mean value for mood and sleep for each recorded month
pk = pk.groupby(['type', pd.Grouper(key='date',freq='M')]).value.mean().unstack(level=0)
pk.index = pk.index.strftime('%b %y')

#Dropping these attributes because they are under-reported and clutter the results
pk.drop('anticipatoryStress', axis=1, inplace=True)
pk.drop('ruminationStress', axis=1, inplace=True)

#create the bar plot
fig, ax = plt.subplots()
pk.plot(kind = 'bar', ax=ax)

#customize x and y axes for legibility
plt.xticks(rotation=35)
plt.yticks([0,1,2,3,4])
labels = ['Awful', 'Bad', 'Okay', 'Good','Great']
ax.set_yticklabels(labels)

ax.yaxis.grid(color='gray', linestyle='dashed')
plt.title('Average recorded attribute per month for patient: id=' +str(id))
plt.show()
