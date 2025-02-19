import streamlit as st
from influxdb_client_3 import Point, InfluxDBClient3
import pandas as pd
import plotly.express as px
import os
from streamlit_autorefresh import st_autorefresh
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(layout="wide")

st_autorefresh(interval=1000, key="datarefresh")

client = InfluxDBClient3(token=os.environ["INFLUXDB_TOKEN"],
                         host=os.environ["INFLUXDB_HOST"],
                         org=os.environ["INFLUXDB_ORG"],
                         database=os.environ["INFLUXDB_DATABASE"])

st.markdown(
    """
    <style>
    .main .block-container {
        padding-top: 1rem;  /* Adjust this value as needed */
    }
    .title-container {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;  /* Align items to the top */
    }
    .title-container svg {
        margin-left: 10px;  /* Adjust this value as needed */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="title-container">
        <div>
            <h1>Racing Car Dashboard</h1>
            <h3>Updated every 1 second</h3>
        </div>
        <svg id="Layer_2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 288.57" width="150">
            <g id="Layer_1-2">
                <g>
                    <rect x="118.03" y="118.03" width="52.46" height="52.46" fill="#0064ff"></rect>
                    <rect x="177.05" y="177.05" width="52.46" height="52.46" rx="7.87" ry="7.87" fill="#bd2eff"></rect>
                    <circle cx="258.36" cy="258.36" r="30.16" fill="#ff7828"></circle>
                    <path d="M283.28,0H5.25C2.35,0,0,2.35,0,5.25V283.28c0,2.9,2.35,5.25,5.25,5.25H165.25c2.9,0,5.25-2.35,5.25-5.25v-41.97c0-2.9-2.35-5.25-5.25-5.25H52.46V52.46H236.07v113.07c0,2.9,2.35,5.25,5.25,5.25h41.97c2.9,0,5.25-2.35,5.25-5.25V5.25c0-2.9-2.35-5.25-5.25-5.25Zm301.68,118.08h-42.05c-2.9,0-5.25,2.35-5.25,5.25v160c0,2.9,2.35,5.25,5.25,5.25h42.05c2.9,0,5.25-2.35,5.25-5.25V123.32c0-2.9-2.35-5.25-5.25-5.25Zm0-91.89h-42.05c-2.9,0-5.25,2.35-5.25,5.25v42.05c0,2.9,2.35,5.25,5.25,5.25h42.05c2.9,0,5.25-2.35,5.25-5.25V31.43c0-2.9-2.35-5.25-5.25-5.25Zm-91.73,91.89h-42.05c-2.9,0-5.25,2.35-5.25,5.25v112.7h-65.63V123.28c0-2.9-2.35-5.25-5.25-5.25h-42.05c-2.9,0-5.25,2.35-5.25,5.25l.22,160.05c0,2.89,2.35,5.24,5.25,5.24h160.01c2.9,0,5.25-2.35,5.25-5.25V123.32c0-2.9-2.35-5.25-5.25-5.25Zm306.77,5.2c0-2.9-2.35-5.25-5.25-5.25h-41.97c-2.9,0-5.25,2.35-5.25,5.25v34.1l-32.79,21.86-32.79-21.86v-34.1c0-2.9-2.35-5.25-5.25-5.25h-41.97c-2.9,0-5.25,2.35-5.25,5.25v47.21l49.18,32.79-49.18,32.79v47.21c0,2.9,2.35,5.25,5.25,5.25h41.97c2.9,0,5.25-2.35,5.25-5.25v-34.45l32.6-21.63,32.98,21.98v34.1c0,2.9,2.35,5.25,5.25,5.25h41.97c2.9,0,5.25-2.35,5.25-5.25v-47.21l-49.29-32.86,49.29-32.71v-47.21Z" fill="#14174d"></path>
                </g>
            </g>        
        </svg>
    </div>
    """,
    unsafe_allow_html=True
)

# Query InfluxDB
query = f'''
SELECT *
FROM "telemetry"
WHERE time > now() - interval '1 minute'
ORDER BY time
'''

df = client.query(query=query, mode="pandas", language="sql")

# Display Speed
speed = df['Speed'].iloc[-1] if 'Speed' in df.columns and not df.empty else 0
st.metric(label="Speed", value=f"{speed} km/h")

# Display Gear
gear = df['Gear'].iloc[-1] if 'Gear' in df.columns and not df.empty else 0
st.metric(label="Gear", value=f"{gear}")

# Display LapNumber
lapnumber = df['LapNumber'].iloc[-1] if 'LapNumber' in df.columns and not df.empty else 0
st.metric(label="LapNumber", value=f"{lapnumber}")

st.markdown(
    """
    For more details, visit the [GitHub repository]().
    """
)

st.markdown(
    """
    Check out and `pip install quixstreams` for more info [here]().
    """
)