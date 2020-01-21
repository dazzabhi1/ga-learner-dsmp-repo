# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data=pd.read_csv(path)
#Code starts here 
data['Gender'].replace('-','Agender',inplace=True)

gender_count=data['Gender'].value_counts()

gender_count.plot(kind='bar')



# --------------
#Code starts here

alignment = data['Alignment'].value_counts()
alignment .plot(kind='pie', label ='Character Alignment')



# --------------
#Code starts here
sc_df=data[['Strength','Combat']].copy()
ic_df=data[['Intelligence','Combat']].copy()

sc_covariance=sc_df['Strength'].cov(sc_df['Combat'])
sc_strength=sc_df['Strength'].std(axis=0, skipna=True)

sc_combat=sc_df['Combat'].std(axis= 0, skipna=True)

sc_pearson = (sc_covariance / (sc_combat*sc_strength))

ic_covariance= ic_df['Intelligence'].cov(ic_df['Combat'])

ic_intelligence = ic_df['Intelligence'].std(axis=0, skipna=True)

ic_combat= ic_df['Combat'].std(axis=0, skipna=True)

ic_pearson= (ic_covariance/(ic_combat*ic_intelligence))

print('Pearson correlation between Strength & Combat:', sc_pearson)
print('Pearson correlation between Intelligence & Combat:', ic_pearson)


# --------------
#Code starts here

total_high= data['Total'].quantile(0.99)

super_best=data[data['Total'] > total_high ]

super_best_names= list([super_best['Name']])

print(super_best_names)


# --------------
#Code starts here

fig,(ax_1,ax_2,ax_3) =plt.subplots(3,1, figsize=(10,10)) 

data.boxplot(column='Intelligence', ax=ax_1)
ax_1.set_title('Intelligence')


data.boxplot(column='Speed', ax=ax_2)
ax_2.set_title('Speed')

data.boxplot(column='Power', ax=ax_3)
ax_3.set_title('Intelligence')




