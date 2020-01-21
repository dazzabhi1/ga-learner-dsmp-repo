# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df= pd.read_csv(path)
fico1 = (df['fico']>700).sum()
total= len(df) 
p_a = fico1 / total

purpose1=(df['purpose'] == 'debt_consolidation').sum()

p_b = purpose1 / len(df)

df1= df[df['purpose']=='debt_consolidation']
p_a_b= ((df1['fico']>700) & (df1['purpose'])).sum() / fico1
result= ((df1['fico']>700) & (df1['purpose'])).sum() / purpose1 ==p_a
result
# code ends here


# --------------
# code starts here
prob_lp = (df['paid.back.loan']=='Yes').sum()/len(df)
prob_cs=(df['credit.policy']=='Yes').sum()/len(df)

new_df=df[df['paid.back.loan']=='Yes']

prob_pd_cs= ((new_df['paid.back.loan']=='Yes') & (new_df['credit.policy']=='Yes')).sum() / (df['paid.back.loan']=='Yes').sum()

bayes = (prob_pd_cs*prob_lp) / prob_cs
print("Bayes:", bayes)
# code ends here


# --------------
# code starts here

df.purpose.value_counts().plot(kind='bar')

df1= df[df['paid.back.loan']=='No']
df1.purpose.value_counts().plot(kind='bar')

# code ends here


# --------------
# code starts here
inst_median=df.installment.median()

inst_mean= df.installment.mean()

plt.subplot(2,1,1)
df.installment.plot.hist(bins=20)





plt.subplot(2,1,2)
df['log.annual.inc'].plot.hist(bins=20)


# code ends here


