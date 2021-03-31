# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file :- Let's check which variable is categorical and which one is numerical so that you will get a basic idea about the features of the bank dataset.


df= pd.read_csv(path)
bank=df
categorical_var=df.select_dtypes(include = 'object')
numerical_var = df.select_dtypes(include = 'number')

#Sometimes customers forget to fill in all the details or they don't want to share other details. Because of that, some of the fields in the dataset will have missing values. Now you have to check which columns have missing values and also check the count of missing values each column has. If you get the columns that have missing values, try to fill them.

banks=bank.drop(columns=['Loan_ID'])
bank_mode=banks.mode(axis=0, numeric_only=False)
banks.fillna(bank_mode, inplace=True)
for x in banks.columns:
        banks[x]=banks[x].fillna(value=bank_mode[x].iloc[0])

#Now let's check the loan amount of an average person based on 'Gender', 'Married', 'Self_Employed'. This will give a basic idea of the average loan amount of a person.

avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')

#Now let's check the percentage of loan approved based on a person's employment type.
loan_approved_se = len(banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status']== 'Y')])

loan_approved_nse = len(banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')])
#Calculate the percentage of loan approval for self-employed people and store result in variable 'percentage_se'.

#Calculate the percentage of loan approval for people who are not self-employed and store the result in variable 'percentage_nse'.
percentage_se = (loan_approved_se * 100)/614
percentage_nse = (loan_approved_nse * 100)/614

#A government audit is happening real soon! So the company wants to find out those applicants with long loan amount term.
loan_term = banks['Loan_Amount_Term'].apply(lambda x: (x/12))

big_loan_term = len(loan_term[loan_term >= 25])

#Now let's check the average income of an applicant and the average loan given to a person based on their income.
loan_groupby= banks.groupby('Loan_Status')
loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']

mean_values = loan_groupby.mean()
print(mean_values)





