# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank=pd.read_csv(path)
categorical_var=bank.select_dtypes(include='object')
print(categorical_var.head(10))

numerical_var=bank.select_dtypes(include=['number'])
print(numerical_var.head(10))





# code ends here


# --------------
# code starts here

# load the dataset and drop the Loan_ID
banks= bank.drop(columns='Loan_ID')


# check  all the missing values filled.

print(banks.isnull().sum())

# apply mode 

bank_mode = banks.mode().iloc[0]

# Fill the missing values with 

banks.fillna(bank_mode, inplace=True)

# check again all the missing values filled.

print(banks.isnull().sum())





#code ends here


# --------------
# Code starts here
import numpy as np



avg_loan_amount=pd.pivot_table(data=banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',
aggfunc=np.mean)



# code ends here



# --------------
# code starts here
loan_approved_se=(banks['Self_Employed']== 'Yes') & (banks['Loan_Status']== 'Y')
loan_approved_nse=(banks['Self_Employed']== 'No') & (banks['Loan_Status']== 'Y')


Loan_Status=614

percentage_se=((loan_approved_se).value_counts().iloc[1]/Loan_Status)*100
percentage_nse=((loan_approved_nse).value_counts().iloc[0]/Loan_Status)*100
# code ends here


# --------------
# code starts here

loan_term=banks['Loan_Amount_Term'].apply(lambda x:x/12)
#print(loan_term)
big_loan_term= (loan_term>=25).sum()


# code ends here


# --------------
# code starts here
#loan_groupby=banks.groupby('Loan_Status')
loan_groupby=banks.groupby('Loan_Status')['ApplicantIncome','Credit_History']

mean_values=loan_groupby.mean()
#print(mean_values)


# code ends here


