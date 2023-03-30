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



#########################################################################
#################### Initialise Mappings
#########################################################################
# Key value pairs for Country - Policy Rate
dict_rate = {"US": "Fed Funds",
            "Canada": "Overnight Rate",
            "Euro Area": "Main Refinancing Operations Rate",
            "UK": "Bank Rate",
            "Japan": "Overnight Call Rate",
            "Switzerland": "Three-Month Libor", #"Policy Rate",
            "Australia": "Cash Rate",
            "New Zealand": "Official Cash Rate",
            "Sweden": "Repo Rate",
            "Norway": "Deposit Rate",
            "Denmark": "Deposit rate", #"Discount Rate",
            "Hong Kong": "Base Rate",
            "China": "Prime Loan Rate",
            "South Korea": "Base Rate",
            "Taiwan": "Discount Rate",
            "Malaysia": "Overnight Policy Rate",
            "Indonesia": "Reverse Repo Rate",
            "Philippines": "Policy Rate", #"Reverse Repo Rate",
            "Thailand": "Overnight Repo Rate",
            "India": "Repo Rate", #"Policy Repo Rate",
            "Russia": "Key Rate",
            "Poland": "Reference Rate",
            "Czech Republic": "Key Interest Rate", #"Repo Rate",
            "Saudi Arabia": "Repo Rate",
            "Turkey": "One-Week Repo Rate", #"Repo Rate",
            "South Africa": "Repo Rate",
            "Nigeria": "Policy Rate",
            "Brazil": "Selic Rate",
            "Mexico": "Policy Rate", #"Target Rate",
            "Colombia": "Policy Rate",
            "Chile": "Policy Rate",
            "Peru": "Monetary Policy Rate" #"Reference Rate"
            }



st.write(dict_rate)



