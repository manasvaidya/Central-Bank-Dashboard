###########################################
########## Package Imports
###########################################
import pandas as pd
import numpy as np
import DatastreamDSWS as DSWS
import streamlit as st





##############################################
######## Initialise Connection
##############################################



# Create connection using the username and password
ds = DSWS.Datastream(username = username, password = password)

st.write("DB username:", st.secrets["username"])
st.write("DB password:", st.secrets["password"])


