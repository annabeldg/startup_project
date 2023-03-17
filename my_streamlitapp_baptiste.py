import streamlit as st
import pandas as pd
import numpy as np
import joblib
import streamlit as st
import datetime
import os

#st.write("Hello, welcome to our project!")
st.title('Predicting Startup Success')

st.subheader("Are you a founder?")
st.subheader("Would you like to know if you startup is going get acquired?")
st.markdown("<h2 style='color: yellow;font-size: 20px;' >Then you came to the right place!</h2>", unsafe_allow_html=True)
# st.subheader(" You came to the right place")
st.markdown("<h2 style='color: yellow; font-size: 20px;' >In this demo, we will start by asking you specific information about your startup:</h2>", unsafe_allow_html=True)
# st.write( "In this demo, we will start by asking you specific information about your startup.")

bullet_points = [
    "Founding Date",
    "Employee Count",
    "Company Location",
    "Market/Industry",
    "Type of Technology",
    "Amounts Raised by Funding Rounds"
    "Last Funding Round Date"
]

# 1. num_funding_rounds => déduire de #7
# 2. last_equity_funding_total => déduire de #7
# 3. employeeCount => done
# 4. industry (multi-select) => done
# 5. technology (multi-select) => done
# 6. headquartersCountry (uni-select) => done
# 7. funding_rounds: each funding round with amount raised => revoir ordre?
# 8. founded_on + last_funding_on => days_between_dates

st.markdown("<h2 style='color: red;' >Company information</h2>", unsafe_allow_html=True)

d = st.date_input("When was your company founded?",datetime.date(2000, 1, 1))
#st.write('Company founded on:', d)

employee_nb = st.number_input("How many employees work in yout company?",0)

industries = st.multiselect("What is your company's industry?",['Advertising', 'Agriculture and Farming', 'Clothing and Apparel', 'Commerce and Shopping',
                                                              'Community and Lifestyle', 'Computer Hardware', 'Consumer Electronics', 'Consumer Goods',
                                                              'Content and Publishing', 'Data and Analytics', 'Design', 'Education', 'Energy', 'Environment and Sustainability',
                                                              'Events', 'Financial Services', 'Food and Beverage', 'Gaming', 'Government and Military', 'Health Care', 'HumanResources',
                                                              'Legal', 'Life Sciences', 'Logistics', 'Manufacturing', 'Media and Entertainment', 'Messaging and Telecommunications',
                                                              'Music and Audio', 'Natural Resources', 'Navigation and Mapping', 'Payments', 'Privacy and Security', 'Professional Services',
                                                              'Real Estate and Construction', 'Sales and Marketing', 'Software', 'Sports', 'Transportation', 'Travel and Tourism', 'Video'])

industries= list(map(lambda x: x.replace('Software', 'Software_x'), industries))

technologies= st.multiselect("On what technology is your company built on?",['AR and VR', 'Artificial Intelligence', 'Biotechnology', 'BlockChain', 'Hardware', 'Science and Engineering', 'Software', 'Sustainability'])

techonlogies= list(map(lambda x: x.replace('Software', 'Software_y'), technologies))

countries = st.multiselect("In which country is company established?",['CN', 'US', 'VN', 'CO', 'CA', 'DK', 'JP', 'SE', 'BE', 'NL', 'IT', 'AU', 'OTHERS', 'IL',
                                                                     'ES', 'DE', 'IN', 'CH', 'AR', 'GB', 'KR', 'BR', 'PT', 'EG', 'PL', 'FR', 'HK', 'TW', 'NO',
                                                                     'RO', 'BD', 'RU', 'ZA', 'MY', 'IE', 'MX', 'NG', 'AE', 'EE', 'CL', 'PK', 'SG', 'HU', 'CZ',
                                                                     'UA', 'LU', 'CY', 'ID', 'KE', 'FI', 'AT', 'UG', 'TR', 'NZ', 'TH', 'GH', 'SA', 'LT', 'PH', 'LV', 'BG', 'GR'])


st.markdown("<h2 style='color: red;' >Funding rounds</h2>", unsafe_allow_html=True)
d_funding = st.date_input("When was your last funding round?",datetime.date(2000, 1, 1))
funding_dict={}
funding_rounds=['seed', 'pre_seed', 'private_equity', 'series_a', 'angel', 'equity_crowdfunding', 'series_b', 'series_c', 'post_ipo_equity', 'series_d', 'series_e', 'series_f', 'series_g', 'series_h']
for funding_round in funding_rounds:
    amount = st.number_input(f'USD amount raised for {str(funding_round).replace("_"," ")}:' + str(),0)
    funding_dict[funding_round]=amount

data_path=os.path.join(os.path.abspath(os.getcwd()),'raw_data')
df=pd.read_csv(os.path.join(data_path,'startups_modified.csv'))
input_columns=df.columns.to_list()
input_df = pd.DataFrame(columns=input_columns)

input_df.loc[0, 'employeeCount'] = employee_nb

for industry in industries:
    input_df.loc[0, industry] = 1

for technology in technologies:
    input_df.loc[0, technology] = 1

for country in countries:
    input_df.loc[0, country] = 1

print(input_df['employeeCount'])


#bullet_points = ["Let's go!"]
#for point in bullet_points:
    #if st.button(point):
        # Add your code for when the button is clicked here
        #st.write(f"You clicked the button for {point}!")

# Iterate through the list of bullet points and add a button for each one
#for point in bullet_points:
    #if st.button(point):
        # Add your code for when the button is clicked here
        #t.write(f"You clicked the button for {point}!")

#for point in bullet_points:
    #st.write(point)
    #user_input = st.text_input(label="", value="")
    #st.write("You typed:", user_input)
