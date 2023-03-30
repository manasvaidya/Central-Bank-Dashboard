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



# create a dataframe with a boolean column
df = pd.DataFrame({"A": [True, False, True, False]})

# show the dataframe with checkboxes
st.dataframe(df)



