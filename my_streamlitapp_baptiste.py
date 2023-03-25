import os
import pickle
import datetime
import numpy as np
import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
import shap

import streamlit as st
from PIL import Image

from useful.variables import new_codes

scalers_path=os.path.join(os.getcwd(),'preprocessing')
minmax_scaler = pickle.load(open(os.path.join(scalers_path,"minmax_scaler.pkl"),"rb"))
standard_scaler = pickle.load(open(os.path.join(scalers_path,"standard_scaler.pkl"),"rb"))

logo = Image.open('images/ExitGPT.png')
st.image(logo, width=250)

st.text("")

st.header('Will your startup successfully exit?')

#st.subheader("Are you a founder?")
#st.subheader("Would you like to know if you startup is going get acquired?")
#st.markdown("<h2 style='color: black;font-size: 20px;' >Then you came to the right place!</h2>", unsafe_allow_html=True)
#st.markdown("<h2 style='color: black; font-size: 20px;' >In this demo, we will start by asking you specific information about your startup:</h2>", unsafe_allow_html=True)

st.text("")

st.subheader('Startup examples')

if st.button('Pabio'):
    date_to_fill= datetime.date(2020, 5, 20)
    employee_nb_to_fill=10
    industry_to_fill=['Professional Services', 'Real Estate and Construction']
    technology_to_fill=["Software"]
    country_to_fill="Europe"
    last_round_date_to_fill=datetime.date(2021, 12, 15)
    round_to_fill=[1000000,2200000,0,0,0]
    last_round_to_fill="seed"
elif st.button('Aleph Farms'):
    date_to_fill= datetime.date(2017, 7, 1)
    employee_nb_to_fill=150
    industry_to_fill=["Food and Beverage"]
    technology_to_fill=["Biotechnology"]
    country_to_fill="Middle East"
    last_round_date_to_fill=datetime.date(2021, 7, 1)
    round_to_fill=[2400000,12000000,105000000,0,0]
    last_round_to_fill="series b"
else:
    date_to_fill=datetime.date(2013, 3, 30)
    employee_nb_to_fill=0
    industry_to_fill=["Advertising"]
    technology_to_fill=["AR and VR"]
    country_to_fill="Europe"
    last_round_date_to_fill=datetime.date(2013, 3, 30)
    round_to_fill=[2,0,0,0,0]
    last_round_to_fill="seed"

st.text("")

st.subheader('Company profile')
#st.markdown("<h2 style='color: red;' >Company information</h2>", unsafe_allow_html=True)

d = st.date_input("Founding Date",date_to_fill)

employee_nb = st.number_input("Number of Employees",employee_nb_to_fill)

industries = st.multiselect("Industries?",
                            ['Advertising', 'Agriculture and Farming', 'Clothing and Apparel', 'Commerce and Shopping',
                             'Community and Lifestyle', 'Computer Hardware', 'Consumer Electronics', 'Consumer Goods',
                             'Content and Publishing', 'Data and Analytics', 'Design', 'Education', 'Energy',
                             'Environment and Sustainability','Events', 'Financial Services', 'Food and Beverage', 'Gaming',
                             'Government and Military', 'Health Care', 'HumanResources',
                             'Legal', 'Life Sciences', 'Logistics', 'Manufacturing', 'Media and Entertainment',
                             'Messaging and Telecommunications','Music and Audio', 'Natural Resources', 'Navigation and Mapping',
                             'Payments', 'Privacy and Security', 'Professional Services','Real Estate and Construction',
                             'Sales and Marketing', 'Software', 'Sports', 'Transportation', 'Travel and Tourism', 'Video'],
                            default=industry_to_fill)

industries= list(map(lambda x: x.replace('Software', 'Software_x'), industries))

technologies= st.multiselect("Technologies used",['AR and VR', 'Artificial Intelligence',
                            'Biotechnology', 'BlockChain', 'Hardware', 'Science and Engineering', 'Software', 'Sustainability'],
                             default=technology_to_fill)

techonlogies= list(map(lambda x: x.replace('Software', 'Software_y'), technologies))

#countries = list(new_codes.keys())
#countries = sorted(countries)
#countries.insert(0, country_to_fill)

region = st.selectbox("Headquarters Region",
                       [country_to_fill, 'Africa', 'Asia', 'Central America', 'Europe', 'Middle East', 'North America', 'Oceania',
                        'South America', 'United States'])

#st.markdown("<h2 style='color: red;' >Funding rounds</h2>", unsafe_allow_html=True)
st.subheader('Company funding')

stages_list=[last_round_to_fill,'seed', 'pre seed', 'private equity', 'series a', 'angel', 'equity crowdfunding', 'series b', 'series c',
             'series d', 'series e', 'series f', 'series g', 'series h']
stage= st.selectbox("Last funding round",stages_list)
stage=stage.replace(" ","_")

d_funding = st.date_input("Closing date of last funding round",last_round_date_to_fill)

funding_dict={}
funding_rounds=['Round 1','Round 2','Round 3','Round 4','Round 5']
for index, funding_round in enumerate(funding_rounds):

    scaler_min=round(int(minmax_scaler.data_min_[index]),0)
    scaler_max=round(int(minmax_scaler.data_max_[index]),0)
    #print(f'scaler min: {scaler_min} / scaler max: {scaler_max}')

    amount = st.number_input(f'USD amount raised for {str(funding_round).replace("_"," ")}:' + str(),
                             value=round_to_fill[index],
                             min_value=scaler_min,
                             max_value=scaler_max
                             )
    funding_dict[funding_round]=amount

#data_path=os.path.join(os.path.abspath(os.getcwd()),'raw_data')
#df=pd.read_csv(os.path.join(data_path,'startups_modified.csv'))
df = pd.read_csv('startups_modified.csv')
input_columns=df.columns.to_list()
input_columns.remove('Target')
input_df = pd.DataFrame(columns=input_columns)

input_df.loc[0, 'employeeCount'] = employee_nb

input_df.loc[0, region] = 1

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

#input_df.to_excel(os.path.join(data_path,'x_new.xlsx'),index=False)

###Predict###

model_path=os.path.join(os.getcwd(),'modeling')

model = pickle.load(open(os.path.join(model_path,"startup_model.pkl"),"rb"))

result=model.predict(input_df)

st.text("")
st.subheader('Prediction')
#st.markdown("<h2 style='color: black;' >Prediction:</h2>", unsafe_allow_html=True)
if result[0]==0:
    pred="Failure"
if result[0]==1:
    pred="Success"

if pred == 'Failure':
    st.markdown("<h2 style='color: red;' >No Exit</h2>", unsafe_allow_html=True)
#    st.markdown("""Prediction: <span style='color:red'>No Exit</span>""",
#               unsafe_allow_html=True)
elif pred == 'Success':
    st.markdown("<h2 style='color: green;' >Successful Exit</h2>", unsafe_allow_html=True)
#    st.markdown("""Prediction: <span style='color:green'>Successful Exit</span>""",
#                unsafe_allow_html=True)

#st.markdown(f"<h2 style='color: black; font-size: 40px;'>Your startup is predicted to be a {pred}.</h2>", unsafe_allow_html=True)
#st.write(pred)

###Shap###

explainer = pickle.load(open(os.path.join(os.path.join(os.getcwd(),'modeling'),"shap_explainer.pkl"),"rb"))
shap_values = explainer(input_df)
#print(shap_values)
shap.plots.waterfall(shap_values[0],show=False, max_display=12)
plt.tight_layout()
plt.savefig(os.path.join(os.getcwd(),'shap.png'),dpi=700)

st.image(os.path.join(os.getcwd(),'shap.png'))
