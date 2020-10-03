import pandas as pd
import zipfile,os
file='../../../Downloads/FL_insurance_sample.csv.zip'
unzip=zipfile.ZipFile(file)
unzip.extractall(os.getcwd())
df=pd.read_csv('FL_insurance_sample.csv')
state=df['statecode']
policy_id=df['policyID']
print(state,policy_id)


