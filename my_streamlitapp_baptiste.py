import os
import pickle
import datetime
import numpy as np
import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
import shap

scalers_path=os.path.join(os.getcwd(),'preprocessing')
minmax_scaler = pickle.load(open(os.path.join(scalers_path,"minmax_scaler.pkl"),"rb"))
standard_scaler = pickle.load(open(os.path.join(scalers_path,"standard_scaler.pkl"),"rb"))

st.title('Predicting Startup Success')

st.subheader("Are you a founder?")
st.subheader("Would you like to know if you startup is going get acquired?")
st.markdown("<h2 style='color: blue;font-size: 20px;' >Then you came to the right place!</h2>", unsafe_allow_html=True)
st.markdown("<h2 style='color: blue; font-size: 20px;' >In this demo, we will start by asking you specific information about your startup:</h2>", unsafe_allow_html=True)
st.markdown("<h2 style='color: red;' >Company information</h2>", unsafe_allow_html=True)

d = st.date_input("When was your company founded?",datetime.date(2013, 3, 30))

employee_nb = st.number_input("How many employees work in yout company?",0)

industries = st.multiselect("What is your company's industry?",
                            ['Advertising', 'Agriculture and Farming', 'Clothing and Apparel', 'Commerce and Shopping',
                             'Community and Lifestyle', 'Computer Hardware', 'Consumer Electronics', 'Consumer Goods',
                             'Content and Publishing', 'Data and Analytics', 'Design', 'Education', 'Energy',
                             'Environment and Sustainability','Events', 'Financial Services', 'Food and Beverage', 'Gaming',
                             'Government and Military', 'Health Care', 'HumanResources',
                             'Legal', 'Life Sciences', 'Logistics', 'Manufacturing', 'Media and Entertainment',
                             'Messaging and Telecommunications','Music and Audio', 'Natural Resources', 'Navigation and Mapping',
                             'Payments', 'Privacy and Security', 'Professional Services','Real Estate and Construction',
                             'Sales and Marketing', 'Software', 'Sports', 'Transportation', 'Travel and Tourism', 'Video'])

industries= list(map(lambda x: x.replace('Software', 'Software_x'), industries))

technologies= st.multiselect("On what technology is your company built on?",['AR and VR', 'Artificial Intelligence', 'Biotechnology', 'BlockChain', 'Hardware', 'Science and Engineering', 'Software', 'Sustainability'])

techonlogies= list(map(lambda x: x.replace('Software', 'Software_y'), technologies))

country = st.selectbox("In which country is company established?",
                       ['OTHERS','CN', 'US', 'VN', 'CO', 'CA', 'DK', 'JP', 'SE', 'BE', 'NL', 'IT', 'AU', 'IL',
                        'ES', 'DE', 'IN', 'CH', 'AR', 'GB', 'KR', 'BR', 'PT', 'EG', 'PL', 'FR', 'HK', 'TW', 'NO',
                        'RO', 'BD', 'RU', 'ZA', 'MY', 'IE', 'MX', 'NG', 'AE', 'EE', 'CL', 'PK', 'SG', 'HU', 'CZ',
                        'UA', 'LU', 'CY', 'ID', 'KE', 'FI', 'AT', 'UG', 'TR', 'NZ', 'TH', 'GH', 'SA', 'LT', 'PH', 'LV', 'BG', 'GR'])

st.markdown("<h2 style='color: red;' >Funding rounds</h2>", unsafe_allow_html=True)

stages_list=['seed', 'pre seed', 'private equity', 'series a', 'angel', 'equity crowdfunding', 'series b', 'series c',
             'post ipo equity', 'series d', 'series e', 'series f', 'series g', 'series h']
stage= st.selectbox("What is your last funding round?",stages_list)
stage=stage.replace(" ","_")

d_funding = st.date_input("When was your last funding round?",datetime.date(2013, 3, 30))

funding_dict={}
funding_rounds=['Round 1','Round 2','Round 3','Round 4','Round 5']
for index, funding_round in enumerate(funding_rounds):

    scaler_min=minmax_scaler.data_min_[index]
    scaler_max=minmax_scaler.data_max_[index]
    print(scaler_min, scaler_max)

    amount = st.number_input(f'USD amount raised for {str(funding_round).replace("_"," ")}:' + str(),0)
                             #min_value=scaler_min,max_value=scaler_max
    funding_dict[funding_round]=amount

data_path=os.path.join(os.path.abspath(os.getcwd()),'raw_data')
df=pd.read_csv(os.path.join(data_path,'startups_modified.csv'))
input_columns=df.columns.to_list()
input_columns.remove('Target')
input_df = pd.DataFrame(columns=input_columns)

input_df.loc[0, 'employeeCount'] = employee_nb

input_df.loc[0, country] = 1

for industry in industries:
    input_df.loc[0, industry] = 1

for technology in technologies:
    input_df.loc[0, technology] = 1

funding_rounds_count=0
last_funding_round_amount=0
for key, value in funding_dict.items():
    input_df.loc[0, key]=value
    if value !=0:
        funding_rounds_count +=1
        last_funding_round_amount=value

input_df.loc[0, 'num_funding_rounds']=funding_rounds_count

input_df.loc[0, 'last_equity_funding_total']=last_funding_round_amount

input_df.loc[0, stage]=1

input_df["days_between_dates"] = (d_funding-d).days

input_df.fillna(0,inplace=True)

if 'Software' in input_df.columns:
    input_df.drop(columns=['Software'], axis=1, inplace =True)


###Scaling###

standard = ['num_funding_rounds','last_equity_funding_total','employeeCount','days_between_dates']
input_df[standard] = standard_scaler.transform(input_df[standard])

minmax = ['Round 1', 'Round 2', 'Round 3', 'Round 4', 'Round 5']
input_df[minmax] = minmax_scaler.transform(input_df[minmax])

input_df.to_excel(os.path.join(data_path,'x_new.xlsx'),index=False)

###Predict###

model_path=os.path.join(os.getcwd(),'modeling')

model = pickle.load(open(os.path.join(model_path,"startup_model.pkl"),"rb"))

result=model.predict(input_df)

print(f'prediction: {result}')

###Shap###

explainer = pickle.load(open(os.path.join(os.path.join(os.getcwd(),'modeling'),"shap_explainer.pkl"),"rb"))
shap_values = explainer(input_df)
#print(shap_values)
shap.plots.waterfall(shap_values[0],show=False, max_display=30)
plt.savefig(os.path.join(os.getcwd(),'shap.png'))
