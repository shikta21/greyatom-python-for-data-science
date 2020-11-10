# --------------
# Importing header files
import numpy as np
import warnings
#Reading file
warnings.filterwarnings('ignore')
# path for the file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census=np.concatenate((data,new_record),axis=0)
age=np.array(census[:,[0]])

max_age=np.max(age)
min_age=np.min(age)
age_mean=np.mean(age)
age_std=np.std(age)
race_0=[]
race_1=[]
race_2=[]
race_3=[]
race_4=[]
for i in range(0,1001):
    item=census[i][2]
    if item == 0:
        race_0.append(census[i])
    elif item == 1:
        race_1.append(census[i])
    elif item == 2:
        race_2.append(census[i])    
    elif item == 3:
        race_3.append(census[i])
    elif item == 4:
        race_4.append(census[i])
race_0=np.array(race_0)
race_1=np.array(race_1)
race_2=np.array(race_2)
race_3=np.array(race_3)
race_4=np.array(race_4)
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
a=min(len_0,len_1,len_2,len_3,len_4)
if a==len_0:
    minority_race=0
elif a==len_1:
    minority_race=1
elif a==len_2:
    minority_race=2
elif a==len_3:
    minority_race=3
elif a==len_4:
    minority_race=4
print(minority_race)   


senior_citizen=[]
for i in range(0,1001):
    item=census[i][0]
    if item > 60:
        senior_citizen.append(census[i])
senior_citizen=np.array(senior_citizen)        

temp=np.array(senior_citizen[:,[6]])
working_hours_sum=np.sum(temp)
senior_citizens_len=len(senior_citizen)
avg_working_hours= working_hours_sum/senior_citizens_len
print(avg_working_hours)

high=[]
low=[]
for i in range(0,1001):
    item=census[i][1]
    if item >10:
        high.append(census[i])
    elif item <=10:
        low.append(census[i])
high=np.array(high)
low=np.array(low)
temp1=np.array(high[:,[7]])
avg_pay_high=np.mean(temp1)
temp2=np.array(low[:,[7]])
avg_pay_low=np.mean(temp2)












