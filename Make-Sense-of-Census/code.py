# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data=np.genfromtxt(path,delimiter=",",skip_header=1)
print("\nData: \n\n", data)
print("\nType of data: \n\n",type(data))
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
census=[]
census=np.concatenate((data,new_record),axis =0)
print(census)


# --------------
#Code starts here
age=census[:,:1]

max_age=np.max(age)
#print(max_age)
min_age=np.min(age)

age_mean=np.mean(age)
print(age_mean)

age_std=np.std(age)
print(age_std)



# --------------
#Code starts here
race=census[:,2]
#print(race)
#race=np.asarray(race)

#print(race)
#race_0=condition(race==0)


race_0=census[race==0]
#print(race_0)

race_1=census[race==1]
race_2=census[race==2]
race_3=census[race==3]
race_4=census[race==4]



#race_5=([[race_0],[race_1],[race_2],[race_3],[race_4]])
#race_len = [len(i) for i in race_5]
#print(race_len)


len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)

len_3=len(race_3)
len_4=len(race_4)



lis=([len_0,len_1,len_2,len_3,len_4])
minority_race=np.min(lis)
minority_race=list(lis).index(minority_race)
print(minority_race)



# --------------
#Code starts here
ages=census[:,0]
ages=np.asarray(ages)


senior_citizens=census[(ages>60)]
working_hours_sum=senior_citizens[:,6:7]
working_hours_sum=np.sum(working_hours_sum)
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)



# --------------
#Code starts here
edu_num=census[:,1]

high=census[(edu_num>10)]
low=census[(edu_num<=10)]
#print(high)
#print(low)

avg_pay_high=np.mean(high[:,7])
print(avg_pay_high)

avg_pay_low=np.mean(low[:,7])
print(avg_pay_low)


