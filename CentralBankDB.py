###########################################
########## Package Imports
###########################################
import pandas as pd, numpy as np
import DatastreamDSWS as DSWS

# from datetime import datetime as dt
# import dataframe_image as dfi

import streamlit as st


##### Get Username ans passowrd
# username = st.text_input("Enter Datastream username:")
# password = st.text_input("Enter Datastream password:", type="password")



data = {'Name': ['John', 'Jane', 'Bob', 'Alice'],
        'Age': [25, 30, 28, 22],
        'Gender': ['M', 'F', 'M', 'F'],
        'Salary': [50000, 70000, 60000, 55000]}



st.write(data)
