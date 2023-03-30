###########################################
########## Package Imports
###########################################
import pandas as pd, numpy as np

!pip install DatastreamDSWS
import DatastreamDSWS as DSWS

from datetime import datetime as dt

!pip install dataframe_image
import dataframe_image as dfi

import streamlit as st




######### Streamlit Title###########
st.title('Central Bank Dashboard')
st.subheader('Source: Refinitiv Datastream, Acorn Macro Consulting')

##############################################
######## Initialise Connection
##############################################

# Set up parameters
username = 'richard@acornmc.co.uk'
password = 'Subban76'

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

# Key value pairs for Country - DS Rate Code
dict_rate_code = {"US": "USPRATE.", 
                  "UK": "UKPRATE.", 
                  "Canada":"CN14309",
                  "Euro Area":"EURODEP",
                  "Japan":"JPPRATE.",
                  "Switzerland":"SWBCBPR",
                    "Australia":"AUPRATE.",
                    "New Zealand":"NZPRATE.",
                    "Sweden":"SDPRATE.",
                    "Norway":"NWPRATE.",
                    "Denmark":"DKI60...",
                    "Hong Kong":"HKBCBPR",
                    "China":"CHLPR1YRR",
                    "South Korea":"KOPRATE.",
                    "Taiwan":"TWPRATE.",
                    "Malaysia":"MYPRATE.",
                    "Indonesia":"IDPRATE.",
                    "Philippines":"pHPREPO.",
                    "Thailand":"THPRATE.",
                    "India":"INPRATE.",
                    "Russia":"RSPRATE.",
                    "Poland":"POPRATE",
                    "Czech Republic":"CZPRATE.",
                    "Saudi Arabia":"SIPRATE",
                    "Turkey":"TKPRATE.",
                    "South Africa":"SAPRATE.",
                    "Nigeria":"NGPRATE.",
                  "Mexico":"MXPRATE.",
                    "Colombia":"CBPRATE.",
                    "Chile":"CLPRATE.",
                    "Peru":"PEPRATE.",
                 "Brazil": "BRPRATE."}

# Key value pairs for Country - DS Inflation Code
dict_inf_code = {"US": "USCONPRCE", 
                 "UK": "UKCONPRCF",
                 "Canada": "CNCONPRCF",
                 "Euro Area": "EMEBCPALE",
                 "Japan": "JPCONPRCF",
                 "Switzerland": "SWCONPRCF",
                 "Australia": "AUCONPRCF",
                 "New Zealand": "NZCONPRCF",
                 "Sweden": "SDCONPRCF",
                 "Norway": "NWCONPRCF",
                 "Denmark": "DKCONPRCF",
                 "Hong Kong": "HKCONPRCF",
                 "China": "CHCCPI..E",
                 "South Korea": "KOCONPRCF",
                 "Taiwan": "TWCONPRCF",
                 "Malaysia": "MYCONPRCF",
                 "Indonesia": "IDCONPRCF",
                 "Philippines": "PHCONPRCF",
                 "Thailand": "THCONPRCF",
                 "India": "INCONPRCF",
                 "Russia": "RSCONPRCF",
                 "Poland": "POCONPRCF",
                 "Czech Republic": "CZCONPRCF",
                 "Saudi Arabia": "SICONPRCF",
                 "Turkey": "TKCONPRCF",
                 "South Africa": "SACONPRCF",
                 "Nigeria": "NGCONPRCF",
                 "Mexico": "MXCONPRCF",
                 "Colombia": "CBCONPRCF",
                 "Chile": "CLCPCOREF",
                 "Peru": "PECCPI..E",
                "Brazil": "BRCONPRCF"}


# Column names map
dict_col = {'country': "Country", 
            'central_bank_rate': "Instrument", 
            'rate_code': "Policy Rate DS Code", 
            'inflation_code': "CPI DS Code", 
            'policy_rate': "Policy Rate (%)",
            'inflation': "Inflation (%)", 
            'real_rate': "Real Rate (%)",
            'direction_of_last_move': "Last Move", 
            'date_of_last_move': "Date of Last Move", 
            'policy_rate_change_pp': "Change (%)",
            'policy_rate_date': "Date of Policy Rate", 
            'inflation_date': "Date of Inflation"
           }




###############################################################################
####################### Parameter Initialisation and Preprocessing
###############################################################################

## Define countries to extract data for
input_list = ["US", "UK", "Canada", "Euro Area", "Japan", "Switzerland", "Australia",
             "New Zealand", "Sweden", "Norway", "Denmark", "Hong Kong", "China",
              "South Korea", "Taiwan", "Malaysia", "Indonesia", "Philippines", 
              "Thailand", "India", "Russia", "Poland", "Czech Republic", "Saudi Arabia",
              "Turkey", "South Africa", "Nigeria", "Mexico", "Colombia", "Chile", "Peru"
              ,"Brazil"
             ]

## Define initial parameters
start='-10Y'




## Make Data frame out of the list
df = pd.DataFrame(input_list, columns=["country"])

## Map Central Bank's choice of Rate
df['central_bank_rate']=df["country"].map(dict_rate)




########## Write Dataframe#######
st.write(df)

