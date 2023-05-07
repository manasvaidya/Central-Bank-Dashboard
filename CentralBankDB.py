###########################################
########## Package Imports
###########################################
import pandas as pd
import numpy as np
import DatastreamDSWS as DSWS
import streamlit as st
from datetime import datetime as dt







##############################################
######## Initialise Connection
##############################################

# Initialise login credentials
username=st.secrets.credentials.username
password=st.secrets.credentials.password

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


## Map Interest rate code
df['rate_code']=df["country"].map(dict_rate_code)

## Map Inflation rate code
df['inflation_code']=df["country"].map(dict_inf_code)




## Create ticker for policy rate
ticker_rate = ','.join(df['rate_code'])


## Create ticker for Inflation rate
ticker_inf = ','.join(df['inflation_code'])




## Extract Policy Rate data
df_rate = ds.get_data(tickers = ticker_rate, 
                          start=start, 
                          #end = end,
                          freq='M', 
                          kind=1).sort_index(ascending=False)



## Extract Policy Rate data
fields_inf = ['PCH#(CSR#(X, M), -12M)']

df_inf = ds.get_data(tickers = ticker_inf, 
                          start=start, 
                          #end = end,
                          freq='M', 
                          fields = fields_inf,
                          kind=1).sort_index(ascending=False)




## Loop to fill up Policy Rate numbers for all countries
#For every column in df_rate
for c in df_rate:
    # Assign latest policy rate to corresponding countries
    df.loc[df['rate_code']==c[0],'policy_rate'] = df_rate[c].sort_index(ascending=False).dropna().iloc[0]
           
    # Assign month of latest policy rate to corresponding countries
    df.loc[df['rate_code']==c[0],'policy_rate_date'] = df_rate[c].sort_index(ascending=False).dropna().index[0]
    
    
    ## Loop to check latest policy rate decision
    # Initialise position of pointer
    i = 0
    
    # Initialise threshold counter
    x = 0
    
    # Loop while we are within the threshold
    while (i<len(df_rate[c].sort_index(ascending=False).dropna())-1)&(x==0):
        # If i'th value != t+1'th value
        if df_rate[c].sort_index(ascending=False).dropna().iloc[i] != df_rate[c].sort_index(ascending=False).dropna().iloc[i+1]:
            # Then we know that interest rate was changed in i'th period. Take that date.
            df.loc[df['rate_code']==c[0], 'date_of_last_move'] = dt.strptime(df_rate[c].sort_index(ascending=False).dropna().index[i], "%Y-%m-%d").strftime("%b-%Y")
            
            # Check if the change was a hike or not
            if df_rate[c].sort_index(ascending=False).dropna().iloc[i] > df_rate[c].sort_index(ascending=False).dropna().iloc[i+1]:
                df.loc[df['rate_code']==c[0], 'direction_of_last_move'] = 'HIKE'
            else:
                df.loc[df['rate_code']==c[0], 'direction_of_last_move'] = 'CUT'
                
            #Calculate % pt change
            df.loc[df['rate_code']==c[0], 'policy_rate_change_pp'] = (df_rate[c].sort_index(ascending=False).dropna().iloc[i] - df_rate[c].sort_index(ascending=False).dropna().iloc[i+1]).round(2)
            
            # Also, mark the threshold counter as we now have our required value
            x = 1
        # If the i'th interest rate = i+1'th interest rate,
        else:
            # And if we're at the end of our series
            if i == len(df_rate[c].sort_index(ascending=False).dropna())-2:
                # Then we know that the interest rate wasn't changed for over 2 years
                df.loc[df['rate_code']==c[0], 'date_of_last_move'] = np.nan
                df.loc[df['rate_code']==c[0], 'direction_of_last_move'] = 'NA for'+start
                # And we end the loop
                x = 1
                df.loc[df['rate_code']==c[0], 'policy_rate_change_pp'] = np.nan
            # Otherwise,
            else:
                # We only increment the value of i to check the next value
                i = i + 1
 




