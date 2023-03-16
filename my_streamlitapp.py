import streamlit as st
st.write("Hello, welcome to our project!")
import pandas as pd
import numpy as np
import joblib
import streamlit as st
st.title('Predicting Startup Success')

st.subheader("Are you a founder? Would you like to know if you startup is going get acquired?")
st.markdown("<h2 style='color: blue;' >Then you came to the right place!</h2>", unsafe_allow_html=True)
# st.subheader(" You came to the right place")
st.markdown("<h2 style='color: black; font-size: 20px;' >In this demo, we will start by asking you specific information about your startup:</h2>", unsafe_allow_html=True)
# st.write( "In this demo, we will start by asking you specific information about your startup.")
st.markdown("""
<ul style='color: green; font-size: 18px;'>
    <li>When was your company founded?</li>
    <li>Where is your company is located?</li>
    <li>What market/industry are you in?</li>
    <li>Which type of technology are you using?</li>
    <li>Have you raised any investment round?</li>
    <li>How much did you raise in each round?</li>
</ul>
""", unsafe_allow_html=True)

bullet_points = ["Let's go!"]
for point in bullet_points:
    if st.button(point):
        # Add your code for when the button is clicked here
        st.write(f"You clicked the button for {point}!")

bullet_points = [
    "Founding Date",
    "Company Location",
    "Market/Industry",
    "Type of Technology",
    "Number of Funding ounds",
    "Amounts Raised"
]

# Iterate through the list of bullet points and add a button for each one
for point in bullet_points:
    if st.button(point):
        # Add your code for when the button is clicked here
        st.write(f"You clicked the button for {point}!")

for point in bullet_points:
    st.write(point)
    user_input = st.text_input(label="", value="")
    st.write("You typed:", user_input)