## Loop to assign Inflation numbers against every country
for c in df_inf:
    # Assign latest policy rate to corresponding countries
    df.loc[df['inflation_code']==c[0],'inflation'] = df_inf[c].sort_index(ascending=False).dropna().iloc[0].round(2)

    # Assign month of latest policy rate to corresponding countries
    df.loc[df['inflation_code']==c[0],'inflation_date'] = df_inf[c].sort_index(ascending=False).dropna().index[0]
             


      
# Calculate Real Rate
df['real_rate'] = (df['policy_rate']-df['inflation']).round(2)

# Assign column order
col_order = ['country', 'central_bank_rate', 'date_of_last_move', 'direction_of_last_move',
             'policy_rate_change_pp', 'policy_rate', 'inflation', 'real_rate']

# Reorder columns
df = df[col_order]
df.columns = df.columns.map(dict_col)

    
######################################################################################
################### Format Output
######################################################################################

def make_pretty(styler, **kwargs):
    styler.format(precision=2)
    
    
    styler.hide(axis=0)
    
    styler.set_caption("Global Central Bank Dashboard [Source: Refinitiv DataStream, Acorn MC Ltd]").set_table_styles([{
        'selector': 'caption',
        'props': [('color', 'Black'),
                  ('font-size', '16px'),
                  ('caption-side', 'top')
                 ]
    }])
    
    # Create border for entire table
    styler.set_table_styles([{'selector' : '',
                            'props' : [('border','0.5px solid black')]}], overwrite=False)
    

    row_hover = {# for row hover use <tr>, for cell hover use <td>
        'selector': 'tr:hover',
        'props': [('background-color', '#ffffb3')]
    }
    
    cells = {# Cells background and font color
        'selector': 'tr:not(.index_name)',
        'props': 'background-color: white; color: black;'
    }

    headers = {#Headers background and font color
        'selector': 'th:not(.index_name)',
        'props': 'background-color: #000066; color: white;'
    }
    styler.set_table_styles([row_hover, cells, headers])
    
    # Align text in columns
    styler.set_table_styles([ 
        {'selector': 'th.col_heading', 'props': 'text-align: left;'},
        {'selector': 'th.col_heading.level0', 'props': 'font-size: 1.1em;'},
        {'selector': 'td', 'props': 'text-align: left;'}
    ], overwrite=False)
    
    # Set border color between columns
    styler.set_table_styles([
        {'selector': 'td', 'props': 'border-left: 0.5px solid black'},
        {'selector': 'td', 'props': 'border-right: 0.5px solid black'}
        # {'selector': 'td', 'props': 'border-left: 1px solid #000066'},
        # {'selector': 'td', 'props': 'border-right: 1px solid #000066'}
    ]
    , overwrite=False, axis=0)
    
    # Set border color between headers
    styler.set_table_styles({("Country"): [
        {'selector': 'th', 'props': 'border-left: 0.5px solid black'},
        #{'selector': 'th', 'props': 'border-right: 1px solid white'}
    ]}
    , overwrite=False, axis=0)
    

#     styler.set_table_styles({("Date of Last Move"): [
#         {'selector': 'th', 'props': 'border-left: 1px solid white'},
#         {'selector': 'th', 'props': 'border-right: 1px solid white'}
#     ]}
#     , overwrite=False, axis=0)
    
#     styler.set_table_styles({("Change (%)"): [
#         {'selector': 'th', 'props': 'border-left: 1px solid white'},
#         {'selector': 'th', 'props': 'border-right: 1px solid white'}
#     ]}
#     , overwrite=False, axis=0)
    
#     styler.set_table_styles({("Inflation (%)"): [
#         {'selector': 'th', 'props': 'border-left: 1px solid white'},
#         {'selector': 'th', 'props': 'border-right: 1px solid white'}
#     ]}
#     , overwrite=False, axis=0)
    
    styler.set_table_styles({("Real Rate (%)"): [
        {'selector': 'th', 'props': 'border-right: 0.5px solid black'}
    ]}
    , overwrite=False, axis=0)
    
    return styler


result = df.style.pipe(make_pretty)



# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)




st.table(result)


